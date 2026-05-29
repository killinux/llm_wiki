---
type: entity
subtype: model
tags: [code-generation, llm, openai]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Codex

Codex 是 OpenAI 基于 GPT 系列在大量公开代码上微调而成的代码生成模型,能够将自然语言描述转换为可执行代码,是早期代码大模型的代表。

## 在本 wiki 中的出现

- [[2022-chain-of-thought]]:Codex 作为实验中评测 chain-of-thought prompting 的代码型大模型之一出现,用于考察在少样本示例中加入中间推理步骤对多步推理任务的提升效果。
- [[2023-self-refine]]:Codex 作为测试时"自我反馈→自我修正"迭代框架(无需额外训练即在多个任务上平均提升约 20%)所适用的 LLM 之一。
- [[2023-self-debugging]]:Codex 作为 SELF-DEBUGGING 方法的基础模型,通过 few-shot prompting 让其执行并解释自己生成的代码,实现无人工反馈的自我调试。

## 相关

- [[chain-of-thought-prompting]]
- [[self-refine]]
- [[self-debugging]]
- [[code-generation]]
- [[gpt]]
- [[few-shot-prompting]]
