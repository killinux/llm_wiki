---
type: source
subtype: paper
tags:
  - llm-agent
  - llm-multi-agent
  - self-evolving-agents
  - real-time-strategy
  - structural-information-theory
  - decision-making
created: 2026-05-29
updated: 2026-05-29
arxiv: "2603.23875"
raw: raw/2603.23875.pdf
authors:
  - Lin Ma
  - Hao Peng
  - Yiming Wang
  - Hongbin Luo
  - Jie Liu
  - Kongjing Gu
  - Guanlin Wu
  - Hui Lin
  - Lei Ren
year: 2026
---

SEMA(Self-Evolving Multi-Agent)是一个面向实时策略(RTS)游戏的 LLM 多智能体框架,用结构熵驱动的观测剪枝降低推理延迟,并通过闭环自演化抑制 LLM 的决策随机性,在 StarCraft II 上实现高胜率与低延迟。

## 问题

把 [[large-language-models]] 直接用于 Real-Time Strategy(RTS,如 StarCraft II)的实时决策面临两个核心矛盾:

- **速度-质量权衡**:RTS 状态空间高维、冗余度高,原始观测会造成 token 爆炸,推理延迟过大,无法满足秒级响应;延迟累积会导致命令下达到已被消灭或已移动的单位,造成资源浪费与逻辑失序。
- **逻辑一致性**:LLM 固有的随机性(stochasticity)使得即便在完全相同的场景下,两次决策也可能给出截然相反的结果(如从 victory 翻转为 defeat),严重削弱对抗环境下的鲁棒性。

传统基于规则的方法泛化能力差;[[reinforcement-learning]] 则训练成本高、需要精心设计的剪枝动作空间与奖励函数。论文把任务形式化为 [[markov-decision-process]] 的部分可观测版本(POMDP)五元组 ⟨S, A, T, Ω, R⟩。

## 方法

SEMA 是一个无需微调的闭环自组织协作框架,包含三个阶段:

**1. 结构熵驱动的动态观测剪枝(Dynamic Pruning)**
基于 [[structural-information-theory]](Structural Information Principles)与结构熵(structural entropy)。先用 LLM 把时刻 t 的原始观测映射为动态属性图 G_t=(V,E),节点为资源/单位状态/建造进度等属性,边权由跨帧属性变化的时空算子 Φ(Δ_i,Δ_j)=|Δ_i·Δ_j|·ln(1+|Δ_i·Δ_j|) 经全局归一化得到。再构造层次编码树(encoding tree),用贪心熵最小化聚类。对每个节点计算结构熵扰动变分度量 δ_H = α·ΔH_G + β·ΔH_T(ΔH_G 为一维结构熵变化,ΔH_T 为二维 H²(G;T) 局部代表性),低于阈值 μ 的非核心属性进入候选删除集,若超出容量因子 N 则按最小 δ_H 排序保留 Top-N。该机制把高维数据压缩为核心语义(Algorithm 1)。

**2. 多智能体决策执行(Interaction Loop)**
多智能体集合 N 包含决策 agent N_D、评估 agent N_V、分析 agent N_A,配合层次存储 L=⟨M, E, K⟩:
- **Decision Agent**:把压缩观测 o_t、历史参考动作 a* 与策略经验 E 映射到动作空间,输出格式化三元组 a_t=⟨e, op, ta⟩(执行主体、动作 id、目标)。
- **Evaluation Agent**:对当前观测 o_t 用余弦相似度 S(o_t, o_m) 从 step 级轨迹记忆库 M(micro-memory block)检索最相似历史状态,抽取参考动作 a*,并从 episode 级经验池 E 检索全局描述先验,做多源融合;通过逻辑一致性约束 ‖a_t − a*_t‖ ≤ η(deviation tolerance)抑制随机偏差。
- **Policy Agent / Cross-Episode Agent**:在 [[reflection]] 与 summary 阶段做赛后复盘,从关键帧元数据抽取策略规则与领域知识,更新到外部知识库 K 与经验池 E。

**3. 双层自演化(Self-Evolution)**
嵌套反馈环:step 级局内评估 + episode 级局后分析,持续校准模型 bias。这是一种 [[self-improvement]] / [[self-evolving-agents]] 的混合知识-记忆机制,融合 micro-trajectories、macro-experience 与层次领域知识。优化目标为 π* = arg max E[𝟙(Σγ^{t-1} r_t > ζ)](最大化期望全局胜率)。

基础模型为 Qwen3-next-80b(见 [[qwen]])。

## 结果

在 8 张 StarCraft II 地图上评测:4 张 Melee 地图(Flat32/Flat48/Flat64/Simple64,两个难度 Lv.1/Lv.2)+ 3 张 SMAC micromanagement 地图(3m/8m/25m)。我方固定 Protoss,对手 Terran 内置 AI,每图 50 次随机试验,指标为胜率与平均延迟。基线含 Random、Rule-Based、Single-LLM、TextStarCraft、HIMA。

**胜率与单局成功时长(Table 2)**:
- SEMA 在全部 4 张 Melee 地图上达到 **100% 胜率**(多数 5m 完成),例如 Flat64 Lv.1/Lv.2 = 100%/94%、Simple64 Lv.1/Lv.2 = 100%/100%。
- SMAC:3m = 88%、8m = 70%、25m = **68%**;在高密度 25m 上 68% 远高于 HIMA 的 10%。
- 相比 HIMA(论文称为 "Society of Mind Meets Real-Time Strategy"),SEMA 把输入 token 减少约 70%,响应时间降低 50%。

**延迟(Figure 3)**:SEMA 平均响应时间稳定在 0.5–1.0s,而其他 LLM 方法约 1.5s 甚至 2.0s。

**Token 消耗(Table 5)**:SEMA 各图 token 远低于基线。25m 上 HIMA 高达 33.1k、SEMA 仅 2.2k;Melee 地图稳定约 2.9k;3m 仅 0.9k。

**消融(Table 3)**:
- 去掉 Dynamic Pruning:延迟升至 >1.0s(Simple64-Lv.2 达 2.1s),3m 胜率从 88% 跌到 50%。
- 去掉 Policy Agent:8m 胜率 70%→52%、Simple64-Lv.2 100%→72%。
- 去掉 Evaluation Agent:延迟影响小(0.6–0.7s)但高难度下随机误差与不稳定上升。

**超参(Figure 5 / Table 4)**:容量因子 N=10 时在信息压缩与语义保留间最优(N>15 引入冗余、过小丢失关键信息)。权重 (α,β)=(0.95,0.05) 时优先全局拓扑熵,保留 Research/Planning 等长周期宏观类别;Planning 节点呈分阶段特性,仅在中期保留。阈值 μ=0.48。

## 在本 wiki 中的位置

SEMA 把 [[structural-information-theory]] 用于 [[llm-agents|llm-agent]] 的观测压缩,是 [[llm-multi-agent]] 在 RTS / 游戏决策上的应用,与 [[generative-agents]]、[[voyager]] 等 LLM agent 在游戏环境的工作同源,但强调实时性与 [[self-evolving-agents]] 的闭环演化。其多 agent 分工(决策/评估/策略反思)和 [[memory-module]]、[[reflection]] 机制与 [[metagpt]]、[[chatdev]]、[[reflexion]] 一脉相承。基线 HIMA 即 "Society of Mind Meets Real-Time Strategy",是直接对照。评测环境为 StarCraft II 与 SMAC,与 [[minedojo]]、[[webarena]] 等 agent benchmark 属同类交互式评测范式。
