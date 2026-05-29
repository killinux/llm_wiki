---
type: concept
subtype: method
tags: [prompting, reasoning, in-context-learning, llm]
created: 2026-05-29
updated: 2026-05-29
sources: 38
---

# Chain-of-Thought Prompting

Chain-of-Thought (CoT) Prompting 是一种提示方法,通过引导大语言模型在给出最终答案前显式生成中间推理步骤,从而显著提升其在多步推理任务上的表现。

## 在本 wiki 中的出现

- [[2022-chain-of-thought]]:提出 chain-of-thought prompting 的原始工作。在 few-shot 示例中加入中间推理步骤,显著提升大模型的多步推理能力,且该增益随模型规模涌现(PaLM 540B 在 GSM8K 达到 57%)。
- [[2022-star-self-taught-reasoner]]:STaR 用少量 CoT 示例让模型自己生成推理过程,只保留答对的 rationale(并用 rationalization 从答错题反向补全),反复微调自身以 bootstrap 推理能力。CoT 在此作为自训练数据生成的基础。
- [[2022-inner-monologue]]:通过持续注入自然语言环境反馈,让 frozen LLM 形成"内心独白"形式的链式推理,实现机器人的闭环、可重规划具身推理。
- [[2022-constitutional-ai]]:Anthropic 的 Constitutional AI 在模型自我批评与修改环节依赖链式推理,用一套人类书写的原则替代人类有害性标注,通过 AI 反馈(RLAIF)训练既无害又非回避的助手。
- [[2023-reflexion]]:用语言化的自我反思反馈(而非梯度更新)强化 LLM 智能体,在 CoT 之上叠加反思链,使其从失败中迭代改进。
- [[2023-self-refine]]:用同一个 LLM 在测试时迭代"自我反馈→自我修正",在推理链基础上无需训练即在 7 个任务上平均提升约 20%。
- [[2023-self-debugging]]:提出 SELF-DEBUGGING,通过 few-shot prompting 让 LLM 执行并解释自己生成的代码,以链式推理实现无人工反馈的自我调试。
- [[2023-plan-and-solve-prompting]]:提出零样本 Plan-and-Solve (PS/PS+) 提示,让 LLM 先制定计划再执行子任务,显著改进 Zero-shot-CoT 的多步推理,是对 CoT 的直接改进。
- [[2023-tree-of-thoughts]]:将 LLM 推理从线性的 CoT 扩展为在「思考」树上的搜索(可前瞻、自评估、回溯),在 24 点上把 GPT-4 成功率从 CoT 的 4% 提升到 74%。
- [[2023-multiagent-debate]]:让多个 LLM 实例多轮辩论、互相批评彼此的推理链,在推理(GSM8K 77%→85%)与事实性(MMLU 63.9%→71.1%)任务上显著提升。
- [[2023-reasoning-via-planning-rap]]:RAP 把 LLM 同时当作世界模型和推理智能体,用 MCTS 在推理空间里做规划,把 CoT 式的 LLM 推理重新表述为带世界模型的规划。
- [[2023-multi-agent-debate]]:提出 Multi-Agent Debate(MAD)框架,用多个 LLM 智能体"针锋相对"辩论加裁判仲裁,缓解自我反思链的 Degeneration-of-Thought 问题并激发发散性思维。
- [[2023-metagpt]]:MetaGPT 把人类 SOP 编码进 prompt,用专业化角色与结构化输出构建 LLM 多智能体软件开发框架,智能体内部依赖链式推理,在 HumanEval/MBPP 上达到 SoTA。
- [[2023-agentbench]]:首个系统评估 LLM-as-Agent 能力的多维基准,横跨 8 个交互环境测评 29 个模型,其智能体任务的求解普遍依赖链式推理,揭示商业与开源模型的巨大差距。
- [[2025-llm-multi-agent-swarm-intelligence]]:把 agent-based modeling 中 agent 的硬编码程序替换为 GPT-4o 驱动的 prompt,在蚁群觅食与鸟群 flocking 两个经典 swarm intelligence 场景中复现并诱导涌现集体行为。
- [[2023-recmind-llm-agent-for-recommendation]]:RecMind 是一个由 LLM 驱动的自主推荐 agent,通过规划、记忆与外部工具实现 zero-shot 个性化推荐,并提出 Self-Inspiring 规划算法保留所有已探索状态以增强规划能力。
- [[2023-chain-of-verification]]:Chain-of-Verification (CoVe) 让 LLM 先生成草稿,再独立回答自我规划的验证问题来核查事实,显著降低幻觉。
- [[2023-ts-llm-tree-search-decoding-training]]:TS-LLM:用学习的 value function 的 AlphaZero 风格树搜索,同时指导 LLM 的推理解码与迭代训练,适配任意规模 LLM 并将搜索深度扩展到 64。
- [[2023-fireact-language-agent-fine-tuning]]:提出用多任务、多 prompting 方法(ReAct/CoT/Reflexion)生成的轨迹微调 backbone LM 来构建语言智能体,在性能、鲁棒性、泛化与成本上全面优于 few-shot prompting。
- [[2024-generative-agents-in-recommendation]]:Agent4Rec 用 1000 个 LLM 驱动的生成式 agent(含 profile/memory/action 模块)构建电影推荐用户模拟器,探究其能否忠实模拟真实用户行为并复现 filter bubble 与 popularity bias。
- [[2023-agenttuning]]:通过构建跨任务 agent 交互轨迹数据集 AgentInstruct 并与通用指令混合微调,使开源 Llama 2 获得可泛化的 agent 能力且不损害通用能力。
- [[2024-quiet-star]]:Quiet-STaR 让语言模型在每个 token 前生成隐式 rationale 来更好预测后续文本,以自监督方式从任意文本学会推理,zero-shot 提升 GSM8K(5.9%→10.9%)与 CommonsenseQA(36.3%→47.2%)。
- [[2024-reflection-on-search-trees]]:RoT 让 strong LLM 反思 weak LLM 的历史树搜索经验、对关键状态总结出任务级 guideline 注入后续 prompt,显著提升 BFS/MCTS 等树搜索 prompting 在 Blocksworld、GSM8k、议价任务上的准确率与搜索效率,且任务越难收益越大。
- [[2024-self-reflection-llm-agents]]:在 9 个 LLM、1000 道多选题上对比 8 种自我反思类型,证明所有 self-reflection 都能显著提升 LLM agent 的解题准确率(p<0.001)。
- [[2024-llm4rerank-auto-reranking-recommendation]]:把推荐 reranking 的 accuracy/diversity/fairness 等目标抽象为全连接图中的 node,让 LLM 以 Chain-of-Thought 多跳方式按用户给定的 "Goal" 自动综合多目标重排候选列表。
- [[2024-tree-search-for-language-model-agents]]:为 LLM web agent 提出 inference-time best-first tree search,在真实 web 环境中显式做探索与多步规划,把 GPT-4o 在 VisualWebArena 上成功率相对提升 39.7% 至 SOTA 26.4%,并展示 test-time compute scaling 的收益。
- [[2024-multi-agent-tot-validator]]:将 Tree-of-Thoughts 与多智能体推理结合,新增 Thought Validator agent 过滤无效推理分支后再共识投票,在 GSM8K 上比标准 ToT 平均提升 5.6 个百分点。
- [[2024-stateact-self-prompting-state-tracking]]:StateAct 通过 self-prompting 与 chain-of-states 状态跟踪增强 LLM base agent,纯 in-context learning 即在 Alfworld/Webshop/Textcraft 上比 ReAct 提升 7%-30%。
- [[2024-agentic-feedback-loop-recommendation]]:提出 AFL，让 recommendation agent 与 user agent 通过基于 memory 的多轮文本反馈回路相互协作，同时提升推荐（平均 +11.52%）与用户模拟（平均 +21.12%），且不放大流行度/位置偏差。
- [[2024-opencity-urban-llm-agents]]:通过 LLM 请求调度器与 group-and-distill 提示优化,把万级城市 LLM agent 模拟加速约 600 倍,使 10000 agent 的一天活动可在 1 小时内于普通硬件完成。
- [[2024-oasis-million-agent-social-simulation]]:通用、可扩展的 LLM-agent 社交媒体模拟器,在 X 与 Reddit 上模拟最多 100 万个 agent,复现信息传播、群体极化与从众效应,并发现规模越大群体动态越丰富、意见越多样有用。
- [[2024-lmagent-multimodal-agents-society]]:基于多模态 LLM 的万级规模 agents 社会,在电商场景模拟多用户的购物、社交、直播行为,复现真实 co-purchase 模式与从众等 emergent behavior。
- [[2024-llm-powered-user-simulator-for-recommender-system]]:用 LLM 离线蒸馏用户偏好关键词与情感,在线用逻辑+统计集成模型显式推断 like/dislike,构建可解释、低幻觉、低成本的推荐系统用户模拟器。
- [[2025-multiagentbench]]:MultiAgentBench 与 MARBLE 框架:在六个交互式场景中评测 LLM 多智能体的协作与竞争,衡量任务完成度与协调质量,gpt-4o-mini 平均任务分最高、graph 协议在研究场景最优、认知规划使里程碑达成率提升约 3%。
- [[2025-simuser-llm-user-simulation-recsys]]:基于 LLM 的 agent 框架,用从历史数据推断的 persona、记忆、感知与决策模块构建可信合成用户来低成本评估推荐系统。
- [[2026-thinkrec-thinking-based-recommendation]]:ThinkRec 通过思考激活(推理数据合成+联合训练)与实例级 LoRA 专家融合,把 LLM 推荐从 System 1 直觉匹配推进到 System 2 推理,在 ML1M/Yelp/Book 上 AUC 平均超 SOTA 7.96%。
- [[2025-mmoagent-economic-simulation-mmo]]:提出 MMOAgent，一个基于 LLM 的 Generative Agent-Based Modeling 框架，用具备 profile/感知/推理/记忆/行动的 LLM 智能体模拟 MMO 游戏经济，涌现出角色分化与符合供需规律的价格波动。
- [[2025-agentsnet-multi-agent-reasoning]]:AGENTSNET 是一个可任意扩展的多 agent LLM 基准,借鉴分布式计算的五个经典问题(coloring、vertex cover、matching、leader election、consensus)来衡量 agent 网络在给定通信拓扑下的自组织、去中心化通信与协作推理能力,实验最多探测 100 个 agent。

## 相关

- [[zero-shot-cot]]
- [[few-shot-prompting]]
- [[in-context-learning]]
- [[tree-of-thoughts]]
- [[self-consistency]]
- [[reasoning]]
- [[plan-and-solve-prompting]]
- [[self-refine]]
- [[reflexion]]
- [[emergent-abilities]]
- [[llm-agents]]
