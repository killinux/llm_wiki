---
type: concept
subtype: method
tags: [recommendation, moe, multi-task, sparsity, scaling]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# HoME

HoME(Hierarchy of Multi-gate Experts)是一类面向多任务推荐的分层专家路由方法,通过对专家进行层次化组织与门控,在多任务、稀疏激活的场景下提升参数 scaling 的稳定性与效率。

## 在本 wiki 中的出现

- [[2026-smes-scalable-multi-task-expert-sparsity]]:SMES 是 Kuaishou 提出的可扩展稀疏 MoE 多任务推荐框架,用 progressive expert routing 与 multi-task load-balancing 解决多任务稀疏路由的 exploded activation 与 load skew,使参数 scaling 在工业延迟约束下带来稳定收益。

## 相关

- [[mixture-of-experts]]
- [[multi-task-learning]]
- [[expert-routing]]
- [[load-balancing]]
