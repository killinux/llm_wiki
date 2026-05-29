---
type: entity
subtype: model
tags: [offline-rl, batch-rl, q-learning, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# BCQ

BCQ(Batch-Constrained deep Q-learning)是一种 offline / batch reinforcement learning 算法,通过约束策略只在数据集中出现过的动作附近选择,以缓解 off-policy 学习中的分布外(out-of-distribution)动作带来的外推误差。

## 在本 wiki 中的出现

- 在 [[2023-dorl-matthew-effect-offline-rl-recommendation]] 中,BCQ 作为 offline RL 的对比 / 基线方法出现。该论文提出 DORL,在 model-based offline RL 的悲观惩罚上加入熵惩罚以缓解推荐中的马太效应,提升交互式推荐的用户长期满意度;BCQ 属于其讨论的 offline RL 方法范畴。

## 相关

- [[offline-rl]]
- [[batch-rl]]
- [[dorl]]
- [[matthew-effect]]
- [[interactive-recommendation]]
