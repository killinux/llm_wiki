---
type: entity
subtype: product
tags: [multi-agent, framework, LLM, microsoft, open-source]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# AutoGen

AutoGen 是微软提出的开源多 agent 框架,通过可定制、可对话的 agent 之间的会话编程来构建复杂的 LLM 应用。

## 在本 wiki 中的出现

- [[2023-autogen]]:本文提出 AutoGen,将其作为一个开源框架,通过多个可定制、可对话 agent 之间的会话编程来支持构建复杂的 LLM 应用。
- [[2024-megaagent-large-scale-mas-without-sop]]:借鉴操作系统进程/线程模型、无需预定义 SOP、可自动生成数百 agent 并行协作的大规模 LLM 多智能体系统,800 秒内开发五子棋、2991 秒协调 590 个 agent 生成国家政策。
- [[2026-orchestration-multi-agent-systems]]:Skan AI 提出的编排式多 agent 系统统一架构(专门化 agent + 四单元编排层 + MCP/A2A 双通信协议 + 治理与可观测性),作为面向企业落地的工程蓝图综述,涉及 AutoGen 一类多 agent 框架的能力定位。
- [[2026-self-organizing-llm-agents]]:一项 25,000 任务的大规模实验发现"内生性悖论"——固定智能体顺序但角色自主的混合协议(Sequential)在质量上同时超越中心化(+14%)与完全自主(+44%)协调,但仅当底层模型足够强(存在能力门槛),为多 agent 框架的协调协议设计提供实证依据。
- [[2026-orgagent-company-style-mas]]:提出公司式层级多智能体框架 OrgAgent(治理/执行/合规三层),实证表明层级组织在多数推理任务上同时提升效果并大幅降低 token 成本。

## 相关

- [[multi-agent-systems|multi-agent]]
- [[agent]]
- [[llm-application]]
- [[microsoft]]
- [[llm-orchestration]]
- [[mcp]]
- [[a2a-protocol]]
