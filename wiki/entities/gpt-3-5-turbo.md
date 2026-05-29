---
type: entity
subtype: model
tags: [llm, openai, chat-model, instruction-tuned]
created: 2026-05-29
updated: 2026-05-29
sources: 20
---

# GPT-3.5-turbo

GPT-3.5-turbo 是 OpenAI 推出的指令微调对话大语言模型,因低成本、低延迟与较强的通用能力,被大量研究用作智能体、推理与代码任务的基座模型。

## 在本 wiki 中的出现

- [[2023-camel-communicative-agents]]:作为 CAMEL 中 AI User 与 AI Assistant 两个角色扮演智能体的基座 LLM,通过 inception prompting 在最少人工干预下自主协作完成任务并生成大规模指令/对话数据。
- [[2023-self-debugging]]:作为 SELF-DEBUGGING 框架中的待评估 LLM 之一,在 few-shot prompting 下执行并解释自己生成的代码,实现无人工反馈的自我调试。
- [[2023-critic]]:作为 CRITIC 框架使用的 LLM,通过与搜索引擎、代码解释器、PERSPECTIVE API 等外部工具交互来自我验证并迭代修正输出。
- [[2023-multi-agent-debate]]:作为 Multi-Agent Debate(MAD)框架中参与辩论的 LLM 智能体与裁判的基座模型,用于缓解自我反思的 Degeneration-of-Thought 问题。
- [[2023-agentbench]]:作为 AgentBench 在 8 个交互环境中评测的 29 个模型之一,用于衡量其 LLM-as-Agent 能力,并揭示商业与开源模型间的差距。
- [[2023-recmind-llm-agent-for-recommendation]]:RecMind 是一个由 LLM 驱动的自主推荐 agent,通过规划、记忆与外部工具实现 zero-shot 个性化推荐,并提出 Self-Inspiring 规划算法保留所有已探索状态以增强规划能力。
- [[2023-llms-cannot-self-correct-reasoning-yet]]:本文证明在无外部反馈的"内在自我纠正"设定下,LLM 无法纠正自身推理错误,性能反而往往下降。
- [[2023-memgpt-llms-as-operating-systems]]:MemGPT 借鉴操作系统的分层内存与虚拟内存分页,用函数调用让 LLM 自主管理上下文内外的多级存储,在固定上下文模型上制造"无限上下文"的假象。
- [[2024-generative-agents-in-recommendation]]:Agent4Rec 用 1000 个 LLM 驱动的生成式 agent(含 profile/memory/action 模块)构建电影推荐用户模拟器,探究其能否忠实模拟真实用户行为并复现 filter bubble 与 popularity bias。
- [[2023-agenttuning]]:通过构建跨任务 agent 交互轨迹数据集 AgentInstruct 并与通用指令混合微调,使开源 Llama 2 获得可泛化的 agent 能力且不损害通用能力。
- [[2024-metacognition-generative-agents]]:为 generative agents 引入元认知(metacognition)模块,让 agent 观察并反思自身思考与行动以动态调整策略,在僵尸末日等目标导向场景中显著提升表现。
- [[2024-sotopia-pi-social-agents]]:通过 behavior cloning 与 self-reinforcement 在 GPT-4 评分过滤的社交对话数据上训练,使 7B LLM 的社交目标完成能力逼近 GPT-4,同时提升安全并保持 MMLU。
- [[2024-autoguide-context-aware-guidelines]]:AUTOGUIDE 从离线经验中自动生成并按当前情境检索上下文感知指引,显著提升 LLM 智能体在 ALFWorld、WebShop、WebArena 等序列决策与网页导航任务上的成功率。
- [[2024-self-reflection-llm-agents]]:在 9 个 LLM、1000 道多选题上对比 8 种自我反思类型,证明所有 self-reflection 都能显著提升 LLM agent 的解题准确率(p<0.001)。
- [[2024-rethinkmcts]]:一个面向代码生成的思路搜索框架,用 MCTS 探索写代码的推理过程,并通过 rethink 机制利用块级代码执行反馈直接精炼搜索树中的错误思路。
- [[2024-multi-agent-tot-validator]]:将 Tree-of-Thoughts 与多智能体推理结合,新增 Thought Validator agent 过滤无效推理分支后再共识投票,在 GSM8K 上比标准 ToT 平均提升 5.6 个百分点。
- [[2024-aipatient-simulated-patient-llm-agents]]:AIPatient,一个由六个任务专用 LLM 智能体 + Reasoning RAG + 基于 MIMIC-III 真实病历构建的知识图谱驱动的模拟病人系统,EHR-QA 准确率达 94.15%、NER 知识库 F1=0.89,用户研究中匹配或优于真人模拟病人。
- [[2025-multiagentbench]]:MultiAgentBench 与 MARBLE 框架,在六个交互式场景中评测 LLM 多智能体的协作与竞争,衡量任务完成度与协调质量,gpt-4o-mini 平均任务分最高、graph 协议在研究场景最优、认知规划使里程碑达成率提升约 3%。
- [[2025-mmoagent-economic-simulation-mmo]]:提出 MMOAgent,一个基于 LLM 的 Generative Agent-Based Modeling 框架,用具备 profile/感知/推理/记忆/行动的 LLM 智能体模拟 MMO 游戏经济,涌现出角色分化与符合供需规律的价格波动。
- [[2025-multi-agent-reflexion-mar]]:把 Reflexion 的单 Agent 自我批评换成多 persona 辩论加 judge 合成反思,在 HotPotQA(EM 44→47)与 HumanEval(pass@1 76.4→82.6)上超过单 Agent Reflexion。

## 相关

- [[gpt-4]]
- [[openai]]
- [[large-language-model]]
- [[llm-agents|llm-agent]]
- [[instruction-tuning]]
- [[in-context-learning]]
- [[few-shot-prompting]]
- [[tool-use]]
