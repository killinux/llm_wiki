---
type: concept
subtype: method
tags: [hyperparameter-optimization, auto-tuning, bayesian-optimization, gaussian-process, thompson-sampling]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Hyperparameter Optimization

超参数优化(Hyperparameter Optimization)是指在不直接参与模型训练梯度更新的前提下,通过系统化的搜索与反馈机制为模型或系统寻找最优配置(如学习率、权重、正则化系数等)的方法。

## 在本 wiki 中的出现

- [[2025-hyperzero-auto-tuning]]:Meta 的端到端超参数自动调优系统 HyperZero,利用推荐系统小时级反馈,通过 semi-i.i.d. delta 信号 + GP/Thompson Sampling 零阶约束优化 + 异步并行,把 value model 权重调优从数周压缩到 2-3 天,合成数据上 Gain 4.951% 远超 Bayesian optimization。

## 相关

- [[bayesian-optimization]]
- [[gaussian-process]]
- [[thompson-sampling]]
- [[zeroth-order-optimization]]
- [[recommender-systems|recommendation-system]]
