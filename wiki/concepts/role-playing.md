---
type: concept
subtype: method
tags: [role-playing, multi-agent, autonomous-agents, prompting, data-generation]
created: 2026-05-29
updated: 2026-05-29
sources: 6
---

# Role-Playing Framework

一种让多个 LLM 智能体各自扮演预设角色、通过相互对话在最少人工干预下自主协作完成任务的框架。

## 在本 wiki 中的出现

- [[2023-camel-communicative-agents]]:CAMEL 提出 role-playing 框架,让两个 LLM 智能体分别扮演 AI User 与 AI Assistant,在 inception prompting 的引导下自主对话协作完成任务,并借此自动生成大规模的指令/对话数据,以研究多智能体的行为与能力。
- [[2023-sotopia-social-intelligence-evaluation]]:SOTOPIA 提出一个开放式社交互动模拟环境与多维评测框架 SOTOPIA-EVAL,交互式地评估 LLM 智能体在目标导向社交场景中的社会智能,发现 GPT-4 在最难子集上的目标完成率显著低于人类。
- [[2024-agentic-feedback-loop-recommendation]]:提出 AFL,让 recommendation agent 与 user agent 通过基于 memory 的多轮文本反馈回路相互协作,同时提升推荐(平均 +11.52%)与用户模拟(平均 +21.12%),且不放大流行度/位置偏差。
- [[2025-multi-agent-collaboration-mechanisms-survey]]:一篇系统综述,沿 actors、types、structures、strategies、coordination protocols 五个维度刻画基于 LLM 的多 agent 系统协作机制,并梳理其跨领域应用与挑战。
- [[2025-socioverse-world-model-social-simulation]]:SocioVerse 是一个由 LLM agents 驱动、依托 1000 万真实用户池与四个对齐模块的社会模拟 world model,在政治、新闻、经济三大领域复现大规模人群行为。
- [[2025-sotopia-s4-social-simulation-system]]:面向非技术用户的快速、灵活、可扩展社会模拟系统,通过模拟引擎+RESTful API+Web UI,让研究者无需编程即可用自然语言设计、并行运行并自动评估多轮多方 LLM 社会交互。

## 相关

- [[2023-camel-communicative-agents]]
- [[inception-prompting]]
- [[multi-agent-collaboration]]
- [[llm-agents]]
- [[instruction-tuning]]
- [[social-intelligence]]
