---
type: concept
subtype: method
tags: [agent, orchestration, multi-agent, LLM]
created: 2026-05-29
updated: 2026-05-29
sources: 9
---

# Agent Orchestration

Agent Orchestration 指对多个 LLM agent 进行协调、调度与编排,使它们通过分工、对话与协作共同完成单个 agent 难以独立完成的复杂任务。

## 在本 wiki 中的出现

- [[2023-autogen]]:微软提出的开源多 agent 框架,通过可定制、可对话的 agent 之间的会话编程来构建复杂 LLM 应用。在该工作中,Agent Orchestration 体现为以 agent 间会话为核心的编排范式——开发者通过组织和定义多个 agent 的角色与对话流程来驱动任务完成。
- [[2024-megaagent-large-scale-mas-without-sop]]:借鉴操作系统进程/线程模型、无需预定义 SOP、可自动生成数百 agent 并行协作的大规模 LLM 多智能体系统,800 秒内开发五子棋、2991 秒协调 590 个 agent 生成国家政策。
- [[2025-multi-agent-collaboration-mechanisms-survey]]:一篇系统综述,沿 actors、types、structures、strategies、coordination protocols 五个维度刻画基于 LLM 的多 agent 系统协作机制,并梳理其跨领域应用与挑战。
- [[2025-llm-multi-agent-autonomous-driving-survey]]:系统综述 LLM 驱动的多智能体自动驾驶系统,按智能体交互模式与结构分类已有方法,并梳理 agent-human 交互、应用、数据集与未来方向。
- [[2025-multiagentbench]]:MultiAgentBench 与 MARBLE 框架,在六个交互式场景中评测 LLM 多智能体的协作与竞争,衡量任务完成度与协调质量;gpt-4o-mini 平均任务分最高、graph 协议在研究场景最优、认知规划使里程碑达成率提升约 3%。
- [[2026-agentorchestra-tea-protocol]]:提出 TEA 协议将工具/环境/智能体建模为带生命周期与版本的一等资源,并构建分层多智能体框架 AgentOrchestra,在 GAIA Test 上达到 89.04% 平均准确率。
- [[2026-orchestration-multi-agent-systems]]:Skan AI 提出的编排式多 agent 系统统一架构:专门化 agent + 四单元编排层 + MCP/A2A 双通信协议 + 治理与可观测性,面向企业落地的工程蓝图综述。
- [[2026-self-organizing-llm-agents]]:一项 25,000 任务的大规模实验发现"内生性悖论":固定智能体顺序但角色自主的混合协议(Sequential)在质量上同时超越中心化(+14%)与完全自主(+44%)协调,但仅当底层模型足够强(存在能力门槛)。
- [[2026-orgagent-company-style-mas]]:提出公司式层级多智能体框架 OrgAgent(治理/执行/合规三层),实证表明层级组织在多数推理任务上同时提升效果并大幅降低 token 成本。

## 相关

- [[multi-agent-systems|multi-agent-system]]
- [[llm-agents|llm-agent]]
- [[conversation-programming]]
- [[2023-autogen]]
- [[standard-operating-procedure]]
- [[coordination-protocol]]
- [[hierarchical-agent-framework]]
