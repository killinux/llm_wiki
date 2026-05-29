---
type: concept
subtype: method
tags: [memory, long-term-memory, retrieval, personalization, dialogue]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# MemoryBank

MemoryBank 是一种为 LLM 设计的类人长期记忆机制,通过存储与分层摘要历史对话、按 Ebbinghaus 遗忘曲线动态更新记忆强度、检索相关记忆并构建用户画像,使模型在长期交互中保持连贯的个性化记忆。

## 在本 wiki 中的出现

- [[2023-memorybank]]:本文提出 MemoryBank 作为核心方法。它为 LLM 设计类人长期记忆机制,负责存储与分层摘要历史对话、按 Ebbinghaus 遗忘曲线更新记忆、检索相关记忆并构建用户画像;并据此实现了情感陪伴机器人 SiliconFriend。
- [[2024-sage-self-evolving-agents]]:由 User/Assistant/Checker 三 agent 组成、结合迭代反馈、反思与基于 Ebbinghaus 遗忘曲线的记忆优化的自进化 LLM agent 框架,对小模型提升尤为显著。
- [[2025-memory-os-of-ai-agent]]:借鉴操作系统内存管理,为 AI agent 设计分层(STM/MTM/LPM)、heat 驱动更新的 MemoryOS,统一 Storage/Updating/Retrieval/Generation 四模块,在 LoCoMo 上 F1 平均提升 49.11%、BLEU-1 提升 46.18%。

## 相关

- [[ebbinghaus-forgetting-curve]]——MemoryBank 借鉴的遗忘曲线理论,用于动态更新记忆强度。
- [[siliconfriend]]——基于 MemoryBank 构建的情感陪伴机器人。
- [[llm-long-term-memory]]——MemoryBank 所属的 LLM 长期记忆研究方向。
- [[memory-stream]]——同样面向 agent 长期记忆的相关机制。
- [[user-profiling]]——MemoryBank 在交互中构建用户画像的能力。
- [[retrieval-augmented-generation]]——MemoryBank 检索相关记忆以增强生成的思路与之相关。
