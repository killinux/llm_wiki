---
type: source
subtype: paper
tags: [survey, self-improvement, llm-agent, llm-multi-agent, lifelong-learning, evaluation, reinforcement-learning]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2507.21046
raw: raw/2507.21046.pdf
title: "A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence"
slug: 2025-survey-self-evolving-agents
authors: [Huan-ang Gao, Jiayi Geng, Wenyue Hua, Mengkang Hu, Xinzhe Juan, Hongzhang Liu, Shilong Liu, Jiahao Qiu, Xuan Qi, Qihan Ren, Yiran Wu, Hongru Wang, Han Xiao, Yuhang Zhou, Shaokun Zhang, Jiayi Zhang, Jinyu Xiang, Yixiong Fang, Qiwen Zhao, Dongrui Liu, Cheng Qian, Zhenhailong Wang, Minda Hu, Huazheng Wang, Qingyun Wu, Heng Ji, Mengdi Wang]
year: 2025
---

首个系统性聚焦"自进化智能体"(self-evolving agents)的综述,沿 **what / when / how / where** 四个维度建立统一框架,并讨论评测体系与通往 ASI 的路线图。

## 问题

[[large-language-models]] 能力强大,但本质上是**静态**的:部署后无法根据新任务、演化的知识领域或动态交互上下文调整自身参数。当 LLM 越来越多地部署到开放、交互式环境时,这种静态性成为关键瓶颈。论文提出一个范式转变——从"扩大静态模型规模"转向"开发能从数据、交互与经验中持续学习与适应的自进化智能体",并将其视为通往 Artificial Super Intelligence(ASI)的核心路径。

此前已有 [[autonomous-agents]] / [[llm-based-agents]] 的综述,但多把"智能体进化"当作通用智能体分类法下的子组件,缺乏把自进化作为**一等研究范式**的专门综述。本文要回答三个基础问题:智能体的**哪些部分**应该进化?进化**何时**发生?进化**如何**实现(以及在**哪里/什么领域**部署)?

论文给出自进化智能体的形式化定义:在 POMDP 环境 $E=(\mathcal{G},\mathcal{S},\mathcal{A},T,R,\Omega,O,\gamma)$ 中,(多)智能体系统 $\Pi=(\Gamma,\{\psi_i\},\{C_i\},\{\mathcal{W}_i\})$ 由架构 $\Gamma$、底层 LLM $\psi_i$、上下文 $C_i$(prompt + memory)、工具集 $\mathcal{W}_i$ 构成;自进化策略 $f(\Pi,\tau,r)=\Pi'$ 基于轨迹 $\tau$ 与反馈 $r$ 把系统更新到新状态,目标是最大化任务序列上的累计效用 $\max_f \sum_j U(\Pi_j,\mathcal{T}_j)$。操作性定义要求更新满足三条:经验依赖(experience-dependent)、持久且改变策略(persistent policy-changing)、具备自主探索/自发学习机制。论文用 proto-evolution(弱自进化,如迭代 bootstrapping)到 strong self-evolution(完全自主诊断与重构)的谱系来涵盖早期工作。

## 方法

综述沿四维度组织(配套 Figure 2 分类法、Figure 3 总览图、Figure 4 2022–2025 时间线):

**What to evolve(进化什么,Sec.3)** 识别智能体系统中四类"进化位点":
- **Model(模型)**:对底层 LLM 参数自进化,分 Policy(策略,如 [[star-self-taught-reasoner]] 类自训练、Self-Challenging Agent SCA、TextGrad)与 Experience(经验,通过环境交互生成数据,如 AgentGen、RAGEN、[[reflexion]]、AdaPlanner、[[self-refine]])。
- **Context(上下文)**:含 **Memory evolution**(记忆进化,如 SAGE 用 [[ebbinghaus-forgetting-curve]]、A-mem、Mem0 的 ADD/MERGE/DELETE、Memory-R1、[[expel]]、ReasoningBank、Agent Workflow Memory)与 **Prompt Optimization**(提示优化,如 APE、PromptAgent 用 [[monte-carlo-tree-search]]、PromptBreeder、SPO、Agentic Context Engineering)。
- **Tool(工具)**:工具的自主 Creation / Mastery / Selection(如 [[voyager]]、Alita、CREATOR、ToolGen)。
- **Architecture(架构)**:单智能体与多智能体结构进化(如 AFlow、ADAS、[[chatdev]] 类、Darwin Gödel Machine、MASS)。

**When to evolve(何时进化,Sec.4)** 按时间阶段与学习范式划分为 **intra-test-time self-evolution**(测试内,如 [[in-context-learning]]、[[reflexion]]、SFT、RL)与 **inter-test-time self-evolution**(测试间,如 SELF、STaR、Quiet-STaR、RAGEN、DigiRL)。

**How to evolve(如何进化,Sec.5)** 归纳三大方法族(配套 cross-cutting 维度 Table 4):
- **Reward-based**(基于奖励):Textual Feedback(文本反馈)、Internal Rewards(内部奖励,如 majority voting、自评判)、External Rewards(外部奖励,环境/工具/规则信号)、Implicit Rewards(隐式奖励,如 "Reward Is Enough"、Endogenous reward、PIT)。
- **Imitation & Demonstration**(模仿与示范):Self-Generated(自生成,如 STaR、Explore-to-Evolve)、Cross-Agent(跨智能体)、Hybrid(混合)。
- **Population-based & Evolutionary**(种群与进化):单智能体(Darwin Gödel Machine、GENOME、AlphaEvolve、CodeEvolve、self-play 如 [[direct-preference-optimization]] 之外的 SPIN、Absolute Zero、R-Zero)与多智能体(EvoMAC、Puppeteer、MDTeamGPT、Agent0)。
- **Cross-cutting 维度**:online/offline、on-policy/off-policy、reward granularity(outcome-based / process-based 如 [[process-reward-model]] Math-Shepherd / hybrid 如 GiGPO、SPA-RL)。

