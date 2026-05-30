---
type: concept
subtype: method
tags: [optimization, fairness, online-learning, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Constrained optimization

约束优化指在满足一组约束条件(如公平性、预算或曝光分配要求)的前提下,最大化或最小化目标函数的一类方法。

## 在本 wiki 中的出现

- [[2024-bankfair-fluctuating-traffic-reranking]]:BankFair 借鉴破产问题的 Talmud rule,把两侧推荐的曝光分配建模为序列化破产问题并用在线学习求解,在波动用户流量下同时保证短期用户准确性与长期提供方公平性。
- [[2025-hyperzero-auto-tuning]]:Meta 的端到端超参数自动调优系统 HyperZero,利用推荐系统小时级反馈,通过 semi-i.i.d. delta 信号 + GP/Thompson Sampling 零阶约束优化 + 异步并行,把 value model 权重调优从数周压缩到 2-3 天,合成数据上 Gain 4.951% 远超 Bayesian optimization。

## 相关

- [[online-learning]]
- [[recommendation-fairness|fairness-in-recommendation]]
- [[two-sided-marketplace]]
- [[reranking]]
- [[bayesian-optimization]]
- [[thompson-sampling]]
- [[gaussian-process]]
- [[zeroth-order-optimization]]
- [[hyperparameter-tuning]]
