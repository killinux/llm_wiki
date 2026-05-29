---
type: concept
subtype: method
tags: [prompting, multi-agent, role-playing, instruction-data, autonomous-agents]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Inception Prompting

Inception Prompting 是一种通过精心设计的初始(种子)提示来设定多个 LLM 智能体的角色与任务,使其在最少人工干预下自主进行多轮对话、协作完成任务的提示方法。

## 在本 wiki 中的出现

- [[2023-camel-communicative-agents]]:CAMEL 使用 role-playing 与 inception prompting 框架,让两个 LLM 智能体(AI User 与 AI Assistant)围绕一个指定任务自主对话、相互引导,从而在最少人工干预下协作完成任务,并以此自动生成大规模的指令/对话数据。在该工作中,inception prompting 是驱动智能体保持角色一致、推进对话并约束行为的核心机制。

## 相关

- [[role-playing]]
- [[2023-camel-communicative-agents]]
- [[ai-user-agent]]
- [[ai-assistant-agent]]
- [[multi-agent-systems]]
- [[autonomous-agents]]
- [[instruction-tuning]]
- [[prompt-engineering]]
