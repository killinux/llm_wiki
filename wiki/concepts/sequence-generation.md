---
type: concept
subtype: method
tags: [sequence-generation, generative-model, tokenization]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Sequence Generation

序列生成是指模型按顺序逐个生成 token（或离散符号）以构成目标输出序列的方法，常用自回归方式将原本的回归/分类等任务重构为对 token 序列的预测任务。

## 在本 wiki 中的出现

- [[2024-generative-regression-watch-time-prediction]]：提出 Generative Regression (GR)，把短视频 watch time 预测从 ordinal regression 重构为 token 序列生成任务，配合 dynamic quantile 词表与 CLEM（curriculum learning + embedding mixup），在 KuaiRec/CIKM16/工业数据集及 Kuaishou 线上 A/B 上超过 SOTA，并可迁移到 LTV 预测。

## 相关

- [[autoregressive-modeling]]
- [[tokenization]]
- [[watch-time-prediction]]
- [[ordinal-regression]]
