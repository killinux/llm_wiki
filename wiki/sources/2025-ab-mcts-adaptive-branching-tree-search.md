---
type: source
subtype: paper
tags:
  - test-time-scaling
  - test-time-compute
  - monte-carlo-tree-search
  - tree-search
  - reasoning
  - code-generation
created: 2026-05-29
updated: 2026-05-29
arxiv: "2503.04412"
raw: raw/2503.04412.pdf
authors:
  - Yuichi Inoue
  - Kou Misaki
  - Yuki Imajuku
  - So Kuroki
  - Taishi Nakamura
  - Takuya Akiba
year: 2025
---

# Wider or Deeper? Scaling LLM Inference-Time Compute with Adaptive Branching Tree Search (AB-MCTS)

提出 **AB-MCTS(Adaptive Branching Monte Carlo Tree Search)**:在推理阶段的树搜索每个节点上,基于外部反馈自适应地决定"向宽展开(go wider,采样新候选)"还是"向深细化(go deeper,refine 已有答案)",从而统一 repeated sampling 与多轮 refinement,实现更高效的 [[test-time-scaling]]。

## 问题

[[test-time-compute]] / inference-time scaling 已被证明能显著提升 [[large-language-models]] 在复杂任务上的推理能力。作者把现有方法分为三类:(1) post-training [[fine-tuning]](如 OpenAI o1/o3 用 RL/CoT 微调);(2) reward-guided [[chain-of-thought]] 逐步搜索;(3) 多答案生成。本文聚焦第三类,且与前两类正交、可组合。

第三类中最成功的是 **repeated sampling**(best-of-n、majority voting、[[self-consistency]]):在非零温度下从同一 prompt 独立采样多个候选再选最优。它充分利用了 LLM 的"多样且广阔的输出空间",但**只做 exploration,缺乏 exploitation**——无法利用真实任务(如 coding 可跑测试)中可得的外部反馈来改进候选。

另一类方法(如 LATS、RAP、SWE-Search、RepoUnderstander 这类把 LLM 与 [[monte-carlo-tree-search]] 结合的工作)虽支持多轮探索,但大多使用**固定 width(固定 branching factor)**作为超参。而 repeated sampling 的成功恰恰说明固定 width 会限制 scaling。核心难题:**如何把"无界分支(unbounded branching)"引入 MCTS**,使搜索能在"宽 vs 深"之间动态权衡。

## 方法

把答案搜索建模为构建搜索树 T,每个非根节点对应一个 LLM 生成的答案,目标是让树中出现尽量高分的答案;打分函数 R(如代码通过测试的比例,可能只是 surrogate / public test)在 [0,1] 区间。每次迭代三步:Selection 选节点 → Expansion 生成子节点(根节点从 prompt 生成,非根节点带外部反馈 refine 父答案)→ Score backup 回传分数。无需额外 rollout。

关键创新:

- **GEN node(自适应分支)**:每个节点都挂一个特殊的 GEN 子节点,代表"再生成一个新分支"的动作。选中 GEN 即向宽展开;选中已有子节点即向深 refine。由于 LLM 非零温度采样的 branching factor 理论上无穷,这样就允许任意节点被重复展开,突破固定 width。
- **用 [[thompson-sampling]] 做节点选择**:因为 GEN node 没有子节点,无法算 UCT/UCB,且 arms 是动态生成的,经典多臂赌博机的 UCT 不适用。改用 **Bayesian 后验预测分布 + Thompson sampling**,对每个动作 a_j 采样一个预测分数,选最大者;还天然支持并行展开。
- **两个变体**:
  - **AB-MCTS-M(Mixed model)**:在每个节点拟合一个节点级 mixed model(分层贝叶斯,组级 intercept + per-instance 噪声),用 MCMC 采样后验。GEN node 作为"新组",其 intercept 由其他组的后验信息推断,跨子树共享统计强度。
  - **AB-MCTS-A(node Aggregation)**:更接近标准 UCT-MCTS,无共享参数、更轻量。引入 **CONT node**(与 GEN 同层,表示"继续 refine 当前答案")以理清分数回传路径。用指数族 + 共轭先验做解析后验更新,提供 Gaussian(normal-inverse-χ²)与 Beta(分数在 [0,1])两种先验。

## 结果

- **模型**:GPT-4o(gpt-4o-2024-08-06)与 DeepSeek-V3(deepseek-chat)。生成预算上限设为 2^7 = 128 次 API 调用。GPT-4o 温度 0.6,DeepSeek-V3 温度 1.0。
- **Benchmark**:LiveCodeBench、CodeContest、ARC-AGI、MLE-Bench(源自 Kaggle 竞赛)。基线:Repeated Sampling(Best-of-n)、Sequential Refinement、Standard MCTS(沿用 LATS 配置,固定每次扩展 5 个子节点)。
- **Table 1(跨 benchmark/模型,括号内为排名,Avg. Rank 越小越好)**:AB-MCTS-M 平均排名 **2.3** 最佳;AB-MCTS-A(Gaussian)与 AB-MCTS-A(Beta)均为 **2.7**;基线 Repeated Sampling 3.5、Standard MCTS 4.2、Sequential Refinement 5.5。代表性数字:LiveCodeBench GPT-4o 上 AB-MCTS-A(Gaussian)39.1(最高),DeepSeek-V3 上 AB-MCTS-M 43.0;CodeContest GPT-4o 上 AB-MCTS-M 40.6(最高,Pass@1),DeepSeek-V3 上 AB-MCTS-A(Beta)44.8(最高);ARC-AGI 上 repeated sampling 仍是强基线(GPT-4o 15.0、DeepSeek-V3 18.6 居首),AB-MCTS 紧随其后。
- **Table 2(MLE-Bench)**:AB-MCTS-M 平均排名 1.3 最佳(Spooky 0.38、Pizza 0.72 均第一)。
- 趋势(Figure 4/5):在相同生成预算下,AB-MCTS 系列普遍优于基线;LiveCodeBench 上在预算小到 2^3 时即开始领先;搜索树形态分析显示 AB-MCTS 能按任务需要自适应地在"更宽/更深"间调整,这种适应性是基线所缺乏的。

结论:把 LLM 输出的多样性(宽)与多轮反馈细化(深)结合,是有效 inference-time scaling 的关键。代码以 `treequest` 开源(github.com/SakanaAI/treequest)。

## 在本 wiki 中的位置

本文是 [[test-time-scaling]] / [[test-time-compute]] 方向中"多答案生成 + 树搜索"路线的代表作,核心是把 [[monte-carlo-tree-search]] 的固定 width 推广为基于 [[thompson-sampling]] 的自适应无界分支。

- 与 [[self-consistency]] / best-of-n 这类纯 exploration 的 repeated sampling 相比,AB-MCTS 增加了用外部反馈做 exploitation 的能力。
- 与 [[tree-of-thoughts]]、[[reasoning-via-planning-rap]]、[[language-agent-tree-search]] 等"LLM + 树搜索 / 规划"工作相比,它不固定 branching factor,并用贝叶斯后验统一"宽 vs 深"决策。
- 与 [[compute-optimal-inference]]、[[rebase]] 等 test-time compute 分配研究互补;也可与 post-training(o1/o3 式 RL 微调)、reward-guided CoT 正交组合。
- 主要落地在 [[code-generation]]([[humaneval]] 系之外的 LiveCodeBench/CodeContest)与 ML engineering / ARC-AGI 等可获得 [[code-execution]] 反馈的任务上。

作者来自 [[sakana-ai]](日本),含 Takuya Akiba 等;论文为 NeurIPS 2025 spotlight。
