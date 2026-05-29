---
type: concept
subtype: method
tags: [recommendation, cross-domain, transfer-learning, knowledge-distillation, user-simulation]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Cross-Domain Recommendation

跨域推荐(Cross-Domain Recommendation, CDR)是指利用来自一个或多个源域(source domain)的用户/物品信息或模型知识,来缓解目标域(target domain)的数据稀疏与冷启动问题,从而提升目标域推荐效果的一类方法。

## 在本 wiki 中的出现

- [[2024-diit-domain-invariant-information-transfer]]:DIIT 通过 gating 域级聚合 + 对抗表示对齐双抽取器和 multi-spot 知识蒸馏迁移器,把多个 source domain 模型的 domain-invariant 信息注入 target domain 模型,实现推理只需 target 模型的高效工业跨域推荐。
- [[2025-agentcf-plus-plus]]:通过双层记忆架构、两步融合机制与兴趣组共享记忆增强 AgentCF 用户模拟器,在跨域推荐中减少无关信息并显式建模流行度因素。

## 相关

- [[knowledge-distillation]]
- [[domain-adaptation]]
- [[user-simulation]]
- [[collaborative-filtering]]
- [[cold-start]]
