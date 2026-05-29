---
type: entity
subtype: model
tags: [model, llm, open-source, meta]
created: 2026-05-29
updated: 2026-05-29
sources: 15
---

# LLaMA-2

LLaMA-2 是 Meta 发布的开源大语言模型系列,提供多种参数规模及对话微调版本,常被用作研究与应用的基础模型。

## 在本 wiki 中的出现

- [[2023-critic]]:作为被验证与改进的基础 LLM 之一。CRITIC 让 LLM 通过与搜索引擎、代码解释器、PERSPECTIVE API 等外部工具交互来自我验证并迭代修正输出,以此证明外部反馈对自我改进至关重要。
- [[2023-recmind-llm-agent-for-recommendation]]:RecMind 是一个由 LLM 驱动的自主推荐 agent,通过规划、记忆与外部工具实现 zero-shot 个性化推荐,并提出 Self-Inspiring 规划算法保留所有已探索状态以增强规划能力。
- [[2023-recommender-ai-agent-interec]]:提出 InteRecAgent,以 LLM 为大脑、传统推荐模型为工具,通过候选总线记忆、plan-first 执行与 actor-critic 反思构建交互式对话推荐 agent,并蒸馏出 7B 的 RecLlama。
- [[2023-chain-of-verification]]:Chain-of-Verification (CoVe) 让 LLM 先生成草稿,再独立回答自我规划的验证问题来核查事实,显著降低幻觉。
- [[2023-ts-llm-tree-search-decoding-training]]:TS-LLM:用学习的 value function 的 AlphaZero 风格树搜索,同时指导 LLM 的推理解码与迭代训练,适配任意规模 LLM 并将搜索深度扩展到 64。
- [[2023-fireact-language-agent-fine-tuning]]:提出用多任务、多 prompting 方法(ReAct/CoT/Reflexion)生成的轨迹微调 backbone LM 来构建语言智能体,在性能、鲁棒性、泛化与成本上全面优于 few-shot prompting。
- [[2023-timesfm-time-series-foundation-model]]:Google Research 的 TimesFM:一个在 O(100B) 时间点真实+合成时序上预训练的 decoder-only 时序预测基础模型,zero-shot 表现接近全监督 SOTA。
- [[2023-self-rag]]:Self-RAG 训练单个 LLM 用 reflection token 实现按需检索与自我反思批判,在推理时可控解码以提升生成质量、事实性与引用准确率。
- [[2023-sotopia-social-intelligence-evaluation]]:SOTOPIA 提出一个开放式社交互动模拟环境与多维评测框架 SOTOPIA-EVAL,交互式地评估 LLM 智能体在目标导向社交场景中的社会智能,发现 GPT-4 在最难子集上的目标完成率显著低于人类。
- [[2023-agenttuning]]:通过构建跨任务 agent 交互轨迹数据集 AgentInstruct 并与通用指令混合微调,使开源 Llama 2 获得可泛化的 agent 能力且不损害通用能力。
- [[2024-v-star-verifiers-for-self-taught-reasoners]]:V-STaR 在自我提升迭代中复用正确与错误的模型生成解,用 DPO 训练 verifier 在测试时对候选解排序,使 LLaMA2 在数学推理上绝对提升 6%~17%、代码生成 4%~12%。
- [[2024-llm-learnable-planners-long-term-recommendation]]:提出 BiLLP 双层可学习 LLM 规划框架(Planner/Reflector 宏观 + Actor/Critic 微观),在稀疏推荐数据上以 LLM 规划能力做长期推荐,Len 与累积奖励超越从零训练的 RL 与现有 LLM agent 基线。
- [[2024-self-reflection-llm-agents]]:在 9 个 LLM、1000 道多选题上对比 8 种自我反思类型,证明所有 self-reflection 都能显著提升 LLM agent 的解题准确率(p<0.001)。
- [[2024-llm4rerank-auto-reranking-recommendation]]:把推荐 reranking 的 accuracy/diversity/fairness 等目标抽象为全连接图中的 node,让 LLM 以 Chain-of-Thought 多跳方式按用户给定的 "Goal" 自动综合多目标重排候选列表。
- [[2024-recursive-introspection-rise]]:RISE 将单轮问题建模为多轮 MDP 并用 reward-weighted regression 迭代微调,让 7B 级 LLM 在无外部反馈下学会跨多轮递归反思并修正答案。

## 相关

- [[critic]]
- [[self-correction]]
- [[tool-use]]
- [[meta]]
- [[llama]]
- [[gpt-4]]
- [[recllama]]
- [[agenttuning]]
- [[self-rag]]
- [[v-star]]
- [[rise]]
