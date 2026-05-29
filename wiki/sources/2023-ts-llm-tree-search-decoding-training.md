---
type: source
subtype: paper
tags: [llm, tree-search, mcts, alphazero, reasoning, planning, rlhf, decoding, training]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2309.17179
raw: raw/2309.17179.pdf
authors: [Xidong Feng, Ziyu Wan, Muning Wen, Stephen Marcus McAleer, Ying Wen, Weinan Zhang, Jun Wang]
year: 2023
---

# AlphaZero-Like Tree-Search can Guide Large Language Model Decoding and Training (TS-LLM)

TS-LLM 是一个 AlphaZero 风格的树搜索框架,用一个**学习得到的 value function**(而非 prompt 大模型)来同时指导 LLM 的推理解码(inference decoding)与训练(training),可适配任意规模 LLM、多类任务,并把搜索树深度拓展到 64。

## 问题

此前用树搜索增强 LLM 推理的工作(如 [[tree-of-thoughts]] / ToT、[[reasoning-via-planning-rap]] / RAP)存在两个核心局限:

1. **value function 来自 prompt 预训练大模型**:依赖精心设计的 prompt 与强大的底座 LLM(如 [[gpt-4]]、LLaMA-33B),通用性差,且 prompt-based self-evaluation 并不可靠。在底座 LLM 知识不足、无法充当有效 value function 的领域会失效。
2. **搜索深度浅**:ToT 用 BFS/DFS、RAP 用 [[monte-carlo-tree-search]],最大深度仅约 10 或 7,远低于 AlphaZero 在国际象棋/围棋中的深度,难以处理需要长程规划(long-horizon planning)的复杂问题,scalability 受限。

## 方法

把语言生成建模为多步 [[markov-decision-process]],LLM 作为 policy $\pi_\theta$,reward 通常是稀疏的(仅最后一步非零,典型如 [[rlhf]] alignment)。

- **action node 两种粒度**:sentence-level(把每个 thought 当作一个动作,树浅;用 tree max width $w$ 子采样,类似 Sampled MuZero)与 token-level(每个 token 为离散动作,树深、更具挑战,用于 RLHF 等无显式中间步骤的任务)。
- **学习 value function 与 ORM**:用一个 decoder-only transformer + MLP 输出标量,得到学习的 value $v_\phi(s)$ 与 final-step outcome reward model([[outcome-reward-model]] / ORM)$\hat r_\phi$;value/reward 网络与 policy 共享 decoder。value target 由 TD-$\lambda$ 或 MC 估计构造,用 MSE loss 训练。
- **五类树搜索算法**:BFS-V/DFS-V(带 value 剪枝,即 ToT 的变体)、MCTS(RAP 采用)、以及两个新提出的 AlphaZero-like 变体——**MCTS-$\alpha$**(AlphaZero 所用,从初始状态多次 select/expand/evaluate/backup,用学习 value 做 backward)与 **MCTS-Rollout**(MCTS-$\alpha$ 的离线版本,每次从初始状态重启搜索,可堆叠更多 token 计算换性能)。
- **多次搜索与聚合**:支持 intra-tree search,聚合方式有 Majority-Vote([[self-consistency]])、ORM-Max、ORM-Vote。
- **训练新范式**:把树搜索当作 policy improvement operator,迭代执行 Policy Improvement(树搜索生成增强数据 $\mathcal D$ 与正样本 $\mathcal D^+$)、Policy Distillation(对正轨迹做监督 [[fine-tuning]] 蒸馏)、Policy Evaluation(在 $\mathcal D$ 上重训 value/ORM),构成 [[reinforcement-learning]] 式的 generalized policy iteration。

## 结果

在五个任务上评测(Table 1):[[gsm8k]](数学推理)、[[game-of-24]] / Game24(数学规划)、PrOntoQA(逻辑推理)、RLHF(对齐,token-level)、Chess Endgame(决策)。rollout policy 在推理任务用 [[llama-2]]-7B,在 RLHF/Chess 用 GPT-2-small(125M)。

- **learned value 优于 prompt-based GPT-3.5**:BFS Path@1 下,即便底座 [[gpt-3-5]] 远强于 LLaMA2-7B,本文学习的 value(LLaMA-V)仍占优。GSM8K 上 GPT-3.5 policy + LLaMA-V 达 **74.0%**(vs GPT-3.5 value 的 72.7%);LLaMA-SFT policy + LLaMA-V 达 **52.5%**(vs LLaMA value 37.4、GPT-3.5 value 45.8)。Game24 上 GPT-3.5 policy + LLaMA-V 达 **19.1%**(vs 15.5);LLaMA-SFT + LLaMA-V 达 **64.8%**(vs 9.2、21.0)。
- **AlphaZero-like 搜索在长程规划任务显著领先**:MCTS-$\alpha$ 与 MCTS-Rollout 在 RLHF 与 Chess Endgame(长程规划重要的任务)上明显优于 BFS-V/MCTS 及 CoT-Greedy;浅树任务上则与 baseline 持平,表现稳健。
- **公平性与计算开销**:作者强调 Path@1/Path@N 指标不公平(树搜索消耗 token 更多),改用 "Equal-Token" 控制相近计算量比较;此时 TS-LLM 优势缩小,GSM8K 上简单的 CoT-SC$_{ORM}$ 反而最佳,但在其余四个更大搜索空间的任务上树搜索仍占主导。比较 BFS-/DFS-V 与 MCTS 时,MCTS 在性能与计算上几乎最优,说明 **value back-propagation 的重要性**。
- 可扩展性:value function 适用 125M 到 7B 的 LLM,树深可达 64(远超 ToT 的 10、RAP 的 7)。

## 在本 wiki 中的位置

本文属于"用搜索/规划增强 LLM 推理与训练"主线,直接延伸并对比 [[tree-of-thoughts]] 与 [[reasoning-via-planning-rap]],把 [[monte-carlo-tree-search]] 与 AlphaZero 的 [[model-based-rl]] 思想引入 LLM。它与 [[chain-of-thought]]、[[self-consistency]] 的线性/采样推理形成对照,并通过学习 [[outcome-reward-model]] 与 value function 关联到 [[process-reward-model]]、[[rlhf]]、[[rejection-sampling-fine-tuning]] 等对齐/自我改进方法,可视为 [[test-time-scaling]] 与 [[self-improvement]] 的一个统一框架。
