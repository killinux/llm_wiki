---
type: concept
subtype: method
tags: [reinforcement-learning, actor-critic, recommendation, value-function]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Hyper-Actor-Critic (HAC)

Hyper-Actor-Critic (HAC) 是一类用于(在线)推荐场景的 Actor-Critic 强化学习方法,可与价值函数分解等通用技术结合使用。

## 在本 wiki 中的出现

- [[2025-value-function-decomposition-mrp]]:提出把在线 RL 推荐中的标准 TD loss 分解为 state TD 与 action TD 两个独立目标,以分离随机策略与随机用户环境两类噪声,获得更准确、更快收敛、对动作探索更鲁棒的价值函数,可通用插入 A2C/DQN/DDPG/HAC/SQN。

## 相关

- [[a2c]]
- [[dqn]]
- [[ddpg]]
- [[sqn]]
- [[value-function-decomposition]]
- [[td-loss]]
