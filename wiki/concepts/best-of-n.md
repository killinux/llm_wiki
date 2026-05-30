---
type: concept
subtype: method
tags: [inference-scaling, sampling, reward-model, reasoning, alignment]
created: 2026-05-30
updated: 2026-05-30
sources: 6
---

# Best-of-N 采样 (Best-of-N / Rejection Sampling)

Best-of-N(BoN)是一种**推理时(test-time)增强**方法:对同一输入用 LLM 采样 **N 个**候选输出,再用一个**验证器 / 奖励模型 (reward model)**
或可执行检验选出最好的一个。它不改模型权重,用**更多算力换更高质量**,是 [[test-time-scaling|推理时扩展]]最简单有效的基线。

## 机制与变体
- **BoN**:采 N 个,取打分最高者(scorer 可为 RM、self-consistency 投票、单元测试通过率等)。
- **加权多数投票 / self-consistency**:对答案做边际化投票(推理任务常用)。
- **与搜索的关系**:BoN 是"无结构"的并行采样;更结构化的是树搜索([[tree-of-thoughts]]、[[language-agent-tree-search]])与
  过程奖励引导的束搜索。
- **训练用途**:BoN 选出的高分样本可回灌做拒绝采样微调(如 [[2023-star-self-taught-reasoner|STaR]]、RFT),把推理时收益蒸馏进权重。

## 扩展规律与代价
N 增大通常单调提升通过率,但**边际收益递减**,且受**奖励模型质量**制约——RM 有偏时 BoN 会**过度优化 (reward hacking)**。
[[2024-compute-optimal-inference]] 等研究在固定算力下权衡 N、模型大小与搜索策略的最优配置。BoN 也是评估 [[reward-model]] 与
对齐质量的常用探针。

## 相关页
[[test-time-scaling]]、[[compute-optimal-inference]]、[[reward-model]]、[[self-consistency]]、[[tree-of-thoughts]]、[[2024-v-star-verifiers-for-self-taught-reasoners]]
