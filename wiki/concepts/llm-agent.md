---
type: concept
subtype: method
tags: [LLM, agent, autonomy, planning, tool-use, multi-agent]
created: 2026-05-29
updated: 2026-05-29
sources: 23
---

# LLM Agent

LLM Agent 是以大语言模型为决策核心、能够感知环境、规划任务、调用工具或技能并通过多轮交互自主完成目标的智能体。

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

## 相关

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
