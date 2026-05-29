---
type: concept
subtype: method
tags: [memory, long-term-memory, retrieval, dialogue, personalization]
created: 2026-05-29
updated: 2026-05-29
sources: 14
---

# LLM Long-term Memory

LLM Long-term Memory 指为大语言模型设计的持久化记忆机制,使其能够跨会话存储、更新并检索历史交互信息,从而维持长期一致的上下文与个性化能力。

## 在本 wiki 中的出现

- [[2023-memorybank]]:该工作的核心目标。MemoryBank 为 LLM 设计类人长期记忆机制,存储并分层摘要历史对话、按 Ebbinghaus 遗忘曲线更新记忆、检索相关记忆并构建用户画像,并以此实现情感陪伴机器人 SiliconFriend。
- [[2023-memgpt-llms-as-operating-systems]]:MemGPT 借鉴操作系统的分层内存与虚拟内存分页,用函数调用让 LLM 自主管理上下文内外的多级存储,在固定上下文模型上制造"无限上下文"的假象。
- [[2024-megaagent-large-scale-mas-without-sop]]:借鉴操作系统进程/线程模型、无需预定义 SOP、可自动生成数百 agent 并行协作的大规模 LLM 多智能体系统,800 秒内开发五子棋、2991 秒协调 590 个 agent 生成国家政策。
- [[2025-agentic-memory-llm-agents]]:受 Zettelkasten 启发的 agentic 记忆系统,通过结构化笔记、自主链接生成与记忆演化为 LLM agent 提供可持续演化的长期记忆。
- [[2025-agentcf-plus-plus]]:通过双层记忆架构、两步融合机制与兴趣组共享记忆增强 AgentCF 用户模拟器,在跨域推荐中减少无关信息并显式建模流行度因素。
- [[2025-reflective-memory-management]]:提出 RMM(Reflective Memory Management):用主题粒度的前瞻反思组织对话记忆,并用 LLM 引用信号在线 RL 精炼检索 reranker,在 LongMemEval 上比无记忆基线提升 10%+ 准确率。
- [[2025-meminsight-autonomous-memory-augmentation]]:提出 MemInsight,让 LLM agent 自主从历史交互挖掘语义属性以增强记忆表示与检索,在对话推荐、问答、事件摘要上显著提升(推荐说服力最高 +14%,LoCoMo 召回比 RAG 基线高 34%)。
- [[2025-llm-driven-cross-platform-npc]]:一个原型系统,让 LLM 驱动的游戏 NPC 通过云数据库在 Unity 游戏内与 Discord 社交平台间跨平台对话并同步记忆。
- [[2025-mem0-scalable-long-term-memory]]:Mem0 是一个以记忆为中心的架构,从持续对话中动态抽取、整合与检索关键信息,并提出图记忆变体 Mem0^g,在 LOCOMO 基准上以约 91% 更低延迟和逾 90% token 节省超越多种基线。
- [[2025-memory-os-of-ai-agent]]:借鉴操作系统内存管理,为 AI agent 设计分层(STM/MTM/LPM)、heat 驱动更新的 MemoryOS,统一 Storage/Updating/Retrieval/Generation 四模块,在 LoCoMo 上 F1 平均提升 49.11%、BLEU-1 提升 46.18%。
- [[2026-memory-in-the-age-of-ai-agents-survey]]:一篇关于智能体记忆的综述,提出 forms-functions-dynamics 三维统一分类法,整合碎片化的 agent memory 研究并汇总相关 benchmark 与开源框架。
- [[2026-evaluating-memory-structure-llm-agents]]:提出 StructMemEval 基准,测试 LLM agent 组织(而非仅回忆)其长期记忆的能力:纯检索系统在任务规模超出检索窗口后崩溃,memory agents 在被提示如何组织记忆时可靠求解,但常不会主动识别所需的记忆结构。
- [[2026-memory-for-autonomous-llm-agents]]:一篇 LLM agent 记忆综述:把 agent memory 形式化为 POMDP 内的写入-管理-读取循环,提出三维分类法、五类机制、四层评测栈与工程实践,覆盖 2022 至 2026 年初。
- [[2026-memori-persistent-memory-layer-llm-agents]]:Memori 是 LLM-agnostic 的持久化记忆层,用 Advanced Augmentation 把对话压缩成语义三元组+摘要,在 LoCoMo 上仅用约 5% 上下文 token(1,294/query)达到 81.95% 准确率,优于 Zep/LangMem/Mem0 且成本远低于 full-context。

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
