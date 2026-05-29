---
type: concept
subtype: method
tags: [agent, tool-use, reasoning]
created: 2026-05-29
updated: 2026-05-29
sources: 14
---

# 工具使用

工具使用(Tool Use)是指 LLM 在生成过程中调用外部工具(如搜索引擎、代码解释器、API 等)以获取信息、执行计算或获得反馈,从而突破自身参数化知识与能力的局限。

## 在本 wiki 中的出现

- [[2023-critic]]:CRITIC 让 LLM 通过与搜索引擎、代码解释器、PERSPECTIVE API 等外部工具交互来自我验证(self-verify)并迭代修正输出,证明外部反馈对自我改进至关重要。
- [[2023-autogen]]:微软提出的开源多 agent 框架,通过可定制、可对话 agent 之间的会话编程来构建复杂 LLM 应用,工具使用是 agent 协作完成任务的重要能力之一。
- [[2023-recmind-llm-agent-for-recommendation]]:RecMind 是一个由 LLM 驱动的自主推荐 agent,通过规划、记忆与外部工具实现 zero-shot 个性化推荐,并提出 Self-Inspiring 规划算法保留所有已探索状态以增强规划能力。
- [[2023-recommender-ai-agent-interec]]:提出 InteRecAgent,以 LLM 为大脑、传统推荐模型为工具,通过候选总线记忆、plan-first 执行与 actor-critic 反思构建交互式对话推荐 agent,并蒸馏出 7B 的 RecLlama。
- [[2023-chain-of-verification]]:Chain-of-Verification (CoVe) 让 LLM 先生成草稿,再独立回答自我规划的验证问题来核查事实,显著降低幻觉。
- [[2023-memgpt-llms-as-operating-systems]]:MemGPT 借鉴操作系统的分层内存与虚拟内存分页,用函数调用让 LLM 自主管理上下文内外的多级存储,在固定上下文模型上制造"无限上下文"的假象。
- [[2023-agenttuning]]:通过构建跨任务 agent 交互轨迹数据集 AgentInstruct 并与通用指令混合微调,使开源 Llama 2 获得可泛化的 agent 能力且不损害通用能力。
- [[2023-concordia-generative-agent-based-modeling]]:Google DeepMind 提出的库 Concordia,用 LLM 驱动的生成式 agent 在物理/社会/数字空间中扎根交互,通过 Game Master 控制环境,支持 Generative Agent-Based Modeling 的社会仿真与数字服务评估。
- [[2023-drivemlm-autonomous-driving]]:DriveMLM 通过将多模态 LLM 的语言决策与模块化 AD 系统的行为规划状态对齐,在 CARLA 仿真器实现闭环自动驾驶,Town05 Long 上 DS 达 76.1,优于 Apollo 4.7 点。
- [[2024-macrec-multi-agent-recommendation]]:清华提出的多 agent 协作推荐框架(SIGIR'24 demo),用 Manager、Analyst、Reflector、Searcher、Task Interpreter 等角色各异的 LLM agent 直接协作完成评分预测、序列推荐、解释生成与对话推荐。
- [[2024-megaagent-large-scale-mas-without-sop]]:借鉴操作系统进程/线程模型、无需预定义 SOP、可自动生成数百 agent 并行协作的大规模 LLM 多智能体系统,800 秒内开发五子棋、2991 秒协调 590 个 agent 生成国家政策。
- [[2024-agentic-feedback-loop-recommendation]]:提出 AFL,让 recommendation agent 与 user agent 通过基于 memory 的多轮文本反馈回路相互协作,同时提升推荐(平均 +11.52%)与用户模拟(平均 +21.12%),且不放大流行度/位置偏差。
- [[2026-agentorchestra-tea-protocol]]:提出 TEA 协议将工具/环境/智能体建模为带生命周期与版本的一等资源,并构建分层多智能体框架 AgentOrchestra,在 GAIA Test 上达到 89.04% 平均准确率。
- [[2025-llm-agent-evaluation-survey]]:SAP Labs 的 LLM agent 评测综述,提出"评测目标 × 评测过程"二维分类法,并强调企业落地中的可靠性、合规与 RBAC 等挑战。

## 相关

- [[react]] — ReAct 的 action 通常就是调用外部工具
- [[llm-agent]] — 工具使用是构建 LLM agent 的核心能力
- [[multi-agent-systems]] — AutoGen 中工具使用是多 agent 协作完成任务的能力之一
- [[self-critique]] — CRITIC 中通过工具反馈实现自我验证
- [[agent-evaluation]] — LLM agent 评测中工具调用能力是关键评测维度
