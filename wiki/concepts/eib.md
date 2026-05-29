---
type: concept
subtype: method
tags: [debiasing, doubly-robust, recommendation, imputation]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# EIB

EIB(Error Imputation Based)是一类去偏方法,通过为缺失/未观测反馈估计预测误差(imputed errors)来纠正推荐系统中的选择偏差。

## 在本 wiki 中的出现

- 在 [[2023-conservative-doubly-robust]] 中,EIB 作为 Doubly Robust(DR)去偏框架所依赖的插补(imputation)组成部分出现:DR 把 EIB 的误差插补与倾向性加权(IPS)结合起来以同时降低偏差与方差。该论文指出此类插补值中可能存在"毒性插补"(toxic imputation),并提出 CDR 通过审查插补值的均值与方差来过滤这些有害插补,从而进一步降低偏差与方差并提升性能。

## 相关

- [[doubly-robust]]
- [[ips]]
- [[2023-conservative-doubly-robust]]
- [[selection-bias]]
- [[debiasing-recommendation|recommendation-debiasing]]
