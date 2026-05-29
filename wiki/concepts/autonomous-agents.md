---
type: concept
subtype: method
tags: [autonomous-agents, multi-agent, role-playing, llm, instruction-following]
created: 2026-05-29
updated: 2026-05-29
sources: 7
---

# Autonomous Agents

Autonomous Agents 指由 LLM 驱动、能够在最少人工干预下自主进行规划、决策与协作以完成任务的智能体。

## 在本 wiki 中的出现

- [[2023-camel-communicative-agents]]:CAMEL 将 Autonomous Agents 作为核心范式,通过角色扮演(role-playing)与 inception prompting,让两个 LLM 智能体(AI User 与 AI Assistant)在最少人工干预下自主对话、协作完成任务,并在此过程中自动生成大规模的指令/对话数据。
- [[2026-generative-social-simulation-validation]]:一篇系统性文献综述(AI Review 2026, 59:15),梳理 LLM 驱动的生成式 Agent-Based Models 在社会模拟中的应用,论证引入 LLM 因黑箱性、文化偏见与随机性而加剧而非缓解了 ABM 长期的"验证"难题。
- [[2023-agenttuning]]:通过构建跨任务 agent 交互轨迹数据集 AgentInstruct 并与通用指令混合微调,使开源 Llama 2 获得可泛化的 agent 能力且不损害通用能力。
- [[2023-concordia-generative-agent-based-modeling]]:Google DeepMind 提出的库 Concordia,用 LLM 驱动的生成式 agent 在物理/社会/数字空间中扎根交互,通过 Game Master 控制环境,支持 Generative Agent-Based Modeling 的社会仿真与数字服务评估。
- [[2024-generative-ai-as-economic-agents]]:立场/理论论文,主张把生成式 AI 本身建模为有独立信息与(可能错位的)偏好的经济主体,并给出一个把 AI agent 嵌入博弈的形式化框架。
- [[2024-tree-search-for-language-model-agents]]:为 LLM web agent 提出 inference-time best-first tree search,在真实 web 环境中显式做探索与多步规划,把 GPT-4o 在 VisualWebArena 上成功率相对提升 39.7% 至 SOTA 26.4%,并展示 test-time compute scaling 的收益。
- [[2024-megaagent-large-scale-mas-without-sop]]:借鉴操作系统进程/线程模型、无需预定义 SOP、可自动生成数百 agent 并行协作的大规模 LLM 多智能体系统,800 秒内开发五子棋、2991 秒协调 590 个 agent 生成国家政策。

## 相关

- [[llm-agents]]
- [[role-playing]]
- [[inception-prompting]]
- [[communicative-agents]]
- [[generative-agents]]
- [[instruction-tuning]]
- [[ai-user-agent]]
- [[ai-assistant-agent]]
- [[multi-agent-systems]]
- [[agent-based-modeling]]
- [[tool-use]]
- [[planning-and-reasoning]]
- [[test-time-compute]]
- [[web-agents]]
