---
type: concept
subtype: method
tags: [offline-rl, recsys, reward-shaping, world-model, uncertainty]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# CIRS

CIRS(Causal Inference for Recommendation Systems / 因果干预推荐方法)是一类用于推荐系统的强化学习方法,旨在通过对反馈回路中的混杂与偏差进行建模与修正,缓解 model-based offline RL 在推荐场景中因 world model 估计误差导致的策略退化问题。

## 在本 wiki 中的出现

- [[2024-roler-reward-shaping-offline-rl-recsys]]:ROLeR 用非参数(kNN/聚类)reward shaping 与解耦的不确定性惩罚修正 model-based offline RL 推荐中 world model 的 reward 估计误差,在 KuaiRand/KuaiRec/Coat/Yahoo 四个 benchmark 上达到 SOTA。

## 相关

- [[reward-shaping]]
- [[model-based-offline-rl]]
- [[world-model]]
- [[uncertainty-penalty]]
- [[recommendation-system]]
