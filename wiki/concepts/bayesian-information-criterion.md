---
type: concept
subtype: method
tags: [model-selection, statistics, causal-discovery, scoring]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Bayesian Information Criterion

贝叶斯信息准则(BIC)是一种用于模型选择的评分准则,在拟合优度的基础上对模型参数数量施加惩罚,从而在解释力与复杂度之间取得平衡,常被用作结构学习(如因果图发现)中评价候选结构的打分函数。

## 在本 wiki 中的出现

- [[2024-causal-discovery-recommender-systems]]:以 KuaiRand 数据集为例,用 Hill-Climbing + 先验知识从观测数据学习推荐系统的因果图,结果显示只有 video duration 与 upload type 等少数变量真正影响用户反馈,反思"特征越多越好"的建模趋势。

## 相关

- [[hill-climbing]]
- [[causal-discovery]]
- [[model-selection]]
- [[akaike-information-criterion]]
