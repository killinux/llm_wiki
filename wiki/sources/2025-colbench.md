---
type: source
subtype: paper
tags: [benchmark, llm-agents, collaborative-coding, code-generation, evaluation]
created: 2026-05-31
updated: 2026-05-31
arxiv: 2503.15478
year: 2025
---

ColBench 是一个评估 LLM 作为协作智能体在迭代开发工作流中表现的基准,聚焦后端编程与前端设计的多轮协作场景。

## 问题

现有 [[code-generation]] 基准大多考察 LLM 独立完成单次编程任务的能力,忽略了真实软件开发中人与 AI（或 AI 与 AI）之间的**迭代协作**过程——包括需求澄清、设计反馈、多轮修改等。缺少一个系统性基准来衡量 LLM 在协作式开发工作流中的有效性。

## 方法

ColBench 构建了覆盖**后端编程**与**前端设计**两大方向的协作任务集。评估重点在于 LLM 作为协作参与者的能力,包括：
- 理解和响应协作伙伴的反馈与迭代指令；
- 在多轮交互中保持代码一致性与质量；
- 在迭代开发流程中逐步改进产出。

基准通过模拟真实的迭代开发工作流,要求模型不仅生成代码,还要根据反馈进行修改和优化。

## 结果

ColBench 的评估揭示了当前 LLM 在协作开发场景中的局限：模型在单轮代码生成上表现尚可,但在需要多轮迭代、理解上下文反馈并持续改进的协作场景中,性能显著下降。该基准为衡量 [[llm-agents]] 的协作能力提供了量化手段。

## 相关页

本文是 [[llm-agents]] 协作能力评估的新 [[benchmark]],与 [[code-generation]] 和 [[agentbench]] 等评估基准互补。不同于 [[agentbench]] 侧重通用 agent 多环境评估,ColBench 专注于软件开发中的迭代协作维度。
