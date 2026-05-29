---
type: source
subtype: paper
tags:
  - code-generation
  - monte-carlo-tree-search
  - tree-search
  - llm-reasoning
  - self-correction
  - test-time-scaling
created: 2026-05-29
updated: 2026-05-29
arxiv: 2409.09584
raw: raw/2409.09584.pdf
authors:
  - Qingyao Li
  - Wei Xia
  - Xinyi Dai
  - Kounianhua Du
  - Weiwen Liu
  - Yasheng Wang
  - Ruiming Tang
  - Yong Yu
  - Weinan Zhang
year: 2024
---

# RethinkMCTS: 在 MCTS 中精炼错误思路以提升代码生成

RethinkMCTS 是一个面向代码生成的「思路搜索」框架,先用 [[monte-carlo-tree-search]] 探索写代码的推理过程(思路)再生成代码,并引入名为 rethink 的精炼机制,利用细粒度代码执行反馈直接修正搜索树中的错误思路,从而沿更优路径继续搜索。

## 问题

[[code-generation]] 是一个需要多次尝试与迭代修正的推理任务,树搜索方法在该领域表现优异。但已有方法面临两大挑战:

- **推理探索不足**:以往的树搜索方法(如 [[language-agent-tree-search]] 在 code-space 搜索、PG-TD 在 token-level 搜索)直接在代码语言空间中搜索,忽略了对代码生成至关重要的底层推理过程(思路)。
- **错误修正无效**:基于 reflection 的方法仅把历史错误累积进 memory,而不提供正确的推理路径。错误思路仍留在搜索树中,后续搜索会继续沿错误路径前进,导致 memory 轨迹越来越长、搜索质量下降。

本文聚焦于「搜索并精炼代码背后的思路过程」,并充分利用代码执行环境提供的详细反馈来指导和改进这一过程。

## 方法

RethinkMCTS 用 [[monte-carlo-tree-search]] 搜索写代码的思路过程,核心设计包括:

- **思路过程的树搜索**:搜索动作空间定义为写代码的「思路」(strategies/thoughts),在累积多步推理后再据此生成代码。实验表明对 [[gpt-3-5-turbo]] 这类模型,thought-level 搜索比 token/line/code-level 更有效。
- **rethink 机制**:当代码未通过 public test case 时,获取 block-level 分析作为详细 verbal feedback,让 LLM 对当前错误思路进行「重思」(z^new ∼ p(z|s,f,z^old)),直接再生成该叶节点的思路。不重新生成父节点,因为父节点已累积多轮 reward 且已各自经历过 rethink。这与 reflection 仅累加错误历史不同,rethink 直接修改错误推理步。
- **block-level 分析反馈**:把代码按 control-flow graph 划分为 basic block,逐块执行并追踪变量状态,交给 LLM 做块级正误分析,作为细粒度反馈。
- **dual evaluation 双重评估**:当代码通过所有 public test case 后,再让 LLM 给出自评分 v^llm,与 public test 通过率 v^test 组合成 reward(reward = v^test 若 0≤v^test<1;= a·v^test + b·v^llm 若 v^test=1),解决 public test 不足以区分多个全通过代码的问题。
- 选择阶段用 P-UCB 评分平衡探索与利用;backpropagation 沿路径更新 Q 值,并把 verbal feedback 存于叶节点供 expansion 与 rethink 使用。

## 结果

在 APPS(introductory/interview/competition 各取前 100 题)和 [[humaneval]] 上评测,backbone 为 [[gpt-3-5-turbo]] 与 [[gpt-4o-mini]],树搜索算法最大 rollout 数设为 16:

- **整体性能**:RethinkMCTS 在两个数据集上全面超越 feedback-enhanced(LDB、Reflexion)与 search-enhanced(PG-TD、ToT、LATS、RAP)基线。GPT-3.5-turbo 上 HumanEval pass@1 达 89.02,平均 pass@1 52.15;GPT-4o-mini 上 HumanEval pass@1 达 94.51,平均 pass@1 62.93。对较弱的 GPT-3.5-turbo 提升更明显。
- **消融**:每个组件均有贡献,其中 verbal feedback 影响最大(GPT-3.5-turbo 上去掉 VF 时 APPS-Intro pass@1 由 45 降至 39);block-level 分析对 HumanEval 影响显著(89.1→86.6),因 HumanEval 的 public test 更少(平均 2.8 vs APPS 27.52)。
- **rethink vs reflection**:rethink 不仅提升搜索效果(如 HumanEval pass@1 93.29→94.51),还显著降低 token 消耗(如 APPS-Intro 平均 token 成本下降 19.3%,HumanEval 下降 35.7%)。
- **rethink 的搜索有效性**:在整棵树中,有效代码(通过 public test)比例从 w/o rethink 的 10.04(APPS-Intro)/48.30(HumanEval)提升到 15.60/53.29。
- **test-time scaling**:在相同 rollout 预算下,增加 rethink 次数比单纯增加 rollout 数带来更大收益。
- **reward 权重 (a,b)**:(0.8,0.2) 配置整体最佳;(1.0,0.2)、(1.0,1.0) 会让全通过代码得分>1,过早丢弃有潜力但 test 未全过的路径,性能更差。

## 在本 wiki 中的位置

本文属于「LLM 推理 + 树搜索增强代码生成」方向,是把 [[monte-carlo-tree-search]] 用于搜索推理「思路」而非直接搜代码的代表性工作,与 [[tree-of-thoughts]]、[[language-agent-tree-search]]、[[reasoning-via-planning-rap]] 等树搜索推理方法相承接。其 rethink 机制可视为对 [[reflection]]/[[reflexion]] 思路的改进:不再累加错误历史,而是直接精炼错误思路,属于 [[self-correction]] 与 [[test-time-scaling]] 的交叉。来自 [[shanghai-jiao-tong-university]] 与 [[huawei-noahs-ark-lab]]。
