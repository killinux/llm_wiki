---
type: entity
subtype: product
tags: [bayesian-optimization, hyperparameter-tuning, optimization, gaussian-process]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# BoTorch

BoTorch 是用于贝叶斯优化(Bayesian Optimization)的开源库,常作为超参数自动调优的基线方法。

## 在本 wiki 中的出现

- [[2025-hyperzero-auto-tuning]]:在 Meta 的端到端超参数自动调优系统 HyperZero 中,贝叶斯优化(Bayesian optimization)作为对比基线;HyperZero 通过 semi-i.i.d. delta 信号 + GP/Thompson Sampling 零阶约束优化 + 异步并行,在合成数据上取得 Gain 4.951%,远超贝叶斯优化基线。

## 相关

- [[hyperzero]]
- [[bayesian-optimization]]
- [[gaussian-process]]
- [[thompson-sampling]]
