---
type: concept
subtype: method
tags: [automatic-differentiation, gradients, optimization, bayesian-inference]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Automatic Differentiation

自动微分(Automatic Differentiation, AD)是一类通过对程序中的基本运算链式求导、从而精确(到机器精度)计算函数梯度的技术,介于符号微分与数值差分之间。

## 在本 wiki 中的出现

- [[2026-automatic-laplace-collapsed-sampling]]:ALCS 用自动微分把高维隐变量在每次 likelihood 评估时坍缩为 MAP+Laplace 标量贡献,使 nested sampling 只在低维超参数空间运行,把 Bayesian evidence 计算扩展到 d_z~25,600。

## 相关

- [[laplace-approximation]]
- [[nested-sampling]]
- [[bayesian-evidence]]
- [[gradient-based-optimization]]
