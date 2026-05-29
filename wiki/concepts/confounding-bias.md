---
type: concept
subtype: method
tags: [causal-inference, confounding, recommendation, bias]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Confounding Bias

Confounding Bias(混杂偏差)是指在因果推断中,由于存在同时影响处理变量(treatment)与结果变量(outcome)的混杂因子(confounder),导致对因果效应的估计出现系统性偏差的现象。

## 在本 wiki 中的出现

- [[2022-deep-causal-reasoning-for-recommendations]]:在该工作中,Confounding Bias 是推荐系统建模需要消除的核心问题。Deep-Deconf 使用深度 VAE 推断 substitute confounders,并将推荐问题建模为 MCMO(multi-cause multi-outcome)因果推断,从而消除混杂偏差并降低方差。
- [[2024-deconfound-release-interval-bias]]:将 release interval 识别为短视频推荐中的 confounder,提出模型无关的因果框架 LDRI,通过 backdoor adjustment 阻断后门路径并按视频自身 recency sensitivity 个性化去偏。
- [[2024-mitigating-dual-latent-confounding-biases]]:IViDR 联合工具变量(IV)与 identifiable VAE,同时缓解推荐系统中 item-feedback 与 exposure-feedback 两类潜在混淆偏差。

## 相关

- [[substitute-confounders|substitute-confounder]]
- [[causal-inference]]
- [[variational-autoencoder]]
- [[recommender-systems|recommendation-system]]
- [[deconfounding]]
- [[backdoor-adjustment]]
