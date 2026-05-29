---
type: concept
subtype: method
tags: [memory, long-term-memory, retrieval, dialogue, personalization]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# LLM Long-term Memory

LLM Long-term Memory 指为大语言模型设计的持久化记忆机制,使其能够跨会话存储、更新并检索历史交互信息,从而维持长期一致的上下文与个性化能力。

## 在本 wiki 中的出现

- [[2023-memorybank]]:该工作的核心目标。MemoryBank 为 LLM 设计类人长期记忆机制,存储并分层摘要历史对话、按 Ebbinghaus 遗忘曲线更新记忆、检索相关记忆并构建用户画像,并以此实现情感陪伴机器人 SiliconFriend。
- [[2023-memgpt-llms-as-operating-systems]]:MemGPT 借鉴操作系统的分层内存与虚拟内存分页,用函数调用让 LLM 自主管理上下文内外的多级存储,在固定上下文模型上制造"无限上下文"的假象。
- [[2024-megaagent-large-scale-mas-without-sop]]:借鉴操作系统进程/线程模型、无需预定义 SOP、可自动生成数百 agent 并行协作的大规模 LLM 多智能体系统,800 秒内开发五子棋、2991 秒协调 590 个 agent 生成国家政策。

## 相关

- [[memorybank]]
- [[siliconfriend]]
- [[ebbinghaus-forgetting-curve]]
- [[memory-retrieval]]
- [[user-profile]]
- [[hierarchical-summarization]]
- [[retrieval-augmented-generation]]
- [[conversational-agent]]
- [[llm-operating-system]]
- [[context-management]]
- [[llm-multi-agent-system]]
