---
type: concept
subtype: method
tags: [prompting, reasoning, in-context-learning, llm]
created: 2026-05-29
updated: 2026-05-29
sources: 26
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
