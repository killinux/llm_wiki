---
type: concept
subtype: method
tags: [memory, long-term-memory, forgetting, llm, cognitive-science]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Ebbinghaus Forgetting Curve

**Ebbinghaus Forgetting Curve** 是描述记忆随时间推移而衰退的经典心理学规律:记忆的留存率随时间近似指数式下降,而每次重新被回忆/复习都会减缓后续的遗忘速度。

## 在本 wiki 中的出现

- [[2023-memorybank]]:MemoryBank 借鉴 Ebbinghaus Forgetting Curve 设计类人记忆更新机制,根据记忆距今的时间与被回忆的次数动态调整其强度,实现"久未提及则淡忘、反复提及则强化"的遗忘与巩固过程,从而让长期记忆更新更贴近人类;该机制服务于其存储分层摘要历史对话、检索相关记忆并构建用户画像的整体记忆系统,并落地于情感陪伴机器人 SiliconFriend。

## 相关

- [[memory-stream]] — 另一种智能体长期记忆机制,同样综合 recency 等维度对记忆排序与衰减
- [[retrieval-augmented-generation]] — 同样依赖从外部记忆中检索相关内容注入 LLM 上下文
- [[llm-agent]] — 遗忘曲线常被用来为 agent 设计类人的长期记忆管理
