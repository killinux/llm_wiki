---
type: entity
subtype: model
tags: [model, recommendation, causal-inference, deconfounding, matrix-factorization]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Deconf-MF

Deconf-MF(Deconfounded Recommender)是一种用浅层 Poisson 矩阵分解推断 substitute confounders、以消除推荐中隐藏混杂偏差的去混杂推荐模型。

## 在本 wiki 中的出现

- [[2022-deep-causal-reasoning-for-recommendations]]:作为前人工作与基线出现。Deconf-MF 用浅层 Poisson 矩阵分解推断 substitute confounders 来去混杂,但因建模能力不足,无法捕捉非线性的 item co-exposure 关系,并退化为忽略 item co-recommendation 效应的 single-cause 情形;该文提出的 Deep-Deconf 用深度 VAE 推断 substitute confounders、把推荐建模为 MCMO(multi-cause multi-outcome)因果推断以消除混杂偏差并降低方差,在 simulated、ML-causal、VG-causal 上均优于 Deconf-MF 基线。

## 相关

- [[matrix-factorization]]
- [[substitute-confounders]]
- [[causal-inference]]
- [[deconfounding]]
- [[collaborative-filtering]]
- [[confounding-bias]]
