---
type: concept
subtype: method
tags: [reinforcement-learning, value-function, td-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Temporal Difference Learning

时序差分(TD)学习是一类强化学习方法,通过自举(bootstrap)用后续状态的价值估计来更新当前状态的价值函数,无需等待完整回合结束即可在线学习。

## 在本 wiki 中的出现

- [[2025-value-function-decomposition-mrp]]:提出把在线 RL 推荐中的标准 TD loss 分解为 state TD 与 action TD 两个独立目标,以分离随机策略与随机用户环境两类噪声,获得更准确、更快收敛、对动作探索更鲁棒的价值函数,可通用插入 A2C/DQN/DDPG/HAC/SQN。
- [[2026-cs3-capability-synergy-two-tower]]:CS3 是快手提出的通用框架,通过 Cycle-Adaptive Structure、Cross-Tower Synchronization、Cascade-Model Sharing 三个模块让 two-tower 召回模型感知自身、对侧塔与下游 cascade 模型,提升容量与跨阶段一致性,线上广告收入最高提升 8.36%。

## 相关

- [[value-function]]
- [[reinforcement-learning]]
- [[actor-critic]]
- [[q-learning]]
