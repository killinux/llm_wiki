---
type: concept
subtype: method
tags: [quantile-regression, pinball-loss, conditional-distribution, regression, watch-time]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Quantile Regression

分位数回归(Quantile Regression)是一类通过最小化 pinball loss(分位数损失)来估计目标变量条件分位数的回归方法,可刻画完整的条件分布,而不仅仅是条件均值。

## 在本 wiki 中的出现

- [[2024-conditional-quantile-estimation-watch-time]]:提出 CQE,用 quantile regression 与 pinball loss 建模短视频观看时长的完整条件分布,并设计保守/动态组合/条件期望三种推断策略,在 Kuaishou 数亿日活平台上线获显著收益。

## 相关

- [[pinball-loss]]
- [[conditional-distribution-modeling]]
- [[watch-time-prediction]]
