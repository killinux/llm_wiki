---
type: concept
subtype: method
tags: [retrieval, vector-search, embedding, indexing]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Approximate nearest neighbor search

Approximate nearest neighbor search(ANN)是一类在高维向量空间中快速检索与查询向量"近似最相近"邻居的方法,以牺牲少量精度为代价,换取相比精确暴力搜索大幅降低的延迟与计算开销。

## 在本 wiki 中的出现

- [[2023-divide-and-conquer-ebr]]:该工作研究推荐系统中的 embedding-based retrieval(EBR),本质上是在物料 embedding 上做 ANN 召回。它把召回流程拆成"物料聚类 + 簇内并行检索 + 可控合并"——先对候选物料聚类以缩小搜索空间,再在各簇内并行执行近似检索,最后做可控合并,并辅以 prompt-like 多任务适配。这一"分而治之"的结构是对 ANN 检索如何在大规模推荐召回中做工程化扩展的一种实践,在公开数据集上 Recall 最高提升约 40%,并已在快手线上部署。
- [[2025-gnolr-progressive-implicit-preference]]:提出 GNOLR,用有序标签映射加嵌套优化把多种隐式反馈编码进统一 embedding 空间,既建模用户参与度递进又把多路检索简化为单次最近邻搜索。

## 相关

- [[embedding-based-retrieval]]
- [[vector-database]]
- [[recommendation-retrieval]]
- [[clustering]]
- [[recall-at-k]]
- [[dense-retrieval]]
