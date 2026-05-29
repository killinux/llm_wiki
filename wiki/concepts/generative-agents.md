---
type: concept
subtype: method
tags: [generative-agents, llm-agent, simulation, memory]
created: 2026-05-29
updated: 2026-05-29
sources: 7
---

# Generative Agents

Generative Agents 指由 LLM 驱动、能够存储与检索记忆、反思并据此自主行动的智能体,用于在交互式环境(如沙盒)中模拟可信的人类个体与群体行为。

## 在本 wiki 中的出现

- [[2023-memorybank]]:面向 Generative Agents 所依赖的核心能力——长期记忆。该工作提出 MemoryBank 机制:存储与分层摘要历史对话、按 Ebbinghaus 遗忘曲线动态更新记忆强度、检索相关记忆并构建用户画像,从而让 agent 在长期交互中保持人格与记忆连贯,并据此实现情感陪伴机器人 SiliconFriend。
- [[2023-recagent-user-behavior-simulation]]:Generative Agents 思路在推荐场景的具体应用。提出 RecAgent,用 LLM-based agent 在沙盒中近乎零样本地模拟用户的推荐与社交行为,并借助这种 agent 模拟研究信息茧房与从众等现象。
- [[2026-generative-social-simulation-validation]]:一篇系统性文献综述(AI Review 2026, 59:15),梳理 LLM 驱动的生成式 Agent-Based Models 在社会模拟中的应用,论证引入 LLM 因黑箱性、文化偏见与随机性而加剧而非缓解了 ABM 长期的"验证"难题。
- [[2023-agentcf-collaborative-learning-agents-recsys]]:把推荐系统中的用户和物品都建模为 LLM agent,通过自主交互与协同反思实现无梯度的协同过滤式优化。
- [[2024-generative-agents-in-recommendation]]:Agent4Rec 用 1000 个 LLM 驱动的生成式 agent(含 profile/memory/action 模块)构建电影推荐用户模拟器,探究其能否忠实模拟真实用户行为并复现 filter bubble 与 popularity bias。
- [[2023-concordia-generative-agent-based-modeling]]:Google DeepMind 提出的库 Concordia,用 LLM 驱动的生成式 agent 在物理/社会/数字空间中扎根交互,通过 Game Master 控制环境,支持 Generative Agent-Based Modeling 的社会仿真与数字服务评估。
- [[2024-metacognition-generative-agents]]:为 generative agents 引入元认知(metacognition)模块,让 agent 观察并反思自身思考与行动以动态调整策略,在僵尸末日等目标导向场景中显著提升表现。

## 相关

- [[2023-generative-agents]]
- [[memory-stream]]
- [[llm-agent]]
- [[autonomous-agents]]
- [[llm-long-term-memory]]
- [[multi-agent-systems]]
- [[role-playing]]
- [[in-context-learning]]
