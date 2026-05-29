---
type: concept
subtype: method
tags: [value-model, ranking, recommendation, hyperparameter-tuning, optimization]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Value Model

价值模型(Value Model)是工业级推荐/排序系统中用于将多个预测目标(如点击、停留、转化等)加权聚合为单一价值分数,从而对候选内容排序的模型,其权重通常需要持续调优以对齐业务目标。

## 在本 wiki 中的出现

- [[2025-hyperzero-auto-tuning]]:Meta 的端到端超参数自动调优系统 HyperZero,利用推荐系统小时级反馈,通过 semi-i.i.d. delta 信号 + GP/Thompson Sampling 零阶约束优化 + 异步并行,把 value model 权重调优从数周压缩到 2-3 天,合成数据上 Gain 4.951% 远超 Bayesian optimization。

## 相关

- [[reward-model]]
- [[hyperparameter-tuning]]
- [[bayesian-optimization]]
- [[thompson-sampling]]
- [[recommender-systems|recommendation-system]]
