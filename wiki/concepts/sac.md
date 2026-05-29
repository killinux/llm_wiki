---
type: concept
subtype: method
tags: [reinforcement-learning, max-entropy, offline-rl, exploration]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# SAC

SAC(Soft Actor-Critic)是一种基于最大熵强化学习框架的离线策略(off-policy)算法,通过在最大化累积奖励的同时最大化策略熵,来鼓励探索并提升样本效率与训练稳定性。

## 在本 wiki 中的出现

- [[2024-edt4rec-max-entropy-decision-transformer]]:EDT4Rec 给 Decision Transformer 加入最大熵探索与基于 CQL Q-function 的 reward relabeling,体现了最大熵思想在序列决策中提升在线探索能力的作用。
- [[2025-policy-guided-causal-state-representation]]:PGCR 面向离线 RL 推荐的两阶段因果状态表示框架,用策略引导的因果特征选择隔离因果相关分量,再用 encoder 学习紧凑状态表示。
- [[2025-xmtf-formula-free-multi-task-fusion]]:xMTF 用可学习的单调融合单元(MFC)替代多任务融合中的预定义公式,配合 RL 外层 + 监督内层的两阶段混合训练,离线 Total Watch Time 1279.7s 超越全部基线,线上 Daily Watch Time +0.833%,Kuaishou 全量部署服务超 1 亿用户。

## 相关

- [[max-entropy-rl]]
- [[decision-transformer]]
- [[offline-rl]]
- [[cql]]
