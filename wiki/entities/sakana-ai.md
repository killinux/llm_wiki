---
type: entity
subtype: lab
tags: [ai-lab, japan, test-time-scaling, tree-search]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Sakana AI

Sakana AI 是一家位于日本东京的人工智能研究实验室,专注于受自然启发的方法以及大模型推理时的高效扩展(test-time scaling)等方向。

## 在本 wiki 中的出现

- [[2025-ab-mcts-adaptive-branching-tree-search]]:提出 AB-MCTS,在推理时树搜索中用 Thompson sampling 自适应决定"向宽采样新候选"还是"向深用外部反馈细化已有答案",统一了 repeated sampling 与多轮 refinement,实现更高效的 test-time scaling。

## 相关

- [[test-time-scaling]]
- [[monte-carlo-tree-search]]
- [[thompson-sampling]]
