---
type: source
subtype: paper
tags: [reinforcement-learning, recommender-systems, short-video, constrained-rl, actor-critic, kuaishou]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2302.01680
raw: raw/2302.01680.pdf
authors: [Qingpeng Cai, Zhenghai Xue, Chi Zhang, Wanqi Xue, Shuchang Liu, Ruohan Zhan, Xueliang Wang, Tianyou Zuo, Wentao Xie, Dong Zheng, Peng Jiang, Kun Gai]
year: 2023
---

# Two-Stage Constrained Actor-Critic for Short Video Recommendation

提出 TSCAC:一个两阶段的约束式 actor-critic 强化学习方法,在最大化短视频主目标(WatchTime)的同时,软约束式地平衡 Like/Follow/Share 等多种稀疏交互信号,已在快手生产系统全量上线。

## 问题

短视频平台上,用户在一个 session 内会连续滑动观看多个视频,并给出多维度反馈:既有稠密的 WatchTime(观看时长,主目标),也有稀疏的交互信号 Like / Follow / Comment / Share / Collect(辅助目标)。平台希望长期最大化累计 WatchTime,同时不过度牺牲其他交互。作者把该问题形式化为一个 **Constrained Markov Decision Process(CMDP)**:在满足辅助响应约束的前提下最大化主响应的累计回报。

传统的约束强化学习方法(如 [[rcpo]] 通过拉格朗日乘子最大化拉格朗日量)在该场景下失效,原因有二:
- **单一价值模型不足**:不同类型的响应有不同的折扣因子和观测频率(WatchTime 稠密、交互稀疏),用一个价值模型联合评估会让稠密信号淹没稀疏信号;
- **多约束难搜索**:多个约束意味着要在高维的拉格朗日乘子空间上做网格搜索,代价高昂、训练耗时。

## 方法

本文提出 **Two-Stage Constrained Actor-Critic(TSCAC)**,核心由两部分组成:

- **Multi-Critic Policy Estimation(多评论家策略评估)**:为每种响应单独学习一个价值模型,而非把所有响应求和后联合评估。作者在快手一天数据上验证:相比联合评估 V_joint,分离评估 V_separate 与 Monte Carlo 真值在 WatchTime 与交互上的相关性分别提升 0.19% 与 0.14%。
- **两阶段 actor 学习**:
  - **阶段一(Stage One)**:为每个辅助响应 i 单独学一个策略 π_{θ_i},用各自的 critic 和折扣因子最大化该响应的累计回报。
  - **阶段二(Stage Two)**:学习主响应策略 π_{θ_1},既最大化主响应(WatchTime)的累计回报,又通过 KL 散度软约束把它限制在阶段一学到的各辅助策略附近。论文给出了该约束优化(拉格朗日)的闭式解(Theorem 1),并把所有约束的拉格朗日乘子 λ 设为同一值以便生产部署。

方法还讨论了离线学习(用重要性采样做策略梯度偏差校正)与确定性策略(用打分函数 h 衡量动作接近度)两种扩展,可用于连续动作空间。整体训练/推理流程基于 actor + critic + replay buffer + ranking function 的工业级管线(Figure 4)。

## 结果

**离线实验(KuaiRand 数据集)**,以 NCIS(Normalised Capped Importance Sampling)评估,与 [[rcpo]]、RCPO-Multi-Critic、[[pareto]]、BC、Wide&Deep、DeepFM 等基线对比(Table 2):
- TSCAC 在主目标 WatchTime 上取得最高分 **13.14**(相对 BC 提升 **+2.23%**);RCPO 为 13.07(+1.70%),Pareto 仅 11.90(-7.4%)。
- 在 4 个辅助分数中的 3 个(Click 0.5570、Like 1.462e-2、Comment 3.728e-3)也取得最高;Hate 上 Pareto 最低(代价是牺牲主目标)。
- 消融显示拉格朗日乘子 **λ=1e-4** 时交互表现最好且能显著改善 WatchTime。

**离线实验(TripAdvisor 酒店评论数据集,257932 条评论,Table 4)**:TSCAC 的 overall rating 达 **3.99**(全场最高),并在 7 个辅助分数中的 5 个(service、cleanliness、value、rooms、location)排第一。

**线上实验(快手生产系统候选排序,Table 3,对比 LTR 基线)**:
- TSCAC:WatchTime **+0.379%**、Share **+3.376%**、Download **+1.733%**、Comment -0.619%。
- 0.1% 的 WatchTime 提升与 1% 的交互提升在该平台均为统计显著。
- 相比 RCPO,TSCAC 在 WatchTime 与各交互维度上均更优。方法已在生产系统全量上线。

## 在本 wiki 中的位置

本文属于把 [[reinforcement-learning]] 应用于推荐系统的方向,聚焦于多目标/约束场景下的 [[constrained-mdp]] 建模。它与 [[rcpo]](拉格朗日约束策略优化)、[[pareto]](多目标 Pareto 最优)等约束/多目标 RL 方法形成对照,代表了工业短视频推荐(快手)中通过 [[actor-critic]] 框架平衡稠密主目标与稀疏辅助目标的实践路线。
