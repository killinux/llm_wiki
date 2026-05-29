---
type: concept
subtype: method
tags: [reinforcement-learning, recommendation, value-function, off-policy]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# SQN

SQN(Supervised Q-Network)是一种将监督学习信号与 Q-learning 价值估计相结合的强化学习方法,常用于推荐场景中,以引导价值函数的训练。

## 在本 wiki 中的出现

- [[2025-value-function-decomposition-mrp]]:提出把在线 RL 推荐中的标准 TD loss 分解为 state TD 与 action TD 两个独立目标,以分离随机策略与随机用户环境两类噪声,获得更准确、更快收敛、对动作探索更鲁棒的价值函数,可通用插入 A2C/DQN/DDPG/HAC/SQN。

## 相关

- [[value-function]]
- [[td-learning]]
- [[dqn]]
- [[a2c]]
- [[ddpg]]
- [[reinforcement-learning-recommendation]]
