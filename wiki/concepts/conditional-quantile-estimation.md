---
type: concept
subtype: method
tags: [quantile-regression, pinball-loss, watch-time, recommendation, distribution-modeling]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Conditional Quantile Estimation (CQE)

Conditional Quantile Estimation (CQE) 是一种用分位数回归(quantile regression)建模目标变量完整条件分布的方法:通过 pinball loss 同时学习多个分位点,而非只回归条件期望,从而刻画给定特征下输出的整体分布形态。

## 在本 wiki 中的出现

- [[2024-conditional-quantile-estimation-watch-time]]:提出 CQE,用 quantile regression 与 pinball loss 建模短视频观看时长的完整条件分布,并设计保守/动态组合/条件期望三种推断策略,在 Kuaishou 数亿日活平台上线获显著收益。

## 相关

- [[quantile-regression]]
- [[pinball-loss]]
- [[watch-time-prediction]]
- [[recommendation-system]]
- [[conditional-distribution-modeling]]
