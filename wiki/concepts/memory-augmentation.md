---
type: concept
subtype: method
tags: [memory, llm-agent, retrieval, augmentation]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Memory Augmentation

记忆增强是指为 LLM 智能体扩充、组织并增强其对历史交互信息的表示与检索能力,使模型能够超越上下文窗口限制,更准确地利用长期记忆完成下游任务。

## 在本 wiki 中的出现

- [[2025-meminsight-autonomous-memory-augmentation]]:提出 MemInsight,让 LLM agent 自主从历史交互挖掘语义属性以增强记忆表示与检索,在对话推荐、问答、事件摘要上显著提升(推荐说服力最高 +14%,LoCoMo 召回比 RAG 基线高 34%)。
- [[2026-memory-in-the-age-of-ai-agents-survey]]:一篇关于智能体记忆的综述,提出 forms-functions-dynamics 三维统一分类法,整合碎片化的 agent memory 研究并汇总相关 benchmark 与开源框架。
- [[2026-memory-for-autonomous-llm-agents]]:一篇 LLM agent 记忆综述,把 agent memory 形式化为 POMDP 内的写入-管理-读取循环,提出三维分类法、五类机制、四层评测栈与工程实践,覆盖 2022 至 2026 年初。

## 相关

- [[retrieval-augmented-generation]]
- [[llm-agents|llm-agent]]
- [[long-term-memory]]
