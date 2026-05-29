---
type: concept
subtype: method
tags: [prompting, reasoning, chain-of-thought, zero-shot, LLM]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Zero-shot CoT

Zero-shot CoT(Zero-shot Chain-of-Thought)是一种无需提供示例的提示方法,通过在问题后追加类似 "Let's think step by step" 的引导语,促使 LLM 在不依赖 few-shot 示例的情况下自发生成中间推理步骤,从而提升多步推理能力。

## 在本 wiki 中的出现

- [[2022-chain-of-thought]]:提出 chain-of-thought prompting,即在 few-shot 示例中加入中间推理步骤来显著提升大模型的多步推理能力,且该增益随模型规模涌现(PaLM 540B 在 GSM8K 达 57%)。这是 CoT 推理范式的源头,Zero-shot CoT 是在其基础上去除示例、改为零样本触发的变体。
- [[2023-plan-and-solve-prompting]]:提出零样本 Plan-and-Solve(PS/PS+)提示,让 LLM 先制定计划再执行子任务,以此作为对 Zero-shot-CoT 的改进,显著缓解其在多步推理中的不足。Zero-shot CoT 在此被作为对照基线与改进对象。

## 相关

- [[chain-of-thought]]
- [[2022-chain-of-thought]]
- [[2023-plan-and-solve-prompting]]
- [[few-shot-prompting]]
- [[prompt-engineering]]
- [[in-context-learning]]
- [[gsm8k]]
