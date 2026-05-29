---
type: concept
subtype: method
tags: [memory, llm-agent, long-term-memory, agentic-memory, retrieval]
created: 2026-05-29
updated: 2026-05-29
sources: 6
---

# 长期记忆 (Long-Term Memory)

长期记忆是指为 LLM agent 提供的、跨会话持久保存的信息存储与管理能力,使其能从持续交互中抽取、组织、巩固并按需检索关键信息,从而突破固定上下文窗口的限制。

## 概述

LLM 的上下文窗口有限且会话结束即遗忘,长期记忆通过把历史交互写入外部存储(向量库、图、结构化笔记或操作系统式分层缓存),并在后续交互中检索回相关片段,让 agent 维持对用户与任务的持续认知。本 wiki 中的相关工作大致覆盖三条主线:一是构建长期记忆系统/产品(MemGPT、MemoryBank、Mem0、A-Mem、MemoryOS、Memori),二是从综述角度统一形式化 agent memory 的写入-管理-读取循环与分类法,三是评测 agent 不仅能回忆、还能主动组织其长期记忆的能力。

## 在本 wiki 中的出现

- [[2025-mem0-scalable-long-term-memory]]:提出 Mem0,一个以记忆为中心的架构,从持续对话中动态抽取、整合与检索关键信息,并给出图记忆变体 Mem0^g,在 LOCOMO 基准上以约 91% 更低延迟和逾 90% token 节省超越多种基线,是长期记忆系统的代表性实现。
- [[2023-memgpt-llms-as-operating-systems]]:把 LLM 类比为操作系统,通过分层记忆与上下文调度在固定上下文窗口之上管理长期记忆,让模型按需在主上下文与外部存储之间换页。
- [[2023-memorybank]]:为 LLM 提供长期记忆机制,可随交互持续存储与回忆历史信息,并据此维持对用户的长期认知。
- [[2025-agentic-memory-llm-agents]]:受 Zettelkasten 启发的 agentic 记忆系统(A-Mem),通过结构化笔记、自主链接生成与记忆演化,为 LLM agent 提供可持续演化的长期记忆。
- [[2026-evaluating-memory-structure-llm-agents]]:提出 StructMemEval 基准,测试 LLM agent 组织(而非仅回忆)其长期记忆的能力——纯检索系统在任务规模超出检索窗口后崩溃,memory agents 在被提示如何组织记忆时可靠求解,但常不会主动识别所需的记忆结构。
- [[2026-memory-for-autonomous-llm-agents]]:一篇 LLM agent 记忆综述,把 agent memory 形式化为 POMDP 内的写入-管理-读取循环,提出三维分类法、五类机制、四层评测栈与工程实践,系统性地把长期记忆纳入统一框架。

## 相关

- [[memory-augmentation]]
- [[agent-memory]]
- [[retrieval-augmented-generation]]
- [[llm-agents|llm-agent]]
- [[memgpt]]
- [[mem0]]
- [[memorybank]]
