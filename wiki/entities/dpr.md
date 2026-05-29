---
type: entity
subtype: model
tags: [retrieval, dense-retrieval, open-domain-qa, embedding]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# DPR (Dense Passage Retriever)

DPR (Dense Passage Retriever) 是一种基于稠密向量表示的段落检索模型,通过双编码器(dual-encoder)将问题与段落分别映射到同一向量空间,以向量相似度进行检索,用于开放域问答等知识密集型任务。

## 在本 wiki 中的出现

- [[2020-rag]]:RAG 使用 DPR 风格的稠密检索器,从 Wikipedia 的稠密索引中检索相关段落,与预训练 seq2seq 生成器结合并统一微调,用于知识密集型 NLP 任务并取得多项 SOTA。在该工作中,DPR 充当 RAG 的 retriever 组件,负责为生成器提供外部知识。

## 相关

- [[rag]]
- [[dense-retrieval]]
- [[dual-encoder]]
- [[open-domain-qa]]
- [[wikipedia-index]]
- [[seq2seq]]
