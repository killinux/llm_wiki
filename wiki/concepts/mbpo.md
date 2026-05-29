---
type: concept
subtype: method
tags: [model-based-rl, reinforcement-learning, world-model, offline-rl]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# MBPO

MBPO(Model-Based Policy Optimization)是一种基于模型的强化学习方法,通过学习环境的 world model 生成短程合成 rollout 来增强样本效率,并在此基础上进行策略优化。

## 在本 wiki 中的出现

- [[2025-reward-balancing-revisited]]:提出 R3S,用 diffusion world model 显式建模 reward 不确定性并配合带衰减的多样性惩罚,在 offline RL 推荐中同时平衡 world model 偏差与策略多样性,在 Coat/Yahoo/KuaiRand 上超越 DORL、ROLeR 等 11 个 baseline。

## 相关

- [[world-model]]
- [[offline-rl]]
- [[reward-model]]
