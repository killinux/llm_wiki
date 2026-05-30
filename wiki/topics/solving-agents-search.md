---
type: topic
tags: [llm-agents, reasoning, tree-search, mcts, test-time-compute, planning]
created: 2026-05-30
updated: 2026-05-30
sources: 18
---

# 求解类智能体:推理时搜索与成本-质量权衡 (Solving Agents: Test-time Search & Cost–Quality Tradeoff)

> 一句话:把 LLM 推理从"一条链走到黑"(System 1)升级为**在解空间里有意识地搜索**(System 2)——探索多条路径、自评估、前瞻与回溯。
> 搜索能大幅提升质量,但**成本随之线性/指数上升**;核心问题是**如何最优地分配推理时算力 (test-time compute)**。

这是 [[llm-agents|LLM 智能体]]的"**任务求解 + 搜索**"分支(与 [[generative-social-simulation]] 的"社会模拟"分支并列,分野最早在
[[2023-generative-agents]] 点明)。它与 [[llm-self-improvement]] 互补:**搜索的成败取决于能否可靠地评估/验证中间状态**(value/verifier)。

---

## 一、从链到树:搜索的深化谱系
| 工作 | 搜索结构 | 关键点 |
|---|---|---|
| [[chain-of-thought]] | 单链(System 1) | 逐步推理,但一步错无法回溯 |
| [[2022-react-reasoning-and-acting]] | 单轨迹 | 交替**推理+行动**,与环境交互获取信息 |
| [[2023-tree-of-thoughts]](ToT) | 思考树 BFS/DFS | 多路径探索 + 自评估 + 回溯;深度 ~10 |
| [[2023-reasoning-via-planning-rap]](RAP) | [[monte-carlo-tree-search\|MCTS]] | LLM 兼任**推理器 + 世界模型**,规划即推理;深度 ~7 |
| [[2023-lats-language-agent-tree-search]](LATS) | MCTS over 推理+行动 | 统一推理/行动/规划,环境反馈 + 价值估计 + 自我反思 |
| [[2023-ts-llm-tree-search-decoding-training]](TS-LLM) | AlphaZero 式 | 用**学习的 value function**(非 prompt)同导**解码与训练**,深度达 **64** |
| [[2025-ab-mcts-adaptive-branching-tree-search]](AB-MCTS) | 自适应分支 MCTS | 动态权衡"采样宽度 vs 搜索深度" |

另见 [[2024-rethinkmcts]]、[[2024-reflection-on-search-trees]]、[[2024-multi-agent-tot-validator]]、[[2025-ctrlbench-control-reasoning]]。

## 二、环境中的搜索:web / 具身 agent
任务式 agent 把问题当 POMDP,只据当前观测预测下一步 → 误差累积、一步走错难纠正。引入推理时搜索可显式做 exploration + planning:
- [[2024-tree-search-for-language-model-agents]] —— 为 web agent 设计 **best-first 树搜索**,把 GPT-4o 在 VisualWebArena 上成功率**相对提升 39.7%**(达 SOTA 26.4%),
  并展示 [[test-time-compute]] 的 scaling 收益(但人类仍达 89%,差距巨大)。动作空间大 → 高效**剪枝**是关键。
- 相关:[[2024-stateact-self-prompting-state-tracking]]、[[2024-tree-search-for-language-model-agents]] 与具身规划 [[2022-inner-monologue]]。

## 三、核心张力:成本-质量与推理扩展律
搜索/采样越多,质量越高,但**LLM 调用数(成本)**随之上升。问题变成"**固定算力预算下怎么花最划算**":
- **最简基线——并行采样**:[[best-of-n]]、[[self-consistency]](宽度扩展,无结构)。
- **结构化搜索**:树搜索(深度扩展)用价值/过程奖励引导,样本效率更高但实现复杂。
- **推理扩展律**:[[2024-compute-optimal-inference]](Inference Scaling Laws)实证分析 **compute-optimal inference**——发现**更小的模型 + 更多搜索**常能在同等算力下**击败更大模型**;最优配置是"模型大小 × 采样数 × 搜索策略"的联合权衡。
- 训练时蒸馏:把搜索收益固化进权重(TS-LLM 同导训练;[[2022-star-self-taught-reasoner|STaR]] 家族),减少推理时反复搜索的成本。

概念枢纽见 [[test-time-scaling]]、[[test-time-compute]]、[[compute-optimal-inference]]。

## 四、成败的关键依赖:价值/验证的可靠性
搜索只有在能**可靠评估节点好坏**时才有效——这正是与 [[llm-self-improvement]] 的接合点:
- **prompt 自评不可靠**:ToT/RAP 用底座 LLM 当 value function,通用性差(TS-LLM 的批评);
- **学习的 verifier/value**:TS-LLM、[[2024-v-star-verifiers-for-self-taught-reasoners]] 用训练的验证器更稳;过程奖励模型 (PRM) 引导束搜索。
- 没有可靠误差信号时,搜索可能只是放大噪声(呼应"内在自我纠错无效"的结论)。

## 五、开放问题
- **宽度 vs 深度 vs 模型大小**的最优分配(AB-MCTS、compute-optimal-inference 是起步)。
- **verifier 的可靠性与过度优化**:奖励/价值有偏时搜索会 reward hacking。
- **真实环境差距**:web/具身 benchmark 上 agent 仍远逊人类(VisualWebArena 26% vs 89%)。
- **搜索 vs 训练**:何时该推理时搜索、何时该把能力蒸馏进权重。

## 相关概念页
[[test-time-scaling]]、[[test-time-compute]]、[[compute-optimal-inference]]、[[best-of-n]]、[[monte-carlo-tree-search]]、
[[tree-of-thoughts]]、[[react]]、[[language-agent-tree-search]]、[[world-model]]、[[reward-model]]
