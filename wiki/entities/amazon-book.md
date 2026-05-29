---
type: entity
subtype: dataset
tags: [dataset, recommendation, llm-agent]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Amazon-Book

Amazon-Book 是源自亚马逊图书品类的用户-物品交互数据集,常用于推荐系统与基于 LLM 的推荐方法的训练与评测。

## 在本 wiki 中的出现

- [[2024-generative-agents-in-recommendation]]:Agent4Rec 用 1000 个 LLM 驱动的生成式 agent(含 profile/memory/action 模块)构建电影推荐用户模拟器,探究其能否忠实模拟真实用户行为并复现 filter bubble 与 popularity bias。
- [[2024-llm-learnable-planners-long-term-recommendation]]:提出 BiLLP 双层可学习 LLM 规划框架(Planner/Reflector 宏观 + Actor/Critic 微观),在稀疏推荐数据上以 LLM 规划能力做长期推荐,Len 与累积奖励超越从零训练的 RL 与现有 LLM agent 基线。
- [[2025-value-function-decomposition-mrp]]:提出把在线 RL 推荐中的标准 TD loss 分解为 state TD 与 action TD 两个独立目标,以分离随机策略与随机用户环境两类噪声,获得更准确、更快收敛、对动作探索更鲁棒的价值函数,可通用插入 A2C/DQN/DDPG/HAC/SQN。

## 相关

- [[recommender-systems|recommendation-system]]
- [[llm-agents|llm-agent]]
- [[movielens]]
