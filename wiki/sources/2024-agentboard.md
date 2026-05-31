---
type: source
subtype: paper
tags: [agent, benchmark, multi-turn, evaluation, partially-observable]
created: 2026-05-31
updated: 2026-05-31
arxiv: "2401.13178"
venue: "NeurIPS 2024 Oral"
affiliations: [HKUST]
year: 2024
---

# AgentBoard：多轮 LLM 智能体分析性评估平台

一句话：AgentBoard 是一个面向多轮 [[llm-agents]] 的**分析性评估框架**（NeurIPS 2024 Oral），在统一接口下提供部分可观测环境中的细粒度能力诊断，而非仅报告最终成功率。

## 问题

现有 agent [[benchmark]]（如 [[agentbench]]）虽然覆盖多种环境，但评估维度较粗——通常只报告最终任务成功率（success rate），无法揭示 agent 在**多轮交互过程中**的行为模式：哪些子能力（规划、工具使用、记忆回溯、错误恢复等）是瓶颈？在部分可观测环境（partially-observable environments）中，agent 如何积累信息、何时做出关键决策？缺乏过程级（process-level）的诊断工具使得改进方向不明。

## 方法

AgentBoard 的核心设计包括：

- **统一框架**：将多个已有的交互环境（涵盖网页浏览、工具使用、知识推理、游戏等）纳入统一的 API 接口，标准化观察/行动空间和评估协议。
- **部分可观测性**：所有任务都设置为部分可观测环境（POMDP），agent 无法一次看到全部信息，需要通过多轮探索逐步获取。
- **分析性评估（Analytical Evaluation）**：除了最终 success rate，还引入了**进度率（progress rate）**等细粒度指标，追踪 agent 在任务执行过程中的中间里程碑完成情况。这使得即使在任务最终失败时，也能量化 agent "走了多远"。
- **能力维度分解**：将 agent 表现分解为多个子能力维度（如规划、推理、[[tool-use|工具调用]]、长程记忆等），为模型对比提供雷达图式的多维画像。
- 配套提供交互式可视化面板（dashboard），支持轨迹回放和跨模型对比。

## 结果

- 评估了多个主流 LLM（包括 [[gpt-4]]、[[claude-2]] 等 API 模型和开源模型）的 agent 能力。
- **进度率分析**揭示：许多模型在最终 success rate 相近时，中间进度差异很大——有些模型能走到任务后期但在最后一步失败，另一些则在早期就偏离正确路径。
- 能力维度分解表明：**长程规划**和**错误恢复**是当前模型最薄弱的环节，而单步 [[tool-use|工具调用]]准确率相对较高。
- 部分可观测环境比全可观测环境难度显著更大，模型在信息收集策略上表现参差不齐。

## 相关页

AgentBoard 由 [[hkust|香港科技大学]] 团队提出，与 [[agentbench]]（清华，首个多环境 agent 基准）形成方法论互补——AgentBench 奠定了多环境评估范式，AgentBoard 则深化了**过程级分析**维度。其进度率指标与 [[evaluation]] 领域中过程奖励模型（Process Reward Models）的思路相呼应。与 [[mint-benchmark]]（多轮交互）、[[osworld]]（真实 OS 环境）共同构成近期 [[llm-agents]] 评估的完整图景。
