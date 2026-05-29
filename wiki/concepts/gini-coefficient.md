---
type: concept
subtype: method
tags: [fairness, metric, inequality, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Gini coefficient

基尼系数(Gini coefficient / Gini Index)是衡量分布不均衡程度的统计指标,取值在 0(完全平等)到 1(完全不平等)之间;在推荐系统中常用来度量曝光或互动在物品之间的集中程度,数值越低表示物品侧分配越公平。

## 在本 wiki 中的出现

- [[2026-proactive-guiding-item-side-fairness]]:HRL4PFG 用分层强化学习"主动引导"用户偏好逐步转向长尾物品,在 KuaiRec/KuaiRand 上同时取得最高累积奖励、最长交互长度与最低 Gini Index,在不牺牲满意度的前提下提升 item-side 公平。

## 相关

- [[item-side-fairness]]
- [[long-tail-recommendation]]
- [[hierarchical-reinforcement-learning]]
