---
type: concept
subtype: method
tags: [multi-agent, llm, collaboration, role-play, sop]
created: 2026-05-29
updated: 2026-05-29
sources: 6
---

# LLM 多智能体系统

LLM 多智能体系统(LLM Multi-Agent System)指由多个基于大语言模型的 agent 通过分工、协作与通信共同完成复杂任务的系统。

## 在本 wiki 中的出现

- [[2023-metagpt]]:MetaGPT 把人类工作流中的标准操作流程(SOP)编码进 prompt,通过为不同 agent 分配专业化角色并要求结构化输出,构建了一个 LLM 多智能体软件开发框架,在 HumanEval 与 MBPP 上达到 SoTA。
- [[2026-generative-social-simulation-validation]]:一篇系统性文献综述(AI Review 2026, 59:15),梳理 LLM 驱动的生成式 Agent-Based Models 在社会模拟中的应用,论证引入 LLM 因黑箱性、文化偏见与随机性而加剧而非缓解了 ABM 长期的"验证"难题。
- [[2025-llm-multi-agent-swarm-intelligence]]:把 agent-based modeling 中 agent 的硬编码程序替换为 GPT-4o 驱动的 prompt,在蚁群觅食与鸟群 flocking 两个经典 swarm intelligence 场景中复现并诱导涌现集体行为。
- [[2023-concordia-generative-agent-based-modeling]]:Google DeepMind 提出的库 Concordia,用 LLM 驱动的生成式 agent 在物理/社会/数字空间中扎根交互,通过 Game Master 控制环境,支持 Generative Agent-Based Modeling 的社会仿真与数字服务评估。
- [[2024-hiagent-hierarchical-working-memory]]:HiAgent 用 subgoal 作为 memory chunk 分层管理 LLM agent 的 working memory(汇总过去 observation、按需检索明细轨迹),在五个长程任务上成功率约翻倍(21→42)、context 减少 35%。
- [[2024-megaagent-large-scale-mas-without-sop]]:借鉴操作系统进程/线程模型、无需预定义 SOP、可自动生成数百 agent 并行协作的大规模 LLM 多智能体系统,800 秒内开发五子棋、2991 秒协调 590 个 agent 生成国家政策。

## 相关

- [[multi-agent-systems]]
- [[multi-agent-debate]]
- [[standard-operating-procedure]]
- [[role-playing]]
- [[llm-agents]]
- [[generative-agents]]
- [[code-generation]]
- [[chatdev]]
- [[agent-based-modeling]]
- [[generative-agent-based-modeling]]
- [[swarm-intelligence]]
- [[emergent-behavior]]
- [[social-simulation]]
- [[llm-agent-memory]]
