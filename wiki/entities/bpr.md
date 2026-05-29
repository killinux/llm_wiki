---
type: entity
subtype: model
tags: [recommendation, ranking, collaborative-filtering]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# BPR

BPR(Bayesian Personalized Ranking,贝叶斯个性化排序)是一种面向隐式反馈的成对排序优化方法,常被用作推荐系统中协同过滤模型的训练目标与基线。

## 在本 wiki 中的出现

- [[2023-agentcf-collaborative-learning-agents-recsys]]:把推荐系统中的用户和物品都建模为 LLM agent,通过自主交互与协同反思实现无梯度的协同过滤式优化。
- [[2025-pub-personality-user-behaviour-simulator]]:PUB 是基于 LLM 的用户行为模拟器,将 Big Five 人格特质嵌入用户建模,从行为日志推断人格并生成高保真合成交互,用于推荐系统的离线评估(BPR 作为相关推荐排序方法语境出现)。

## 相关

- [[collaborative-filtering]]
- [[recommendation-system]]
- [[implicit-feedback]]
