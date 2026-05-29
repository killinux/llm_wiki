---
type: entity
subtype: model
tags: [sequential-recommendation, llm, world-knowledge, retrieval-augmented, attention]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# GRASP

GRASP 是一种将 LLM 世界知识作为辅助输入(而非监督信号)注入序列推荐的方法,通过"生成增强检索 + Sigmoid 整体注意力增强"在抵抗 LLM 幻觉噪声的同时提升推荐效果。

## 在本 wiki 中的出现

- [[2025-grasp-world-knowledge-sequential-recommendation]]:GRASP 用"生成增强检索 + Sigmoid 整体注意力增强"把 LLM 世界知识作为辅助输入(而非监督信号)注入序列推荐,抵抗 LLM 幻觉噪声,在 Beauty/Fashion/Industry-100K 上叠加多种 backbone 均达 SOTA,并通过线上 A/B 验证 GMV +1.71%。

## 相关

- [[sequential-recommendation]]
- [[llm-world-knowledge]]
- [[retrieval-augmented-recommendation]]
- [[llm-hallucination]]
