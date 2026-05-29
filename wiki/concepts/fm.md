---
type: concept
subtype: method
tags: [recommendation, feature-interaction, eeg, affective-computing]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# FM

FM(Factorization Machine,因子分解机)是一种通过特征隐向量内积来建模二阶特征交互的通用预测模型,常用于推荐系统中的点击率/参与度预测等稀疏特征场景。

## 在本 wiki 中的出现

- [[2024-eeg-svrec-eeg-affective-engagement-dataset]]:首个在真实短视频观看场景下采集 EEG 脑电信号并配以六维情感参与度标注(MAES)与行为日志的推荐数据集,benchmark 显示加入 EEG 特征可提升推荐 AUC。
- [[2025-causality-constraint-debiasing-recommender]]:LCDR 用 identifiable VAE (iVAE) 作为因果约束去对齐标准 VAE 的潜在表征,即使 proxy variable 低质/有噪声也能恢复 latent confounder,从而缓解推荐系统中的潜在混杂偏差。

## 相关

- [[recommendation-system]]
- [[ctr-prediction]]
- [[eeg]]
- [[affective-engagement]]
