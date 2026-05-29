---
type: source
subtype: paper
tags:
  - llm-multi-agent
  - multi-agent-systems
  - agent-orchestration
  - self-organizing-agents
  - coordination-protocol
  - emergent-abilities
created: 2026-05-29
updated: 2026-05-29
arxiv: 2603.28990
raw: raw/2603.28990.pdf
authors:
  - Victoria Dochkina
year: 2026
---

# Drop the Hierarchy and Roles: How Self-Organizing LLM Agents Outperform Designed Structures

一句话:一项 25,000 任务的大规模实验发现"内生性悖论"(endogeneity paradox)——固定智能体顺序但让角色自主选择的混合协议(Sequential),在质量上同时超越中心化的 Coordinator(+14%)和完全自主的 Shared(+44%),前提是底层模型足够强。

## 问题

[[llm-multi-agent]] 系统当前主要依赖**外生(exogenous)协调**:角色、层级、交互拓扑都由人类在运行前设计固定,如 [[chatdev]](固定软件工程角色)、[[metagpt]](固化 SOP)、[[autogen]]、[[agentverse]]。已有研究分裂为两个方向:垂直自我提升(让单个智能体更强,如 Meta 的 DGM-Hyperagents)和水平协调(多个智能体如何协作)。核心未被回答的问题是:**智能体在协调中的自主程度(从中心化到内生)如何影响规模化下的集体性能?** 作者主张 LLM 智能体与人类工人本质不同(可瞬间切换专长、处理完整组织上下文、空闲时零边际成本),因此把人类组织模式(固定角色、中心化分工、刚性层级)强加给它们可能是反模式。

## 方法

把自治 AI 组织建模为离散时间系统:每步 $x_{t+1}=F(x_t,u_t,w_t,\varepsilon_t)$,状态编码角色、拓扑与组织记忆,$u_t$ 为协调决策,$w_t$ 为外部冲击,$\varepsilon_t$ 为 LLM 随机性。优化目标在质量 $Q$、任务相关性 $M$、执行时间 $T$、成本 $C$(token)、风险 $R$ 五项指标上加权。

四种协调协议覆盖**从外生到内生**的谱系:

- **Coordinator(中心化,外生)**:Agent 0 分析任务并给所有智能体派角色与阶段,其余并行执行;单点控制,$N+1$ 次 LLM 调用。
- **Sequential(混合)**:智能体按固定顺序处理,每个观察所有前驱的**已完成输出**后自主选角色、决定是否参与或弃权;顺序外生,角色与参与内生;类比体育选秀。$N$ 次调用。
- **Broadcast(信号式,内生)**:两轮——先同时广播角色意图,再据全部意图做最终决定。$2N$ 次调用。
- **Shared(完全自主,内生)**:共享组织记忆(历史任务),所有决策同时独立做出。$N$ 次调用。

评估用 [[llm-as-judge]] 多准则方法(独立 judge 模型避免自评偏差),按 Accuracy/Completeness/Coherence/Actionability 四维 4 分制聚合,$Q=\frac{s_{acc}+s_{comp}+s_{coh}+s_{act}}{16}\in[0.25,1.0]$。任务分四个复杂度级别 L1(单域)到 L4(对抗,利益冲突无唯一解)。实验三系列共约 20,810 配置:Series 1(660 任务,[[gpt-4o]] judge)、Series 2(8,020 任务,规模化 4→64,[[gpt-4-1-mini]])、Series 3(12,130 任务,多模型+协议,扩展到 256 智能体)。冲击测试包括随机移除、枢纽移除、25% 模型替换。模型涵盖 8 个:[[claude]] Sonnet 4.6、GPT-5.4、[[gpt-4o]]、[[gpt-4-1-mini]]、Gemini-3-flash、GigaChat 2 Max(闭源)与 [[deepseek-v3]].2、GLM-5(开源)。

## 结果

