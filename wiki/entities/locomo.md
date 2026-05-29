---
type: entity
subtype: benchmark
tags: [benchmark, long-term-memory, conversational-memory, llm-agent, evaluation]
created: 2026-05-29
updated: 2026-05-29
sources: 8
---

# LoCoMo

LoCoMo(Long Conversational Memory)是用于评测 LLM agent 在超长多轮对话中长期记忆能力的基准,常用于衡量记忆系统在问答、召回、延迟与 token 开销等维度上的表现。

## 在本 wiki 中的出现

- [[2025-agentic-memory-llm-agents]]:受 Zettelkasten 启发的 agentic 记忆系统,通过结构化笔记、自主链接生成与记忆演化为 LLM agent 提供可持续演化的长期记忆。
- [[2025-meminsight-autonomous-memory-augmentation]]:提出 MemInsight,让 LLM agent 自主从历史交互挖掘语义属性以增强记忆表示与检索,在对话推荐、问答、事件摘要上显著提升(推荐说服力最高 +14%,LoCoMo 召回比 RAG 基线高 34%)。
- [[2025-mem0-scalable-long-term-memory]]:Mem0 是一个以记忆为中心的架构,从持续对话中动态抽取、整合与检索关键信息,并提出图记忆变体 Mem0^g,在 LOCOMO 基准上以约 91% 更低延迟和逾 90% token 节省超越多种基线。
- [[2026-memory-in-the-age-of-ai-agents-survey]]:一篇关于智能体记忆的综述,提出 forms-functions-dynamics 三维统一分类法,整合碎片化的 agent memory 研究并汇总相关 benchmark 与开源框架。
- [[2026-evaluating-memory-structure-llm-agents]]:提出 StructMemEval 基准,测试 LLM agent 组织(而非仅回忆)其长期记忆的能力:纯检索系统在任务规模超出检索窗口后崩溃,memory agents 在被提示如何组织记忆时可靠求解,但常不会主动识别所需的记忆结构。
- [[2026-memory-for-autonomous-llm-agents]]:一篇 LLM agent 记忆综述,把 agent memory 形式化为 POMDP 内的写入-管理-读取循环,提出三维分类法、五类机制、四层评测栈与工程实践,覆盖 2022 至 2026 年初。
- [[2026-memori-persistent-memory-layer-llm-agents]]:Memori 是 LLM-agnostic 的持久化记忆层,用 Advanced Augmentation 把对话压缩成语义三元组+摘要,在 LoCoMo 上仅用约 5% 上下文 token(1,294/query)达到 81.95% 准确率,优于 Zep/LangMem/Mem0 且成本远低于 full-context。
- [[2026-omnibehavior]]:OmniBehavior 是首个完全基于真实工业日志(快手)构建的用户模拟基准,刻画长时程、跨场景、异质行为轨迹,并揭示当前 LLM 模拟器存在"积极且趋均值"的结构性偏差。

## 相关

- [[agentic-memory]]
- [[long-term-memory]]
- [[llm-agents|llm-agent]]
- [[rag]]
- [[mem0]]
- [[memori-persistent-memory-layer]]
- [[structmemeval]]
