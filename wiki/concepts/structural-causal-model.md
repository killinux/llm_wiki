---
type: concept
subtype: method
tags: [causal-inference, recommender-systems, debiasing]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Structural Causal Model

一种用结构方程与有向无环图(DAG)刻画变量间因果机制的形式化框架,通过显式建模每个变量如何由其直接原因(及外生噪声)生成,从而支持对干预(intervention)与反事实(counterfactual)进行推理。

## 在本 wiki 中的出现

- [[2023-causal-inference-for-recommendation]]:综述将 Structural Causal Model 作为引入因果推断的基础形式化工具之一,用它来表述推荐场景中的因果记号、假设与变量间结构关系,进而定义并估计干预效应、识别与消除各类偏差。
- [[2024-deconfound-release-interval-bias]]:将 release interval 识别为短视频推荐中的 confounder,提出模型无关的因果框架 LDRI,通过 backdoor adjustment 阻断后门路径并按视频自身 recency sensitivity 个性化去偏。
- [[2025-policy-guided-causal-state-representation]]:PGCR:面向离线 RL 推荐的两阶段因果状态表示框架,用策略引导的因果特征选择隔离因果相关分量,再用 encoder 学习紧凑状态表示。

## 相关

- [[causal-inference]]
- [[confounding-bias]]
- [[deconfounding]]
- [[multi-cause-confounders]]
- [[recommender-systems]]
- [[debiasing]]
