---
type: concept
subtype: method
tags: [multi-agent, agents, llm, collaboration, framework]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# Multi-Agent Systems

Multi-Agent Systems 指由多个基于 LLM 的自主智能体(agent)通过相互沟通、协作或分工来共同完成复杂任务的方法范式。

## 在本 wiki 中的出现

- [[2023-camel-communicative-agents]]:CAMEL 采用角色扮演(role-playing)与 inception prompting,让两个 LLM 智能体(AI User 与 AI Assistant)在最少人工干预下自主对话、协作完成任务,并借此自动生成大规模的指令/对话数据,展示了多智能体协作作为研究与数据生成手段的可行性。
- [[2023-autogen]]:微软提出的开源多 agent 框架,通过可定制、可对话(conversable)的 agent 之间的会话编程(conversation programming)来编排多智能体协作,从而构建复杂的 LLM 应用。
- [[2026-generative-social-simulation-validation]]:一篇系统性文献综述(AI Review 2026, 59:15),梳理 LLM 驱动的生成式 Agent-Based Models 在社会模拟中的应用,论证引入 LLM 因黑箱性、文化偏见与随机性而加剧而非缓解了 ABM 长期的"验证"难题。
- [[2025-llm-multi-agent-swarm-intelligence]]:把 agent-based modeling 中 agent 的硬编码程序替换为 GPT-4o 驱动的 prompt,在蚁群觅食与鸟群 flocking 两个经典 swarm intelligence 场景中复现并诱导涌现集体行为。
- [[2023-concordia-generative-agent-based-modeling]]:Google DeepMind 提出的库 Concordia,用 LLM 驱动的生成式 agent 在物理/社会/数字空间中扎根交互,通过 Game Master 控制环境,支持 Generative Agent-Based Modeling 的社会仿真与数字服务评估。

## 相关

- [[role-playing]]
- [[inception-prompting]]
- [[llm-agent]]
- [[tool-use]]
- [[conversation-programming]]
- [[instruction-tuning]]
- [[agent-based-modeling]]

- [[generative-agents]]
- [[swarm-intelligence]]
- [[social-simulation]]
