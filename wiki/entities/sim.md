---
type: entity
subtype: model
tags: [user-interest-modeling, long-sequence-modeling, ctr-prediction, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# SIM

SIM(Search-based Interest Model)是一种面向超长用户行为序列的兴趣建模方法,通过两阶段(General Search Unit 检索 + Exact Search Unit 精排)从海量历史行为中检索与目标物品相关的兴趣表示,用于 CTR 预估等推荐排序任务。

## 在本 wiki 中的出现

- [[2025-deep-interest-life-cycle-network]]:提出 DILN,显式建模用户兴趣生命周期(emergent/stable/declining)并用 VQ 聚类离散化、注入 MMOE 排序模型,Lofter 线上 CTR +0.38%、CVR +1.04%、时长 +0.25%。

## 相关

- [[din]]
- [[dupn]]
- [[user-interest-modeling]]
- [[diln]]
- [[mmoe]]
