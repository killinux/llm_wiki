---
type: concept
subtype: method
tags: [recommendation, debiasing, doubly-robust, imputation]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# DR-JL

DR-JL(Doubly Robust Joint Learning)是一种推荐系统去偏方法,通过联合学习插补模型与倾向得分模型,在 Doubly Robust 框架下同时估计缺失数据的偏差。

## 在本 wiki 中的出现

- [[2023-conservative-doubly-robust]]:作为 Doubly Robust 推荐去偏的代表性基线/前置方法出现。该论文提出 CDR,通过审查插补值(imputation)的均值与方差来过滤其中的"毒性插补",从而在 Doubly Robust 去偏(包括 DR-JL 这类联合学习方法)中降低偏差与方差并提升性能。

## 相关

- [[doubly-robust]]
- [[2023-conservative-doubly-robust]]
- [[propensity-score]]
- [[imputation]]
- [[debiasing-recommendation|recommendation-debiasing]]
