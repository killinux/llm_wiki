---
type: concept
subtype: method
tags: [agent, memory, LLM, experience, retrieval]
created: 2026-05-29
updated: 2026-05-29
sources: 19
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
- [[2024-sage-self-evolving-agents]]:由 User/Assistant/Checker 三 agent 组成、结合迭代反馈、反思与基于 Ebbinghaus 遗忘曲线的记忆优化的自进化 LLM agent 框架,对小模型提升尤为显著。
- [[2024-agentic-feedback-loop-recommendation]]:提出 AFL,让 recommendation agent 与 user agent 通过基于 memory 的多轮文本反馈回路相互协作,同时提升推荐(平均 +11.52%)与用户模拟(平均 +21.12%),且不放大流行度/位置偏差。
- [[2024-positive-experience-reflection]]:提出 Sweet&Sour:让 LLM agent 在交互式文本环境中不仅从失败、也从成功经验做反思,并配合双缓冲 managed memory,缓解 self-reflection 在初始成功与小模型上失效的问题;ScienceWorld 上 GPT-4o 平均 54.6、Llama 8B 32.5 均超 Reflexion。
- [[2024-lmagent-multimodal-agents-society]]:基于多模态 LLM 的万级规模 agents 社会,在电商场景模拟多用户的购物、社交、直播行为,复现真实 co-purchase 模式与从众等 emergent behavior。
- [[2025-agentsociety-large-scale-social-simulation]]:一个整合 LLM 生成式社会 agent、真实城市-社会-经济环境与大规模分布式仿真引擎的社会模拟器,支持上万 agent 并复现极化、谣言、UBI、飓风、城市可持续性五类真实社会实验。
- [[2025-agentic-memory-llm-agents]]:受 Zettelkasten 启发的 agentic 记忆系统,通过结构化笔记、自主链接生成与记忆演化为 LLM agent 提供可持续演化的长期记忆。
- [[2025-agentcf-plus-plus]]:通过双层记忆架构、两步融合机制与兴趣组共享记忆增强 AgentCF 用户模拟器,在跨域推荐中减少无关信息并显式建模流行度因素。
- [[2025-llm-multi-agent-autonomous-driving-survey]]:系统综述 LLM 驱动的多智能体自动驾驶系统,按智能体交互模式与结构分类已有方法,并梳理 agent-human 交互、应用、数据集与未来方向。
- [[2025-meminsight-autonomous-memory-augmentation]]:提出 MemInsight,让 LLM agent 自主从历史交互挖掘语义属性以增强记忆表示与检索,在对话推荐、问答、事件摘要上显著提升(推荐说服力最高 +14%,LoCoMo 召回比 RAG 基线高 34%)。
- [[2025-llm-driven-cross-platform-npc]]:一个原型系统,让 LLM 驱动的游戏 NPC 通过云数据库在 Unity 游戏内与 Discord 社交平台间跨平台对话并同步记忆。
- [[2025-mem0-scalable-long-term-memory]]:Mem0 是一个以记忆为中心的架构,从持续对话中动态抽取、整合与检索关键信息,并提出图记忆变体 Mem0^g,在 LOCOMO 基准上以约 91% 更低延迟和逾 90% token 节省超越多种基线。
- [[2025-memory-os-of-ai-agent]]:借鉴操作系统内存管理,为 AI agent 设计分层(STM/MTM/LPM)、heat 驱动更新的 MemoryOS,统一 Storage/Updating/Retrieval/Generation 四模块,在 LoCoMo 上 F1 平均提升 49.11%、BLEU-1 提升 46.18%。

## 相关

- [[llm-long-term-memory]]
- [[lifelong-learning]]
- [[memory-module]]
- [[memory-stream]]
- [[in-context-learning]]
- [[retrieval-augmented-generation]]
- [[self-reflection]]
- [[llm-agent]]
