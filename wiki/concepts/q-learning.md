---
type: concept
subtype: method
tags: [reinforcement-learning, value-based, off-policy, temporal-difference]
created: 2026-05-31
updated: 2026-05-31
sources: 0
---

# Q-Learning

Q-Learning 是一种经典的**无模型、off-policy** 强化学习算法。它学习一个动作-价值函数 Q(s, a)，表示在状态 s 下执行动作 a 后能获得的期望累积回报，并用 Bellman 最优方程的 TD 更新逐步逼近最优 Q*。

## 核心机制

- **TD 更新**：Q(s,a) ← Q(s,a) + α[r + γ max_a' Q(s',a') − Q(s,a)]
- **Off-policy**：行为策略（如 ε-greedy 探索）与目标策略（greedy on Q）分离，因此可以从任意经验中学习。
- **Deep Q-Network (DQN)**：将 Q 函数用神经网络参数化，加入经验回放和目标网络稳定训练（Mnih et al., 2015），是深度强化学习的里程碑。

## 在推荐中的应用

推荐系统中，Q-Learning / DQN 被用于将推荐建模为序列决策：状态为用户历史，动作为推荐物品，奖励为用户反馈。[[offline-rl]] 场景下需额外处理 OOD 动作问题（如 [[bcq]]）。

## 相关页

[[reinforcement-learning]]、[[offline-rl]]、[[temporal-difference]]、[[actor-critic]]、[[bcq]]、[[exploration-exploitation]]
