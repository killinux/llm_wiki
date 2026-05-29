---
type: entity
subtype: model
tags: [recommendation, ranking, scaling, moe]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# RankMixer

RankMixer 是一种面向工业推荐排序场景的可扩展模型架构,旨在在严格的在线延迟约束下,通过参数 scaling 获得稳定的效果收益。

## 在本 wiki 中的出现

- [[2026-smes-scalable-multi-task-expert-sparsity]]:SMES 是 Kuaishou 提出的可扩展稀疏 MoE 多任务推荐框架,用 progressive expert routing 与 multi-task load-balancing 解决多任务稀疏路由的 exploded activation 与 load skew,使参数 scaling 在工业延迟约束下带来稳定收益。

## 相关

- [[smes-scalable-multi-task-expert-sparsity]]
- [[mixture-of-experts]]
- [[recommendation-ranking]]
