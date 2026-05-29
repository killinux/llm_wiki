---
type: entity
subtype: model
tags: [causal-inference, recommendation, debiasing, confounder, counterfactual]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Deconfounder

Deconfounder 是一类用于在存在未观测混杂变量(unobserved confounder)的情况下,通过对混杂因素进行建模或调整以获得无偏因果效应估计的方法,在推荐系统去偏(debiasing)中常用于校正反馈数据中的混杂偏差。

## 在本 wiki 中的出现
- [[2024-mitigating-dual-latent-confounding-biases]]:IViDR 联合工具变量(IV)与 identifiable VAE,同时缓解推荐系统中 item-feedback 与 exposure-feedback 两类潜在混淆偏差。
- [[2025-causality-constraint-debiasing-recommender]]:LCDR 用 identifiable VAE (iVAE) 作为因果约束去对齐标准 VAE 的潜在表征,即使 proxy variable 低质/有噪声也能恢复 latent confounder,从而缓解推荐系统中的潜在混杂偏差。
- [[latent-confounder]]
- [[identifiable-vae]]
- [[instrumental-variable]]
- [[recommender-debiasing]]

- [[2023-idcf-debiasing-recommendation]]:该工作针对推荐反事实反馈中的未观测混杂变量问题,提出 iDCF(identifiable Deconfounder)。它借助代理变量(用户特征)与近端因果推断(proximal causal inference),在存在未观测混杂变量时为反事实反馈提供可识别性(identifiability)保证,从而扩展并改进了已有的 Deconfounder 类去混杂方法,并在 Coat、Yahoo!R3、KuaiRand 等数据集上优于现有去混杂方法。

## 相关

- [[2023-idcf-debiasing-recommendation]]
- [[proximal-causal-inference]]
- [[unobserved-confounder]]
- [[proxy-variable]]
- [[counterfactual-feedback]]
- [[recommendation-debiasing]]
- [[causal-inference]]
