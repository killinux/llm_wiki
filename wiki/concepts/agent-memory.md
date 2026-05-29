---
type: concept
subtype: method
tags: [agent, memory, LLM, experience, retrieval]
created: 2026-05-29
updated: 2026-05-29
sources: 7
---

# Agent 记忆

Agent 记忆指 LLM Agent 在不更新模型参数的前提下,把过往交互、任务经验或外部知识存储下来,并在后续决策时召回利用的机制,用于跨任务、跨回合地积累与复用经验。

## 在本 wiki 中的出现

- [[2023-expel]]:把 Agent 记忆作为参数不更新的经验复用手段。Agent 从跨任务的成功与失败轨迹中自主抽取自然语言形式的洞见(insights),并在面对新任务时召回相似的成功轨迹,以此提升决策表现,而无需对 LLM 进行任何梯度更新。
- [[2023-recommender-ai-agent-interec]]:提出 InteRecAgent,以 LLM 为大脑、传统推荐模型为工具,通过候选总线记忆、plan-first 执行与 actor-critic 反思构建交互式对话推荐 agent,并蒸馏出 7B 的 RecLlama。
- [[2023-memgpt-llms-as-operating-systems]]:MemGPT 借鉴操作系统的分层内存与虚拟内存分页,用函数调用让 LLM 自主管理上下文内外的多级存储,在固定上下文模型上制造"无限上下文"的假象。
- [[2023-agentcf-collaborative-learning-agents-recsys]]:把推荐系统中的用户和物品都建模为 LLM agent,通过自主交互与协同反思实现无梯度的协同过滤式优化。
- [[2023-concordia-generative-agent-based-modeling]]:Google DeepMind 提出的库 Concordia,用 LLM 驱动的生成式 agent 在物理/社会/数字空间中扎根交互,通过 Game Master 控制环境,支持 Generative Agent-Based Modeling 的社会仿真与数字服务评估。
- [[2024-llm-learnable-planners-long-term-recommendation]]:提出 BiLLP 双层可学习 LLM 规划框架(Planner/Reflector 宏观 + Actor/Critic 微观),在稀疏推荐数据上以 LLM 规划能力做长期推荐,Len 与累积奖励超越从零训练的 RL 与现有 LLM agent 基线。
- [[2024-hiagent-hierarchical-working-memory]]:HiAgent 用 subgoal 作为 memory chunk 分层管理 LLM agent 的 working memory(汇总过去 observation、按需检索明细轨迹),在五个长程任务上成功率约翻倍(21→42)、context 减少 35%。

## 相关

- [[llm-long-term-memory]]
- [[lifelong-learning]]
- [[memory-module]]
- [[memory-stream]]
- [[in-context-learning]]
- [[retrieval-augmented-generation]]
- [[self-reflection]]
- [[llm-agent]]
