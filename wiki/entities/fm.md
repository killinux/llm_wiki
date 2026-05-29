---
type: entity
subtype: model
tags: [recommendation, watch-time, debiasing, causal-inference]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# FM

FM(Factorization Machine,因子分解机)是一类通过特征隐向量的内积来建模特征之间二阶交互的预测模型,常用于推荐与点击/时长预估等任务。

## 在本 wiki 中的出现
- [[2024-eeg-svrec-eeg-affective-engagement-dataset]]:首个在真实短视频观看场景下采集 EEG 脑电信号并配以六维情感参与度标注(MAES)与行为日志的推荐数据集,benchmark 显示加入 EEG 特征可提升推荐 AUC。
- [[2025-causality-constraint-debiasing-recommender]]:LCDR 用 identifiable VAE (iVAE) 作为因果约束去对齐标准 VAE 的潜在表征,即使 proxy variable 低质/有噪声也能恢复 latent confounder,从而缓解推荐系统中的潜在混杂偏差。
- [[recommender-systems|recommendation-system]]
- [[eeg]]
- [[affective-engagement]]

- 在 [[2023-d2co-watch-time-debias]] 中,FM 作为视频推荐中观看时长预估的基础模型之一出现。该论文提出 D²Co,从统一的因果视角同时矫正观看时长的时长偏差(duration bias)与噪声观看(noisy watching),以还原用户的真实兴趣;FM 在这一背景下作为可被该去偏框架应用的预估模型出现。
- [[2024-feature-level-bias-ctr]]:自上而下分析揭示 CTR 模型的 feature-level bias 主要源自线性部分,并提出移除/重建线性权重的极简非侵入式去偏策略。

## 相关

- [[d2co]]
- [[watch-time-prediction]]
- [[duration-bias]]
- [[noisy-watching]]
- [[video-recommendation]]
- [[causal-inference]]
- [[ctr-prediction]]
- [[feature-level-bias]]
