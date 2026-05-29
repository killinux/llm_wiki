---
type: concept
subtype: method
tags: [agent-memory, llm-agent, memory, retrieval, lifelong-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 6
---

# Agent Memory

Agent Memory 指赋予 LLM 智能体在单次上下文窗口之外持久存储、管理与读取信息的机制,使其能够跨任务、跨会话地积累经验、保持一致性并实现自我改进。

## 在本 wiki 中的出现

- [[2026-memory-in-the-age-of-ai-agents-survey]]:一篇关于智能体记忆的综述,提出 forms-functions-dynamics 三维统一分类法,整合碎片化的 agent memory 研究并汇总相关 benchmark 与开源框架。
- [[2026-ab-agent-recsys-evaluation]]:A/B Agent:一个多模态 LLM 用户智能体,在带海报的推荐沙盒 UI 中模拟用户多模态感知、多页交互与疲劳退出,用以替代昂贵的在线 A/B testing 评估推荐模型并做数据增强。
- [[2026-evaluating-memory-structure-llm-agents]]:提出 StructMemEval 基准,测试 LLM agent 组织(而非仅回忆)其长期记忆的能力:纯检索系统在任务规模超出检索窗口后崩溃,memory agents 在被提示如何组织记忆时可靠求解,但常不会主动识别所需的记忆结构。
- [[2026-memory-for-autonomous-llm-agents]]:一篇 LLM agent 记忆综述:把 agent memory 形式化为 POMDP 内的写入-管理-读取循环,提出三维分类法、五类机制、四层评测栈与工程实践,覆盖 2022 至 2026 年初。
- [[2026-memori-persistent-memory-layer-llm-agents]]:Memori 是 LLM-agnostic 的持久化记忆层,用 Advanced Augmentation 把对话压缩成语义三元组+摘要,在 LoCoMo 上仅用约 5% 上下文 token(1,294/query)达到 81.95% 准确率,优于 Zep/LangMem/Mem0 且成本远低于 full-context。
- [[2026-experiential-reflective-learning]]:ERL:agent 反思单次任务轨迹与成败信号、提炼可迁移启发式存入持久池,新任务时按相关性检索 top-k 注入上下文,无需更新参数即可自我改进,在 Gaia2 上比 ReAct 基线提升 7.8% 成功率。

## 相关

- [[llm-agents|llm-agent]]
- [[retrieval-augmented-generation]]
- [[lifelong-learning]]
- [[context-window]]
- [[self-improvement]]
- [[benchmark]]
