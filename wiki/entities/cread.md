---
type: entity
subtype: model
tags: [recommendation, watch-time-prediction, generative-model, ltv]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# CREAD

CREAD 是与短视频观看时长(watch time)预测相关的实体,关联到把序数回归(ordinal regression)重构为 token 序列生成的 Generative Regression(GR)方法。

## 在本 wiki 中的出现

- [[2024-generative-regression-watch-time-prediction]]:提出 Generative Regression (GR),把短视频 watch time 预测从 ordinal regression 重构为 token 序列生成任务,配合 dynamic quantile 词表与 CLEM(curriculum learning + embedding mixup),在 KuaiRec/CIKM16/工业数据集及 Kuaishou 线上 A/B 上超过 SOTA,并可迁移到 LTV 预测。

## 相关

- [[generative-regression]]
- [[watch-time-prediction]]
- [[ordinal-regression]]
- [[ltv-prediction]]
