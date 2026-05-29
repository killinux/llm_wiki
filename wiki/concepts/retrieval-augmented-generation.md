---
type: concept
subtype: method
tags: [retrieval, generation, knowledge-intensive, seq2seq, dense-retrieval]
created: 2026-05-29
updated: 2026-05-29
sources: 6
---

# Retrieval-Augmented Generation

Retrieval-Augmented Generation (RAG) 是一种将参数化的生成模型与可检索的非参数化外部知识(如稠密向量索引)结合的方法,在生成时检索相关文档以增强输出。

## 在本 wiki 中的出现

- [[2020-rag]]:提出 RAG,将预训练 seq2seq 生成器与可检索的 Wikipedia 稠密索引结合,统一进行端到端微调,用于知识密集型 NLP 任务并取得多项 SOTA。
- [[2023-chain-of-verification]]:Chain-of-Verification (CoVe) 让 LLM 先生成草稿,再独立回答自我规划的验证问题来核查事实,显著降低幻觉。
- [[2023-memgpt-llms-as-operating-systems]]:MemGPT 借鉴操作系统的分层内存与虚拟内存分页,用函数调用让 LLM 自主管理上下文内外的多级存储,在固定上下文模型上制造"无限上下文"的假象。
- [[2023-self-rag]]:Self-RAG 训练单个 LLM 用 reflection token 实现按需检索与自我反思批判,在推理时可控解码以提升生成质量、事实性与引用准确率。
- [[2024-metacognition-generative-agents]]:为 generative agents 引入元认知(metacognition)模块,让 agent 观察并反思自身思考与行动以动态调整策略,在僵尸末日等目标导向场景中显著提升表现。
- [[2024-self-reflection-llm-agents]]:在 9 个 LLM、1000 道多选题上对比 8 种自我反思类型,证明所有 self-reflection 都能显著提升 LLM agent 的解题准确率(p<0.001)。

## 相关

- [[dense-retrieval]]
- [[seq2seq]]
- [[knowledge-intensive-nlp]]
