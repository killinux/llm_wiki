---
type: concept
subtype: method
tags: [reasoning, prompting, code-generation, math-reasoning]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Program-of-Thought

Program-of-Thought (PoT) 是一种推理范式:让 LLM 把推理过程表达为可执行的程序(通常是 Python),并将实际的计算交给外部解释器执行,从而把"推理"与"计算"解耦,减少模型在算术等步骤上的错误。

## 在本 wiki 中的出现

- [[2023-plan-and-solve-prompting]]:该论文提出零样本 Plan-and-Solve (PS / PS+) 提示,让 LLM 先制定计划、再分步执行子任务,以改进 Zero-shot-CoT 在多步推理上的表现。Program-of-Thought 在此语境中作为相关的推理/提示方法被提及,代表了将推理外化为程序执行的另一条技术路线,可与 Plan-and-Solve 这类"先规划后执行"的链式推理思路对照。

## 相关

- [[chain-of-thought]]
- [[zero-shot-cot]]
- [[least-to-most-prompting]]
- [[self-consistency]]
- [[prompt-engineering]]
- [[code-generation]]
- [[program-aided-language-model]]
- [[tool-use]]
