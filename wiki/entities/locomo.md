---
type: entity
subtype: benchmark
tags: [benchmark, long-term-memory, conversational-memory, llm-agent, evaluation]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# LoCoMo

LoCoMo(Long Conversational Memory)是用于评测 LLM agent 在超长多轮对话中长期记忆能力的基准,常用于衡量记忆系统在问答、召回、延迟与 token 开销等维度上的表现。

## 在本 wiki 中的出现

- [[2025-agentic-memory-llm-agents]]:受 Zettelkasten 启发的 agentic 记忆系统,通过结构化笔记、自主链接生成与记忆演化为 LLM agent 提供可持续演化的长期记忆。
- [[2025-meminsight-autonomous-memory-augmentation]]:提出 MemInsight,让 LLM agent 自主从历史交互挖掘语义属性以增强记忆表示与检索,在对话推荐、问答、事件摘要上显著提升(推荐说服力最高 +14%,LoCoMo 召回比 RAG 基线高 34%)。
- [[2025-mem0-scalable-long-term-memory]]:Mem0 是一个以记忆为中心的架构,从持续对话中动态抽取、整合与检索关键信息,并提出图记忆变体 Mem0^g,在 LOCOMO 基准上以约 91% 更低延迟和逾 90% token 节省超越多种基线。

## 相关

- [[agentic-memory]]
- [[long-term-memory]]
- [[llm-agent]]
- [[rag]]
