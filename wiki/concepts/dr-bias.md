---
type: concept
subtype: method
tags: [debiasing, doubly-robust, recommendation, bias-variance]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# DR-BIAS

DR-BIAS 是 Doubly Robust (DR) 推荐去偏框架中用于刻画与控制偏差的方法/指标,关注 DR 估计在存在不准确插补值(imputation)时所产生的偏差及其与方差之间的权衡。

## 在本 wiki 中的出现

- [[2023-conservative-doubly-robust]]:在 Conservative Doubly Robust (CDR) 方法的语境下,DR-BIAS 体现为 Doubly Robust 推荐去偏中由"毒性插补"(toxic imputation)带来的偏差。CDR 通过审查插补值的均值与方差来过滤这类毒性插补,从而降低偏差与方差并提升推荐性能。

## 相关

- [[doubly-robust]]
- [[conservative-doubly-robust]]
- [[poisonous-imputation]]
- [[debiasing]]
- [[dr-jl]]
- [[mrdr]]
- [[tdr]]
