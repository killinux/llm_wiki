---
type: concept
subtype: method
tags: [reinforcement-learning, constrained-optimization, mdp, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Constrained MDP

Constrained MDP(CMDP,约束马尔可夫决策过程)是在标准 MDP 的基础上引入一个或多个约束信号的决策框架:在最大化主奖励(累积回报)的同时,要求若干辅助代价(cost)的期望累积值满足给定阈值,从而把"在限制条件下做最优决策"的问题形式化。

## 在本 wiki 中的出现

- [[2023-two-stage-constrained-actor-critic]]:将短视频推荐建模为多目标优化问题,并借鉴 Constrained MDP 的思路提出 TSCAC(Two-Stage Constrained Actor-Critic)。第一阶段为每个辅助目标(如 Like、Share 等稀疏交互)各自训练 policy,第二阶段以最大化主目标 WatchTime 为优化目标,同时把辅助目标作为软约束(soft constraint)加以平衡,使主目标提升而不显著牺牲辅助交互。该方法已在快手生产系统全量上线。

## 相关

- [[markov-decision-process]]
- [[actor-critic]]
- [[reinforcement-learning]]
- [[multi-objective-optimization]]
- [[lagrangian-relaxation]]
- [[short-video-recommendation]]
