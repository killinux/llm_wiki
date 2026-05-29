---
type: concept
subtype: method
tags: [bayesian-inference, evidence, monte-carlo, sampling]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Nested Sampling

Nested Sampling 是一种 Monte Carlo 算法,通过将多维后验积分重参数化为关于先验体积的一维积分,主要用于估计 Bayesian evidence(模型证据),同时也能产生后验样本。

## 在本 wiki 中的出现

- [[2026-automatic-laplace-collapsed-sampling]]:ALCS 用自动微分把高维隐变量在每次 likelihood 评估时坍缩为 MAP+Laplace 标量贡献,使 nested sampling 只在低维超参数空间运行,把 Bayesian evidence 计算扩展到 d_z~25,600。

## 相关

- [[bayesian-evidence]]
- [[laplace-approximation]]
- [[automatic-differentiation]]
- [[map-estimation]]
