---
type: source
subtype: paper
tags:
  - recommender-system
  - reinforcement-learning
  - multi-agent
  - model-based-rl
  - short-video
  - selection-bias
created: 2026-05-29
updated: 2026-05-29
arxiv: "2405.01847"
raw: raw/2405.01847.pdf
authors:
  - Peilun Zhou
  - Xiaoxiao Xu
  - Lantao Hu
  - Han Li
  - Peng Jiang
year: 2024
---

# A Model-based Multi-Agent Personalized Short-Video Recommender System

提出 MMRF(Model-based Multi-agent Ranking Framework):用协作式多智能体 RL 最大化短视频会话的累计 WatchTime,并用 model-based 的反馈拟合模型缓解工业推荐中的样本选择偏差(SSB),已在快手量级平台部署、服务数亿用户。

## 问题

短视频 app(TikTok、YouTube Shorts、Kuaishou 等)把一次推荐会话(session)建模为 [[markov-decision-process]] 并用 [[reinforcement-learning]] 求解,以优化每次会话的长期累计满意度。两个关键但少被公开讨论的问题:

1. **多维用户偏好的协作关系**:用户体验由多方面反馈衡量——WatchTime(观看时长,主目标)以及 Follow、Like、Comment 等显式交互(辅助目标)。已有工作多把 WatchTime 与显式交互当作此消彼长的 trade-off(如 TSCAC),但实际上并非全部交互都与 WatchTime 竞争(例如评论一个视频的用户往往观看更久),存在可利用的**协作关系**。
2. **样本选择偏差 SSB(Sample Selection Bias)**:工业推荐多用 logged impressions 离线训练,以免在线学习损害体验。但排序模型对全空间(约 400 个候选)打分,只有约 6 个被曝光并获得反馈,未曝光样本(non-impression)无反馈,导致 SSB。

## 方法

**MMRF** 把会话建模为 MDP 的多智能体扩展:取 N 个 agent,第 N 个 agent 最大化 WatchTime(主目标),其余 N-1 个 agent 各负责一个辅助偏好维度。State 含用户画像、行为历史、请求上下文与候选特征(各 agent 共享);Action 是各 agent 给出的 item 打分列表;Reward 按维度分解。目标是最大化会话级折扣累计 WatchTime。

- **Attentive Collaboration Mechanism**:用多头 [[attention]] 在 agent 间选择性聚合有益信息(query/key/value 权重跨 agent 共享,鼓励共同 embedding 空间);WatchTime agent 综合各辅助 agent 的中间决策知识与直接打分结果做最终决策。
- **Policy Learning**:动作空间连续,采用 deterministic policy gradient(DPG);各 agent 为 [[actor-critic]] 结构,辅助 agent 同时兼顾私有辅助目标与主目标的梯度。
- **Model-based 缓解 SSB**:引入 non-impression 样本(随机采约 25%),用一个 RNN 的**用户反馈拟合模型(feedback simulator)** 为它们模拟多维反馈(多头输出 + MSE 拟合)。借鉴 [[random-network-distillation]] 的思路,用 siamese 双预测器 + dropout 估计不确定性,把不确定性以 KL 散度形式放大模拟 reward,鼓励对高不确定性样本探索。simulator 与多 agent 迭代交替训练(Algorithm 1)。

## 结果

**离线**:数据集为公开 [[kuairand]]1K 与一份真实生产数据(一周日志,1.8B 用户、1.0B 视频、245B 交互)。评测指标为 NCIS(Normalised Capped Importance Sampling)与 GAUC。基线含 BC、Wide&Deep、[[deepfm]]、[[pareto]] (多目标 RL)、TSCAC(两阶段约束 actor-critic)、MASSA(无通信多 agent)。

- 主目标 WatchTime:MMRF 取得最高,相对提升约 **+7.3% GAUC、+7.1% NCIS**。
- 辅助目标:MMRF 在 6 个维度中 4 个进入 top2。Pareto 虽是 pareto 最优但 WatchTime 表现平庸(GAUC -0.7%)。
- 消融:MMRF 在 7 个满意度维度中 5 个优于 MMRF-CO(无协作);相比 MMRF-DA(不学 non-impression 样本),反馈 simulator 在 follow 上带来 >12.7% NCIS、hate 上 2.3% NCIS 提升;MMRF-NS(对未曝光样本赋负常数 reward)无明显优势,说明简单引入未曝光样本不能有效解决 SSB。

**在线 A/B**:相对 LTR 基线(对比 TSCAC),MMRF 取得 WatchTime **+0.55%**、Depth **+0.54%**、Follow **+1.45%**、Comment **+1.28%**,均高于已被高度优化的 TSCAC(分别 +0.32%/+0.31%/+0.69%/+0.42%)。作者指出在成熟平台上 0.5% 的 WatchTime 提升已很关键。已部署于真实大规模短视频平台,服务数亿用户。

## 在本 wiki 中的位置

本文属于 [[recommender-systems|recommender-system]] 中的 RL 排序方向,与 [[watch-time]] 优化、会话级 [[markov-decision-process]] 建模一脉相承。它把 [[llm-multi-agent]] 之外的另一类"多智能体"——每个偏好维度一个 RL agent 的协作 actor-critic——用于工业短视频排序,并以 [[model-based-rl]] 的反馈模拟应对 [[selection-bias]]。可与 [[qingpeng-cai]] 等人的 TSCAC、[[kuairand]] 数据集、[[peng-jiang]] / [[kuaishou]] 的工业推荐工作互参。作者来自 [[kuaishou]] / [[bytedance-research]] 之外的工业推荐团队(快手系作者署名),与 [[deepfm]]、[[pareto]] 等推荐基线形成对照。
