---
type: concept
subtype: method
tags: [recommender-system, fairness, multi-stakeholder, exposure]
created: 2026-05-30
updated: 2026-05-30
sources: 8
---

# 物品侧公平 (Item-Side Fairness)

物品侧公平关注推荐系统对**被推荐对象**(item / 创作者 / 提供方)的公平待遇——典型如**曝光 (exposure)** 是否在创作者间合理分配,
而非只优化用户侧效用。它是**多边/多利益相关方公平 (multi-stakeholder fairness)** 的供给侧,与用户侧公平相对。

## 核心问题
- **曝光不均 / 马太效应**:热门 item 越推越热,长尾创作者拿不到曝光,损害生态可持续性(见 [[2023-dorl-matthew-effect-offline-rl-recommendation]])。
- **流量波动下的公平**:真实流量是动态的,静态配额会失效——[[2024-bankfair-fluctuating-traffic-reranking]]、[[2025-bankfair-plus-regret-aware-reranking]]
  在波动流量下做 regret-aware 重排。
- **生命周期公平**:item 在不同生命周期阶段需求不同,[[2025-lhrl-lifecycle-fairness-recommendation]] 用分层 RL 调控。
- **主动 item 侧公平**:[[2026-proactive-guiding-item-side-fairness]]。

## 实现位置
多数在 [[reranking|重排]]阶段以**约束/配额**或**公平正则**实现,常与 [[multi-objective-optimization|多目标优化]] 联立(公平 vs 用户效用的权衡);
也可在 RL 奖励中加入公平项。与三方 agent 框架 [[2026-trirec-tri-party-agent-recommendation]] 的"用户—物品—平台"建模相关。

## 相关页
[[recommender-systems]]、[[reranking]]、[[multi-objective-optimization]]、[[two-sided-fairness-reranking]]、[[user-creator-feature-polarization]]
