---
type: concept
subtype: method
tags: [retrieval, search, embedding, rag, information-retrieval]
created: 2026-05-30
updated: 2026-05-30
sources: 9
---

# 检索 (Retrieval)

检索指从大规模语料/物料库中**找出与查询相关的条目**,是搜索、问答、[[rag|RAG]] 与推荐召回的共同底层操作。
按表示方式分**稀疏**与**稠密**两大范式,工业系统常用**召回→重排**的级联。

## 两大范式
- **稀疏检索 (sparse)**:基于词项匹配(TF-IDF、BM25),可解释、对精确词面强,但有词汇鸿沟(同义不同词召不回)。
- **稠密检索 (dense)**:用学习到的 [[embedding|向量]] 做语义匹配(bi-encoder),召回语义相关项——见 [[dense-retrieval]]、[[dense-passage-retrieval]]、[[embedding-based-retrieval]];
  大规模用 [[faiss]] 等 ANN 索引。
- **混合 (hybrid)**:稀疏+稠密融合,兼顾精确与泛化。

## 级联与下游
- **召回→重排**:bi-encoder 召回 + cross-encoder/[[reranking|重排]]精排少量候选。
- **检索增强生成**:[[rag|RAG]]/[[retrieval-augmented-generation]] 把检索结果喂给生成模型抗幻觉;
  agentic RAG 让 agent 主动决定检索时机([[2025-agentic-memory-llm-agents]] 把 agency 下沉到记忆结构)。
- **记忆即检索**:LLM agent 的长期记忆本质是对历史的检索(见 [[llm-agent-memory]] 这条线),但纯检索在需要"组织知识"的任务上会失效([[2026-evaluating-memory-structure-llm-agents]])。

## 相关页
[[dense-retrieval]]、[[embedding]]、[[rag]]、[[reranking]]、[[faiss]]、[[recommender-systems]]
