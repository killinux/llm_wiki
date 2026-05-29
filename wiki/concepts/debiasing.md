---
type: concept
subtype: method
tags: [debiasing, recommendation, unbiased-data, exploration]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Debiasing

Debiasing(去偏)是指在推荐、排序等系统中识别并消除由记录数据采集方式引入的系统性偏差(如曝光偏差、流行度偏差),从而获得能反映用户真实偏好的无偏信号,提升模型与系统的长期质量。

## 在本 wiki 中的出现

- [[2025-where-to-explore-reach-cost-aware-unbiased-data]]:提出按用户 scroll-depth 触发、低成本高触达的专用 UI 行("Something Completely Different")来交付随机化探索内容,在不损害短期参与度的前提下大规模收集无偏交互数据,并回灌候选生成提升长期推荐质量(线上 +0.94% 参与度,无偏数据 Gini 0.203 vs 0.494)。

## 相关

- [[exploration-exploitation]]
- [[exposure-bias]]
- [[recommender-systems|recommendation-systems]]
- [[unbiased-learning-to-rank]]
