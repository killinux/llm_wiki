---
type: concept
subtype: method
tags: [recommendation, debiasing, doubly-robust, imputation, variance-reduction]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Conservative Doubly Robust (CDR)

Conservative Doubly Robust (CDR) 是一种用于推荐系统去偏的方法,它在 Doubly Robust (DR) 框架基础上,通过审查插补值(imputation)的均值与方差来过滤"毒性插补"(poisonous imputation),从而降低估计量的偏差与方差并提升推荐性能。

## 在本 wiki 中的出现

- [[2023-conservative-doubly-robust]]:提出 CDR。该工作指出 Doubly Robust 推荐去偏中存在"毒性插补"会损害估计质量,CDR 通过审查插补值的均值与方差对这些插补进行过滤,降低偏差方差并提升性能。

## 相关

- [[doubly-robust]]:CDR 在 DR 估计量基础上构建,是对其的保守化改进。
- [[debiasing-recommendation|recommendation-debiasing]]:CDR 所要解决的总体问题领域。
- [[inverse-propensity-scoring]]:DR/去偏推荐中与插补互补的另一类估计手段。
- [[variance-reduction]]:CDR 的核心收益之一来自对估计量方差的控制。
