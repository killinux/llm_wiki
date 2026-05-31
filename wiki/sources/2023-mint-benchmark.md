---
type: source
subtype: paper
tags: [agent, benchmark, multi-turn, tool-use, evaluation, reasoning, code-generation, decision-making]
created: 2026-05-31
updated: 2026-05-31
arxiv: "2309.10691"
year: 2023
---

# MINT：多轮交互评估基准

一句话：MINT（Multi-turn INTeraction）是一个评估 LLM 智能体通过**多轮交互**利用工具和自然语言反馈来解决复杂任务能力的 [[benchmark]]。

## 问题

现有的 LLM 评估多聚焦于**单轮**输入-输出（如 [[mmlu]]、[[humaneval]]），无法衡量模型在真实应用场景中最关键的能力之一：通过**多轮对话交互**，根据工具返回的结果和用户/环境的自然语言反馈不断修正策略、逐步逼近正确答案。这种迭代式问题求解在 [[llm-agents]] 实际部署中至关重要，但缺乏系统化的评测框架。

## 方法

MINT 构建了一个覆盖三类核心能力的多轮交互评估框架：

- **推理（Reasoning）**：数学与逻辑推理任务，模型需多步求解并可利用 [[tool-use|工具]]（如计算器、代码解释器）辅助验证中间步骤。
- **代码生成（Code Generation）**：编程任务，模型可在多轮中执行代码、观察输出、调试错误。
- **决策（Decision-Making）**：需要与环境交互的序贯决策任务。

评估协议允许模型在每一轮中选择使用工具或接收自然语言反馈，衡量模型在有限轮次内的任务完成率以及利用反馈的效率。这与 [[react]] 和 [[reflexion]] 等方法的核心理念相呼应——交替推理与行动、根据反馈自我修正。

## 结果

- 实验表明，多轮交互和工具使用能显著提升任务完成率，但不同模型从反馈中获益的程度差异很大。
- 顶级模型（如 [[gpt-4]]）在利用自然语言反馈和工具返回结果进行自我修正方面表现最佳，而较弱模型即使给予更多轮次也难以有效改进。
- [[chain-of-thought]] 推理能力与多轮交互效果正相关——具备更强推理链的模型更擅长将反馈整合到后续步骤中。

## 相关页

本文是 [[llm-agents]] 评估领域的重要工作，与 [[agentbench]]（多环境 agent 基准）互补：AgentBench 侧重环境多样性，MINT 侧重多轮交互机制的深度评估。与 [[tool-use]] 评估（如 [[toolbench]]）、[[chain-of-thought]] 推理评估（如 [[gsm8k]]）以及反馈利用方法（[[reflexion]]、[[react]]）密切相关。
