---
type: concept
subtype: method
tags: [llm, agents, reasoning, memory, multi-agent]
created: 2026-05-29
updated: 2026-05-29
sources: 7
---

# LLM Agents

LLM Agents 指以大语言模型为核心决策器、并通过记忆、规划、工具调用或多实例协作等机制与环境持续交互以完成复杂任务的智能体系统。

## 在本 wiki 中的出现
- [[2023-reflexion]]:将 LLM Agent 作为被强化的主体,用语言化的自我反思反馈(verbal reinforcement)代替梯度更新,使智能体能从失败中迭代改进。
- [[2023-voyager]]:构建了首个由 GPT-4 驱动的具身 LLM Agent,在 Minecraft 中通过自动课程、可执行代码技能库与自我验证实现终身学习。
- [[2023-recagent-user-behavior-simulation]]:提出 RecAgent,用 LLM-based agent 在沙盒中近乎零样本地模拟用户的推荐与社交行为,以研究信息茧房与从众现象。
- [[2023-chatdev]]:用多个 LLM 驱动的角色化软件 Agent,通过对话链沿瀑布式流程协作完成设计、编码、测试与文档的完整软件开发。
- [[2023-agentbench]]:提出首个系统评估 LLM-as-Agent 能力的多维基准,横跨 8 个交互环境测评 29 个模型,揭示商业与开源模型在智能体能力上的巨大差距。
- [[2023-autogen]]:微软提出的开源多 Agent 框架,通过可定制、可对话的 Agent 之间的会话编程来构建复杂的 LLM 应用。
- [[2023-recmind-llm-agent-for-recommendation]]:RecMind 是一个由 LLM 驱动的自主推荐 agent,通过规划、记忆与外部工具实现 zero-shot 个性化推荐,并提出 Self-Inspiring 规划算法保留所有已探索状态以增强规划能力。
- [[2023-recommender-ai-agent-interec]]:提出 InteRecAgent,以 LLM 为大脑、传统推荐模型为工具,通过候选总线记忆、plan-first 执行与 actor-critic 反思构建交互式对话推荐 agent,并蒸馏出 7B 的 RecLlama。
- [[2023-fireact-language-agent-fine-tuning]]:提出用多任务、多 prompting 方法(ReAct/CoT/Reflexion)生成的轨迹微调 backbone LM 来构建语言智能体,在性能、鲁棒性、泛化与成本上全面优于 few-shot prompting。
- [[2023-memgpt-llms-as-operating-systems]]:MemGPT 借鉴操作系统的分层内存与虚拟内存分页,用函数调用让 LLM 自主管理上下文内外的多级存储,在固定上下文模型上制造"无限上下文"的假象。
- [[2023-agentcf-collaborative-learning-agents-recsys]]:把推荐系统中的用户和物品都建模为 LLM agent,通过自主交互与协同反思实现无梯度的协同过滤式优化。
- [[2023-agenttuning]]:通过构建跨任务 agent 交互轨迹数据集 AgentInstruct 并与通用指令混合微调,使开源 Llama 2 获得可泛化的 agent 能力且不损害通用能力。
- [[2024-eureka-reward-design-via-coding-llms]]:Eureka 用编码 LLM(GPT-4)零样本生成可执行奖励函数代码,结合进化搜索与奖励反思迭代改进,在 29 个 RL 环境上达到人类专家级奖励设计并首次让模拟 Shadow Hand 学会转笔。
- [[2023-drivemlm-autonomous-driving]]:DriveMLM 通过将多模态 LLM 的语言决策与模块化 AD 系统的行为规划状态对齐,在 CARLA 仿真器实现闭环自动驾驶,Town05 Long 上 DS 达 76.1,优于 Apollo 4.7 点。
- [[2024-metacognition-generative-agents]]:为 generative agents 引入元认知(metacognition)模块,让 agent 观察并反思自身思考与行动以动态调整策略,在僵尸末日等目标导向场景中显著提升表现。
- [[2024-macrec-multi-agent-recommendation]]:清华提出的多 agent 协作推荐框架(SIGIR'24 demo),用 Manager、Analyst、Reflector、Searcher、Task Interpreter 等角色各异的 LLM agent 直接协作完成评分预测、序列推荐、解释生成与对话推荐。
- [[2024-llm-learnable-planners-long-term-recommendation]]:提出 BiLLP 双层可学习 LLM 规划框架(Planner/Reflector 宏观 + Actor/Critic 微观),在稀疏推荐数据上以 LLM 规划能力做长期推荐,Len 与累积奖励超越从零训练的 RL 与现有 LLM agent 基线。
- [[2024-sotopia-pi-social-agents]]:通过 behavior cloning 与 self-reinforcement 在 GPT-4 评分过滤的社交对话数据上训练,使 7B LLM 的社交目标完成能力逼近 GPT-4,同时提升安全并保持 MMLU。
- [[2024-autoguide-context-aware-guidelines]]:AUTOGUIDE 从离线经验中自动生成并按当前情境检索上下文感知指引,显著提升 LLM 智能体在 ALFWorld、WebShop、WebArena 等序列决策与网页导航任务上的成功率。
- [[2024-self-reflection-llm-agents]]:在 9 个 LLM、1000 道多选题上对比 8 种自我反思类型,证明所有 self-reflection 都能显著提升 LLM agent 的解题准确率(p<0.001)。
- [[2024-generative-ai-as-economic-agents]]:立场/理论论文,主张把生成式 AI 本身建模为有独立信息与(可能错位的)偏好的经济主体,并给出一个把 AI agent 嵌入博弈的形式化框架。
- [[2024-tree-search-for-language-model-agents]]:为 LLM web agent 提出 inference-time best-first tree search,在真实 web 环境中显式做探索与多步规划,把 GPT-4o 在 VisualWebArena 上成功率相对提升 39.7% 至 SOTA 26.4%,并展示 test-time compute scaling 的收益。
- [[2024-hiagent-hierarchical-working-memory]]:HiAgent 用 subgoal 作为 memory chunk 分层管理 LLM agent 的 working memory(汇总过去 observation、按需检索明细轨迹),在五个长程任务上成功率约翻倍(21→42)、context 减少 35%。
- [[2024-limits-of-agency-in-agent-based-models]]:提出 LLM archetypes——为少数代表性 agent 类型查询 LLM 行为再概率采样到个体,从而在百万级 ABM 仿真(NYC 840 万人 COVID-19)中保持规模的同时引入 LLM 自适应行为。
- [[2024-unbounded-generative-infinite-game]]:提出"生成式无限游戏"概念并实现一个角色生活模拟系统:游戏机制、叙事与角色/环境图像全部由 LLM 与 text-to-image 模型实时生成,核心创新是带 Block Drop 的 regional IP-Adapter(保证角色与环境一致性)与将多 LLM 协作能力蒸馏进 Gemma-2B 的实时游戏引擎。
- [[2024-agentic-feedback-loop-recommendation]]:提出 AFL，让 recommendation agent 与 user agent 通过基于 memory 的多轮文本反馈回路相互协作，同时提升推荐（平均 +11.52%）与用户模拟（平均 +21.12%），且不放大流行度/位置偏差。
- [[2024-opencity-urban-llm-agents]]:通过 LLM 请求调度器与 group-and-distill 提示优化,把万级城市 LLM agent 模拟加速约 600 倍,使 10000 agent 的一天活动可在 1 小时内于普通硬件完成。
- [[2024-positive-experience-reflection]]:提出 Sweet&Sour:让 LLM agent 在交互式文本环境中不仅从失败、也从成功经验做反思,并配合双缓冲 managed memory,缓解 self-reflection 在初始成功与小模型上失效的问题;ScienceWorld 上 GPT-4o 平均 54.6、Llama 8B 32.5 均超 Reflexion。
- [[2024-generative-agents-self-reports]]:用基于真人深度访谈与问卷自述构建的 generative agents,可对单个个体在多种社会科学结果上做通用模拟,留出题目预测精度接近个体两周后的重测一致性。
- [[2024-lmagent-multimodal-agents-society]]:基于多模态 LLM 的万级规模 agents 社会,在电商场景模拟多用户的购物、社交、直播行为,复现真实 co-purchase 模式与从众等 emergent behavior。
- [[2025-llm-agents-cooperate-social-dilemma]]:让 ChatGPT-4o 与 Claude 3.5 Sonnet 为 iterated Prisoner's Dilemma 写出完整策略(而非逐步出招),用 evolutionary game theory / Moran process 模拟 LLM agent 群体演化,发现多数场景下侵略策略劣势、系统倾向合作,但博弈论 prompt 与 self-refine 会增强侵略策略并提高收敛到侵略均衡的风险。
- [[2025-agentsociety-large-scale-social-simulation]]:一个整合 LLM 生成式社会 agent、真实城市-社会-经济环境与大规模分布式仿真引擎的社会模拟器,支持上万 agent 并复现极化、谣言、UBI、飓风、城市可持续性五类真实社会实验。
- [[2025-llm-agents-for-recommender-systems-survey]]:系统综述 LLM 驱动 agent 在推荐系统中的应用,提出"面向推荐/交互/模拟"三范式,并用 Profile-Memory-Planning-Action 四模块统一架构对比 23 个方法、汇总数据集与评测。
- [[2025-agentic-memory-llm-agents]]:受 Zettelkasten 启发的 agentic 记忆系统,通过结构化笔记、自主链接生成与记忆演化为 LLM agent 提供可持续演化的长期记忆。
- [[2025-socioverse-world-model-social-simulation]]:SocioVerse 是一个由 LLM agents 驱动、依托 1000 万真实用户池与四个对齐模块的社会模拟 world model,在政治、新闻、经济三大领域复现大规模人群行为。
- [[2025-simuser-llm-user-simulation-recsys]]:基于 LLM 的 agent 框架,用从历史数据推断的 persona、记忆、感知与决策模块构建可信合成用户来低成本评估推荐系统。
- [[2025-llm-driven-cross-platform-npc]]:一个原型系统,让 LLM 驱动的游戏 NPC 通过云数据库在 Unity 游戏内与 Discord 社交平台间跨平台对话并同步记忆。
- [[2025-mem0-scalable-long-term-memory]]:Mem0 是一个以记忆为中心的架构,从持续对话中动态抽取、整合与检索关键信息,并提出图记忆变体 Mem0^g,在 LOCOMO 基准上以约 91% 更低延迟和逾 90% token 节省超越多种基线。
- [[2025-pub-personality-user-behaviour-simulator]]:PUB 是一个基于 LLM 的用户行为模拟器,把 Big Five 人格特质嵌入用户建模,从行为日志推断人格并生成高保真合成交互,用于推荐系统的离线评估。
- [[2025-mmoagent-economic-simulation-mmo]]:提出 MMOAgent，一个基于 LLM 的 Generative Agent-Based Modeling 框架，用具备 profile/感知/推理/记忆/行动的 LLM 智能体模拟 MMO 游戏经济，涌现出角色分化与符合供需规律的价格波动。
- [[2025-memory-os-of-ai-agent]]:借鉴操作系统内存管理,为 AI agent 设计分层(STM/MTM/LPM)、heat 驱动更新的 MemoryOS,统一 Storage/Updating/Retrieval/Generation 四模块,在 LoCoMo 上 F1 平均提升 49.11%、BLEU-1 提升 46.18%。
- [[2025-ai-agent-behavioral-science]]:立场/综述论文,提出 AI Agent Behavioral Science 范式:把 LLM agent 当作行为实体,通过系统观察、干预与理论解释来研究其在个体、多 agent、人-agent 交互三类场景下的行为、适应与 responsible AI。
- [[2025-llm-agent-evaluation-survey]]:SAP Labs 的 LLM agent 评测综述,提出"评测目标 × 评测过程"二维分类法,并强调企业落地中的可靠性、合规与 RBAC 等挑战。
- [[reflexion]] —— LLM Agent 的自我反思机制
- [[react]] —— 推理与行动交织的智能体范式
- [[llm-planning]] —— 智能体的任务分解与规划
- [[tree-of-thoughts]] —— 智能体的搜索式推理
- [[language-agent-tree-search]] —— 将搜索与智能体结合
- [[generative-agents]] —— 模拟人类行为的智能体
- [[embodied-reasoning]] —— 具身智能体的推理
- [[grounding]] —— 将语言落到环境/工具上的能力
- [[in-context-learning]] —— 智能体能力的基础
- [[self-improvement]] —— 智能体从经验中改进
- [[reinforcement-learning]] —— 智能体决策的另一类训练范式
- [[tool-use]] —— 智能体调用外部工具(页面或待建)
- [[multi-agent-system]] —— 多智能体协作(页面或待建)
- [[agent-memory]] —— 智能体的长期记忆(页面或待建)
- [[social-simulation]] —— 大规模社会模拟(页面或待建)
- [[user-simulation]] —— 用户行为模拟(页面或待建)
- [[agent-evaluation]] —— 智能体能力评测(页面或待建)

- [[2023-hyper-actor-critic-recommendation]]:把推荐系统视为序列决策智能体,提出 Hyper-Actor Critic(HAC)框架,将推荐列表生成解耦为 hyper-action 推断与 effect-action 选择两步,并以对齐与监督模块稳定大动作空间下的 RL 推荐策略学习——体现 agent 在巨大离散动作空间中的决策范式。
- [[2023-memorybank]]:为 LLM Agent 设计类人长期记忆机制 MemoryBank,通过存储与分层摘要历史对话、按 Ebbinghaus 遗忘曲线更新记忆、检索相关记忆并构建用户画像,使 agent 具备跨会话的持久记忆能力,并据此实现情感陪伴机器人 SiliconFriend。
- [[2023-multi-agent-debate|2023-multiagent-debate]]:研究 multi-agent 协作范式,让多个 LLM 实例多轮辩论、互相批评彼此答案,在推理(GSM8K 77%→85%)与事实性(MMLU 63.9%→71.1%)任务上显著提升,展示多智能体交互对单体能力的增益。
- [[2023-sotopia-social-intelligence-evaluation]]:SOTOPIA 提出一个开放式社交互动模拟环境与多维评测框架 SOTOPIA-EVAL,交互式地评估 LLM 智能体在目标导向社交场景中的社会智能,发现 GPT-4 在最难子集上的目标完成率显著低于人类。
- [[2024-sage-self-evolving-agents]]:由 User/Assistant/Checker 三 agent 组成、结合迭代反馈、反思与基于 Ebbinghaus 遗忘曲线的记忆优化的自进化 LLM agent 框架,对小模型提升尤为显著。
- [[2024-stateact-self-prompting-state-tracking]]:StateAct 通过 self-prompting 与 chain-of-states 状态跟踪增强 LLM base agent,纯 in-context learning 即在 Alfworld/Webshop/Textcraft 上比 ReAct 提升 7%-30%。
- [[2024-oasis-million-agent-social-simulation]]:通用、可扩展的 LLM-agent 社交媒体模拟器,在 X 与 Reddit 上模拟最多 100 万个 agent,复现信息传播、群体极化与从众效应,并发现规模越大群体动态越丰富、意见越多样有用。

## 相关

- [[generative-agents]]
- [[react]]
- [[reflexion]]
- [[memory-stream]]
- [[reinforcement-learning]]
- [[llm-planning]]
- [[chain-of-thought]]
- [[hyper-actor-critic]]
- [[recommender-systems]]
- [[multi-agent-systems]]
- [[tool-use]]
- [[social-intelligence]]
- [[agent-evaluation]]
- [[in-context-learning]]
- [[social-simulation]]
