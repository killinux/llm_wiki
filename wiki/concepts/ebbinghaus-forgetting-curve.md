---
type: concept
subtype: method
tags: [memory, long-term-memory, forgetting, llm, cognitive-science]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# Ebbinghaus Forgetting Curve

**Ebbinghaus Forgetting Curve** 是描述记忆随时间推移而衰退的经典心理学规律:记忆的留存率随时间近似指数式下降,而每次重新被回忆/复习都会减缓后续的遗忘速度。

## 在本 wiki 中的出现

- [[2023-memorybank]]:MemoryBank 借鉴 Ebbinghaus Forgetting Curve 设计类人记忆更新机制,根据记忆距今的时间与被回忆的次数动态调整其强度,实现"久未提及则淡忘、反复提及则强化"的遗忘与巩固过程,从而让长期记忆更新更贴近人类;该机制服务于其存储分层摘要历史对话、检索相关记忆并构建用户画像的整体记忆系统,并落地于情感陪伴机器人 SiliconFriend。
- [[2024-sage-self-evolving-agents]]:由 User/Assistant/Checker 三 agent 组成、结合迭代反馈、反思与基于 Ebbinghaus 遗忘曲线的记忆优化的自进化 LLM agent 框架,对小模型提升尤为显著。
- [[2024-lmagent-multimodal-agents-society]]:基于多模态 LLM 的万级规模 agents 社会,在电商场景模拟多用户的购物、社交、直播行为,复现真实 co-purchase 模式与从众等 emergent behavior。
- [[2025-mmoagent-economic-simulation-mmo]]:提出 MMOAgent,一个基于 LLM 的 Generative Agent-Based Modeling 框架,用具备 profile/感知/推理/记忆/行动的 LLM 智能体模拟 MMO 游戏经济,涌现出角色分化与符合供需规律的价格波动。
- [[2025-memory-os-of-ai-agent]]:借鉴操作系统内存管理,为 AI agent 设计分层(STM/MTM/LPM)、heat 驱动更新的 MemoryOS,统一 Storage/Updating/Retrieval/Generation 四模块,在 LoCoMo 上 F1 平均提升 49.11%、BLEU-1 提升 46.18%。

## 相关

- [[memory-stream]] — 另一种智能体长期记忆机制,同样综合 recency 等维度对记忆排序与衰减
- [[retrieval-augmented-generation]] — 同样依赖从外部记忆中检索相关内容注入 LLM 上下文
- [[llm-agent]] — 遗忘曲线常被用来为 agent 设计类人的长期记忆管理
