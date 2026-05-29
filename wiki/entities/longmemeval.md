---
type: entity
subtype: benchmark
tags: [benchmark, memory, long-term-memory, conversational-ai, retrieval, llm-agents, evaluation]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# LongMemEval

LongMemEval 是一个用于评测对话型 AI 系统长期记忆能力的基准,考察模型在长跨度多轮对话中检索与利用历史信息的准确性。

## 在本 wiki 中的出现

- [[2025-reflective-memory-management]]:提出 RMM(Reflective Memory Management):用主题粒度的前瞻反思组织对话记忆,并用 LLM 引用信号在线 RL 精炼检索 reranker,在 LongMemEval 上比无记忆基线提升 10%+ 准确率。
- [[2026-memory-in-the-age-of-ai-agents-survey]]:一篇关于智能体记忆的综述,提出 forms-functions-dynamics 三维统一分类法,整合碎片化的 agent memory 研究并汇总相关 benchmark 与开源框架。
- [[2026-evaluating-memory-structure-llm-agents]]:提出 StructMemEval 基准,测试 LLM agent 组织(而非仅回忆)其长期记忆的能力:纯检索系统在任务规模超出检索窗口后崩溃,memory agents 在被提示如何组织记忆时可靠求解,但常不会主动识别所需的记忆结构。

## 相关

- [[reflective-memory-management]]
- [[long-term-memory]]
- [[conversational-ai]]
- [[retrieval]]
- [[structmemeval]]
- [[agent-memory]]
- [[2026-memory-in-the-age-of-ai-agents-survey]]
- [[2026-evaluating-memory-structure-llm-agents]]
