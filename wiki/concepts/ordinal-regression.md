---
type: concept
subtype: method
tags: [ordinal-regression, regression, ranking, watch-time, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Ordinal Regression

Ordinal Regression(序回归)是一类介于分类与回归之间的监督学习方法,用于预测具有自然有序关系但间隔未必等距的离散标签(如评分、等级、分桶后的连续值),其目标是在保持标签序关系的前提下进行预测。

## 在本 wiki 中的出现

- [[2024-generative-regression-watch-time-prediction]]:提出 Generative Regression (GR),把短视频 watch time 预测从 ordinal regression 重构为 token 序列生成任务,配合 dynamic quantile 词表与 CLEM(curriculum learning + embedding mixup),在 KuaiRec/CIKM16/工业数据集及 Kuaishou 线上 A/B 上超过 SOTA,并可迁移到 LTV 预测。

## 相关

- [[generative-regression]]
- [[watch-time-prediction]]
- [[ltv-prediction]]
- [[dynamic-quantile-tokenization]]
- [[curriculum-learning]]
