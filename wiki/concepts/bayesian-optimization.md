---
type: concept
subtype: method
tags: [optimization, hyperparameter-tuning, gaussian-process, black-box-optimization]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Bayesian Optimization

贝叶斯优化是一种用于黑盒函数全局优化的序贯策略,通过构建目标函数的概率代理模型(常用高斯过程)并结合采集函数在探索与利用之间权衡,以尽可能少的昂贵评估次数找到最优解,常用于超参数调优等评估成本高的场景。

## 在本 wiki 中的出现

- [[2025-hyperzero-auto-tuning]]:Meta 的端到端超参数自动调优系统 HyperZero,利用推荐系统小时级反馈,通过 semi-i.i.d. delta 信号 + GP/Thompson Sampling 零阶约束优化 + 异步并行,把 value model 权重调优从数周压缩到 2-3 天,合成数据上 Gain 4.951% 远超 Bayesian optimization。

## 相关

- [[gaussian-process]]
- [[thompson-sampling]]
- [[hyperparameter-tuning]]
- [[black-box-optimization]]
