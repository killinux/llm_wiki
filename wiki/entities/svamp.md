---
type: entity
subtype: benchmark
tags: [math-reasoning, arithmetic, word-problems, benchmark, nlp]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# SVAMP

SVAMP(Simple Variations on Arithmetic Math word Problems)是一个用于评估模型数学应用题(math word problem)求解与算术推理能力的小学水平测试基准,通过对已有题目施加细微变体来检验模型是否真正理解题意。

## 在本 wiki 中的出现

- [[2023-critic]]:在 CRITIC 中,SVAMP 作为算术推理(arithmetic reasoning)类任务的评测基准之一,用于检验 LLM 借助外部工具(如 code interpreter)交互获得反馈、自我验证并迭代修正输出后,在数学应用题上的表现提升。
- [[2024-recursive-introspection-rise]]:RISE 将单轮问题建模为多轮 MDP 并用 reward-weighted regression 迭代微调,让 7B 级 LLM 在无外部反馈下学会跨多轮递归反思并修正答案。

## 相关

- [[gsm8k]]
- [[chain-of-thought]]
- [[program-of-thoughts]]
- [[tool-use]]
- [[self-correction]]
