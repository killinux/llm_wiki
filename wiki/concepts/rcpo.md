---
type: concept
subtype: method
tags: [reinforcement-learning, constrained-optimization, actor-critic, lagrangian, reward-shaping]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# RCPO

RCPO(Reward Constrained Policy Optimization)是一种用于约束强化学习的方法,通过 Lagrangian 松弛将约束以惩罚项的形式融入 reward,从而在优化主目标的同时满足对其它指标的约束。

## 在本 wiki 中的出现

- [[2023-two-stage-constrained-actor-critic]]:该工作提出 TSCAC(两阶段约束式 actor-critic),在最大化短视频 WatchTime 主目标的同时软约束平衡 Like/Share 等稀疏交互,并已在快手生产系统全量上线。RCPO 作为约束强化学习中处理多目标/约束的经典 Lagrangian 类方法,与该工作所采用的约束式 actor-critic 思路同源,常被用作此类问题的对照或基础方法。

## 相关

- [[constrained-policy-optimization]]
- [[lagrangian-relaxation]]
- [[actor-critic]]
- [[2023-two-stage-constrained-actor-critic]]
- [[reward-shaping]]
