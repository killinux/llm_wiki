---
type: concept
subtype: method
tags: [retrieval, embedding, recommendation, recall, ANN]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Embedding-based retrieval

Embedding-based retrieval(EBR)是一种把 query 与候选物料映射到同一向量空间、用向量相似度进行近似最近邻检索来召回候选的方法,广泛用于搜索与推荐系统的召回阶段。

## 在本 wiki 中的出现

- [[2023-divide-and-conquer-ebr]]:作为推荐系统召回阶段的核心方法被改造。该工作把推荐召回的 embedding-based retrieval 拆成"物料聚类 + 簇内并行检索 + 可控合并"三步,并使用 prompt-like 的多任务适配来统一不同检索目标。在公开数据集上 Recall 最高提升约 40%,且已在快手线上部署。

## 相关

- [[approximate-nearest-neighbor-search]]
- [[recommendation-retrieval]]
- [[embedding]]
- [[two-tower-model]]
- [[multi-task-learning]]
