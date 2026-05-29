---
type: concept
subtype: method
tags: [causal-inference, debiasing, recommendation, propensity]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Inverse Propensity Score

Inverse Propensity Score(IPS,逆倾向分数)是一种基于倾向分数(propensity score)倒数对观测样本进行重加权的方法,用于校正非随机缺失/曝光机制带来的选择偏差,从而对感兴趣的目标量做出无偏估计。

## 在本 wiki 中的出现

- [[2023-data-heterogeneity-recommendation]]:该论文提出双层聚类方法 BHE,显式挖掘推荐数据中的预测机制异质性与协变量分布异质性,用于多子模型预测与去偏。IPS 在此作为推荐系统去偏的经典基线/技术背景出现——通过倾向分数加权来缓解曝光偏差,论文工作可视为在异质性建模视角下对这一去偏范式的补充与改进(在 Yelp/MovieLens-1M 上 NFM 骨干 NDCG@20 从 14.01 提升到 22.57)。
- [[2023-conservative-doubly-robust]]:该论文提出 CDR,通过审查插补值(imputation)的均值与方差过滤 Doubly Robust 推荐去偏中的"毒性插补"。IPS 在此是 Doubly Robust(DR)估计器的两大组成之一——DR 将 IPS 的倾向加权项与 imputation 模型结合,以降低单独使用 IPS 时的高方差;CDR 即针对该框架中的插补质量做保守化改进,从而降低偏差方差并提升性能。
- [[2024-feature-level-bias-ctr]]:自上而下分析揭示 CTR 模型的 feature-level bias 主要源自线性部分,并提出移除/重建线性权重的极简非侵入式去偏策略。

## 相关

- [[debiasing]]
- [[exposure-bias]]
- [[off-policy-evaluation]]
- [[inverse-propensity-scoring]]
- [[recommender-system]]
- [[doubly-robust]]
- [[2023-conservative-doubly-robust]]
- [[2023-data-heterogeneity-recommendation]]
