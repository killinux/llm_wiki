---
type: concept
subtype: method
tags: [causal-inference, graphical-models, feature-selection, bayesian-network]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Markov Blanket

在一个图模型(如贝叶斯网络)中,某个节点的 Markov Blanket 是使该节点与图中所有其他节点条件独立的最小变量集合,通常由它的父节点、子节点以及子节点的其他父节点组成。

## 在本 wiki 中的出现

- [[2024-causal-discovery-recommender-systems]]:以 KuaiRand 数据集为例,用 Hill-Climbing + 先验知识从观测数据学习推荐系统的因果图,结果显示只有 video duration 与 upload type 等少数变量真正影响用户反馈,反思"特征越多越好"的建模趋势。

## 相关

- [[markov-equivalence-class]]
- [[causal-discovery]]
- [[bayesian-network]]
- [[feature-selection]]
- [[hill-climbing]]
