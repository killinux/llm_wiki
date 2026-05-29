---
type: source
subtype: paper
tags:
  - test-time-compute
  - test-time-scaling
  - tree-search
  - process-reward-model
  - reasoning
  - inference-optimization
created: 2026-05-29
updated: 2026-05-29
arxiv: 2408.00724
raw: raw/2408.00724.pdf
authors:
  - Yangzhen Wu
  - Zhiqing Sun
  - Shanda Li
  - Sean Welleck
  - Yiming Yang
year: 2024
---

# Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving

本文(ICLR 2025)提出 inference scaling laws / compute-optimal inference 的研究问题,并设计了新的树搜索算法 REBASE(REward BAlanced SEarch),实证表明在固定推理算力预算下,搭配高级推理策略的小模型往往比大模型更具性价比。

## 问题

训练阶段的 scaling laws(模型规模、训练算力、数据规模的最优配置,如 Kaplan/Chinchilla)已被充分研究,但推理阶段的 inference scaling laws / [[test-time-scaling]] 仍未被深入探讨。核心问题(论文 Fig. 2 把它与 Chinchilla 训练 scaling law 对照)是:给定固定的推理算力预算(以 FLOPs 计),应如何同时配置**模型规模 N**与**推理策略 S**(inference strategy)以最小化错误率 E(N, T; S)?形式化为在约束 FLOPs(N, T; S) = C 下求 (N_opt(C), T_opt(C))。本文聚焦数学问题求解场景(problem-solving),研究 [[test-time-compute]] 与性能之间的权衡。

## 方法

作者将推理算力近似为 C = N × C_inference,其中对于 N_params 参数的 transformer,每 token 的 FLOPs 约为 2 N_params。在此预算框架下系统比较了多种推理策略:

- **Greedy Search**:每步选最大概率 token,生成单一解。
- **Majority Voting**([[self-consistency]]):采样多解,取最常见答案。
- **Best-of-N**:采样 N 个解,用 [[reward-model]] 选最高分。
- **Weighted Voting**:结合多数投票与奖励加权,每个解的投票按其奖励加权。
- 两种树搜索:[[monte-carlo-tree-search]](MCTS)与本文提出的 REBASE。

**REBASE(REward BAlanced SEarch)** 是本文的核心贡献,是一种用于 compute-optimal inference 的新型树搜索算法。树中每个节点代表一个部分解(一段推理步骤序列,root 为问题 x)。其关键思想是用 [[process-reward-model]](PRM)来平衡探索与利用:在第 i 层 expansion 时,奖励为 R(n_j) 的节点扩展宽度按 softmax 归一化奖励分配,W_j = Round(B_i × exp(R(n_j)/T_b) / Σ_k exp(R(n_k)/T_b)),其中 B_i 是该层剩余总扩展预算、T_b 是 balance temperature。每完成 C_i 个解便更新预算 B_i ← B_{i-1} − C_i,直到凑满 N 个解。这样把更多探索预算分配给奖励更高的节点。与 MCTS 不同,REBASE 不需要 value model 或 rollouts/模拟来估计节点质量,而是直接依赖 PRM 打分,因此在相同生成 token 数下比 MCTS 更高效。树构建完成后,对叶节点(完整解)按其 PRM 分数做 weighted voting 或 best-of-N 选出最终答案。

理论上,作者证明了两条定理:采样类的 majority voting / weighted voting 的准确率随采样数 n 收敛到由模型输出分布(及 reward model)决定的固定上限,收敛速度为 O(c^{-n}),即无 oracle verifier 时单纯采样存在 diminishing returns,从而论证需要更复杂的搜索算法。

实验围绕两个问题展开:compute-optimal model size 与 compute-optimal inference strategy。在两个数学推理数据集上进行:[[gsm8k]] 和 MATH(使用 MATH500 子集)。研究模型规模时用 Pythia(410M / 1.4B / 2.8B / 6.9B / 12B);研究推理策略时用数学专用模型 Llemma(7B 与 34B,在 MetaMath 上做 Full-SFT)与 Mistral-7B。reward model 统一使用在 Math-Shepherd 数据集上微调的 Llemma-34B PRM。

## 结果

- **compute-optimal model size 随预算变化**:在 Pythia 系列上(Fig. 1),算力预算小时小模型 compute-optimal,预算增大、小模型准确率饱和后大模型更优;回归得到最优模型规模与预算的关系 **log₁₀(C) = 1.19 log₁₀(N) + 2.03**。但现实部署可用算力通常远低于"大模型开始占优"的临界点,因此相对更小的模型常常 compute-optimal。
- **小模型 + 高级策略 = Pareto-optimal**:Llemma-7B 达到与 Llemma-34B 相当的准确率时,在 MATH500(Fig. 4)与 GSM8K(Fig. 5)上均仅需约 **2× 更少**的总 FLOPs;此结论跨采样、MCTS、REBASE 三类策略与两个数据集都成立。论文摘要进一步指出 Llemma-7B + REBASE 在所有测试预算下都超过 Llemma-34B 的标准 majority voting。
- **REBASE 全面占优**:在 GSM8K 与 MATH500 上,REBASE 在所有测试算力预算下都取得 Pareto-optimal,在相同预算下超过 sampling 的 weighted voting / best-of-N 与 MCTS,且 7B 通常是最优模型规模。
- **MCTS 表现不佳**:在本文设定下 MCTS 甚至低于 weighted voting,因为大量搜索路径(rollouts)消耗算力却产生许多未完成解、对最终投票贡献少;GSM8K 对比图因其性价比差直接未纳入 MCTS。
- 采样类方法中,weighted voting 一致优于 majority voting(只要 reward model "好于随机"),且随采样数增加性能趋于饱和(与理论一致);REBASE 用更少生成 token 就能达到更高准确率,饱和点也更高。

## 在本 wiki 中的位置

本文是 [[test-time-scaling]] / [[test-time-compute]] 方向的代表性实证工作,把训练阶段熟知的 scaling laws 视角迁移到推理阶段。它与 [[self-consistency]]、Best-of-N、[[process-reward-model]]、[[outcome-reward-model]] 等推理增强方法直接相关,并把 [[tree-search]] 思路(对比 [[monte-carlo-tree-search]] 与 [[tree-of-thoughts]])用于 [[reasoning]] 任务。其核心结论——小模型配合复杂解码算法可在预算受限场景(如端侧设备)更具性价比——为 [[large-language-models]] 的高效部署提供了实证依据。
