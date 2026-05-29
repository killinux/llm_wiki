---
type: concept
subtype: method
tags: [missing-data, causal-inference, recommendation, unbiased-data, statistics]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Missing at random

Missing at random (MAR) 指数据的缺失机制只依赖于已观测到的变量,而不依赖于缺失值本身,因而在条件于观测变量后缺失是"随机"的——这与推荐系统中常见的"非随机缺失"(MNAR,如用户只与被曝光/感兴趣的内容交互)形成对照。

## 在本 wiki 中的出现

- [[2025-where-to-explore-reach-cost-aware-unbiased-data]]:提出按用户 scroll-depth 触发、低成本高触达的专用 UI 行("Something Completely Different")来交付随机化探索内容,在不损害短期参与度的前提下大规模收集无偏交互数据,并回灌候选生成提升长期推荐质量(线上 +0.94% 参与度,无偏数据 Gini 0.203 vs 0.494)。

## 相关

- [[selection-bias]]
- [[exploration-exploitation]]
- [[unbiased-data-collection]]
- [[recommender-systems]]
