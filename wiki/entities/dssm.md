---
type: entity
subtype: model
tags: [recall, two-tower, embedding, retrieval]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# DSSM

DSSM(Deep Structured Semantic Model)是一种典型的双塔(two-tower)深度模型,通过用户塔与物品塔分别将输入编码为向量,以向量内积衡量相关性,广泛用于推荐与广告系统的召回阶段。

## 在本 wiki 中的出现
- [[2024-recflow-full-flow-recommendation-dataset]]:首个包含工业推荐系统多级漏斗各阶段未曝光样本的大规模全流程数据集,用于研究分布偏移、选择偏差与多阶段联合优化。
- [[two-tower-model]]
- [[recommender-systems|recommendation-system]]
- [[selection-bias]]

- [[2026-cs3-capability-synergy-two-tower]]:CS3 是快手提出的通用框架,通过 Cycle-Adaptive Structure、Cross-Tower Synchronization、Cascade-Model Sharing 三个模块让 two-tower 召回模型感知自身、对侧塔与下游 cascade 模型,提升容量与跨阶段一致性,线上广告收入最高提升 8.36%。

## 相关

- [[two-tower]]
- [[recall]]
- [[cs3]]
