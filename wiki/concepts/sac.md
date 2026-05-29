---
type: concept
subtype: method
tags: [reinforcement-learning, max-entropy, offline-rl, exploration]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# SAC

SAC(Soft Actor-Critic)是一种基于最大熵强化学习框架的离线策略(off-policy)算法,通过在最大化累积奖励的同时最大化策略熵,来鼓励探索并提升样本效率与训练稳定性。

## 在本 wiki 中的出现

- [[2024-edt4rec-max-entropy-decision-transformer]]:EDT4Rec 给 Decision Transformer 加入最大熵探索与基于 CQL Q-function 的 reward relabeling,体现了最大熵思想在序列决策中提升在线探索能力的作用。

## 相关

- [[max-entropy-rl]]
- [[decision-transformer]]
- [[offline-rl]]
- [[cql]]
