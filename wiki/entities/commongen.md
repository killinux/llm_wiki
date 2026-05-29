---
type: entity
subtype: benchmark
tags: [benchmark, nlp, generative-commonsense, constrained-generation, text-generation]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# CommonGen

CommonGen 是一个用于评测生成式常识推理(generative commonsense reasoning)的约束文本生成基准:给定一组日常概念(concept set),要求模型生成一个连贯、合理且涵盖这些概念的自然语言句子。

## 在本 wiki 中的出现

- [[2023-self-refine]]:作为 Self-Refine 评测的任务之一。Self-Refine 让同一个 LLM 在测试时迭代执行"自我反馈 → 自我修正",无需额外训练即可在 7 个任务上平均提升约 20%,CommonGen(及其更难的变体)在其中被用来检验该方法在约束式常识生成上的改进效果。

## 相关

- [[commonsenseqa]]:同属常识推理类的评测,但 CommonGen 侧重生成而非选择题式问答。
- [[self-refine]]:在本 wiki 中将 CommonGen 用作评测任务的方法。
- [[constrained-generation]]:CommonGen 所属的约束文本生成任务范式。
