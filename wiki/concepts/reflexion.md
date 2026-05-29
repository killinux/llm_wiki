---
type: concept
subtype: method
tags: [agent, self-reflection, self-improvement, llm, in-context-learning, verbal-feedback]
created: 2026-05-29
updated: 2026-05-29
sources: 20
---

# Reflexion

Reflexion 是一种通过语言化(verbal)的自我反思反馈来强化 LLM 智能体的方法:它不更新模型权重,而是让智能体把失败的试验转化为自然语言反思并存入记忆,用于在后续尝试中迭代改进决策。

## 在本 wiki 中的出现

- [[2023-reflexion]]:Reflexion 的提出者。用语言化的自我反思反馈而非梯度更新来强化 LLM 智能体,使其从失败中迭代改进。
- [[2023-self-refine]]:同源的测试时自我改进思路。用同一个 LLM 在测试时迭代"自我反馈→自我修正",无需训练即在 7 个任务上平均提升约 20%。
- [[2023-self-debugging]]:Reflexion 思想在代码场景的延伸。提出 SELF-DEBUGGING,通过 few-shot prompting 让 LLM 执行并解释自己生成的代码,实现无人工反馈的自我调试。
- [[2023-critic]]:对自我反馈来源的拓展与对照。CRITIC 让 LLM 通过与搜索引擎、代码解释器、PERSPECTIVE API 等外部工具交互来自我验证并迭代修正输出,证明外部反馈对自我改进至关重要,与 Reflexion 依赖语言化内省反馈的方式形成互补。
- [[2023-voyager]]:把自我验证用于具身终身学习。首个由 GPT-4 驱动、在 Minecraft 中通过自动课程、可执行代码技能库与自我验证实现终身学习的具身智能体,其自我验证机制与 Reflexion 的迭代反思相呼应。
- [[2023-metagpt]]:多智能体框架中的相关实践。MetaGPT 把人类 SOP 编码进 prompt,用专业化角色与结构化输出构建 LLM 多智能体软件开发框架,在 HumanEval/MBPP 上达到 SoTA,其角色间反馈与校验可视为对自我反思机制的组织化扩展。
- [[2023-recmind-llm-agent-for-recommendation]]:RecMind 是一个由 LLM 驱动的自主推荐 agent,通过规划、记忆与外部工具实现 zero-shot 个性化推荐,并提出 Self-Inspiring 规划算法保留所有已探索状态以增强规划能力。
- [[2023-recommender-ai-agent-interec]]:提出 InteRecAgent,以 LLM 为大脑、传统推荐模型为工具,通过候选总线记忆、plan-first 执行与 actor-critic 反思构建交互式对话推荐 agent,并蒸馏出 7B 的 RecLlama。
- [[2023-llms-cannot-self-correct-reasoning-yet]]:本文证明在无外部反馈的"内在自我纠正"设定下,LLM 无法纠正自身推理错误,性能反而往往下降。
- [[2023-fireact-language-agent-fine-tuning]]:提出用多任务、多 prompting 方法(ReAct/CoT/Reflexion)生成的轨迹微调 backbone LM 来构建语言智能体,在性能、鲁棒性、泛化与成本上全面优于 few-shot prompting。
- [[2023-agentcf-collaborative-learning-agents-recsys]]:把推荐系统中的用户和物品都建模为 LLM agent,通过自主交互与协同反思实现无梯度的协同过滤式优化。
- [[2023-agenttuning]]:通过构建跨任务 agent 交互轨迹数据集 AgentInstruct 并与通用指令混合微调,使开源 Llama 2 获得可泛化的 agent 能力且不损害通用能力。
- [[2024-eureka-reward-design-via-coding-llms]]:Eureka 用编码 LLM(GPT-4)零样本生成可执行奖励函数代码,结合进化搜索与奖励反思迭代改进,在 29 个 RL 环境上达到人类专家级奖励设计并首次让模拟 Shadow Hand 学会转笔。
- [[2024-llm-learnable-planners-long-term-recommendation]]:提出 BiLLP 双层可学习 LLM 规划框架(Planner/Reflector 宏观 + Actor/Critic 微观),在稀疏推荐数据上以 LLM 规划能力做长期推荐,Len 与累积奖励超越从零训练的 RL 与现有 LLM agent 基线。
- [[2024-autoguide-context-aware-guidelines]]:AUTOGUIDE 从离线经验中自动生成并按当前情境检索上下文感知指引,显著提升 LLM 智能体在 ALFWorld、WebShop、WebArena 等序列决策与网页导航任务上的成功率。
- [[2024-self-reflection-llm-agents]]:在 9 个 LLM、1000 道多选题上对比 8 种自我反思类型,证明所有 self-reflection 都能显著提升 LLM agent 的解题准确率(p<0.001)。
- [[2024-when-can-llms-correct-mistakes]]:批判性综述:细分自我纠错的三类研究问题并提出实验检查清单,论证 LLM 仅凭 prompting 在一般任务上无法可靠自我纠错,瓶颈在于反馈生成,而外部工具/大规模 fine-tuning 可使其奏效。
- [[2024-tree-search-for-language-model-agents]]:为 LLM web agent 提出 inference-time best-first tree search,在真实 web 环境中显式做探索与多步规划,把 GPT-4o 在 VisualWebArena 上成功率相对提升 39.7% 至 SOTA 26.4%,并展示 test-time compute scaling 的收益。
- [[2024-recursive-introspection-rise]]:RISE 将单轮问题建模为多轮 MDP 并用 reward-weighted regression 迭代微调,让 7B 级 LLM 在无外部反馈下学会跨多轮递归反思并修正答案。
- [[2024-hiagent-hierarchical-working-memory]]:HiAgent 用 subgoal 作为 memory chunk 分层管理 LLM agent 的 working memory(汇总过去 observation、按需检索明细轨迹),在五个长程任务上成功率约翻倍(21→42)、context 减少 35%。

## 相关

- [[self-critique]]
- [[self-improvement]]
- [[react]]
- [[chain-of-thought]]
- [[tree-of-thoughts]]
- [[language-agent-tree-search]]
- [[llm-agents]]
- [[in-context-learning]]
- [[memory-stream]]
- [[closed-loop-feedback]]
