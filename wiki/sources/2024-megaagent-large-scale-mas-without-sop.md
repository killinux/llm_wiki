---
type: source
subtype: paper
tags:
  - llm-multi-agent
  - autonomous-agents
  - agent-orchestration
  - multi-agent-collaboration
  - llm-planning
created: 2026-05-29
updated: 2026-05-29
arxiv: 2408.09955
raw: raw/2408.09955.pdf
authors:
  - Qian Wang
  - Tianyu Wang
  - Zhenheng Tang
  - Qinbin Li
  - Nuo Chen
  - Jingsheng Liang
  - Bingsheng He
year: 2024
---

# MegaAgent: A Large-Scale Autonomous LLM-based Multi-Agent System Without Predefined SOPs

MegaAgent 借鉴操作系统(OS)的进程/线程模型,提出一个无需预定义 SOP、可根据任务复杂度自动生成数百个 agent 并行协作的大规模 LLM 多智能体系统。

## 问题

现有的 [[llm-multi-agent]] 系统(MAS)有两大局限:

1. **缺乏自适应的大规模协调**:当任务很大很复杂(例如社会模拟需要生成数百个 agent)时,现有系统无法做到自适应的任务协调,也未考虑大规模 agent 之间的协调。
2. **重度依赖人工配置**:像 [[metagpt]]、[[autogen]]、[[chatdev]] 这类系统大量依赖用户预定义的 agent 角色、Standard Operating Procedures(SOP)和静态通信图,灵活性差且部署大量 agent 时需要巨大的人力。

由此带来两个关键挑战:(1) 如何在大规模、并行、多轮通信下实现 agent 之间以及与外部文件系统的高效自适应通信;(2) 如何在不依赖预定义 SOP 的情况下保证每个 agent 准确完成任务——LLM agent 常产生 [[hallucination]] 或在单轮内无法正确完成任务,而在 MAS 中幻觉会传播并拖垮整个系统。

## 方法

MegaAgent 受操作系统启发(进程内多线程、进程间并行、生产者-消费者消息队列),用户只需向 Boss Agent 提供一个 meta-prompt,任务即自主完成。核心是两套层次化机制:

**(1) 层次化任务管理(Hierarchical Task Management)**
- **多级任务拆分**:Boss Agent 把主任务拆为子任务(类比进程),分派给带明确角色的 admin agent;admin agent 若觉得子任务太复杂可递归招募更多 agent 组成动态分组(类比线程),形成 Level 1/2/3 多级层次。
- **并行机制**:同一层级的 agent 分组可并行执行(例如一组生成经济政策、另一组生成卫生政策),把串行的 O(n) 通信成本降为层次化的 O(log n)。
- **两层协调**:组内聊天(Intra-group Chat)与组间聊天(Inter-group Chat,仅 admin agent 之间);普通(ordinary)agent 只在本组内通信以提升效率。
- **消息队列**:每个 agent 用生产者-消费者范式管理异步通信,有 Idle / Processing / Response 三种状态(Idle 不产生 token 成本),可批量合并消息以充分利用 LLM 吞吐。
- **文件管理**:外部 storage module 提供执行日志、记忆数据库、Python 执行器、checklist 等;用 **基于 Git 的版本控制**(commit hash + 全局互斥锁)防止并发写冲突;用 **向量数据库长期记忆**(chroma)缓解 token 长度限制导致的遗忘。

**(2) 层次化监控(Hierarchical Monitoring)**:为减少幻觉传播,分三级监控——Agent-Level(每个 agent 用 checklist 自查进度)、Group-Level(admin agent 审查组内输出)、System-Level(Boss Agent 审查所有组输出)。监控聚焦输出格式校验与结果校验,并处理 TODO 未完成、任务重复、安全对齐中断等失败场景(类似 [[self-refine]] / [[self-reflection]] 的自纠机制)。

实验主要用 GPT-4o / GPT-4o-mini API(NVIDIA A100-80G)。

## 结果

**标准 benchmark(GPT-4o,准确率 %)**:MegaAgent 在 [[mbpp]] 92.2、[[humaneval]] 93.3、[[math-benchmark]] 69.0、[[gsm8k]] 93.0,均优于 [[metagpt]](81.7 / 82.3)、CAMEL(78.1 / 57.9 / 22.3 / 45.6)、AgentVerse(82.4 / 89.0 / 54.5 / 81.2)、[[autogen]](85.3 / 85.9 / 69.5 / 87.8)。

**软件开发(五子棋 Gobang Game)**:MegaAgent 自主生成含 7 个 agent 的 SOP,在 **800 秒内** 唯一完整开发出带交互界面、可运行的五子棋游戏(Error-Free Execution / User Move / AI Move / Game Termination 四项全过,每 agent 114 秒)。AutoGen(2 agent)生成 `# To be continued..` 卡死、MetaGPT(6 agent)产出不可执行代码甚至误做成 tic-tac-toe、CAMEL 与 AgentVerse 均失败。成本仅 $6.90。消融:去掉层次→只达基本指标;去掉并行→执行时间从 800 秒升至 4505 秒(每 agent 114→643 秒);去掉监控→300 秒但无法满足关键指标。

**社会模拟(国家政策生成 National Policy Generation,GPT-4o-mini)**:MegaAgent 扩展到 **590 个 agent,在 2991 秒内** 生成完整的多领域政策,平均每 agent 仅 5 秒(最好的 baseline 为 40 秒/agent);baseline 通常只能协调少于 10 个 agent 且失败(AutoGen 1 agent 只出大纲、MetaGPT 6 agent 只出 Python 程序、CAMEL 出 plans、AgentVerse 无输出)。用 [[llm-as-judge]](Claude-3.5、GPT-4o-mini、GPT-4o、o1-mini、o1-preview 五模型)评估,平均 27.4/31 条政策被判为合理(judge 在 50 真实政策 + 50 非政策文本上识别准确率约 89%)。消融显示并行不仅有益而且对大规模任务"至关重要"。

**TravelPlanner**:在 sole-planning 模式(验证集 #180)上,MegaAgent 的 Delivery Rate 100、CS-Micro 81.88、Hard Constraint Micro 40.48,整体优于 Direct/CoT/ReAct/Reflexion 等 GPT-3.5/GPT-4 基线。

成本/token 分析揭示:任务求解阶段(Task-Solving)消耗绝大部分时间与 token,且输入 token 远多于输出 token(五子棋约 23:1、国家政策约 25:1),指出 agent 间对话效率是重要优化方向。

## 在本 wiki 中的位置

MegaAgent 属于 [[llm-multi-agent]] / [[multi-agent-collaboration]] 与 [[autonomous-agents]] 方向,与依赖人工 SOP 和静态角色的 [[metagpt]]、[[chatdev]]、[[autogen]] 形成对比——它强调 **去 SOP 化的自主性** 与 **数百 agent 的可扩展性**(O(log n) 层次化通信)。其设计借鉴操作系统(进程/线程/消息队列),与 [[agent-orchestration]]、[[agent-memory]]([[llm-long-term-memory]] 用向量数据库)、[[tool-use]](function call)、以及通过层次化监控做 [[self-correction]] 抑制 [[hallucination]] 等概念相关;评估用到 [[mbpp]]、[[humaneval]]、[[gsm8k]]、[[math-benchmark]] 等 benchmark 与 [[llm-as-judge]] 方法,社会模拟思路上与 [[generative-agents]] 的 Simulacra 一脉相承。
