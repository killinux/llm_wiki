---
type: concept
subtype: method
tags: [causal-inference, debiasing, recommendation, confounder]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# backdoor adjustment

后门调整(backdoor adjustment)是因果推断中的一种方法,通过对满足后门准则的混淆变量进行条件化与边缘化,阻断处理变量与结果之间的后门路径,从而估计无偏的因果效应。

## 在本 wiki 中的出现

- [[2024-deconfound-release-interval-bias]]:将 release interval 识别为短视频推荐中的 confounder,提出模型无关的因果框架 LDRI,通过 backdoor adjustment 阻断后门路径并按视频自身 recency sensitivity 个性化去偏。
- [[2025-causality-constraint-debiasing-recommender]]:LCDR 用 identifiable VAE (iVAE) 作为因果约束去对齐标准 VAE 的潜在表征,即使 proxy variable 低质/有噪声也能恢复 latent confounder,从而缓解推荐系统中的潜在混杂偏差。

## 相关

- [[confounder]]
- [[causal-inference]]
- [[debiasing]]
