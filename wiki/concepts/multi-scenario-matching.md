---
type: concept
subtype: method
tags: [recommendation, retrieval, multi-scenario, two-tower, personalization]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Multi-Scenario Matching

多场景匹配(Multi-Scenario Matching)指在推荐系统的召回(matching)阶段,统一建模来自多个业务场景的数据,以共享知识并刻画场景间差异,从而为不同场景高效检索候选物品。

## 在本 wiki 中的出现

- [[2025-perscen-multi-scenario-matching]]:首个将用户个性化建模引入多场景匹配(召回)的两塔方法,用 user-specific 特征图 + 轻量 GNN、向量量化的场景偏好与渐进式 GLU,在 KuaiRand-Pure 与 Alimama 上以高效率刷新召回性能。
- [[2601-dsmoe-scenario-adaptive-moe-matching]]:DSMOE 将 MMOE 迁移到多场景推荐召回阶段,用低秩场景自适应投影(SAP)缓解头部场景统治专家,并用 user-item 联合特征 teacher 蒸馏指导双塔 student,在保持检索效率的同时显著提升长尾稀疏场景的召回质量。

## 相关

- [[two-tower|two-tower-retrieval]]
- [[user-personalization]]
- [[vector-quantization]]
- [[graph-neural-network]]
- [[recommendation-retrieval]]
- [[mixture-of-experts]]
- [[knowledge-distillation]]
