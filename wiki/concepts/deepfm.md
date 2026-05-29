---
type: concept
subtype: method
tags: [recommendation, ctr-prediction, factorization-machine, deep-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# DeepFM

DeepFM 是一种用于 CTR 预估的端到端推荐模型,将因子分解机(FM)与深度神经网络(DNN)结合,共享同一套特征嵌入,从而同时建模低阶与高阶特征交互,无需人工特征工程。

## 在本 wiki 中的出现

- [[2023-video-length-debiasing-microvideo-rec]]:VLDRec 通过 play-progress 去偏标注、视频长度条件采样与多任务学习缓解微视频推荐中长视频被偏好的 video-length bias,以 NFM 为基座在 View_Time@120 上较最佳基线提升 1.81%(Kuaishou)与 11.32%(WeChat)。
- [[2024-bi-level-user-modeling-deep-recommenders]]:GPRec 提出即插即用的双层用户建模:用可学习分类器与双向(正/负)群体嵌入做群体建模,从 ID 类特征提炼个体偏好并以正交损失解耦,在 ML1M/TenRec/KuaiRand 上稳定提升各类 DRS 主干(含 DeepFM 等)的 CTR 预测。
- [[2025-causality-constraint-debiasing-recommender]]:LCDR 用 identifiable VAE (iVAE) 作为因果约束去对齐标准 VAE 的潜在表征,即使 proxy variable 低质/有噪声也能恢复 latent confounder,从而缓解推荐系统中的潜在混杂偏差。

## 相关

- [[factorization-machine]]
- [[nfm]]
- [[ctr-prediction]]
- [[microvideo-recommendation]]
- [[2024-bi-level-user-modeling-deep-recommenders]]
- [[2025-causality-constraint-debiasing-recommender]]
