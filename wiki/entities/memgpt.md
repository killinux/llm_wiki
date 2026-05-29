---
type: entity
subtype: product
tags: [llm-agent, memory, long-term-memory, agentic-memory]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# MemGPT

MemGPT 是一种为 LLM agent 提供长期记忆管理能力的系统,通过分层记忆与上下文调度让模型突破固定上下文窗口的限制。

## 在本 wiki 中的出现

- [[2025-agentic-memory-llm-agents]]:受 Zettelkasten 启发的 agentic 记忆系统,通过结构化笔记、自主链接生成与记忆演化为 LLM agent 提供可持续演化的长期记忆。
- [[2026-memory-in-the-age-of-ai-agents-survey]]:一篇关于智能体记忆的综述,提出 forms-functions-dynamics 三维统一分类法,整合碎片化的 agent memory 研究并汇总相关 benchmark 与开源框架。
- [[2026-evaluating-memory-structure-llm-agents]]:提出 StructMemEval 基准,测试 LLM agent 组织(而非仅回忆)其长期记忆的能力:纯检索系统在任务规模超出检索窗口后崩溃,memory agents 在被提示如何组织记忆时可靠求解,但常不会主动识别所需的记忆结构。
- [[2026-memory-for-autonomous-llm-agents]]:一篇 LLM agent 记忆综述:把 agent memory 形式化为 POMDP 内的写入-管理-读取循环,提出三维分类法、五类机制、四层评测栈与工程实践,覆盖 2022 至 2026 年初。

## 相关

- [[agentic-memory]]
- [[long-term-memory]]
- [[llm-agents|llm-agent]]
- [[zettelkasten]]
