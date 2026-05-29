---
type: entity
subtype: model
tags: [reinforcement-learning, deep-learning, q-learning, model]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# DQN

DQN(Deep Q-Network)是一种将深度神经网络与 Q-learning 结合的强化学习模型,用神经网络近似动作价值函数 Q(s, a),并通过经验回放与目标网络稳定训练。

## 在本 wiki 中的出现

- [[2024-llm-powered-user-simulator-for-recommender-system]]:该工作用 LLM 离线蒸馏用户偏好关键词与情感,在线用逻辑+统计集成模型显式推断 like/dislike,构建可解释、低幻觉、低成本的推荐系统用户模拟器;此类模拟器常用于为基于 RL(如 DQN)的推荐策略提供训练与评估环境。

## 相关

- [[q-learning]]
- [[reinforcement-learning]]
- [[recommender-systems|recommender-system]]
- [[2024-llm-powered-user-simulator-for-recommender-system]]
