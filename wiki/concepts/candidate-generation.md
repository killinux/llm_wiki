---
type: concept
subtype: method
tags: [recommendation, retrieval, embedding-based-retrieval, recall]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Candidate generation

Candidate generation 是推荐/检索系统中的召回阶段,从海量物料库中快速筛选出一个规模较小、与用户兴趣相关的候选集,供后续精排(ranking)进一步打分排序。

## 在本 wiki 中的出现

- [[2023-divide-and-conquer-ebr]]:把推荐召回的 embedding-based retrieval(EBR)拆成"物料聚类 + 簇内并行检索 + 可控合并"的分治流程,并采用 prompt-like 的多任务适配方式提升候选生成质量;在公开数据集上 Recall 最高提升约 40%,已在快手线上部署。这里 Candidate generation 正是 EBR 所承担的角色——通过 embedding 相似度从全量物料中产出候选集。
- [[2025-t2diff-two-tower-diffusion-matching]]:T2Diff 在双塔召回的用户塔内用扩散模型重建用户"下一个正向意图",并以 mixed-attention 实现交叉交互,在保持低延迟的同时打破双塔的 Late Interaction 瓶颈,离线/在线均显著超越 SOTA。
- [[2025-perscen-multi-scenario-matching]]:首个将用户个性化建模引入多场景匹配(召回)的两塔方法,用 user-specific 特征图 + 轻量 GNN、向量量化的场景偏好与渐进式 GLU,在 KuaiRand-Pure 与 Alimama 上以高效率刷新召回性能。

## 相关

- [[embedding-based-retrieval]]
- [[recall]]
- [[ranking]]
- [[recommender-systems|recommendation-system]]
- [[clustering]]
- [[multi-task-learning]]
- [[two-tower-model]]
- [[diffusion-models|diffusion-model]]
- [[multi-scenario-recommendation]]
- [[late-interaction]]
