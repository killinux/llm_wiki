---
type: concept
subtype: method
tags: [human-in-the-loop, llm-agent, multi-agent]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Human-in-the-loop

Human-in-the-loop 指在自动化系统(尤其是 LLM/agent 系统)的运行过程中引入人类参与,由人类在关键环节提供输入、反馈、确认或干预,以提升系统的可控性与可靠性。

## 在本 wiki 中的出现

- [[2023-autogen]]:AutoGen 是微软提出的开源多 agent 框架,通过可定制、可对话 agent 之间的会话编程来构建复杂 LLM 应用。其 agent 支持 LLM、工具与人类之间灵活的对话模式,可在自动对话中按需引入 human-in-the-loop,让人类在 agent 协作过程中提供输入或干预。
- [[2024-generative-ai-as-economic-agents]]:立场/理论论文,主张把生成式 AI 本身建模为有独立信息与(可能错位的)偏好的经济主体,并给出一个把 AI agent 嵌入博弈的形式化框架;在该框架下,人类对可能错位的 AI 偏好进行监督与介入,正是 human-in-the-loop 的核心动机。
- [[2025-llm-agent-evaluation-survey]]:SAP Labs 的 LLM agent 评测综述,提出"评测目标 × 评测过程"二维分类法,并强调企业落地中的可靠性、合规与 RBAC 等挑战。

## 相关

- [[llm-agents|llm-agent]]
- [[llm-multi-agent]]
- [[tool-use]]
- [[scalable-oversight]]
