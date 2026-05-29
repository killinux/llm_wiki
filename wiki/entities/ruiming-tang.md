---
type: entity
subtype: person
tags: [person, researcher, recommender-systems, llm, feature-selection]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Ruiming Tang

Ruiming Tang 是一位研究者,工作涉及大语言模型(LLM)与深度推荐系统的结合,尤其关注利用 LLM 的世界知识改进推荐系统中的特征选择。

## 在本 wiki 中的出现

- [[2025-self-surrogate-light-feature-selection]]:提出 SELF,用多个 LLM 的世界知识对特征做语义排序、再以轻量 bridge network 融合任务信号,缓解深度推荐系统特征选择对 surrogate model 的依赖。
- [[2026-ab-agent-recsys-evaluation]]:A/B Agent,一个多模态 LLM 用户智能体,在带海报的推荐沙盒 UI 中模拟用户多模态感知、多页交互与疲劳退出,用以替代昂贵的在线 A/B testing 评估推荐模型并做数据增强。
- [[2026-smes-scalable-multi-task-expert-sparsity]]:SMES 是 Kuaishou 提出的可扩展稀疏 MoE 多任务推荐框架,用 progressive expert routing 与 multi-task load-balancing 解决多任务稀疏路由的 exploded activation 与 load skew,使参数 scaling 在工业延迟约束下带来稳定收益。

## 相关

- [[feature-selection]]
- [[deep-recommender-systems]]
- [[large-language-models]]
- [[recommender-systems]]
- [[mixture-of-experts]]
- [[multi-task-learning]]
- [[llm-agents|llm-agent]]
