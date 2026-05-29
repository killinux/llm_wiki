---
type: entity
subtype: model
tags: [offline-rl, recommendation, model-based-rl, matthew-effect]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# DORL

DORL 是一种基于模型的离线强化学习(model-based offline RL)推荐方法,通过在悲观惩罚之外引入熵惩罚来缓解推荐系统中的马太效应(Matthew effect),从而提升交互式推荐的用户长期满意度。

## 在本 wiki 中的出现

- [[2023-dorl-matthew-effect-offline-rl-recommendation]]:提出 DORL,在 model-based offline RL 的悲观惩罚上加入熵惩罚以缓解推荐中的马太效应,提升交互式推荐的用户长期满意度。
- [[2025-reward-balancing-revisited]]:提出 R3S,用 diffusion world model 显式建模 reward 不确定性并配合带衰减的多样性惩罚,在 offline RL 推荐中同时平衡 world model 偏差与策略多样性,在 Coat/Yahoo/KuaiRand 上超越 DORL、ROLeR 等 11 个 baseline。

## 相关

- [[offline-rl]]
- [[model-based-rl]]
- [[matthew-effect]]
- [[interactive-recommendation]]
- [[pessimism-penalty]]
- [[roler]]
