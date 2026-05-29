---
type: concept
subtype: method
tags: [generative-model, latent-variable, variational-inference, deep-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Variational Autoencoder

Variational Autoencoder(VAE)是一种基于变分推断的深度生成模型,用 encoder 将输入数据映射到隐变量(latent variable)的近似后验分布,再由 decoder 从该隐空间采样并重建数据,从而学习数据的概率生成过程。

## 在本 wiki 中的出现

- [[2022-deep-causal-reasoning-for-recommendations]]:该工作的 Deep-Deconf 方法使用深度 VAE 来推断 substitute confounders(替代混杂变量),将推荐建模为 MCMO(multi-cause multi-outcome)因果推断问题,从而消除混杂偏差并降低估计方差。VAE 在此作为隐变量推断工具,用于从观测的多因暴露中恢复潜在的混杂结构。

## 相关

- [[deconfounding]]
- [[multi-cause-confounders]]
- [[confounding-bias]]
- [[causal-inference]]
- [[deep-deconf]]
- [[deconfounder]]
- [[ivae]]
- [[collaborative-filtering]]
