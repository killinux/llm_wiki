---
type: entity
subtype: dataset
tags: [recommendation, dataset, debiasing, doubly-robust]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# KuaiRand-Pure

KuaiRand-Pure 是用于推荐系统去偏研究的公开数据集,其中包含在随机曝光场景下采集的用户反馈,常作为评估无偏推荐与去偏方法的基准。

## 在本 wiki 中的出现

- [[2023-conservative-doubly-robust]]:作为实验数据集,用于评估 CDR(Conservative Doubly Robust)方法。该工作提出通过审查插补值(imputation)的均值与方差来过滤 Doubly Robust 推荐去偏中的"毒性插补",从而降低偏差与方差并提升性能。
- [[2023-kuaisim-recommender-simulator]]:面向推荐系统的综合性用户模拟器,提供 multi-behavior 与 cross-session 反馈,统一支持 request 级 list-wise、whole-session 级 sequential 与 cross-session 级 retention 三类 RL 推荐任务并配套 benchmark。

## 相关

- [[2023-conservative-doubly-robust]]
- [[doubly-robust]]
- [[recommendation-debiasing]]
- [[2023-kuaisim-recommender-simulator]]
- [[user-simulator]]
