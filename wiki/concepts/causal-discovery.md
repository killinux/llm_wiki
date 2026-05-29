---
type: concept
subtype: method
tags: [causal-inference, causal-discovery, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Causal Discovery

Causal discovery 指从观测数据中自动地推断变量之间的因果结构(如因果图/DAG 与因果方向),而非依赖人为预先给定的因果假设。

## 在本 wiki 中的出现

- [[2023-causal-inference-for-recommendation]]:这篇将因果推断引入推荐系统的系统综述,在梳理因果记号、假设、效应与估计方法的整体框架时,涉及如何确定变量间的因果关系。Causal discovery 在此作为获取因果结构的一种途径,与人为设定因果图的方式互补,为后续的效应估计、去偏与无偏推荐提供结构基础。
- [[2024-generative-agents-in-recommendation]]:Agent4Rec 用 1000 个 LLM 驱动的生成式 agent(含 profile/memory/action 模块)构建电影推荐用户模拟器,探究其能否忠实模拟真实用户行为并复现 filter bubble 与 popularity bias。
- [[2024-causal-discovery-recommender-systems]]:以 KuaiRand 数据集为例,用 Hill-Climbing + 先验知识从观测数据学习推荐系统的因果图,结果显示只有 video duration 与 upload type 等少数变量真正影响用户反馈,反思"特征越多越好"的建模趋势。

## 相关

- 上位领域:[[causal-inference]]
- 结构表示:[[causal-graph]]、[[directed-acyclic-graph]]、[[structural-causal-model]]
- 与 [[confounding-bias]] 的处理相关:识别 confounder 依赖于已知或推断出的因果结构
- 估计与去偏方法:[[backdoor-adjustment]]、[[inverse-propensity-weighting]]
- 应用场景:推荐系统中的 [[uplift-modeling]]、无偏推荐与鲁棒性
