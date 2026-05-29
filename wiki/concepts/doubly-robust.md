---
type: concept
subtype: method
tags: [causal-inference, recommendation, debiasing, doubly-robust, off-policy]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# Doubly Robust Learning

Doubly Robust (DR) Learning 是一类去偏估计方法,它同时结合倾向性得分(propensity score)模型与误差插补(imputation)模型,只要两者中至少有一个被正确指定,估计量即保持无偏(unbiased),因而具有"双重稳健"特性。

## 在本 wiki 中的出现

- [[2023-conservative-doubly-robust]]:该工作以 Doubly Robust 作为推荐系统去偏的基础框架,并指出 DR 在实践中容易受到"毒性插补"(poisonous imputation)的影响——即误差插补模型产生的高偏差、高方差插补值会损害去偏效果。其提出的 CDR(Conservative Doubly Robust)方法通过审查插补值的均值与方差来过滤这些毒性插补,从而降低估计的偏差与方差,并提升整体性能。
- [[2024-edt4rec-max-entropy-decision-transformer]]:EDT4Rec 给 Decision Transformer 加入最大熵探索与基于 CQL Q-function 的 reward relabeling,解决 offline RL 推荐中缺乏 stitching 能力和在线探索不足的问题。
- [[2025-debias-can-be-unreliable]]:揭示用随机曝光数据集传统评估去偏推荐不可靠,提出 URE 方案无偏估计全曝光数据上的 Recall@K。
- [[2025-multiscale-contextual-bandits-long-term]]:提出 MultiScale Policy Learning 框架与 MSBL 算法,用分层 off-policy contextual bandit 在多个时间尺度上协调短期反馈与长期目标,让低尺度数据作为高尺度稀疏数据的 PAC-Bayes 先验。
- [[2025-causality-constraint-debiasing-recommender]]:LCDR 用 identifiable VAE (iVAE) 作为因果约束去对齐标准 VAE 的潜在表征,即使 proxy variable 低质/有噪声也能恢复 latent confounder,从而缓解推荐系统中的潜在混杂偏差。

## 相关

- [[propensity-score]]
- [[inverse-propensity-scoring]]
- [[imputation-model]]
- [[recommendation-debiasing]]
- [[2023-conservative-doubly-robust]]
- [[2024-edt4rec-max-entropy-decision-transformer]]
