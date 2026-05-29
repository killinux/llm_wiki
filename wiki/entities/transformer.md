---
type: entity
subtype: model
tags: [transformer, attention, sequence-model, generative]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Transformer

Transformer 是一种基于自注意力(self-attention)机制的序列建模架构,通过并行处理 token 序列来捕捉长距离依赖,是现代大语言模型与众多生成式建模任务的基础骨干。

## 在本 wiki 中的出现

- [[2024-generative-regression-watch-time-prediction]]:提出 Generative Regression (GR),把短视频 watch time 预测从 ordinal regression 重构为 token 序列生成任务,配合 dynamic quantile 词表与 CLEM(curriculum learning + embedding mixup),在 KuaiRec/CIKM16/工业数据集及 Kuaishou 线上 A/B 上超过 SOTA,并可迁移到 LTV 预测。

## 相关

- [[attention-mechanism]]
- [[generative-regression]]
- [[watch-time-prediction]]
- [[sequence-to-sequence]]
