---
type: concept
subtype: method
tags: [reinforcement-learning, value-function, td-learning, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# TD Decomposition

TD Decomposition(时序差分分解)是一种把标准 TD loss 拆分为 state TD 与 action TD 两个独立学习目标的方法,用于分离价值函数学习中随机策略与随机环境带来的不同噪声来源。

## 在本 wiki 中的出现

- [[2025-value-function-decomposition-mrp]]:提出把在线 RL 推荐中的标准 TD loss 分解为 state TD 与 action TD 两个独立目标,以分离随机策略与随机用户环境两类噪声,获得更准确、更快收敛、对动作探索更鲁棒的价值函数,可通用插入 A2C/DQN/DDPG/HAC/SQN。

## 相关

- [[temporal-difference-learning]]
- [[value-function]]
- [[reinforcement-learning-recommendation]]
- [[a2c]]
- [[dqn]]
- [[ddpg]]
