---
type: entity
subtype: model
tags: [recommendation, causal-inference, confounder, VAE]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Deep-Deconf

Deep-Deconf 是一个面向推荐系统的因果去混杂模型,通过深度 VAE 推断 substitute confounders,以消除推荐中的混杂偏差。

## 在本 wiki 中的出现
- [[2025-policy-guided-causal-state-representation]]:PGCR:面向离线 RL 推荐的两阶段因果状态表示框架,用策略引导的因果特征选择隔离因果相关分量,再用 encoder 学习紧凑状态表示。
- [[causal-representation-learning]]
- [[offline-rl]]

- [[2022-deep-causal-reasoning-for-recommendations]]:Deep-Deconf 使用深度 VAE 推断 substitute confounders,将推荐建模为 MCMO(multi-cause multi-outcome)因果推断问题,从而消除混杂偏差并降低方差。

## 相关

- [[variational-autoencoder]]
- [[substitute-confounder]]
- [[causal-inference]]
- [[recommender-systems|recommendation-system]]
- [[confounding-bias]]
