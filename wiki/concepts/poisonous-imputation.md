---
type: concept
subtype: method
tags: [debiasing, doubly-robust, recommendation, imputation, variance-reduction]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Poisonous Imputation

Poisonous Imputation 指在 Doubly Robust 推荐去偏中,那些质量低劣、会显著放大偏差与方差的插补值(imputed values),它们如同"毒素"般损害去偏估计器的稳定性与准确性。

## 在本 wiki 中的出现

- [[2023-conservative-doubly-robust]]:该工作提出 Conservative Doubly Robust (CDR),通过审查插补值的均值与方差来识别并过滤掉 Doubly Robust 推荐去偏中的 "Poisonous Imputation",从而降低估计的偏差与方差,并提升整体推荐性能。在此语境下,Poisonous Imputation 是 CDR 所要诊断和剔除的核心问题对象。

## 相关

- [[doubly-robust-estimation]]
- [[2023-conservative-doubly-robust]]
- [[debiasing]]
- [[inverse-propensity-score]]
- [[recommender-systems|recommender-system]]
- [[bias-variance-tradeoff]]
