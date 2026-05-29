---
type: concept
subtype: method
tags: [knowledge-distillation, model-compression, knowledge-transfer, training]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# Knowledge Distillation

知识蒸馏(Knowledge Distillation)是一种把一个或多个"教师"模型中习得的知识迁移到通常更小、更高效的"学生"模型中的训练方法,使学生在保持性能的同时降低推理成本。

## 在本 wiki 中的出现

- [[2024-diit-domain-invariant-information-transfer]]:DIIT 通过 gating 域级聚合 + 对抗表示对齐的双抽取器和 multi-spot 知识蒸馏迁移器,把多个 source domain 模型的 domain-invariant 信息注入 target domain 模型,实现推理只需 target 模型的高效工业跨域推荐。
- [[2024-unbounded-generative-infinite-game]]:在"生成式无限游戏"角色生活模拟系统中,将多 LLM 协作能力蒸馏进 Gemma-2B,得到可实时运行的游戏引擎(配合带 Block Drop 的 regional IP-Adapter 保证角色与环境一致性)。
- [[2601-dsmoe-scenario-adaptive-moe-matching]]:DSMOE 将 MMOE 迁移到多场景推荐召回阶段,用低秩场景自适应投影(SAP)缓解头部场景统治专家,并用 user-item 联合特征 teacher 蒸馏指导双塔 student,在保持检索效率的同时显著提升长尾稀疏场景的召回质量。
- [[2026-cs3-capability-synergy-two-tower]]:CS3 是快手提出的通用框架,通过 Cycle-Adaptive Structure、Cross-Tower Synchronization、Cascade-Model Sharing 三个模块让 two-tower 召回模型感知自身、对侧塔与下游 cascade 模型,提升容量与跨阶段一致性,线上广告收入最高提升 8.36%。

## 相关

- [[model-compression]]
- [[knowledge-transfer]]
- [[domain-adaptation]]
- [[cross-domain-recommendation]]
- [[two-tower-retrieval]]
- [[mixture-of-experts]]
