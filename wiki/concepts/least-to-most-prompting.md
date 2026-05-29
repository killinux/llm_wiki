---
type: concept
subtype: method
tags: [prompting, reasoning, decomposition, in-context-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Least-to-Most Prompting

Least-to-Most Prompting 是一种提示策略：先将一个复杂问题分解为一系列由易到难、循序渐进的子问题，再依次求解每个子问题，并把已解决子问题的答案作为后续子问题的上下文，从而提升大模型在需要泛化与多步推理任务上的表现。

## 在本 wiki 中的出现

- [[2022-chain-of-thought]]：作为 chain-of-thought prompting 的相关/对比方法被提及。chain-of-thought 在 few-shot 示例中加入中间推理步骤以提升多步推理能力（该增益随模型规模涌现，PaLM 540B 在 GSM8K 达 57%），而 Least-to-Most Prompting 代表的是另一类「先分解、再逐步求解」的推理提示思路。
- [[2023-plan-and-solve-prompting]]：作为「先规划/分解、后执行」一脉提示方法的相关工作出现。Plan-and-Solve (PS/PS+) 让 LLM 先制定计划再执行子任务以改进 Zero-shot-CoT，其「分解—逐步求解」的核心理念与 Least-to-Most Prompting 一致。

## 相关

- [[2022-chain-of-thought]]
- [[2023-plan-and-solve-prompting]]
- [[chain-of-thought-prompting]]
- [[plan-and-solve-prompting]]
- [[zero-shot-cot]]
- [[problem-decomposition]]
- [[in-context-learning]]
- [[multi-step-reasoning]]
