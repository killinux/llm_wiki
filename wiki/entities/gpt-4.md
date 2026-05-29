---
type: entity
subtype: model
tags: [llm, foundation-model, openai, gpt, reasoning, agent]
created: 2026-05-29
updated: 2026-05-29
sources: 36
---

# GPT-4

GPT-4 是 OpenAI 推出的大规模多模态语言模型,凭借强大的推理、代码与指令遵循能力,被广泛用作各类 LLM 智能体与推理方法研究的基础模型。

## 在本 wiki 中的出现

- [[2023-reflexion]]:作为被强化的 LLM 智能体底座,通过语言化的自我反思反馈而非梯度更新从失败中迭代改进。
- [[2023-self-refine]]:作为在测试时执行"自我反馈→自我修正"迭代的同一个 LLM,无需训练即在 7 个任务上平均提升约 20%。
- [[2023-camel-communicative-agents]]:作为 CAMEL 中通过角色扮演与 inception prompting 自主协作的 LLM 智能体(AI User 与 AI Assistant),用于在最少人工干预下完成任务并自动生成大规模指令/对话数据。
- [[2023-self-debugging]]:作为 SELF-DEBUGGING 中通过 few-shot prompting 执行并解释自身生成代码、实现无人工反馈自我调试的 LLM。
- [[2023-memorybank]]:作为配备 MemoryBank 类人长期记忆机制的 LLM,支撑情感陪伴机器人 SiliconFriend。
- [[2023-tree-of-thoughts]]:作为 Tree of Thoughts 的推理模型,在 24 点任务上把成功率从 CoT 的 4% 提升到 74%。
- [[2023-reasoning-via-planning-rap]]:作为 RAP 中同时充当世界模型与推理智能体、用 MCTS 在推理空间做规划的 LLM。
- [[2023-voyager]]:作为驱动 Voyager 的核心模型——首个由 GPT-4 驱动、在 Minecraft 中通过自动课程、可执行代码技能库与自我验证实现终身学习的具身智能体。
- [[2023-multi-agent-debate]]:作为 MAD 框架中"针锋相对"辩论并接受裁判仲裁的多个 LLM 智能体,缓解自我反思的 Degeneration-of-Thought 问题。
- [[2023-lets-verify-step-by-step]]:作为过程监督(PRM)研究中在 MATH 多步数学推理上的评测模型,best-of-N 达 78.2%。
- [[2023-metagpt]]:作为 MetaGPT 多智能体软件开发框架中扮演专业化角色的 LLM,在 HumanEval/MBPP 上达到 SoTA。
- [[2023-agentbench]]:作为 AgentBench 评估的 LLM-as-Agent 之一,横跨 8 个交互环境揭示商业与开源模型的巨大差距。
- [[2023-autogen]]:作为 AutoGen 中可定制、可对话 agent 的底层 LLM,通过会话编程构建复杂 LLM 应用。
- [[2023-expel]]:作为 ExpeL 中不更新参数、从跨任务经验中抽取自然语言洞见并召回相似成功轨迹的 LLM Agent。
- [[2026-generative-social-simulation-validation]]:作为 LLM 驱动生成式 ABM 的代表性模型,文献综述据此讨论黑箱性、文化偏见与随机性如何加剧社会模拟的验证难题。
- [[2025-llm-multi-agent-swarm-intelligence]]:作为驱动 swarm 中各 agent 的 LLM(GPT-4o),在蚁群觅食与鸟群 flocking 场景复现并诱导涌现集体行为。
- [[2023-shepherd-critic-for-lm-generation]]:作为评估 7B critic 模型 Shepherd 的裁判,GPT-4 评测得到 53-87% 的 win-rate。
- [[2023-recmind-llm-agent-for-recommendation]]:作为驱动 RecMind 自主推荐 agent、配合 Self-Inspiring 规划实现 zero-shot 个性化推荐的 LLM。
- [[2023-recommender-ai-agent-interec]]:作为 InteRecAgent 的"大脑",调度传统推荐模型工具构建交互式对话推荐 agent。
- [[2023-ts-llm-tree-search-decoding-training]]:作为 TS-LLM 中被 AlphaZero 风格树搜索同时指导推理解码与迭代训练的 LLM。
- [[2023-llms-cannot-self-correct-reasoning-yet]]:作为论证内在自我纠正设定下无法纠正自身推理错误的被测 LLM。
- [[2023-fireact-language-agent-fine-tuning]]:作为 FireAct 中用多任务多 prompting 轨迹微调以构建语言智能体的 backbone LM 参考。
- [[2023-memgpt]]:作为 MemGPT 中借鉴操作系统分层内存、用函数调用自主管理多级存储以制造"无限上下文"的 LLM。
- [[2023-self-rag]]:作为 Self-RAG 训练单个 LLM 用 reflection token 实现按需检索与自我反思批判的参考模型。
- [[2023-sotopia-social-intelligence-evaluation]]:作为 SOTOPIA-EVAL 评测的社交智能体,在最难子集上目标完成率显著低于人类。
- [[2023-agenttuning]]:作为对比基线,与微调获得可泛化 agent 能力的开源 Llama 2 对照。
- [[2024-eureka-reward-design-via-coding-llms]]:作为 Eureka 中零样本生成可执行奖励函数代码、结合进化搜索与奖励反思的编码 LLM。
- [[2024-metacognition-generative-agents]]:作为引入元认知模块、观察并反思自身思考与行动的 generative agents 底层 LLM。
- [[2024-sotopia-pi-social-agents]]:作为 SOTOPIA-π 中评分过滤社交对话数据的裁判,7B LLM 训练后社交目标完成能力逼近 GPT-4。
- [[2024-autoguide-context-aware-guidelines]]:作为 AUTOGUIDE 中被上下文感知指引增强的 LLM 智能体。
- [[2024-reflection-on-search-trees]]:作为 RoT 中反思 weak LLM 树搜索经验并总结任务级 guideline 注入后续 prompt 的 strong LLM。
- [[2024-self-reflection-llm-agents]]:作为对比 8 种自我反思类型实验中被评测的 LLM agent 之一。
- [[2024-llm-critics-help-catch-llm-bugs]]:作为 OpenAI 用 RLHF 训练的 GPT-4 级别 critic 模型 CriticGPT 的底座,以可扩展监督帮助人类发现代码 bug。
- [[2024-tree-search-for-language-model-agents]]:作为被 inference-time best-first 树搜索增强的 web agent 模型(GPT-4o),在 VisualWebArena 上成功率相对提升 39.7%。
- [[2024-recursive-introspection-rise]]:作为讨论递归反思与自我纠错能力的参考大模型,RISE 让 7B 级 LLM 在无外部反馈下学会跨多轮修正答案。
- [[2024-hiagent-hierarchical-working-memory]]:作为 HiAgent 用 subgoal 分层管理 working memory 的底层 LLM agent。

## 相关

- [[gpt-3-5]]
- [[chatgpt]]
- [[openai]]
- [[llm]]
- [[foundation-model]]
- [[llm-agent]]
- [[chain-of-thought]]
- [[tree-of-thoughts]]
- [[mcts]]
- [[in-context-learning]]
- [[process-reward-model]]
- [[multi-agent-system]]
- [[reasoning]]
- [[benchmark]]
