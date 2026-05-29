---
type: concept
subtype: method
tags:
  - distributionally-robust-optimization
  - robust-optimization
  - distribution-shift
  - heterogeneity
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Distributionally Robust Optimization

Distributionally Robust Optimization (DRO) 是一类优化方法,它不针对单一经验分布做优化,而是在一个围绕经验分布构造的"分布不确定集"(ambiguity set)上最小化最坏情况下的期望损失,从而对分布偏移(distribution shift)与数据异质性更加鲁棒。

## 在本 wiki 中的出现

- [[2023-data-heterogeneity-recommendation]]:该工作关注推荐数据中的异质性问题,提出双层聚类方法 BHE,显式挖掘预测机制异质性与协变量分布异质性,用于多子模型预测与去偏,在 Yelp/MovieLens-1M 上以 NFM 为骨干将 NDCG@20 从 14.01 提升到 22.57。DRO 在此语境中作为应对数据分布异质性 / 子群体差异的一类相关思路出现——与 BHE 通过显式聚类刻画异质性不同,DRO 通过对最坏情况分布的鲁棒优化来缓解异质子群体带来的性能不均。

## 相关

- [[2023-data-heterogeneity-recommendation]]
- [[data-heterogeneity]]
- [[distribution-shift]]
- [[robust-optimization]]
- [[debiasing]]
- [[recommendation-system]]
