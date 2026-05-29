---
type: concept
subtype: method
tags: [recommendation, retrieval, embedding-based-retrieval, recall]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Candidate generation

Candidate generation 是推荐/检索系统中的召回阶段,从海量物料库中快速筛选出一个规模较小、与用户兴趣相关的候选集,供后续精排(ranking)进一步打分排序。

## 在本 wiki 中的出现

- [[2023-divide-and-conquer-ebr]]:把推荐召回的 embedding-based retrieval(EBR)拆成"物料聚类 + 簇内并行检索 + 可控合并"的分治流程,并采用 prompt-like 的多任务适配方式提升候选生成质量;在公开数据集上 Recall 最高提升约 40%,已在快手线上部署。这里 Candidate generation 正是 EBR 所承担的角色——通过 embedding 相似度从全量物料中产出候选集。

## 相关

- [[embedding-based-retrieval]]
- [[recall]]
- [[ranking]]
- [[recommendation-system]]
- [[clustering]]
- [[multi-task-learning]]
