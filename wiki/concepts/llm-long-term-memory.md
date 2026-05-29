---
type: concept
subtype: method
tags: [llm, agent, memory, long-term-memory]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# LLM Long-term Memory

LLM 长期记忆指让大语言模型智能体跨会话、跨任务地持久化保存并按需检索信息(对话、知识、经验)的机制,通常以"写入-管理-读取"循环组织,以突破上下文窗口的限制。

## 在本 wiki 中的出现

- [[2026-memory-in-the-age-of-ai-agents-survey]]:一篇关于智能体记忆的综述,提出 forms-functions-dynamics 三维统一分类法,整合碎片化的 agent memory 研究并汇总相关 benchmark 与开源框架。
- [[2026-evaluating-memory-structure-llm-agents]]:提出 StructMemEval 基准,测试 LLM agent 组织(而非仅回忆)其长期记忆的能力:纯检索系统在任务规模超出检索窗口后崩溃,memory agents 在被提示如何组织记忆时可靠求解,但常不会主动识别所需的记忆结构。
- [[2026-memory-for-autonomous-llm-agents]]:一篇 LLM agent 记忆综述:把 agent memory 形式化为 POMDP 内的写入-管理-读取循环,提出三维分类法、五类机制、四层评测栈与工程实践,覆盖 2022 至 2026 年初。
- [[2026-memori-persistent-memory-layer-llm-agents]]:Memori 是 LLM-agnostic 的持久化记忆层,用 Advanced Augmentation 把对话压缩成语义三元组+摘要,在 LoCoMo 上仅用约 5% 上下文 token(1,294/query)达到 81.95% 准确率,优于 Zep/LangMem/Mem0 且成本远低于 full-context。

## 相关

- [[llm-agents|llm-agent]]
- [[retrieval-augmented-generation]]
- [[context-window]]
- [[memory-benchmark]]
