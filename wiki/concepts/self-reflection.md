---
type: concept
subtype: method
tags: [self-reflection, reasoning, llm-agent, self-correction]
created: 2026-05-29
updated: 2026-05-29
sources: 15
---

# Self-Reflection

Self-Reflection 是指让单个 LLM 通过自我审视、自我评价并迭代修正其先前输出的一类方法,以期在不依赖外部反馈的情况下提升推理质量。

## 在本 wiki 中的出现

- [[2023-multi-agent-debate]]:该工作针对 Self-Reflection 提出的 Multi-Agent Debate(MAD)框架。论文指出,单一 LLM 进行 Self-Reflection 时容易陷入 Degeneration-of-Thought(DoT)问题——一旦模型对某个(可能错误的)答案建立起自信,后续反思难以再产生新的、发散性的想法。MAD 通过引入多个 LLM 智能体彼此"针锋相对"地辩论,并由一个裁判(judge)进行仲裁,从而缓解 Self-Reflection 的 DoT 问题、激发发散性思维。在此语境中,Self-Reflection 既是被对比的基线方法,也是 MAD 所要改进的对象。
- [[2023-llms-cannot-self-correct-reasoning-yet]]:本文证明在无外部反馈的"内在自我纠正"设定下,LLM 无法纠正自身推理错误,性能反而往往下降。
- [[2023-agentcf-collaborative-learning-agents-recsys]]:把推荐系统中的用户和物品都建模为 LLM agent,通过自主交互与协同反思实现无梯度的协同过滤式优化。
- [[2024-generative-agents-in-recommendation]]:Agent4Rec 用 1000 个 LLM 驱动的生成式 agent(含 profile/memory/action 模块)构建电影推荐用户模拟器,探究其能否忠实模拟真实用户行为并复现 filter bubble 与 popularity bias。
- [[2023-self-rag]]:Self-RAG 训练单个 LLM 用 reflection token 实现按需检索与自我反思批判,在推理时可控解码以提升生成质量、事实性与引用准确率。
- [[2024-metacognition-generative-agents]]:为 generative agents 引入元认知(metacognition)模块,让 agent 观察并反思自身思考与行动以动态调整策略,在僵尸末日等目标导向场景中显著提升表现。
- [[2024-macrec-multi-agent-recommendation]]:清华提出的多 agent 协作推荐框架(SIGIR'24 demo),用 Manager、Analyst、Reflector、Searcher、Task Interpreter 等角色各异的 LLM agent 直接协作完成评分预测、序列推荐、解释生成与对话推荐。
- [[2024-autoguide-context-aware-guidelines]]:AUTOGUIDE 从离线经验中自动生成并按当前情境检索上下文感知指引,显著提升 LLM 智能体在 ALFWorld、WebShop、WebArena 等序列决策与网页导航任务上的成功率。
- [[2024-self-reflection-llm-agents]]:在 9 个 LLM、1000 道多选题上对比 8 种自我反思类型,证明所有 self-reflection 都能显著提升 LLM agent 的解题准确率(p<0.001)。
- [[2024-when-can-llms-correct-mistakes]]:批判性综述:细分自我纠错的三类研究问题并提出实验检查清单,论证 LLM 仅凭 prompting 在一般任务上无法可靠自我纠错,瓶颈在于反馈生成,而外部工具/大规模 fine-tuning 可使其奏效。
- [[2024-llm4rerank-auto-reranking-recommendation]]:把推荐 reranking 的 accuracy/diversity/fairness 等目标抽象为全连接图中的 node,让 LLM 以 Chain-of-Thought 多跳方式按用户给定的 "Goal" 自动综合多目标重排候选列表。
- [[2024-sage-self-evolving-agents]]:由 User/Assistant/Checker 三 agent 组成、结合迭代反馈、反思与基于 Ebbinghaus 遗忘曲线的记忆优化的自进化 LLM agent 框架,对小模型提升尤为显著。
- [[2024-positive-experience-reflection]]:提出 Sweet&Sour,让 LLM agent 在交互式文本环境中不仅从失败、也从成功经验做反思,并配合双缓冲 managed memory,缓解 self-reflection 在初始成功与小模型上失效的问题;ScienceWorld 上 GPT-4o 平均 54.6、Llama 8B 32.5 均超 Reflexion。
- [[2025-llm-agents-for-recommender-systems-survey]]:系统综述 LLM 驱动 agent 在推荐系统中的应用,提出"面向推荐/交互/模拟"三范式,并用 Profile-Memory-Planning-Action 四模块统一架构对比 23 个方法、汇总数据集与评测。
- [[2026-agentorchestra-tea-protocol]]:提出 TEA 协议将工具/环境/智能体建模为带生命周期与版本的一等资源,并构建分层多智能体框架 AgentOrchestra,在 GAIA Test 上达到 89.04% 平均准确率。

## 相关

- [[2023-multi-agent-debate]]
- [[multi-agent-debate]]
- [[degeneration-of-thought]]
- [[self-correction]]
- [[chain-of-thought]]
- [[llm-agent]]
