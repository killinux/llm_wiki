---
type: concept
subtype: method
tags: [causal-inference, recommender-systems, latent-confounder, vae, debiasing]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# deconfounder

一种因果推断方法,通过推断/恢复潜在混淆因子(latent confounder)并加以控制,从而消除观测数据中混淆变量带来的偏差。

## 在本 wiki 中的出现

- [[2024-mitigating-dual-latent-confounding-biases]]:IViDR 联合工具变量(IV)与 identifiable VAE,同时缓解推荐系统中 item-feedback 与 exposure-feedback 两类潜在混淆偏差。
- [[2025-causality-constraint-debiasing-recommender]]:LCDR 用 identifiable VAE (iVAE) 作为因果约束去对齐标准 VAE 的潜在表征,即使 proxy variable 低质/有噪声也能恢复 latent confounder,从而缓解推荐系统中的潜在混杂偏差。

## 相关

- [[latent-confounder]]
- [[identifiable-vae]]
- [[instrumental-variable]]
- [[recommender-debiasing]]
