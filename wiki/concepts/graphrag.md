---
type: concept
subtype: method
tags: [graphrag, retrieval, graph, llm, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# GraphRAG

GraphRAG 是一类把图结构(graph-grounded)信息与检索增强生成结合的方法,利用实体/关系图为 LLM 提供更具结构性的上下文或候选,从而提升检索、排序与生成质量。

## 在本 wiki 中的出现

- [[2026-graphrag-irl]]:GraphRAG-IRL 把 graph-grounded 特征、Maximum Entropy 逆强化学习预排序与 persona-guided LLM 重排融合,LLM 只对 IRL 短候选列表做语义重排,在 MovieLens/KuaiRand 上 NDCG@10 比监督基线提升 15.7%/16.6%。

## 相关

- [[inverse-reinforcement-learning]]
- [[llm-reranking]]
- [[retrieval-augmented-generation]]
- [[recommendation-systems]]
