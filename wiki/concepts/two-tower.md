---
type: concept
subtype: method
tags: [retrieval, embedding, recommendation, ranking]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# two-tower

双塔模型是一种检索/推荐架构,用两个独立的编码器(塔)分别把用户/查询和物品映射到同一嵌入空间,通过向量相似度(如最近邻搜索)进行高效匹配。

## 在本 wiki 中的出现

- [[2025-gnolr-progressive-implicit-preference]]:提出 GNOLR,用有序标签映射加嵌套优化把多种隐式反馈编码进统一 embedding 空间,既建模用户参与度递进又把多路检索简化为单次最近邻搜索。
- [[2601-dsmoe-scenario-adaptive-moe-matching]]:DSMOE 将 MMOE 迁移到多场景推荐召回阶段,用低秩场景自适应投影(SAP)缓解头部场景统治专家,并用 user-item 联合特征 teacher 蒸馏指导双塔 student,在保持检索效率的同时显著提升长尾稀疏场景的召回质量。
- [[2026-cs3-capability-synergy-two-tower]]:CS3 是快手提出的通用框架,通过 Cycle-Adaptive Structure、Cross-Tower Synchronization、Cascade-Model Sharing 三个模块让 two-tower 召回模型感知自身、对侧塔与下游 cascade 模型,提升容量与跨阶段一致性,线上广告收入最高提升 8.36%。

## 相关

- [[embedding]]
- [[nearest-neighbor-search]]
- [[implicit-feedback]]
- [[retrieval]]
- [[mmoe]]
- [[knowledge-distillation]]
