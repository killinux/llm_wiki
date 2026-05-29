---
type: concept
subtype: method
tags: [gaussian-process, bayesian-optimization, surrogate-model, hyperparameter-tuning, machine-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Gaussian Process

高斯过程(Gaussian Process,GP)是一种基于贝叶斯思想的非参数模型,它把对未知函数的先验建模为一族联合服从多元高斯分布的随机变量,从而在给出预测均值的同时还提供不确定性估计,常被用作贝叶斯优化中的代理(surrogate)模型。

## 在本 wiki 中的出现

- [[2025-hyperzero-auto-tuning]]:Meta 的端到端超参数自动调优系统 HyperZero,利用推荐系统小时级反馈,通过 semi-i.i.d. delta 信号 + GP/Thompson Sampling 零阶约束优化 + 异步并行,把 value model 权重调优从数周压缩到 2-3 天,合成数据上 Gain 4.951% 远超 Bayesian optimization。

## 相关

- [[bayesian-optimization]]
- [[thompson-sampling]]
- [[hyperparameter-tuning]]
- [[zeroth-order-optimization]]
