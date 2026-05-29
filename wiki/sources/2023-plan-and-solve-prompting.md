---
type: source
subtype: paper
tags: [prompting, reasoning, chain-of-thought, zero-shot, llm]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2305.04091
raw: raw/2305.04091.pdf
authors: [Lei Wang, Wanyu Xu, Yihuai Lan, Zhiqiang Hu, Yunshi Lan, Roy Ka-Wei Lee, Ee-Peng Lim]
year: 2023
---

Plan-and-Solve (PS) Prompting 是一种零样本提示方法,通过让 LLM 先"制定计划再执行子任务"来改进 [[zero-shot-cot]] 的多步推理能力,无需任何人工标注示例。

## 问题

少样本 [[chain-of-thought]] (CoT) 提示通过手工编写的逐步推理示例显著提升了 LLM 的多步推理准确率,但需要人工标注。[[zero-shot-cot]] 用一句 "Let's think step by step" 取代了人工示例,实现了零样本推理,但仍存在三类典型错误:

- 计算错误 (calculation errors)
- 缺步错误 (missing-step errors)
- 语义误解错误 (semantic misunderstanding errors)

作者希望在不引入任何人工示例的前提下,缓解尤其是缺步错误与计算错误。

## 方法

提出 **Plan-and-Solve (PS) Prompting**,核心是用更结构化的触发指令替代单纯的 "Let's think step by step",包含两步:

1. **制定计划 (Plan)**:把整个任务拆解为更小的子任务;
2. **执行 (Solve)**:按计划逐步执行子任务。

在此基础上扩展为 **PS+ Prompting**,加入更详细的指令(例如"提取相关变量及其对应数值""计算中间结果"),以针对性缓解计算错误、提升推理步骤质量。

整个流程仍是零样本的两阶段推理:先用 PS/PS+ 触发提示生成推理过程,再用答案抽取提示获得最终答案。实验基于 [[gpt-3]] (text-davinci-003)。

## 结果

在 10 个数据集、3 类推理任务上评测,与 [[zero-shot-cot]]、Zero-shot-[[program-of-thought]] (PoT) 及 8-shot CoT 对比。

数学推理(6 个数据集,准确率 %):

| 方法 | MultiArith | [[gsm8k]] | AddSub | AQuA | SingleEq | SVAMP | 平均 |
|---|---|---|---|---|---|---|---|
| Zero-Shot-CoT | 83.8 | 56.4 | 85.3 | 38.9 | 88.1 | 69.9 | 70.4 |
| Zero-Shot-PoT | 92.2 | 57.0 | 85.1 | 43.9 | 91.7 | 70.8 | 73.5 |
| Zero-Shot-PS | 87.2 | 58.2 | 88.1 | 42.5 | 89.2 | 72.0 | 72.9 |
| Zero-Shot-PS+ | 91.8 | 59.3 | 92.2 | 46.0 | 94.7 | 75.7 | 76.6 |
| Few-Shot-CoT (Manual) | 93.6 | 58.4 | 91.6 | 48.4 | 93.5 | 80.3 | 77.6 |

- Zero-shot-PS+ 在所有数据集上大幅超越 Zero-shot-CoT(平均 76.6 vs 70.4),并优于 Zero-shot-PoT(73.5),与 8-shot Few-shot-CoT(77.6)接近。

常识推理:Zero-shot-PS+ 在 [[commonsenseqa]] (CSQA) 上 71.9(CoT 65.2),在 [[strategyqa]] 上 65.4(CoT 63.8)。

符号推理:Zero-shot-PS+ 在 Last Letter 上 75.2(CoT 64.8),在 Coin Flip 上 99.6(CoT 96.8)。

## 在本 wiki 中的位置

本文属于 [[prompt-engineering]] 中的零样本推理提示分支,是 [[chain-of-thought]] / [[zero-shot-cot]] 的直接改进,与 [[program-of-thought]] 同属减少 LLM 推理错误的提示策略,可与 [[least-to-most-prompting]]、[[self-consistency]] 等结构化推理方法对照阅读。
