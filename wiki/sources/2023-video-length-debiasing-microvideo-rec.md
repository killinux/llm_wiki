---
type: source
subtype: paper
tags: [recommender-system, debiasing, micro-video, multi-task-learning, watch-time, selection-bias]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2308.14276
raw: raw/2308.14276.pdf
authors: [Yuhan Quan, Jingtao Ding, Chen Gao, Nian Li, Lingling Yi, Depeng Jin, Yong Li]
year: 2023
---

# Alleviating Video-Length Effect for Micro-video Recommendation (VLDRec)

本文提出 VLDRec(Video Length Debiasing Recommendation),针对 TikTok/微信视频号等微视频平台中"长视频天然获得更高平均观看时长"所导致的 video-length bias,通过去偏数据标注、视频长度条件采样与多任务学习,在以观看时长为目标的推荐中学习不被视频长度扭曲的真实用户偏好。

## 问题

在微视频平台(如 TikTok、[[kuaishou]]、[[wechat-channels-dataset]]/微信视频号)中,交互范式发生根本变化:视频自动连播,用户不再通过"点击"选择感兴趣的视频,因此传统以点击率(CTR)为正信号的做法失效,平台只能采集新型反馈——观看时长([[watch-time]])。

直接按预测观看时长排序会引入 **video-length bias**:长视频更容易积累较高的平均观看时长,于是模型偏向推荐长视频。作者的实证分析(图 2,微信视频号数据)显示,用户退出 App 前观看的最后一个视频往往更长,说明长视频更易引发用户疲劳;同时这种偏置会放大(bias amplification),把长视频组里的低质内容也一并推上去,损害推荐准确性。

与流行度偏置、位置偏置不同,该问题有两点独特难点:(1) 视频长度与观看时长都是近似连续量,连续标签使无偏学习建模困难,且对 [[inverse-propensity-scoring]] 这类方法会带来极端取值导致的方差问题;(2) 视频长度与观看时长关系复杂,长度直接影响偏好指标(观看时长)的度量,难以定义能代表真实偏好的标签。这使本问题区别于已有 [[debiasing]]/[[selection-bias]] 工作。

## 方法

VLDRec 把任务形式化为 learn-to-rank(基于 BPR 损失 L_BPR),不直接用观看时长当标签,而是用 play progress p_ij = t_ij / l_j(观看时长除以视频长度)来刻画偏好。其设计包含三部分:

- **面向观看时长的去偏标注(labeling approach)**:用基于 play progress 的两种标注。(1) Pointwise hard labeling:按视频长度分组后,组内阈值 τ(g) 取该组 play progress 分布的 p80(即组内 top 20% 为正样本)。(2) Pairwise margin-based labeling:要求正样本与负样本的 progress 差大于 margin ε,聚焦同一用户内部比较。两者由超参数 β 切换。这一设计源于关键观察:视频长度相近的视频其完成率(completion rate)分布相近,因此据长度分组定阈值能得到与长度无关的偏好标签。
- **视频长度条件采样(length-conditioned sample generation,Algorithm 1)**:对每个正样本 (u_i, v_j) 额外从 v_j 所在长度组中采一个负样本 v_k^un 构成训练对,从而在长度相近的视频之间学习 pairwise rank,缓解 video-length bias 并起到 hard negative mining 的作用。
- **多任务用户偏好学习(multi-task learning,公式 3)**:共享 embedding + 两个不共享参数的前馈网络 f、f_un(可用 [[deepfm]]、[[autoint]]、NFM 等),分别处理有偏样本对与去偏(长度条件)样本对;总损失 L = α·L1 + (1−α)·L2,联合优化。

此外,作者提出长度不变的 **Top-T 评估指标 View_Time@T**(公式 5):固定推荐列表总视频长度为 T(而非固定列表长度 K),累加观看时长,从而在评测阶段也去除长度偏置。整体遵循数据驱动、正则化(从较少偏置的反馈中学习内在偏好)的思路,与纯 backdoor adjustment 等 [[causal-inference]] 方法路径不同(论文也指出视频长度可视为 user-video 间的 confounder)。

## 结果

在两个真实大规模数据集上实验:Kuaishou(1,945,502 样本 / 9,829 用户 / 136,317 视频,平均视频长 17.54s)与 WeChat Channels(3,264,803 样本 / 54,595 用户 / 62,569 视频,平均视频长 32.97s)。主指标为 View_Time@120 / View_Time@240。对比 3 类基线:回归类(TimeRegression、RateRegression)、排序类(TimeRanking、RateRanking)、无偏类(IPS、IPS-C、IPS-CN、IPS-CNSR、CausE、DecRS、DVR)。

- 以 NFM 为基座,VLDRec 在 View_Time@120 上较最佳基线相对提升 **1.81%**(Kuaishou,达 44.96,次优 DecRS 44.16)与 **11.32%**(WeChat,达 29.71,次优 CausE 26.69);较两种回归方法中较优者更是分别提升 **25.66%** 与 **137.30%**。
- 以 DeepFM、AutoInt 为基座,View_Time@120 也至少分别提升 **5.49%** 与 **7.31%**。
- 消融:采样超参 β 与多任务权重 α 均在中间值表现最佳(α=0.5 最优),呈先升后降;说明在去偏与拟合数据分布之间取得了平衡。
- 内容兴趣匹配(仅 WeChat 有类别信息):VLDRec 的 size of intersection 最大、Jensen-Shannon divergence(JSD)最小,即推荐结果在个体与群体层面都最贴合用户真实兴趣,而回归类与 DecRS 表现较差。
- 论文还指出:回归方法在分长度组的 View_Time@K 上看似不错,但其预测分均值随视频长度上升、方差集中,说明它们只是"在每组内拟合得好"却无法跨长度区分真实偏好;VLDRec 各组均值、方差更平稳,因此更不受长度影响。

## 在本 wiki 中的位置

本文属于 [[recommender-system]] 的 [[debiasing]] 方向,聚焦微视频场景下以 [[watch-time]] 为目标的 video-length bias,可与 duration bias 相关工作(如 [[d2q]]、[[d2co]]、本文基线 DVR/[[wtg]])及 [[selection-bias]]/[[inverse-propensity-scoring]]、[[deconfounding]] 等通用去偏方法对照。其用 [[multi-task-learning]] 联合有偏/去偏样本、并以 [[deepfm]]/[[autoint]] 等为可替换基座的思路,体现了"从较少偏置反馈中学习内在偏好"的正则化范式;数据集 [[kuairand]]/[[kuairec]] 系列与本文 Kuaishou 数据同源。
