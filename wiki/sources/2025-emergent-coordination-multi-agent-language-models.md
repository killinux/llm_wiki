---
type: source
subtype: paper
tags:
  - llm-multi-agent
  - emergence
  - collective-intelligence
  - information-decomposition
  - theory-of-mind
  - persona
created: 2026-05-29
updated: 2026-05-29
arxiv: "2510.05174"
raw: raw/2510.05174.pdf
authors:
  - Christoph Riedl
year: 2025
---

# Emergent Coordination in Multi-Agent Language Models

本文提出一个基于 information decomposition(信息分解)的、纯数据驱动的框架,用以检验 [[llm-multi-agent]] 系统究竟是"一群各自为政的 agent 的简单聚合",还是"具有高阶结构(higher-order structure)的整合性集体",并发现 theory-of-mind(ToM)prompt 能把松散聚合steer 为目标导向的整合性集体。

## 问题

[[llm-multi-agent]] 系统常被报告在软件开发、医疗等任务上优于单 agent,流行解释诉诸 "greater-than-the-sum-of-its-parts"(大于部分之和)效应,归因于 differentiated agent 之间的分工。但作者指出:社区缺乏一个原则性的度量来判断 synergy(协同)何时出现、agent differentiation(角色分化)起什么作用、以及能否系统性地 steer 它。本文的核心问题是 conditional cross-agent synergy——即在多 agent 约束下、agent 之间是否真的产生协同与互补信息(论文明确声明不追求 team-over-solo 的绝对优势)。围绕此提出三个研究问题:RQ1 多 agent LLM 系统是否具备 emergence(涌现)能力;RQ2 涌现带来什么功能优势;RQ3 能否用 prompt/角色/推理结构 steer 内部协同机制。

## 方法

- **任务**:无通信的 group guessing game(group binary search,源自 Goldstone et al. 2024)。多个 agent 各自私下提出整数,使其总和匹配一个随机隐藏目标数,仅收到 group-level 反馈 "too high"/"too low";agent 互不知道彼此猜测与群体规模。该设定让 redundancy(对齐)与 synergy(有用的多样性)直接对立,适合隔离 cross-agent 互补性。
- **三种干预**:Plain(仅游戏指令的控制组);[[persona]](给每个 agent 赋予 name/gender/age/职业/性格/价值观等属性);ToM(指示 agent 思考其他 agent 可能怎么做,即引入 [[theory-of-mind]])。
- **分析框架**:基于 partial information decomposition(PID;Williams & Beer 2010)与 time-delayed mutual information(TDMI)的 dynamical emergence(动态涌现)形式化理论(Rosas et al. 2020;Mediano et al. 2022)。实现四类检验:(1) emergence capacity——用两 agent 现态对其联合未来态的预测性 synergy(k=2 阶 PID);(2) practical criterion——宏观信号 V 的自预测性是否超过各部分之和 S_macro(ℓ)=I(V_t;V_{t+ℓ})−ΣI(X_k,t;V_{t+ℓ});(3) coalition test——三元组的 I₃ 及超过最佳配对的增益 G₃;(4) agent differentiation——用 hierarchical(mixed)model 的 likelihood ratio test 检验 agent 是否有 identity-linked 的截距/斜率差异。
- **falsification 与稳健性**:用 row-wise shuffle(打破身份)与 column-wise time-shift surrogate(打破跨 agent 对齐)两种 null,Fisher 法合并 p 值;并用 bias-corrected(Jeffreys prior、Miller-Madow)熵估计、quantile binning、functional null baseline 等多重稳健性检验。

## 结果

- **预备实验**(GPT-4.1,group size 3-15 × temperature 0-1,共 7,150 次实验):任务对更小群体显著更易,每多一个成员成功几率约下降 8%(OR=0.92, p<10⁻¹⁶);temperature 每增加一个单位成功几率约上升 50%(OR=1.50, p<10⁻⁷)。
- **主实验**(N=10, T=1, [[gpt-4-1]],每条件复制 200 次共 600 次):三种干预的总体 success rate 无显著差异。但 emergence 在所有条件下都存在——practical criterion 的 bias-corrected 估计在各条件都显著大于 0(Plain p=1.5×10⁻¹⁶;Persona p=6.6×10⁻⁷;ToM p=0.02),Fisher 合并 p<10⁻¹⁶。
- **动态机制**:仅 ToM 条件出现显著正的三元组 I₃(p=3.5×10⁻¹⁴)与 Total Stability(p=2.9×10⁻¹⁴),把群体从 "gaseous" 的混沌态steer 进入稳定吸引子;Plain/Persona 的 I₃ 与 Total Stability 与 0 无异。triadic gain G₃ 在 Persona/ToM 约为 0,说明稳定性靠 dense pairwise alignment(类似 "Mean Field" 耦合)而非不可约的三元组复杂性。
- **角色分化**:Persona 条件 agent 分化显著增强,ToM 条件更甚(agent 推理 trace 常引用所赋 persona 的"个人经验")。
- **功能作用**:synergy 或 redundancy 单独都不预测成功;二者同时存在时表现显著提升(交互项 β=0.24, p=0.014;在 log-odds 尺度上彼此放大约 27%)。causal mediation 显示 ToM 通过提升 synergy 间接提升表现(ACME=0.034, p=0.053,边际显著)。
- **跨模型泛化**:[[llama-3]]-3.1-70B、[[gemini]] 2.0 Flash、[[qwen]]3 的 success rate 与 GPT-4.1 相当且呈现强 emergence;小模型 LLAMA-3.1-8B 因 ToM 推理能力弱,基本无法打破振荡;reasoning 模型 Qwen3 出现作者称为 "paralysis under coordination ambiguity" 的失败——陷入无限 chain-of-thought 循环。

## 在本 wiki 中的位置

本文属于 [[llm-multi-agent]] / [[multi-agent-collaboration]] 与 [[emergent-abilities]]、[[collective-intelligence]] 主题,把人类群体认知理论(collective intelligence)经由 information-theoretic 度量桥接到 LLM 集体。其 ToM 干预与 [[theory-of-mind]]、[[persona]]、[[role-playing]] 相关,方法上提供了区分"虚假时间耦合"与"性能相关 cross-agent synergy"的诊断工具,可与 [[multi-agent-debate]]、[[generative-agents]]、[[social-simulation]] 等方向对照阅读。作者(Christoph Riedl,[[northeastern-university]])强调结论不应被解读为 agent 具备类人认知或意识,synergy 只是 part-whole 关系的结构性属性。
