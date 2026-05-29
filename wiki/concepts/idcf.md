---
type: concept
subtype: method
tags: [recommendation, causal-inference, confounding-bias, identifiable-vae, debiasing]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# iDCF

iDCF(identifiable Deconfounder)是一类借助可识别变分自编码器(identifiable VAE / iVAE)从代理变量中恢复潜在混淆因子,从而缓解推荐系统中潜在混杂偏差的因果去偏方法思路。

## 在本 wiki 中的出现

- [[2024-mitigating-dual-latent-confounding-biases]]:IViDR 联合工具变量(IV)与 identifiable VAE,同时缓解推荐系统中 item-feedback 与 exposure-feedback 两类潜在混淆偏差。
- [[2025-policy-guided-causal-state-representation]]:PGCR,面向离线 RL 推荐的两阶段因果状态表示框架,用策略引导的因果特征选择隔离因果相关分量,再用 encoder 学习紧凑状态表示。
- [[2025-causality-constraint-debiasing-recommender]]:LCDR 用 identifiable VAE (iVAE) 作为因果约束去对齐标准 VAE 的潜在表征,即使 proxy variable 低质/有噪声也能恢复 latent confounder,从而缓解推荐系统中的潜在混杂偏差。

## 相关

- [[identifiable-vae]]
- [[latent-confounder]]
- [[instrumental-variable]]
- [[debiasing-recommender]]
- [[causal-state-representation]]
