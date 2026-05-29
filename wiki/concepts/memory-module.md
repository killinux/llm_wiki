---
type: concept
subtype: method
tags: [memory, llm-agent, agent-architecture, simulation]
created: 2026-05-29
updated: 2026-05-29
sources: 9
---

# Memory Module

Memory Module 是 LLM-based agent 架构中负责存储、组织与检索 agent 历史经验和观察信息的组件,使 agent 能够基于过去的交互做出连贯且具上下文感知的决策。

## 在本 wiki 中的出现

- [[2023-recagent-user-behavior-simulation]]:在 RecAgent 中,Memory Module 是每个 LLM-based agent 的核心组件之一,用于记录 agent 在沙盒环境中的推荐与社交行为经验。借助对历史行为的存储与检索,agent 能够近乎零样本地模拟出连贯的用户行为,从而支撑对信息茧房(filter bubble)与从众现象(conformity)等群体现象的研究。
- [[2023-recmind-llm-agent-for-recommendation]]:RecMind 是一个由 LLM 驱动的自主推荐 agent,通过规划、记忆与外部工具实现 zero-shot 个性化推荐,并提出 Self-Inspiring 规划算法保留所有已探索状态以增强规划能力。
- [[2023-agentcf-collaborative-learning-agents-recsys]]:把推荐系统中的用户和物品都建模为 LLM agent,通过自主交互与协同反思实现无梯度的协同过滤式优化。
- [[2024-generative-agents-in-recommendation]]:Agent4Rec 用 1000 个 LLM 驱动的生成式 agent(含 profile/memory/action 模块)构建电影推荐用户模拟器,探究其能否忠实模拟真实用户行为并复现 filter bubble 与 popularity bias。
- [[2024-sage-self-evolving-agents]]:由 User/Assistant/Checker 三 agent 组成、结合迭代反馈、反思与基于 Ebbinghaus 遗忘曲线的记忆优化的自进化 LLM agent 框架,对小模型提升尤为显著。
- [[2024-agentic-feedback-loop-recommendation]]:提出 AFL,让 recommendation agent 与 user agent 通过基于 memory 的多轮文本反馈回路相互协作,同时提升推荐(平均 +11.52%)与用户模拟(平均 +21.12%),且不放大流行度/位置偏差。
- [[2025-reflective-memory-management]]:提出 RMM(Reflective Memory Management):用主题粒度的前瞻反思组织对话记忆,并用 LLM 引用信号在线 RL 精炼检索 reranker,在 LongMemEval 上比无记忆基线提升 10%+ 准确率。
- [[2025-simuser-llm-user-simulation-recsys]]:基于 LLM 的 agent 框架,用从历史数据推断的 persona、记忆、感知与决策模块构建可信合成用户来低成本评估推荐系统。
- [[2025-memory-os-of-ai-agent]]:借鉴操作系统内存管理,为 AI agent 设计分层(STM/MTM/LPM)、heat 驱动更新的 MemoryOS,统一 Storage/Updating/Retrieval/Generation 四模块,在 LoCoMo 上 F1 平均提升 49.11%、BLEU-1 提升 46.18%。

## 相关

- [[memory-stream]]
- [[llm-long-term-memory]]
- [[memorybank]]
- [[llm-agent]]
- [[generative-agents]]
- [[recommender-system]]
