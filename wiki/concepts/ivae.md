---
type: concept
subtype: method
tags: [VAE, identifiability, causal-inference, latent-confounder, recommender-debiasing]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# identifiable VAE (iVAE)

identifiable VAE (iVAE) 是一种在辅助变量(如标签、proxy、工具变量)条件下学习潜在表征的变分自编码器,通过对潜变量先验施加条件可识别性约束,使其能够在理论保证下恢复出真实的潜在因子(包括潜在混杂因子)。

## 在本 wiki 中的出现

- [[2024-mitigating-dual-latent-confounding-biases]]:IViDR 联合工具变量(IV)与 identifiable VAE,同时缓解推荐系统中 item-feedback 与 exposure-feedback 两类潜在混淆偏差。
- [[2025-causality-constraint-debiasing-recommender]]:LCDR 用 identifiable VAE (iVAE) 作为因果约束去对齐标准 VAE 的潜在表征,即使 proxy variable 低质/有噪声也能恢复 latent confounder,从而缓解推荐系统中的潜在混杂偏差。

## 相关

- [[vae]]
- [[latent-confounder]]
- [[instrumental-variable]]
- [[recommender-debiasing]]
- [[causal-inference]]
