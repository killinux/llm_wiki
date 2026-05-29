---
type: entity
subtype: benchmark
tags: [benchmark, code-generation, evaluation, llm]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# LiveCodeBench

LiveCodeBench 是一个面向大语言模型代码能力的评测基准,通过持续收集新发布的编程竞赛题目来减少数据污染,综合考察代码生成、自我修复、代码执行与测试输出预测等多项任务。

## 在本 wiki 中的出现

- [[2025-ab-mcts-adaptive-branching-tree-search]]:提出 AB-MCTS,在推理时树搜索中用 Thompson sampling 自适应决定"向宽采样新候选"还是"向深用外部反馈细化已有答案",统一 repeated sampling 与多轮 refinement,实现更高效的 test-time scaling;LiveCodeBench 作为评测该方法代码能力提升的基准之一。

## 相关

- [[test-time-scaling]]
- [[monte-carlo-tree-search|mcts]]
- [[thompson-sampling]]
- [[code-generation]]
