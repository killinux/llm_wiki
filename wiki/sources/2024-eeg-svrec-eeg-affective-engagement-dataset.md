---
type: source
subtype: paper
tags:
  - dataset
  - recommender-system
  - short-video
  - eeg
  - affective-computing
  - user-modeling
created: 2026-05-29
updated: 2026-05-29
arxiv: 2404.01008
raw: raw/2404.01008.pdf
authors:
  - Shaorun Zhang
  - Zhiyu He
  - Ziyi Ye
  - Peijie Sun
  - Qingyao Ai
  - Min Zhang
  - Yiqun Liu
year: 2024
---

# EEG-SVRec: An EEG Dataset with User Multidimensional Affective Engagement Labels in Short Video Recommendation

EEG-SVRec 是首个在真实短视频观看场景下采集 EEG(脑电)信号、并配以多维情感参与度标注(MAES)与用户行为日志的数据集,用于探索短视频[[recommender-system]]中用户的情感体验与认知活动。

## 问题

现有短视频推荐系统主要依赖行为指标(点赞、停留时长、view percentage 等)作为隐式反馈来推断用户偏好。但行为数据存在两个核心局限:

- **数据稀疏**:点赞、评论等显式行为本身就少。
- **噪声**:误触、个人习惯造成的偶然交互会污染信号可靠性。

更重要的是,仅靠行为数据无法刻画用户在观看时的**认知活动**与**情感体验**。论文主张引入 EEG 这一神经电信号——它含有丰富的空间、时间、频带信息,能反映认知、情绪、注意力等底层神经机制,且近年低成本、便携、高时间分辨率的设备使其在真实短视频场景落地成为可能。目标是建立一个把脑信号、情感参与度与推荐行为关联起来的数据集与 benchmark。

## 方法

**数据采集流程**(实验室用户研究):

- 招募 30 名 18–30 岁大学生(M=22.17,16 男 14 女),每人先经历一周共 10 小时的偏好信息采集阶段,再进入约 3 小时的实验室阶段。
- 实验室阶段分为 **Browsing Stage**(15 分钟浏览,可点赞 like / 划走 swipe away)与 **Labelling Stage**(约 10 分钟逐视频自评),每次 session 含 20–30 个短视频,每人观看 4–5 个 session。
- 设备:6.67 英寸 120Hz 手机播放;64 通道 Quik-Cap(Compumedics NeuroScan)采集 EEG/ECG,采样率 1000Hz,采集 62 个有效通道,阻抗 <10kΩ。

**视频池(open domain)**:从平台真实的 personalized(个性化推荐)、non-personalized(按热度)、randomized(按播放量分层随机)三类视频池抽取,组合出 personalized / randomized / mixed / non-personalized 四种 session 模式;mixed 模式按 1:1 混合个性化与随机视频。

**多维情感参与度评分(MAES, Multidimensional Affective Engagement Scores)**:每个视频在 5 分制 Likert 量表上从六个维度自评——valence(效价)、arousal(唤醒度)、immersion(沉浸)、interest(兴趣)、visual(视觉)、auditory(听觉)。

**EEG 预处理与特征**:baseline correction → 以 M1/M2 乳突电极平均做 re-referencing → 0.5–50Hz 带通滤波(并去 50Hz 工频)→ 伪迹去除(眼动/头动)。特征采用 differential entropy(DE,微分熵),在 delta(0.5–4Hz)、theta(4–8Hz)、alpha(8–13Hz)、beta(13–30Hz)、gamma(25–50Hz)五个频带上,对每个电极每秒提取一个 DE,公式为 DE = −∫ P(f) log(P(f)) df,功率谱用 Welch 方法估计。

## 结果

**数据集规模**(Table 2):30 用户、2,636 个短视频(item)、3,657 次交互、62GB EEG 数据。每次交互对应一段 EEG/ECG、一条行为日志和一组六维 MAES 自评。

**行为与 session 模式统计**(Figure 3):like 比例 personalized=35.9%、mixed=35.4% 相近,而 randomized=21.4% 明显偏低;personalized 与 mixed 的 view percentage 高于 randomized。

**行为—MAES 相关性**(Figure 5):Liking 与 Interest 相关最强(0.56),其次 Immersion(0.53)、Valence(0.51);View Percentage 与 Immersion(0.50)、Interest(0.52)相关最高——说明浏览时长更受兴趣与沉浸度驱动,而非单纯效价/唤醒。

**EEG—行为/情感相关性**(Figure 6):额叶区域 gamma 频带与多个 MAES 及行为标注一致地呈现强相关,提示 gamma 波与决策、注意、工作记忆等高级认知功能相关。

**推荐 benchmark**(Table 3,AUC,使用 RecBole,5 种模型 FM / DeepFM / AFM / WideDeep / DCN-V2,数据 7:1:2 划分,EEG 用 310 维 DE = 62 通道 × 5 频带):在多数 model × 反馈信号组合上,加入 EEG(id+EEG)优于仅 id。例如 FM 的 Like AUC 0.7152→0.7312(*),DeepFM 的 Like 0.7331→0.7368、Valence 0.6379→0.6586(*),WideDeep 的 Like 0.7324→0.7387、VisualPref 0.6718→0.6978(*)。表明 EEG 含有超出行为数据的额外有用信息(* 表示 p<0.05)。

**局限**:样本仅 30 人(EEG 采集成本高);30–60 秒视频可能与一般场景不同;数据可能带有平台推荐算法偏置(论文用 randomized 视频作为无偏数据应对)。

## 在本 wiki 中的位置

本文属于 [[recommender-system]] 与用户建模方向的数据集论文,其特色是把脑机接口/情感计算引入推荐:用 EEG 信号补充传统[[user-simulation]]之外的真实生理反馈,提供超越点赞/[[watch-time]]的人本评估维度。

可与本 wiki 中其它推荐场景数据集对照:同为短视频/快手系数据集的 [[kuairand]]、[[kuairec]];以及推荐工具与模型谱系中的 [[deepfm]]、[[factorization-machines]]([[fm]])、[[autoint]] 等(本文 benchmark 即在 FM/DeepFM/AFM 等[[ctr]]模型上验证 EEG 特征的增益)。作者团队来自 [[tsinghua-university]],与 [[qingyao-ai]]、[[min-zhang]] 等信息检索研究者相关。
