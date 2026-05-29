---
type: entity
subtype: dataset
tags: [recommendation, dataset, debiasing, doubly-robust]
created: 2026-05-29
updated: 2026-05-29
sources: 6
---

# KuaiRand-Pure

KuaiRand-Pure 是用于推荐系统去偏研究的公开数据集,其中包含在随机曝光场景下采集的用户反馈,常作为评估无偏推荐与去偏方法的基准。

## 在本 wiki 中的出现

- [[2023-conservative-doubly-robust]]:作为实验数据集,用于评估 CDR(Conservative Doubly Robust)方法。该工作提出通过审查插补值(imputation)的均值与方差来过滤 Doubly Robust 推荐去偏中的"毒性插补",从而降低偏差与方差并提升性能。
- [[2023-kuaisim-recommender-simulator]]:面向推荐系统的综合性用户模拟器,提供 multi-behavior 与 cross-session 反馈,统一支持 request 级 list-wise、whole-session 级 sequential 与 cross-session 级 retention 三类 RL 推荐任务并配套 benchmark。
- [[2024-causal-discovery-recommender-systems]]:以 KuaiRand 数据集为例,用 Hill-Climbing + 先验知识从观测数据学习推荐系统的因果图,结果显示只有 video duration 与 upload type 等少数变量真正影响用户反馈,反思"特征越多越好"的建模趋势。
- [[2025-multi-objective-controllable-decision-transformer]]:提出 MocDT,一种基于 Decision Transformer 的离线 RL 推荐方法,把未来多目标作为控制信号,在推理阶段自回归生成对齐指定目标(累积评分与多样性)的物品序列,无需重训。
- [[2025-perscen-multi-scenario-matching]]:首个将用户个性化建模引入多场景匹配(召回)的两塔方法,用 user-specific 特征图+轻量 GNN、向量量化的场景偏好与渐进式 GLU,在 KuaiRand-Pure 与 Alimama 上以高效率刷新召回性能。
- [[2025-tadt-csa-temporal-advantage-decision-transformer]]:面向工业生成式推荐的 Decision Transformer 改进框架,用 Temporal Advantage 信号和对比式状态抽象解决 DT 的轨迹拼接弱与状态空间过大问题。

## 相关

- [[2023-conservative-doubly-robust]]
- [[doubly-robust]]
- [[recommendation-debiasing]]
- [[2023-kuaisim-recommender-simulator]]
- [[user-simulator]]
- [[decision-transformer]]
- [[offline-reinforcement-learning]]
- [[causal-discovery]]
- [[alimama-dataset]]
