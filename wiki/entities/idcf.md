---
type: entity
subtype: model
tags: [recommendation, debiasing, causal-inference, proximal-causal-inference, confounding]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# iDCF

iDCF(identifiable Deconfounder)是一种用于推荐系统去混杂的方法,在存在未观测混杂变量时,借助代理变量与近端因果推断为反事实反馈提供可识别性保证。

## 在本 wiki 中的出现
- [[2024-mitigating-dual-latent-confounding-biases]]:IViDR 联合工具变量(IV)与 identifiable VAE,同时缓解推荐系统中 item-feedback 与 exposure-feedback 两类潜在混淆偏差。
- [[2025-policy-guided-causal-state-representation]]:PGCR,面向离线 RL 推荐的两阶段因果状态表示框架,用策略引导的因果特征选择隔离因果相关分量,再用 encoder 学习紧凑状态表示。
- [[2025-causality-constraint-debiasing-recommender]]:LCDR 用 identifiable VAE (iVAE) 作为因果约束去对齐标准 VAE 的潜在表征,即使 proxy variable 低质/有噪声也能恢复 latent confounder,从而缓解推荐系统中的潜在混杂偏差。
- [[identifiable-vae]]
- [[latent-confounder]]
- [[instrumental-variable]]
- [[debiasing-recommender]]
- [[causal-state-representation]]

- 在 [[2023-idcf-debiasing-recommendation]] 中作为核心方法被提出:利用代理变量(用户特征)与近端因果推断(proximal causal inference),在存在未观测混杂变量(unobserved confounders)的情形下,为推荐中的反事实反馈(counterfactual feedback)提供可识别性(identifiability)保证;实验在 Coat、Yahoo!R3、KuaiRand 数据集上优于现有去混杂方法。

## 相关

- [[proximal-causal-inference]]
- [[unobserved-confounders]]
- [[counterfactual-feedback]]
- [[debiasing-recommendation]]
- [[coat-dataset]]
- [[yahoo-r3-dataset]]
- [[kuairand-dataset]]
