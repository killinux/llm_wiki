---
type: source
subtype: paper
tags: [llm-multi-agent, benchmark, multi-agent-collaboration, agent-orchestration, evaluation, llm-agents]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2503.01935
raw: raw/2503.01935.pdf
authors: [Kunlun Zhu, Hongyi Du, Zhaochen Hong, Xiaocheng Yang, Shuyi Guo, Zhe Wang, Zhenhailong Wang, Cheng Qian, Xiangru Tang, Heng Ji, Jiaxuan You]
year: 2025
---

# MultiAgentBench: Evaluating the Collaboration and Competition of LLM agents

MultiAgentBench 是一个用于评测 LLM-based 多智能体系统的 benchmark,它在六个交互式场景中同时衡量任务完成度与协作/竞争质量,并配套提出 MARBLE 框架,支持 star/tree/graph/chain 多种协调拓扑与多种规划策略。

## 问题

[[large-language-models]] 已展现出作为自主 [[autonomous-agents]] 的强大能力,但现有 benchmark 要么聚焦单智能体任务,要么局限于狭窄领域,无法刻画多智能体协调(coordination)与竞争(competition)的动态特征。传统单智能体 benchmark(如 [[agentbench]]、VisualAgentBench、GAIA、ToolBench、[[humaneval]])主要关注孤立的推理与生成,忽视了多智能体交互中固有的动态性。论文要解决的核心问题是:如何系统性地评测 [[llm-multi-agent]] 系统的协作与竞争能力,而不仅仅是最终任务成功率。

## 方法

论文提出 **MultiAgentBench** 评测基准与 **MARBLE**(Multi-agent cooRdination Backbone with LLM Engine)框架。

- **框架模块**:核心是 Coordination Engine(协调引擎),负责初始化与同步各模块,区分 planner(规划者)与 actor(执行者)两类角色。
  - **Agent Graph 模块**:把配置数据转为结构化图 G=(A,E),边为三元组 (ai, r, aj),关系 r 含 collaborates / supervises / negotiates,确保通信仅发生在显式定义关系的智能体之间。
  - **Cognitive Module(认知模块)**:维护并更新每个 agent 的 persona、智能体间关系与推理策略(如 [[chain-of-thought]]、[[react-reasoning-and-acting]]),融合 theory-of-mind 与 [[social-intelligence]] 元素。
  - 记忆机制包含 short-term memory、shared memory 与带 [[retrieval-augmented-generation]] 的 long-term memory。
- **四种协调协议(coordination protocols)**(参考 [[chatdev]] 团队 Qian et al. 2025):集中式的 star、tree;去中心化的 graph-mesh、chain。
- **四种规划策略**:vanilla prompting、CoT、group discussion(群组讨论)、cognitive self-evolving planning(认知自演化规划,思路类似 [[reflexion]],生成预期结果存入记忆并与实际表现对比迭代)。
- **Benchmark 设计**:六个场景,分为目标一致(mutual goal)的任务型——research(沿用 ResearchTown 设定)、Minecraft 建造、database error analysis(恰好 5 个 agent)、coding;以及目标冲突(conflicting goal)的社会模拟型——Werewolf(狼人杀)、Bargaining(讨价还价)。任务型每类构造 100 个测试用例。
- **评测指标**:任务完成维度用基于 milestone 的 KPI(由 LLM 检测器动态判定里程碑达成,KPI_overall = (1/NM)·Σ nj)与 task-based score;协调维度用 Communication Score 与 Planning Score(各 5 分制),平均得到 Coordination Score (CS)。

## 结果

主实验评测 5 个模型:Meta-Llama-3.1-8B、Meta-Llama-3.1-70B、Meta-Llama-3.3-70B、[[gpt-3-5-turbo]]、[[gpt-4o-mini]](开源模型经 togetherai 服务,温度 0.7,top_p 1.0,max_token 1024,主实验用 graph-mesh 协议)。

- **gpt-4o-mini 任务表现最佳**:Research 场景 Task Score (TS) 达 **84.13%**,优于 Meta-Llama-3.1-8B(80.87%)与 Meta-Llama-3.1-70B(80.80%);Coding 场景 TS 为 65.10,也居首。
- **协调分(CS)作用复杂**:Minecraft 场景中 Meta-Llama-3.1-70B 的 CS 高达 75.00 但 TS 极低仅 0.21,说明协调不能弥补任务执行能力的固有缺陷;模型本身能力仍是任务完成的主导因素。
- **协议对比(Research 场景)**:graph 协议在任务表现、规划效率、token 用量上最优;star 与 graph 任务分相近;tree 协议最差(token 消耗高、任务与协调分最低)。
- **规划策略对比(Research 场景)**:Cognitive Evolve Planning 协调分最高(CS 59.00,KPI 49.87,TS 76.67),TS 与最佳的 COT 相当;group discussion 在所有指标上最差(论文推测过大的规划群组类似大组织反而低效)。整体上 cognitive planning 使 milestone 达成率提升约 **3%**。
- **消融**:迭代数从 1 增到 7 时任务/协调分上升,10 次时骤降,20 次时任务分有所恢复但协调分基本不变;agent 数从 1 增到 7 时整体 KPI 下降,但协调分在 1→3 时显著提升。
- **涌现行为**:观察到 "aha-moments",包括 Strategic Information Sharing(策略性信息共享)、Trust-Polarized Collaboration(信任极化协作)、Role-Driven Strategy Iteration(角色驱动的策略迭代)。

## 在本 wiki 中的位置

本文是 [[llm-multi-agent]] 与 [[multi-agent-collaboration]] 方向的评测性工作,与 [[autogen]]、[[chatdev]]、[[metagpt]]、CAMEL([[camel-communicative-agents]])等多智能体框架以及 [[agentbench]] 等单智能体 benchmark 形成对照。其 [[agent-orchestration]] 协议(star/tree/graph/chain)与 [[reflexion]] 式认知自演化规划,可与本 wiki 中 [[role-playing-agent]]、[[generative-agents]]、[[social-simulation]] 等条目互相参照。
