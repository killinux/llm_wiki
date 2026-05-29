---
type: entity
subtype: model
tags: [feature-selection, recommender-systems, llm, deep-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# AutoField

AutoField 是面向深度推荐系统的自动特征选择方法,通过 surrogate model 等机制自动判别哪些特征对模型有用,以替代人工特征工程。

## 在本 wiki 中的出现

- [[2025-self-surrogate-light-feature-selection]]:提出 SELF,用多个 LLM 的世界知识对特征做语义排序,再以轻量 bridge network 融合任务信号,缓解深度推荐系统特征选择对 surrogate model 的依赖。

## 相关

- [[self]]
- [[feature-selection]]
- [[deep-recommender-systems]]
- [[surrogate-model]]