- **内生性悖论**:相同条件四协议对比中,Sequential 质量最高。Pilot($N=8$,L3+L4)$Q=0.724$ vs Coordinator $0.640$、Broadcast $0.510$、Shared $0.503$;最佳与最差相差 **44%**,效应量 Cohen's $d=1.86$($p<0.0001$)。Final($N=16$,Claude Sonnet 4.6,L3 任务)Sequential $Q_{L3}=0.875$ vs Coordinator $0.767$,即 **+14%**($p<0.001$)。
- **跨模型复现**:L3 任务上 Sequential 对 Coordinator 优势在三个强模型一致——Claude Sonnet 4.6 +14.1%、[[deepseek-v3]].2 +12.4%、GLM-5 +12.2%(均 $p<0.001$)。
- **亚线性规模化**:Series 2 固定角色 $N=8\to64$,质量几乎不变($Q\in[0.949,0.955]$,CV=4.4%),成本仅增 11.8%。Series 3 自组织 $N=64\to256$ 无统计显著质量下降(Kruskal-Wallis $H=1.84$,$p=0.61$)。$N=256$ 时约 45% 智能体通过自我弃权变为空闲,形成内生节省成本机制。
- **能力门槛**:自组织是强模型的特权。自由式 vs 固定角色对比中,Claude Sonnet 4.6 自由式 $Q=0.594>$ 固定 $0.574$(+3.5%,自主有益);GLM-5 自由式 $0.519<$ 固定 $0.574$(-9.6%,自主有害,出现**反转**)。门槛需三种能力:自我反思、深度推理、指令遵循。
- **闭源 vs 开源**:[[deepseek-v3]].2 达到 Claude L3 质量的 **95%**(-5.5%),但 API 成本约低 **24×**;L4 上 DeepSeek 反有 +6.0% 趋势($p=0.082$)。模型间质量差距达 174%(最好 DeepSeek $Q=0.978$ vs 最差 Gemini $0.357$)。
- **涌现性质**:动态角色发明(8 智能体下 5,006 个唯一角色,RSI→0);自愿弃权(Sequential 下 60 个非贡献智能体中 38 个自主退出,Claude 弃权率最高 8.6%);浅层自组织层级(规模化时 Hierarchy Depth 仅从 1.0 增到 2.0;随任务复杂度 L1→L4 从 1.22 增到 1.56)。谱系分析显示专业化随规模增强(RSI 0.750→0.906,+21%),谱隙 $\lambda_2\approx1.93$ 保持稳定(连通性恒定)。
- **抗冲击**:随机移除、枢纽移除、25% 模型替换三类冲击下质量均在 1 次迭代内恢复;系统越大适应越快($T_{adapt}$ 0.7→3.0)。
- **三环宪法框架**:Ring 1 不可变核心(使命/价值,仅人类)、Ring 2 标准(人+系统,系统提议人类批准)、Ring 3 协议(自主,A/B 测试)。原则:越接近"为什么"人类控制越多,越接近"怎么做"系统自主越多。

实践配方:给智能体使命、协议和强模型,而不是预分配角色;协议是集体能力的放大器;投资模型质量而非智能体数量(64→256 无收益,$p=0.61$);组合模型而非择一(开源跑 L1/L2,强模型跑 L3/L4)。

## 在本 wiki 中的位置

本文属于 [[llm-multi-agent]] / [[multi-agent-collaboration]] 与 [[agent-orchestration]] 主题,聚焦"协调架构设计"这一维度。它与固定外生架构的代表作 [[chatdev]]、[[metagpt]]、[[autogen]]、[[gptswarm]] 形成对照,后者均采用人类预设的角色/层级;与垂直自我提升路线([[darwin-godel-machine]] 类的 DGM-Hyperagents)互补——本文主张水平自组织,并提出二者是乘性关系。其"角色是涌现的计算函数而非预分配标签"观点呼应 [[self-evolving-agents]] / [[self-improvement]] 与 [[emergent-abilities]];评估依赖 [[llm-as-judge]];实验涉及 [[claude]]、[[gpt-4o]]、[[gpt-4-1-mini]]、[[deepseek-v3]]、[[gemini]] 等模型。可作为研究"智能体自主度 × 模型能力门槛 × 规模化"三者交互的参考来源。
