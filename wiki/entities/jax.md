---
type: entity
subtype: product
tags: [jax, autodiff, machine-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# JAX

JAX 是一个用于高性能数值计算与机器学习的 Python 库,核心能力是自动微分(autodiff)以及 JIT 编译、向量化和并行化等可组合的函数变换。

## 在本 wiki 中的出现

- [[2026-automatic-laplace-collapsed-sampling]]:ALCS 用自动微分把高维隐变量在每次 likelihood 评估时坍缩为 MAP+Laplace 标量贡献,使 nested sampling 只在低维超参数空间运行,把 Bayesian evidence 计算扩展到 d_z~25,600。

## 相关

- [[automatic-laplace-collapsed-sampling]]
- [[nested-sampling]]
- [[automatic-differentiation]]
- [[bayesian-evidence]]
