---
type: concept
subtype: method
tags: [value-function, reinforcement-learning, td-learning, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Value Function

价值函数(Value Function)用于估计在某状态(或状态-动作对)下,智能体遵循特定策略所能获得的期望累积回报,是强化学习中评估与改进策略的核心。

## 在本 wiki 中的出现

- [[2025-value-function-decomposition-mrp]]:提出把在线 RL 推荐中的标准 TD loss 分解为 state TD 与 action TD 两个独立目标,以分离随机策略与随机用户环境两类噪声,从而学到更准确、更快收敛、对动作探索更鲁棒的价值函数,并可通用插入 A2C/DQN/DDPG/HAC/SQN。

## 相关

- [[temporal-difference-learning]]
- [[reinforcement-learning]]
- [[policy-gradient]]
- [[rl-for-recommendation]]
