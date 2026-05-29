---
type: source
subtype: paper
tags: [llm-multi-agent, training, direct-preference-optimization, monte-carlo-tree-search, communication-efficiency, test-time-scaling]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2410.08115
raw: raw/2410.08115.pdf
authors: [Weize Chen, Jiarui Yuan, Chen Qian, Cheng Yang, Zhiyuan Liu, Maosong Sun]
year: 2024
---

# OPTIMA: Optimizing Effectiveness and Efficiency for LLM-Based Multi-Agent System

OPTIMA 是一个面向 LLM 多智能体系统(MAS)的训练框架,通过"生成-排序-选择-训练"的迭代范式,同时优化智能体间的通信效率与任务有效性,在重信息交换任务上实现最高 2.8x 的性能提升且只用不到 10% 的 token。

## 问题

基于 [[large-language-models]] 的 [[llm-multi-agent]] 系统(MAS)在协作问题求解上潜力巨大,但面临三个关键挑战:

1. **通信效率低**:智能体之间的交流往往冗长,导致 token 消耗大、推理时间长、计算成本高。这一问题被 LLM 因对齐训练而产生的 length bias(倾向生成更长回复)进一步放大。
2. **可扩展性差**:系统规模增长时,协调与通信成本急剧上升。
3. **缺乏有效的参数更新优化方法**:已有工作多依赖简单的 agent profile 演化或 memory 更新(如 [[chatdev]]、[[metagpt]]、[[agentcf]]),而单智能体训练与多智能体强化学习虽各有研究,却缺少专门为"把 LLM-based MAS 当作统一系统来训练"的参数更新方法。

核心研究问题:能否设计一个训练框架,同时提升 LLM-based MAS 的通信效率和任务有效性?

## 方法

OPTIMA 基于一个迭代的 **generate, rank, select, and train(生成、排序、选择、训练)** 范式,迭代式地令 $\mathcal{M}_{t+1} = f(\mathcal{M}_t, \mathcal{D})$:

- **奖励函数(核心)**:对每条对话轨迹 $\tau$ 定义
  $$R(\tau) = R_{\text{task}}(\tau) - \lambda_{\text{token}} R_{\text{token}}(\tau) + \lambda_{\text{loss}} \frac{1}{R_{\text{loss}}(\tau)}$$
  其中 $R_{\text{task}}$ 是任务表现,$R_{\text{token}}$ 是归一化 token 数(惩罚冗长),$R_{\text{loss}}$ 基于 base model 的语言建模损失(用作可读性/自然度的正则,避免退化成不可读的"智能体黑话")。该奖励同时平衡任务有效性、token 效率与对话质量。
- **初始化**:借鉴 AutoForm 的观察,用一个 format specification prompt pool(JSON、列表、表格、缩写记号等 20 多种格式)给 base model 注入多样的通信格式,缓解高温采样下轨迹风格同质化的问题;再用 SFT 得到起点模型 $\mathcal{M}_0$,使其无需显式格式提示即可产生多样通信模式。
- **三种实例化**:
  - **iSFT(Iterative SFT)**:每轮采样 $N$ 条轨迹,按奖励选出最优且超过阈值的 top 70% 做 SFT。
  - **iDPO(Iterative DPO)**:用 [[direct-preference-optimization]] 优化比较偏好。为在多智能体场景生成高质量配对数据,集成了受 [[monte-carlo-tree-search]] 启发的技术——把多智能体对话视为树,节点为对话轮、边为续写,通过 Expansion / Simulation / Backpropagation 探索多样交互轨迹,再按"共同祖先 + 奖励差超过阈值"构造 chosen/rejected 配对(使用 RPO 损失,即 DPO+NLL)。
  - **iSFT-DPO(Hybrid)**:交替进行一轮 iSFT 与一轮 iDPO,兼顾 SFT 的直接性与 DPO 的细粒度偏好学习。
- **训练设置**:base model 为 [[llama-3]] 8B 与 [[llama-2]] 系列对应的 Llama 3.2 3B,聚焦无外部工具的两智能体场景,8 卡 A100 上多数任务 12 小时内完成(MATH 约 24 小时)。

## 结果

评测覆盖两类任务:信息交换(IE)与辩论/推理(debate)。

- **信息交换任务**:在 2WMHQA 上,iSFT-DPO 相比 [[self-consistency]](SC, n=8)将 F1 提升 **38.3%(即 2.8x)**,且只用 [[multi-agent-debate]](MAD)约 **10%** 的 token。在 HotpotQA、TriviaQA、CBT 上各 OPTIMA 变体也在大幅降低 token 的同时保持高性能。
- **辩论/推理任务**:在 ARC-C、MMLU 上性能与效率均更优;在 MATH、GSM8k 上性能与 SC 相当或略低,但 token 效率显著更高。
- **泛化/迁移**:HotpotQA→2WMHQA 迁移时,iSFT 的 F1 是 MAD 两倍以上而只用 14.6% 的 token;MATH→GSM8k 迁移的 iDPO 甚至能匹敌直接在 GSM8k 上训练的模型。
- **推理时扩展(inference scaling)**:OPTIMA 的 token 节省让相同算力下能采样更多样本,改善 inference-time scaling law。GSM8k 上经训练的 iDPO 以 **88.5% 更少的 token** 匹配 CoT-SC 的表现,即把扩展曲线"左移"。
- **消融**:去掉 token 正则会使生成显著变长;去掉 LM loss 会让消息过度精简、信息不足并易 [[hallucination]],验证三项奖励组件缺一不可。
- **三智能体**:在三智能体场景下仍能同时提升效果与效率(IE 任务因信息更分散整体略逊于两智能体)。

## 在本 wiki 中的位置

本文属于 [[llm-multi-agent]] 训练方向,与本 wiki 中关注多智能体协作的 [[chatdev]]、[[metagpt]]、[[autogen]]、[[multi-agent-debate]] 等资源互补——它们多聚焦框架或 memory/profile 演化,而 OPTIMA 提供了对 MAS 进行端到端参数训练的方法。其奖励设计与数据生成借鉴了 [[direct-preference-optimization]]、[[monte-carlo-tree-search]] 与 [[self-improvement]] 类工作(如 [[star-self-taught-reasoner]]、ReST),并把 [[test-time-scaling]] / inference scaling 作为衡量 MAS 的关键维度,可与本 wiki 中 [[chain-of-thought]]、[[self-consistency]] 等推理增强方法对照阅读。
