---
type: concept
subtype: method
tags: [recommender-systems, debiasing, doubly-robust, causal-inference, off-policy-evaluation]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# MRDR

**MRDR (More Robust Doubly Robust)** 是一种用于推荐系统去偏的 Doubly Robust 类估计方法,通过优化插补(imputation)模型以降低 DR 估计量的方差,从而获得相比标准 Doubly Robust 更鲁棒的去偏效果。

## 在本 wiki 中的出现

- [[2023-conservative-doubly-robust]]:MRDR 作为 Doubly Robust(DR)系列方法之一(与 DR-JL、DR-BIAS、TDR 并列)出现,既是 CDR 衡量"毒性插补"(poisonous imputation)比例的实测对象,也是 CDR 即插即用、加以改进的基线之一。CDR 通过审查插补值的均值与方差过滤毒性插补,在 MRDR 等方法上进一步降低偏差与方差并提升性能。

## 相关

- [[doubly-robust]]
- [[debiasing]]
- [[inverse-propensity-score]]
- [[off-policy-evaluation]]
- [[causal-inference]]
- [[recommender-systems]]
