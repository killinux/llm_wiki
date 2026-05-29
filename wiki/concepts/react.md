---
type: concept
subtype: method
tags: [agents, reasoning, acting, tool-use, prompting]
created: 2026-05-29
updated: 2026-05-29
sources: 18
---

# ReAct

ReAct(Reasoning + Acting)是一种让 LLM 交替生成推理痕迹(reasoning trace)与行动(action)的范式,使模型一边思考一边与外部环境/工具交互,并依据观测反馈调整后续推理与计划。

## 在本 wiki 中的出现
- [[2024-tree-search-for-language-model-agents]]:为 LLM web agent 提出 inference-time best-first tree search,在真实 web 环境中显式做探索与多步规划,把 GPT-4o 在 VisualWebArena 上成功率相对提升 39.7% 至 SOTA 26.4%,并展示 test-time compute scaling 的收益。
- [[2024-stateact-self-prompting-state-tracking]]:StateAct 通过 self-prompting 与 chain-of-states 状态跟踪增强 LLM base agent,纯 in-context learning 即在 Alfworld/Webshop/Textcraft 上比 ReAct 提升 7%-30%。
- [[2025-multiagentbench]]:MultiAgentBench 与 MARBLE 框架在六个交互式场景中评测 LLM 多智能体的协作与竞争,衡量任务完成度与协调质量,gpt-4o-mini 平均任务分最高、graph 协议在研究场景最优、认知规划使里程碑达成率提升约 3%。
- [[tree-search]]
- [[working-memory]]
- [[test-time-compute-scaling]]
- [[in-context-learning]]
- [[multi-agent-systems]]
- [[2023-expel]]:以 ReAct 风格的 LLM Agent 为基础。ExpeL 在不更新模型参数的前提下,让 Agent 从跨任务经验中自主抽取自然语言洞见,并召回相似的成功轨迹,以提升其在决策任务上的表现。
- [[2024-positive-experience-reflection]]:提出 Sweet&Sour,让 LLM agent 在交互式文本环境中不仅从失败、也从成功经验做反思,并配合双缓冲 managed memory,缓解 self-reflection 在初始成功与小模型上失效的问题;ScienceWorld 上 GPT-4o 平均 54.6、Llama 8B 32.5 均超 Reflexion。
- [[reflexion]]
- [[llm-agents|llm-agent]]
- [[scienceworld]]

- [[2023-reflexion]]:以 ReAct 式的"推理-行动"智能体为基础,叠加语言化的自我反思反馈(而非梯度更新)来强化 LLM 智能体,使其从失败中迭代改进。
- [[2023-critic]]:CRITIC 在 ReAct 这类工具增强的推理流程之上,让 LLM 通过与搜索引擎、代码解释器、PERSPECTIVE API 等外部工具交互来自我验证并迭代修正输出,体现了"行动"环节中外部反馈对自我改进的关键作用。
- [[2023-voyager]]:作为首个 GPT-4 驱动的具身智能体,在 Minecraft 中通过自动课程、可执行代码技能库与自我验证实现终身学习,其"推理后执行代码并依据环境反馈修正"的循环延续了 ReAct 的思路。
- [[2023-metagpt]]:MetaGPT 把人类 SOP 编码进 prompt,用专业化角色与结构化输出构建 LLM 多智能体软件开发框架(在 HumanEval/MBPP 上达到 SoTA);其各角色智能体内部的"思考-行动"循环可视为 ReAct 在多智能体协作中的运用。
- [[2023-autogen]]:微软提出的开源多 agent 框架,通过可定制、可对话 agent 之间的会话编程构建复杂 LLM 应用,支持 agent 在对话中交错推理与调用工具/执行代码,承袭 ReAct 的交互模式。
- [[2023-recmind-llm-agent-for-recommendation]]:RecMind 是一个由 LLM 驱动的自主推荐 agent,通过规划、记忆与外部工具实现 zero-shot 个性化推荐,并提出 Self-Inspiring 规划算法保留所有已探索状态以增强规划能力。
- [[2023-recommender-ai-agent-interec]]:提出 InteRecAgent,以 LLM 为大脑、传统推荐模型为工具,通过候选总线记忆、plan-first 执行与 actor-critic 反思构建交互式对话推荐 agent,并蒸馏出 7B 的 RecLlama。
- [[2023-fireact-language-agent-fine-tuning]]:提出用多任务、多 prompting 方法(ReAct/CoT/Reflexion)生成的轨迹微调 backbone LM 来构建语言智能体,在性能、鲁棒性、泛化与成本上全面优于 few-shot prompting。
- [[2023-agentcf-collaborative-learning-agents-recsys]]:把推荐系统中的用户和物品都建模为 LLM agent,通过自主交互与协同反思实现无梯度的协同过滤式优化。
- [[2023-agenttuning]]:通过构建跨任务 agent 交互轨迹数据集 AgentInstruct 并与通用指令混合微调,使开源 Llama 2 获得可泛化的 agent 能力且不损害通用能力。
- [[2024-macrec-multi-agent-recommendation]]:清华提出的多 agent 协作推荐框架(SIGIR'24 demo),用 Manager、Analyst、Reflector、Searcher、Task Interpreter 等角色各异的 LLM agent 直接协作完成评分预测、序列推荐、解释生成与对话推荐。
- [[2024-llm-learnable-planners-long-term-recommendation]]:提出 BiLLP 双层可学习 LLM 规划框架(Planner/Reflector 宏观 + Actor/Critic 微观),在稀疏推荐数据上以 LLM 规划能力做长期推荐,Len 与累积奖励超越从零训练的 RL 与现有 LLM agent 基线。
- [[2024-autoguide-context-aware-guidelines]]:AUTOGUIDE 从离线经验中自动生成并按当前情境检索上下文感知指引,显著提升 LLM 智能体在 ALFWorld、WebShop、WebArena 等序列决策与网页导航任务上的成功率。
- [[2024-hiagent-hierarchical-working-memory]]:HiAgent 用 subgoal 作为 memory chunk 分层管理 LLM agent 的 working memory(汇总过去 observation、按需检索明细轨迹),在五个长程任务上成功率约翻倍(21→42)、context 减少 35%。
- [[2025-mmoagent-economic-simulation-mmo]]:提出 MMOAgent,一个基于 LLM 的 Generative Agent-Based Modeling 框架,用具备 profile/感知/推理/记忆/行动的 LLM 智能体模拟 MMO 游戏经济,涌现出角色分化与符合供需规律的价格波动。
- [[2025-generative-mmo-simulation]]:用 LLM 驱动的生成式多智能体 MMO 游戏仿真系统,在真实玩家数据上 SFT+GRPO 微调 agent,高保真模拟玩家决策,低成本评估数值系统与机制设计的干预效果。
- [[2025-multi-agent-reflexion-mar]]:把 Reflexion 的单 Agent 自我批评换成多 persona 辩论加 judge 合成反思,在 HotPotQA(EM 44→47)与 HumanEval(pass@1 76.4→82.6)上超过单 Agent Reflexion。
- [[2026-experiential-reflective-learning]]:ERL,agent 反思单次任务轨迹与成败信号、提炼可迁移启发式存入持久池,新任务时按相关性检索 top-k 注入上下文,无需更新参数即可自我改进,在 Gaia2 上比 ReAct 基线提升 7.8% 成功率。

## 相关

- [[chain-of-thought]]
- [[tool-use]]
- [[llm-agents]]
- [[self-reflection]]
- [[language-agent-tree-search]]
- [[tree-of-thoughts]]
