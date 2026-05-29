---
type: concept
subtype: method
tags: [out-of-distribution, invariance, causality, debiasing, heterogeneity]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Invariant Risk Minimization

Invariant Risk Minimization (IRM) 是一种跨多个训练环境(environment)学习不变预测机制的学习范式,通过约束模型在所有环境上共享同一个最优分类器,促使表征只捕捉因果不变的特征、忽略随环境变化的伪相关(spurious correlation),从而提升分布外(out-of-distribution)泛化能力。

## 在本 wiki 中的出现

- [[2023-data-heterogeneity-recommendation]]:该工作关注推荐数据中的异质性问题,提出双层聚类方法 BHE 来显式挖掘**预测机制异质性**与**协变量分布异质性**,据此训练多个子模型进行预测与去偏。IRM 在这里作为相关的思想背景——同样以"区分不变机制与随环境/分布变化的伪相关"为出发点,只是 BHE 通过聚类划分子群(而非预设环境)来刻画异质性。该方法在 Yelp/MovieLens-1M 上以 NFM 为骨干,将 NDCG@20 从 14.01 提升到 22.57。

## 相关

- [[empirical-risk-minimization]]
- [[out-of-distribution-generalization]]
- [[spurious-correlation]]
- [[causal-inference]]
- [[distribution-shift]]
- [[data-heterogeneity]]
- [[debiasing-recommendation]]
- [[2023-data-heterogeneity-recommendation]]
