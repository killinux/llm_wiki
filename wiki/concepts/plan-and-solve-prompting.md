---
type: concept
subtype: method
tags: [prompting, reasoning, chain-of-thought, zero-shot, planning]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Plan-and-Solve Prompting

Plan-and-Solve (PS) Prompting 是一种零样本(zero-shot)提示方法,引导 LLM 先制定解决问题的整体计划,再按计划逐步执行各个子任务,以改进多步推理的准确性。

## 在本 wiki 中的出现

- [[2023-plan-and-solve-prompting]]:提出本方法。该论文给出零样本 Plan-and-Solve(PS 及其增强版 PS+)提示,让 LLM 先制定计划再执行子任务,从而显著改进 Zero-shot-CoT 在多步推理任务上的表现。

## 相关

- [[zero-shot-cot]]:Plan-and-Solve 旨在改进的基线方法,二者同属零样本推理提示。
- [[chain-of-thought]]:思维链提示,Plan-and-Solve 在其"逐步推理"思路上引入显式的"先计划后求解"结构。
- [[least-to-most-prompting]]:同样采用"先分解再求解"思路的相关提示方法。
- [[prompt-engineering]]:Plan-and-Solve 属于提示工程下的具体方法。
