---
type: concept
subtype: method
tags: [data-heterogeneity, recommendation, clustering, debiasing]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Data Heterogeneity

Data Heterogeneity(数据异质性)指同一数据集中不同子群体在预测机制或特征分布上存在系统性差异,使得单一全局模型难以同时拟合所有样本。

## 在本 wiki 中的出现

- [[2023-data-heterogeneity-recommendation]]:作为该论文的核心研究对象。论文将推荐数据中的 Data Heterogeneity 显式拆分为两类——预测机制异质性(predictive mechanism heterogeneity)与协变量分布异质性(covariate distribution heterogeneity),并提出双层聚类方法 BHE 显式挖掘这两类异质性,用于多子模型预测与去偏。在 Yelp / MovieLens-1M 上,以 NFM 为骨干时 NDCG@20 从 14.01 提升到 22.57。

## 相关

- [[2023-data-heterogeneity-recommendation]]
- [[recommender-systems|recommendation-system]]
- [[clustering]]
- [[debiasing]]
- [[distribution-shift]]
- [[ndcg]]