**Where to evolve(在哪里进化,Sec.6)** 分通用域(memory mechanism、model-agent co-evolution、curriculum-driven training)与专业域(coding 如 SICA/EvoMAC/AgentCoder、GUI/Web 如 WebVoyager/AutoGUI/UI-Genie、financial 如 QuantAgent/TradingAgents、medical 如 Agent Hospital/EvoPatient/STELLA、education 如 PACE/MathVC、others 如 Arxiv Copilot/Richelieu)。

**Evaluation(评测,Sec.7)** 提出五大评测目标 **Adaptivity / Retention / Generalization / Efficiency / Safety**,并按时间尺度区分 Static / Short-horizon adaptive / Long-horizon lifelong learning 三类评测范式;给出标准化评测协议(Table 10)与成本分类(Table 5,含 Cost-per-Gain CPG、Tool Productivity)。

## 结果

本文是综述,核心产出为框架与对比而非单一实验数字,但给出若干具体度量与案例:

- **指标公式**:遗忘度 $\mathrm{FGT}_t=\frac{1}{t-1}\sum_i[\max_j J_{i,j}-J_{i,t}]$、后向迁移 $\mathrm{BWT}_t=\frac{1}{t-1}\sum_i(J_{i,t}-J_{i,i})$;Cost-per-Gain $\mathrm{CPG}_t=\frac{\text{Total Cost}_t}{\text{Performance Gain}_t+\epsilon}$;Tool Productivity $\mathrm{TP}=\frac{\Delta\text{score}}{\sum_i \text{cost(tool}_i)}$。
- **成本案例**(Table 5,SWE-bench 上):SWE-Agent + Qwen3-32B 用 440K tokens、35 次调用、28% 成功率,而 [[gpt-4o-mini]] 用 8.1M tokens、181 次调用、10% 成功率——模型-脚手架协同对效率至关重要(18× token 差异)。
- **对比合成**(Table 11,共享设置下):
  - code/WebArena:[[gpt-4]] 系 vs [[claude]]-3.5-sonnet 上 Reflexion 14.3%/54.4%、Learn-by-Interact 18.7%/60.0%;WebArena 上 Reflexion 40.4%、Learn-by-Interact 48.0%;WebArena-Lite(GLM-4-9B)DigiRL 31.5%、WebRL 43.0%。
  - math/GSM8K([[gpt-4o-mini]]):ADAS 90.5%、AFlow 90.8%、ScoreFlow 94.6%;MATH(Gemini-1.5-pro-002):ADAS 80.0%、AFlow 76.0%、Mass 84.7%。
- **EvoAgent 长程案例**(Table 10):67 个 Minecraft 任务上整体成功率从 21.80% 提升到 30.29%(相对增益约 105.9%),探索效率约 6× 优于基线、训练 wall-clock 约 2.7 天 vs 7 天。
- **GUI 案例**:WebVoyager 经自微调在未见网站成功率从 30% 升至 59%;WindowsAgentArena 上 Navi 在 150 个 Windows 挑战上任务完成率翻倍。

论文指出当前评测的覆盖缺口:Retention(灾难性遗忘)最被忽视,多数 benchmark 采用 episodic 评测(任务间状态重置),无法测量知识累积/退化;长程隐私约束下的记忆、架构在运行约束下的适应、工具生态进化、多智能体协同进化下的安全(misevolution、social contagion)等交叉能力均缺乏评测。未来方向(Sec.8)聚焦个性化智能体、数据治理(data minimization、on-device personalization、记忆衰减与遗忘策略)、安全与公平审计。

## 在本 wiki 中的位置

这是一篇把"自进化/自我改进"作为一等研究范式的总纲性综述,可作为本 wiki 中 [[self-improvement]] 与 [[llm-agent]] 主题的顶层索引。它把多条已有线索整合进统一框架:

- **方法侧**:[[star-self-taught-reasoner]]、[[reflexion]]、[[self-refine]]、[[voyager]]、[[expel]] 等被归入不同进化位点与方法族;[[reinforcement-learning]]、[[direct-preference-optimization]]、[[process-reward-model]]、[[monte-carlo-tree-search]] 是其 how-to-evolve 的核心机制。
- **记忆侧**:与 [[agent-memory]]、[[llm-long-term-memory]]、[[memory-module]] 相关页互补,提供 memory evolution 的方法分类。
- **多智能体侧**:与 [[llm-multi-agent]]、[[multi-agent-collaboration]]、[[chatdev]]、[[autogen]] 衔接,补充架构/种群级进化视角。
- **范式辨析**:明确区分自进化智能体与 [[lifelong-learning]]、[[active-learning]](curriculum learning)、[[model-editing]] 的异同(Table 1 / Sec.2.2)。
- **评测侧**:可与 [[benchmark]]、[[evaluation]] 及 [[agentbench]] 等页关联,补充 Adaptivity/Retention/Generalization/Efficiency/Safety 五维与 long-horizon 评测协议。
