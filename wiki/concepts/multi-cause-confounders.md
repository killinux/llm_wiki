---
type: concept
subtype: method
tags:
  - causal-inference
  - confounders
  - latent-variable
  - recommendation
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Substitute Confounders / Multi-cause Confounders

Substitute Confounders(替代混杂因子)指在存在多个 cause(多原因)的因果推断场景中,用一个推断出来的 latent variable 去代理那些未观测到的混杂因子(unobserved confounders),从而在无法直接观测真实混杂因子时仍能近似地进行 deconfounding(去混杂)。

## 在本 wiki 中的出现

- [[2022-deep-causal-reasoning-for-recommendations]]:提出 Deep-Deconf,使用深度 VAE 从数据中推断 substitute confounders,并把推荐问题建模为 MCMO(Multiple-Cause-Multiple-Outcome)因果推断,以消除混杂偏差(confounding bias)并降低估计方差。在该工作中,substitute confounders 充当未观测混杂因子的替身,使得 backdoor 类校正得以在推荐场景中落地。

## 相关

- [[deconfounding]]
- [[variational-autoencoder]]
- [[causal-inference]]
- [[confounding-bias]]
- [[backdoor-adjustment]]
- [[multiple-cause-multiple-outcome]]
- [[2022-deep-causal-reasoning-for-recommendations]]
