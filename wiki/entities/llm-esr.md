---
type: entity
subtype: model
tags: [llm, sequential-recommendation, world-knowledge, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# LLM-ESR

LLM-ESR 是一类将大语言模型(LLM)世界知识引入序列推荐(sequential recommendation)的方法/模型范式,旨在借助 LLM 对物品与用户行为的语义理解来增强传统推荐 backbone。

## 在本 wiki 中的出现

- [[2025-grasp-world-knowledge-sequential-recommendation]]:GRASP 用"生成增强检索 + Sigmoid 整体注意力增强"把 LLM 世界知识作为辅助输入(而非监督信号)注入序列推荐,抵抗 LLM 幻觉噪声,在 Beauty/Fashion/Industry-100K 上叠加多种 backbone 均达 SOTA,并通过线上 A/B 验证 GMV +1.71%。

## 相关

- [[grasp]]
- [[2025-grasp-world-knowledge-sequential-recommendation]]
- [[sequential-recommendation]]
- [[llm-world-knowledge]]
