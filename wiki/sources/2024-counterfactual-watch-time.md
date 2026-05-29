---
type: source
subtype: paper
tags:
  - recommender-system
  - duration-bias
  - watch-time
  - counterfactual-inference
  - video-recommendation
created: 2026-05-29
updated: 2026-05-29
arxiv: 2406.07932
raw: raw/2406.07932.pdf
authors:
  - Haiyuan Zhao
  - Guohao Cai
  - Jieming Zhu
  - Zhenhua Dong
  - Jun Xu
  - Ji-Rong Wen
year: 2024
---

提出 counterfactual watch time(CWT)概念与 Counterfactual Watch Model(CWM),从经济学视角建模用户观看行为,以消除视频推荐中的 duration bias 并更准确地估计用户兴趣与 watch time。

## 问题

在视频推荐中,watch time 被广泛用作用户兴趣的隐式反馈信号,但它会受到视频时长(duration)的影响,产生 **duration bias**:用户对越长的视频自然倾向于看更久,使得平均 watch time 在长视频上偏高,无法忠实反映兴趣。

已有的 label-correction 方法(如 Play Completion Rate (PCR)、Watch Time Gain (WTG)、Quantile-based D2Q)通过按视频时长分组并归一化来对齐不同时长下的 watch time 尺度。但作者在 KuaiRand 与 WeChat Channels 数据集上观察到:这些方法把所有 **完整播放(completely played)** 记录都当作同等的最高兴趣,而真实数据中完整播放视频的显式正反馈(点赞、转发)比例随时长增加而升高——也就是说不同时长下的完整播放并不代表相同兴趣水平。这说明现有方法不能正确解释和消除 duration bias。

## 方法

- **Counterfactual Watch Time(CWT)**:定义为"若视频时长足够长,用户基于兴趣愿意观看的潜在时长",与视频时长 $d_v$ 无关。观测 watch time 是 CWT 被视频时长截断(truncation)后的结果:$w_{u,v}=\min(w^c_{u,v}, d_v)$。完整播放记录对应 CWT 被截断,真实兴趣可能高于观测值。
- **存在性证据**:用真实数据中的两个现象支持 CWT 存在——(1) 用户的 repeated playing(重复回放导致实际观看超过时长),其比例与程度随时长缩短而增大;(2) 固定时长下 watch time 呈 **bimodal distribution**(双峰分布),可由被截断的 Gaussian CWT 解释。
- **经济学视角(economic view)**:把观看建模为累积 reward 与 cost 的过程,基于 utility maximization 与 rational choice,假设 diminishing marginal reward、constant marginal cost、rational users。当 marginal reward 等于 marginal cost 时用户停止观看,该时间点即 CWT。
- **cost-based transform function**:推导出 CWT 与用户兴趣 $r_{u,v}$ 的双向转换式 $w^c_{u,v}=g(r_{u,v};c)=\frac{1}{-c\log r_{u,v}}-1$,其中 $c$ 为每秒观看成本超参数。
- **counterfactual likelihood function**:借鉴 survival analysis,把观测 watch time 视为截断后的 CWT 分布;当 $w_{u,v}<d_v$ 时为 MSE 项,当完整播放时为 CWT 超过 $d_v$ 的概率项(amplification 项),通过最大似然 (MLE) 训练 duration-debiased 推荐模型。作者并给出 Theorem 1:仅靠对观测 watch time 的 transform function 无法恢复用户真实兴趣,论证现有方法的局限。

## 结果

- 数据集:KuaiRand(26,988 用户 / 6,598 视频 / 1.27M 交互,完整播放比例 17.5%)、WeChat(20,000 / 96,418 / 7.31M,45.5%)、工业 Product 数据集(2M / 1.01M / 36.4M,32.8%)。
- 评测两类任务:watch time 预测(指标 MAE、XAUC)与 relevance ranking(指标 AUC、nDCG@k),并在 FM、DCN、AutoInt 三种 backbone 上验证。
- watch time 预测:CWM 在几乎所有数据集与 backbone 上取得最优。例如 KuaiRand + FM 上 MAE 17.738(vs 第二名 D2Q 18.271)、XAUC 0.714;Product + FM 上 MAE 7.789、XAUC 0.833。
- relevance ranking:CWM 普遍最优,如 KuaiRand + FM AUC 0.735 / nDCG@3 0.486;Product + FM AUC 0.660 / nDCG@3 0.582,接近用真实标签训练的 Oracle 上界。
- 关键发现:WeChat 完整播放记录更多(45.5%),WTG、D2Q 等 debiasing 方法甚至差于直接拟合的 naive Value Regression (VR);CWM 在 WeChat 上提升反而更大,验证了"完整播放记录越多,现有方法越失效"的动机。
- 在 KuaiRand 按时长十等分的子集上,基线在长视频段表现下降,而 CWM 通过建模截断 CWT 在各时长段给出更公平的兴趣估计;消融与离线/在线 A/B 测试均证明其有效性。

## 在本 wiki 中的位置

本文属于 [[recommender-systems|recommender-system]] 方向中针对隐式反馈偏差的去偏研究,聚焦视频推荐特有的 duration bias 与 watch time 建模。其方法论根植于 [[causal-inference]] / [[counterfactual-reasoning]] 中的 [[debiasing]] 与 [[selection-bias]] 思路,与处理 position bias、popularity bias 的 counterfactual information retrieval 工作一脉相承。与本 wiki 中关于 watch time 去偏的相关概念 [[watch-time]]、[[duration-bias]]、[[d2q]] 直接相关,数据集层面涉及 [[kuairand]]、[[wechat-channels-dataset]]。作者团队来自 [[renmin-university-of-china]] 与 [[huawei-noahs-ark-lab]],相关研究者包括 [[jun-xu]]、[[ji-rong-wen]]、[[zhenhua-dong]]、[[jieming-zhu]]。
