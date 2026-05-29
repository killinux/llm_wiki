---
type: entity
subtype: model
tags: [model-based-offline-rl, offline-rl, pessimism, uncertainty-penalty]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# MOPO

MOPO(Model-based Offline Policy Optimization)是一种 model-based offline RL 方法,通过在学习到的环境模型奖励上施加基于模型不确定性的悲观惩罚来约束策略,避免在数据分布之外的区域过度乐观。

## 在本 wiki 中的出现
- [[2024-roler-reward-shaping-offline-rl-recsys]]:ROLeR 用非参数(kNN/聚类)reward shaping 与解耦的不确定性惩罚修正 model-based offline RL 推荐中 world model 的 reward 估计误差,在 KuaiRand/KuaiRec/Coat/Yahoo 四个 benchmark 上达到 SOTA。
- [[2025-reward-balancing-revisited]]:提出 R3S,用 diffusion world model 显式建模 reward 不确定性并配合带衰减的多样性惩罚,在 offline RL 推荐中同时平衡 world model 偏差与策略多样性,在 Coat/Yahoo/KuaiRand 上超越 DORL、ROLeR 等 11 个 baseline。
- [[model-based-rl]]
- [[world-model]]
- [[uncertainty-penalty]]
- [[reward-shaping]]

- 在 [[2023-dorl-matthew-effect-offline-rl-recommendation]] 中,MOPO 作为 model-based offline RL 中"悲观惩罚"思路的基础/参照:DORL 在这类悲观惩罚之上额外加入熵惩罚,以缓解交互式推荐中的马太效应并提升用户长期满意度。

## 相关

- [[2023-dorl-matthew-effect-offline-rl-recommendation]]
- [[model-based-offline-rl]]
- [[offline-rl]]
- [[pessimism]]
- [[matthew-effect]]
