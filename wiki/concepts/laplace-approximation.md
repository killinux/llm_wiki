---
type: concept
subtype: method
tags: [bayesian-inference, approximation, gaussian, marginalization]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Laplace Approximation

拉普拉斯近似是一种用以 MAP(最大后验)点为中心的高斯分布来逼近概率分布(通常是后验分布)的方法,通过在峰值处对对数密度做二阶泰勒展开,从而得到积分(如归一化常数/证据)的解析近似。

## 在本 wiki 中的出现

- [[2026-automatic-laplace-collapsed-sampling]]:ALCS 用自动微分把高维隐变量在每次 likelihood 评估时坍缩为 MAP+Laplace 标量贡献,使 nested sampling 只在低维超参数空间运行,把 Bayesian evidence 计算扩展到 d_z~25,600。

## 相关

- [[bayesian-evidence]]
- [[nested-sampling]]
- [[automatic-differentiation]]
- [[map-estimation]]
- [[marginal-likelihood]]
