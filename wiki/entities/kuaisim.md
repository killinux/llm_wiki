---
type: entity
subtype: benchmark
tags: [recommendation, simulator, reinforcement-learning, long-term-user-satisfaction]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# KuaiSim

KuaiSim 是一个面向交互式推荐系统的用户模拟器,用于在模拟环境中评估和优化(尤其是基于强化学习的)推荐策略对长期用户满意度的影响。

## 在本 wiki 中的出现
- [[2025-value-function-decomposition-mrp]]:提出把在线 RL 推荐中的标准 TD loss 分解为 state TD 与 action TD 两个独立目标,以分离随机策略与随机用户环境两类噪声,获得更准确、更快收敛、对动作探索更鲁棒的价值函数,可通用插入 A2C/DQN/DDPG/HAC/SQN。
- [[reinforcement-learning]]
- [[recommender-systems|recommendation-system]]
- [[temporal-difference-learning]]
- [[value-function-decomposition]]

- [[2026-lerl-llm-enhanced-rl-long-term-recommendation]]:分层框架 LERL 用 LLM 做高层语义类别规划、用 RL(PPO)做低层细粒度物品选择,在 KuaiSim 模拟器上优化交互式推荐的长期用户满意度并缓解 filter bubble。
- [[2026-fairness-begins-with-state-dsrm-hrl]]:DSRM-HRL 用扩散模型把被 popularity bias 污染的用户状态提纯回真实偏好流形,再用分层 RL 解耦长期公平与短期参与,在 KuaiRec/KuaiRand 上实现 accuracy 与 fairness 更优的 Pareto 前沿。
- [[2026-entropy-guided-agentic-recommendation]]:提出 IDSS,用 Shannon 熵作为统一信号贯穿对话式推荐的偏好询问、排序与多样化呈现三阶段,在用户意图模糊时兼顾追问效率与残余不确定性驱动的多样化推荐。

## 相关

- [[kuairec]]
- [[kuairand]]
- [[hierarchical-reinforcement-learning]]
- [[interactive-recommendation]]
- [[long-term-user-satisfaction]]
