---
type: concept
subtype: method
tags: [recommender-system, multi-domain, multi-scenario, transfer-learning, multi-task-learning]
created: 2026-05-30
updated: 2026-05-30
sources: 9
---

# 多域推荐 (Multi-Domain / Multi-Scenario Recommendation)

多域推荐指用**统一模型**同时服务多个业务域 / 场景(如首页 feed、搜索、详情页猜你喜欢、不同 App tab),共享跨域的共性知识、
又保留各域特性,以避免为每个域单独建模带来的维护成本与数据稀疏。

## 核心挑战
- **域间分布差异**:不同场景的用户意图、item 分布、反馈密度差异大;
- **负迁移 (negative transfer)**:简单共享参数会让强势域淹没弱势域;
- **共享-特化平衡**:既要迁移共性,又要保留域专属信号。

## 方法谱系
- **共享底座 + 域专属塔**:借鉴 [[multi-task-learning]] 的 MMoE/PLE/STAR 思路,把"任务"换成"域"。
- **域不变 + 域特定信息分解**:[[2024-diit-domain-invariant-information-transfer]] 显式拆分域不变 / 域特定表示做迁移。
- **大规模多域**:[[2024-dfei-large-scale-multi-domain-recommendation]] 面向工业级多域;[[2024-scenario-wise-rec]]、
  [[2023-hierrec-scenario-aware-hierarchical-dynamic-network]] 按场景做层次化动态网络;[[2601-dsmoe-scenario-adaptive-moe-matching]] 用场景自适应 MoE。
- **统一用户兴趣建模**:[[2025-cross-scenario-unified-user-interest-modeling-red-rec]]、[[2025-perscen-multi-scenario-matching]] 跨场景对齐用户表示。

## 与相邻概念
是 [[personalization|个性化]]在"场景维度"的展开;与 [[multi-objective-optimization|多目标]](不同域常有不同目标)、
[[representation-learning|表示学习]](跨域共享表示)交叉。

## 相关页
[[recommender-systems]]、[[multi-task-learning]]、[[personalization]]、[[mmoe]]、[[representation-learning]]
