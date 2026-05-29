---
type: source
subtype: paper
tags: [llm-agent, agent-behavior, machine-behavior, multi-agent-systems, human-agent-interaction, responsible-ai, survey]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2506.06366
raw: raw/2506.06366.pdf
authors: Lin Chen, Yunke Zhang, Jie Feng, Haoye Chai, Honglin Zhang, Bingbing Fan, Yibo Ma, Shiyuan Zhang, Nian Li, Tianhui Liu, Nicholas Sukiennik, Keyu Zhao, Yu Li, Ziyi Liu, Fengli Xu, Yong Li
year: 2025
---

《AI Agent Behavioral Science》是一篇立场/综述论文,提出把 AI agent 当作"行为实体"来系统研究的新范式——AI Agent Behavioral Science,强调通过系统观察、干预设计与理论解释来理解 agent 如何在情境中行动、适应与互动,而不只是分析模型内部机制。

## 问题

理解 AI 的传统路径是"模型中心"(model-centric)的:研究架构、权重、attention 模式、训练目标,假设行为可以完全从模型内部确定和解释。但作者指出,随着模型日益复杂,定位"哪个神经元/组件触发了某种行为"越来越难;而在社会嵌入、开放式的环境中,行为不只由内部计算决定,还由交互历史、社会情境与反馈回路塑造。诸如谈判、协调、欺骗等复杂行为很少单独从模型本身涌现,而是当模型被嵌入带有 memory、planning、tool use、action 模块的 agentic 系统并进行情境化交互时才出现。作者用"模型之于行为,如同大脑之于行动"来比喻:模型是使能基底,但不决定行为。因此需要一种新的科学视角,把 AI agent 当作可经验观察、可系统理解的行为主体。

## 方法

论文不提出单一模型,而是构建一个研究范式与综述框架,系统梳理三类场景下的 agent 行为,并提出行为塑造与 responsible AI 的统一视角:

- **范式定位**:AI Agent Behavioral Science 借鉴人类与动物行为研究,强调系统观察、假设驱动的干预设计、理论指导的解释。论文用一张表对比"模型中心视角"与"行为视角"(分析焦点、方法工具、科学目标、本体论假设等)。该工作建立在 [[machine-behavior]] 等基础工作之上。
- **个体 agent 行为(Section 2)**:借鉴社会认知理论(Social Cognitive Theory, SCT),从三个维度组织——内在属性(emotions/cognition、economic rationality、bias)、环境约束(cultural、institutional、其他规范规则)、行为反馈(self-interaction 如 [[alphago]] 自博弈、与其他 agent 交互、与人类交互)。涉及 [[theory-of-mind]]、CogBench 等评测。
- **多 agent 行为(Section 3)**:按目标关系分为合作动态(agreement-/structure-/norm-driven)、竞争动态(博弈论场景、社会沟通游戏如 Werewolf/Hoodwinked/剧本杀、模拟真实冲突)、开放式交互动态(社会结构涌现如 [[generative-agents]]、集体认知涌现、宏观经济现象如 EconAgent 复现 Phillips Curve 与 Okun's Law)。
- **人-agent 交互行为(Section 4)**:把 agent 在人类交互中扮演的角色分为合作语境(companion、catalyst、clarifier)与对抗语境(contender、manipulator),讨论自我披露、Mutual Theory of Mind、说服、操纵、信息环境影响等行为。
- **行为适应与优化(Section 5)**:用 Fogg Behavior Model(ability、motivation、trigger 三要素必须同时具备)统一解读现有方法——ability 对应 pretraining(含 [[transformer]]、[[vit]]、[[clip]]、[[decision-transformer]]、Gato、RT-1 等行为骨干);motivation 对应 [[reinforcement-learning]](带 reward model 的 [[rlhf]]、EUREKA、[[rejection-sampling-fine-tuning]] 类 ReFT、[[process-reward-model]] 与 outcome reward、GRPO、PAVs;无 reward model 的 [[direct-preference-optimization]]、TDPO、ODPO、MCTS 增强偏好学习)与 fine-tuning(persona-/role-/context-conditioned);trigger 对应 [[prompt-engineering]](instructional/demonstration/goal-setting/context prompt)。
- **Responsible AI(Section 6)**:把 fairness、safety、interpretability、accountability、privacy 五大原则从静态属性重构为可测量、可优化的行为属性,逐项给出 measurement 与 optimization 方法(如 causal fairness prompting、overconfidence detection、hybrid moral reasoning、LLM deception benchmarking、membership inference attack 等)。
- **开放问题(Section 7)**:提出 prompt design、复杂环境鲁棒性、长期适应与持续学习等六个未来方向。

## 结果

作为综述/立场论文,贡献在于框架与系统化梳理而非单一数字结果。文中汇总的代表性发现与数字包括:

- **个体行为**:GPT-4 在概念典型性判断上与人类高度一致;CogBench 用 7 个心理学实验、10 个认知指标测试了 35 个 LLM,发现参数规模与 reinforcement fine-tuning 显著提升认知能力;经济理性方面,参数少于 40B 的 LLM 多为随机作答,GPT-4 最理性但在博弈论场景仍不令人满意;ChatGPT 被视为 human-like bias 出现的转折点。
- **多 agent**:LLM 在多轮博弈中普遍采用 tit-for-tat;Llama2 与 GPT-3.5 比人类更宽容,GPT-4 报复性更强;[[generative-agents]] 中 25 个 agent 涌现出角色分工、日常作息与集体筹办 Valentine's Day party;EconAgent 复现 Phillips Curve、Okun's Law 及 COVID-19 期间失业率上升。
- **人-agent**:在二手车谈判实验中,约 60% 的交互成功达成交易,LLM 展现锚定、小幅让步等经典谈判策略,但也易被人类"hacking";少量策略性放置的 AI agent 可在网络中操纵投票结果(gerrymandering)。
- **行为适应**:综述引用 PAVs(Process Advantage Verifiers)等结果——process-based reward 相比 outcome-based 实现约 8% 更高准确率、5–6× 的 compute/sample 效率提升;GRPO 显示对中间推理步骤显式打分在复杂数学推理上优于 outcome-only 方法。
- 论文用 Table 1–6 系统汇总各类 emergent behavior、适应方法与 responsible AI 方法,并配 Figure 1–6 给出技术发展时间线、SCT 框架、多 agent 三类动态、Fogg Behavior Model 适应框架等。

## 在本 wiki 中的位置

本文是一篇"行为科学视角"的 [[llm-agent]] 综述,可作为连接 [[multi-agent-systems]]、[[human-in-the-loop]] 人机交互、[[generative-agents]]/[[social-simulation]] 与 [[ai-safety]]/[[ai-alignment]] 的总览性入口。它把本 wiki 中分散的训练/对齐方法——[[rlhf]]、[[direct-preference-optimization]]、[[process-reward-model]]、[[prompt-engineering]]——纳入 Fogg Behavior Model(ability/motivation/trigger)的统一叙事,并把 fairness、safety、interpretability 等 responsible AI 议题重述为可测量的行为属性。与单一方法论文(如 [[react-reasoning-and-acting]]、[[reflexion]]、[[autogen]])相比,本文提供的是范式与分类骨架,适合作为 agent 行为相关条目的导航与背景参考。
