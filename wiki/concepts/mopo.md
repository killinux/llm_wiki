---
type: concept
subtype: method
tags: [offline-rl, model-based-rl, uncertainty, reward-shaping]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# MOPO

MOPO(Model-based Offline Policy Optimization)是一种基于模型的离线强化学习方法,通过对学习到的 world model 施加不确定性惩罚来约束策略在数据分布外区域的行为,从而在离线数据上安全地进行 model-based 策略优化。

## 在本 wiki 中的出现

- [[2024-roler-reward-shaping-offline-rl-recsys]]:ROLeR 用非参数(kNN/聚类)reward shaping 与解耦的不确定性惩罚修正 model-based offline RL 推荐中 world model 的 reward 估计误差,在 KuaiRand/KuaiRec/Coat/Yahoo 四个 benchmark 上达到 SOTA。
- [[2025-reward-balancing-revisited]]:提出 R3S,用 diffusion world model 显式建模 reward 不确定性并配合带衰减的多样性惩罚,在 offline RL 推荐中同时平衡 world model 偏差与策略多样性,在 Coat/Yahoo/KuaiRand 上超越 DORL、ROLeR 等 11 个 baseline。

## 相关

- [[offline-rl]]
- [[model-based-rl]]
- [[world-model]]
- [[uncertainty-penalty]]
- [[reward-shaping]]
