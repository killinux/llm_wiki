---
type: source
subtype: paper
tags: [agent-based-modeling, llm-agent, social-simulation, large-scale-simulation, counterfactual-reasoning, multi-agent-systems, calibration, covid-19, policy]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2409.10568
raw: raw/2409.10568.pdf
authors: [Ayush Chopra, Shashank Kumar, Nurullah Giray Kuru, Ramesh Raskar, Arnau Quera-bofarull]
year: 2024
---

这是一篇 AAMAS 2025 论文(MIT + University of Oxford),提出 **LLM archetypes(LLM 原型)** 方法:不为每个个体单独查询 LLM,而是为少数"代表性 agent 类型"查询 LLM 行为,从而在保持 **百万级仿真规模** 的同时引入 LLM 驱动的自适应行为,案例为纽约市 840 万人口的 COVID-19 [[agent-based-modeling]] 仿真。

## 问题

[[agent-based-modeling]](ABM)能刻画疫情、住房、灾害响应等复杂系统,但长期受两大限制:(1)大规模仿真与校准的高计算成本——可微 ABM(differentiable ABM)+ 向量化已部分缓解,可在消费级硬件上仿真千万级 agent;(2)更关键的是 **agent 行为缺乏表达力**,多数 ABM 仍用简单的 rule-based 启发式更新规则,无法捕捉真实个体的自适应决策。

把 [[large-language-models]] 接入 ABM 可以解耦"agent 行为动态"与"环境动态",带来更真实的 [[llm-agents|llm-agent]] 行为。但已有 LLM 多智能体仿真(如 [[generative-agents]] 的 Smallville 25 个 agent、宏观经济 300 个 agent、Minecraft 1000 个 agent)都局限在 **几百个 agent 的小规模**:在每个时间步为每个个体查询一次 LLM,当 agent 数达百万时计算上不可行。本文目标就是弥合"个体能动性(agency)"与"仿真规模(scale)"之间的鸿沟。

## 方法

核心洞察:**不同行为类型的数量远小于 agent 数量**。因此只需为每个"独特特征组合"(如年龄 × 性别)查询一次 LLM,即可代表整组相似 agent——这些组合称为 **archetypes(原型)**。

- **agent 更新规则改写**:在标准 ABM 更新 `s_i(t+1)=f(s_i(t), Σ m_ij, e(t), θ)` 基础上,加入 LLM 输出 `ℓ(·|s_i, e, θ)` 作为行为代理;把 LLM 输出解释为对 yes/no 问题(如"是否居家隔离?""是否去工作?")的回答,即 `α ~ Bernoulli(p)=ℓ(·)`。
- **Monte-Carlo 估计原型动作概率**:对每个原型 k,用 M 次 LLM 生成估计动作概率 `p_α(k) ≈ (1/M)Σ ξ_i`;个体决策再从所属原型的动作分布中 **概率采样**,从而在组内保持 **action heterogeneity**(不退化为全组同一决策)。
- **复杂度**:K 个原型 × A 个可查询动作 = K×A 次查询,远小于 N 个 agent。NYC 案例中仅需约 **400 次 LLM 查询** 即可为 840 万 agent 每周采样一次决策。
- **自回归 prompt**:prompt 用 **仿真轨迹**(上一步的病例数、疫情持续时长、是否收到 stimulus 补贴)而非 ground-truth 填充,因为面向未来政策的 prospective 仿真没有真值;这要求 LLM 在线采样、行为无法离线预存,凸显 scale-agency 的权衡。
- **实现**:扩展开源大规模 ABM 框架 **AgentTorch**(支持对 (f,g) 可微、梯度优化结构参数 θ),新增 `Archetype` / `Behavior` API,支持离线 / 在线 LLM。实验用 [[gpt-3-5]](GPT-3.5),敏感性分析对比 [[gpt-4o-mini]] 与 GPT-3.5-turbo。
- **环境**:NYC COVID-19,840 万人;数据源含 2022 ACS、BLS 就业数据、CDC 疫情数据、Google Mobility;耦合 **疾病传播模型** 与 **劳动力市场计量模型**,通过反馈闭环互相影响。

## 结果

- **预测精度(Table 1,MSE,越低越好)**:Archetype 在失业率预测 MSE = **24.59 ± 1.5**(Heuristic 41.05、LLM-as-agent 56.98)、感染数预测 MSE = **95.17 ± 20.23**(Heuristic 2914.73、LLM-as-agent 4311.70)。Archetype 在两项上均最优——既有自适应表达力,又不牺牲仿真规模。
- **计算效率**:仅需约 **400 次查询** 仿真 840 万 agent(对比传统逐个体方案需百万级查询);Figure 4 显示 Archetype 比 LLM-as-agent **节省约 95% 运行时**,仅比 heuristic agent 略多。
- **行为校准(Figure 2)**:随 prompt 加入更多上下文(仅人口属性 → +疾病动态 → +stimulus 信息),与 census 就业行为的相关性递增;Archetype 在 5 个 borough 中的 3 个(约 500 万人)捕捉到正向的随时间变化的行为相关。
- **counterfactual 分析(Figure 5)**:对 Delta(β=2.5–4.0)与 Omicron(β=5.5–8.0)两变种做反事实("若 Delta 来得更晚""若 Omicron 来得更早"),发现 "pandemic fatigue" 引发的行为变化与传染性提升的耦合,使真实 Omicron 波峰高于原始与"类 Omicron" Delta 波——回应 Lucas Critique(历史数据无法独立预测新政策下的行为适应)。
- **敏感性(Figure 6)**:M 较小时用更强的 GPT-4o 表现更好;M 较大(聚合多次查询)时 GPT-3.5 也显著改善。
- **局限**:LLM 输出的鲁棒性 / 公平性 / [[hallucination]] 偏差、原型选择与插值方法、动作空间仍较简单、LLM 知识的"时间污染"(anachronistic info)、个体行为缺乏形式化验证基准。

## 在本 wiki 中的位置

本文属于 **大规模社会仿真 + LLM agent** 方向,是把 [[llm-agents|llm-agent]] 接入 [[agent-based-modeling]] 并扩展到百万级的代表性工作。它与 [[generative-agents]]、[[social-simulation]]、[[recagent]]、[[replicantlife]] 等小规模 LLM 社会仿真形成对照(强调 scale-agency 权衡);其可微校准与 AgentTorch 框架连接 [[deep-neural-network]] 与 ABM;counterfactual 分析与 [[counterfactual-reasoning]]、[[causal-inference]] 相关。可与同样面向 generative ABM 的 [[2023-concordia-generative-agent-based-modeling]] 对照阅读。
