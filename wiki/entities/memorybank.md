---
type: entity
subtype: product
tags: [memory, llm-agent, long-term-memory, retrieval]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# MemoryBank

MemoryBank 是面向 LLM agent 的长期记忆系统/方向,通过结构化存储、自主组织与演化机制,为 agent 提供可持续积累、检索与更新的对话与交互记忆。

## 在本 wiki 中的出现
- [[2023-memorybank]]:本文提出 MemoryBank 作为核心方法。它为 LLM 设计类人长期记忆机制,负责存储与分层摘要历史对话、按 Ebbinghaus 遗忘曲线更新记忆、检索相关记忆并构建用户画像;并据此实现了情感陪伴机器人 SiliconFriend。
- [[2024-sage-self-evolving-agents]]:由 User/Assistant/Checker 三 agent 组成、结合迭代反馈、反思与基于 Ebbinghaus 遗忘曲线的记忆优化的自进化 LLM agent 框架,对小模型提升尤为显著。
- [[2025-memory-os-of-ai-agent]]:借鉴操作系统内存管理,为 AI agent 设计分层(STM/MTM/LPM)、heat 驱动更新的 MemoryOS,统一 Storage/Updating/Retrieval/Generation 四模块,在 LoCoMo 上 F1 平均提升 49.11%、BLEU-1 提升 46.18%。
- [[ebbinghaus-forgetting-curve]]——MemoryBank 借鉴的遗忘曲线理论,用于动态更新记忆强度。
- [[siliconfriend]]——基于 MemoryBank 构建的情感陪伴机器人。
- [[llm-long-term-memory]]——MemoryBank 所属的 LLM 长期记忆研究方向。
- [[memory-stream]]——同样面向 agent 长期记忆的相关机制。
- [[user-profiling]]——MemoryBank 在交互中构建用户画像的能力。
- [[retrieval-augmented-generation]]——MemoryBank 检索相关记忆以增强生成的思路与之相关。

- [[2025-agentic-memory-llm-agents]]:受 Zettelkasten 启发的 agentic 记忆系统,通过结构化笔记、自主链接生成与记忆演化为 LLM agent 提供可持续演化的长期记忆。
- [[2025-reflective-memory-management]]:提出 RMM(Reflective Memory Management):用主题粒度的前瞻反思组织对话记忆,并用 LLM 引用信号在线 RL 精炼检索 reranker,在 LongMemEval 上比无记忆基线提升 10%+ 准确率。
- [[2025-meminsight-autonomous-memory-augmentation]]:提出 MemInsight,让 LLM agent 自主从历史交互挖掘语义属性以增强记忆表示与检索,在对话推荐、问答、事件摘要上显著提升(推荐说服力最高 +14%,LoCoMo 召回比 RAG 基线高 34%)。
- [[2026-memory-in-the-age-of-ai-agents-survey]]:一篇关于智能体记忆的综述,提出 forms-functions-dynamics 三维统一分类法,整合碎片化的 agent memory 研究并汇总相关 benchmark 与开源框架。

## 相关

- [[long-term-memory]]
- [[llm-agents|llm-agent]]
- [[retrieval-augmented-generation]]
- [[zettelkasten]]
