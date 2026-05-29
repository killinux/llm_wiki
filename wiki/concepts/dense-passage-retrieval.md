---
type: concept
subtype: method
tags: [retrieval, dense, passage, embedding, ir]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---
# Dense Passage Retrieval

Dense Passage Retrieval(DPR)是一种用稠密向量表示 query 与 passage、通过向量相似度从大规模文本库中检索相关段落的方法。

## 在本 wiki 中的出现

- [[2023-memorybank]]:MemoryBank 的记忆检索(Memory Retrieval)模块采用类似 Dense Passage Retrieval 的双塔稠密检索。每条记忆用编码器 E(·) 预编码为向量并以 FAISS 建立索引,当前对话上下文编码为查询向量后检索最相关记忆;编码器可灵活替换(开源版英文用 MiniLM、中文用 Text2vec)。检索出的记忆用于构建用户画像并支撑 LLM 回应,应用于情感陪伴机器人 SiliconFriend。

## 相关

- [[embedding-based-retrieval]]
- [[approximate-nearest-neighbor-search]]
- [[hard-negative-mining]]
- [[open-domain-qa]]
- [[retrieval-augmented-generation]]
- [[llm-long-term-memory]]
