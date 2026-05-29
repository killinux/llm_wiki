---
type: concept
subtype: method
tags: [recommendation, debiasing, doubly-robust, imputation]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# TDR

TDR(Toxic-imputation Doubly Robust,毒性插补 Doubly Robust)指 Doubly Robust 推荐去偏中那些插补误差异常、会放大偏差与方差的"毒性插补"(toxic imputation)值。

## 在本 wiki 中的出现

- [[2023-conservative-doubly-robust]]:该工作提出 CDR(Conservative Doubly Robust),通过审查插补值的均值与方差来识别并过滤掉这类毒性插补,从而降低 Doubly Robust 推荐去偏估计的偏差与方差,并提升推荐性能。

## 相关

- [[doubly-robust]]
- [[conservative-doubly-robust]]
- [[selection-bias]]
- [[debiasing-recommendation|recommendation-debiasing]]
- [[imputation]]
