---
type: concept
subtype: method
tags: [optimization, hyperparameter-tuning, gradient-free, black-box-optimization]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Zeroth-Order Optimization

零阶优化(Zeroth-Order Optimization)是一类不依赖目标函数显式梯度、仅通过函数值(零阶信息)来引导搜索方向的优化方法,常用于梯度不可得或代价高昂的黑盒优化与超参数调优场景。

## 在本 wiki 中的出现

- [[2025-hyperzero-auto-tuning]]:Meta 的端到端超参数自动调优系统 HyperZero,利用推荐系统小时级反馈,通过 semi-i.i.d. delta 信号 + GP/Thompson Sampling 零阶约束优化 + 异步并行,把 value model 权重调优从数周压缩到 2-3 天,合成数据上 Gain 4.951% 远超 Bayesian optimization。

## 相关

- [[bayesian-optimization]]
- [[thompson-sampling]]
- [[gaussian-process]]
- [[hyperparameter-tuning]]
- [[black-box-optimization]]
