---
type: concept
subtype: method
tags: [recommender-system, fairness, multi-stakeholder, debiasing]
created: 2026-05-30
updated: 2026-05-30
sources: 9
---

# 推荐公平性 (Recommendation Fairness)

推荐公平性研究推荐系统是否对**各方主体**(用户、物品/创作者、提供方/平台)以及**敏感群体**给予公平待遇。
它是多边市场的核心议题:单纯优化用户侧效用会系统性损害创作者生态与弱势群体。

## 两侧 / 多边
- **用户侧公平 (user-side)**:不同用户群(性别、活跃度、地域)是否获得同等质量的推荐;缺标签下的公平见 [[2024-fairness-recommendation-missing-labels]]。
- **物品侧公平 (item-side)**:创作者/物品的**曝光分配**——见 [[item-side-fairness]],典型工作 [[2024-bankfair-fluctuating-traffic-reranking]]、
  [[2025-bankfair-plus-regret-aware-reranking]]、[[2026-proactive-guiding-item-side-fairness]]。
- **多边 / 三方**:用户—物品—平台联合权衡,[[2026-trirec-tri-party-agent-recommendation]]、[[two-sided-fairness-reranking]]。

## 与偏差/因果的关系
不公平常源于**反馈偏差**(曝光/流行度/位置偏置)——隐式反馈的 MNAR 性质([[implicit-feedback]])会放大马太效应
([[2023-dorl-matthew-effect-offline-rl-recommendation]]);故公平与**去偏/因果推断**([[causal-inference]]、[[deconfounder]])一脉相承。

## 实现位置与张力
多在 [[reranking|重排]]阶段以约束/正则实现,与 [[multi-objective-optimization|多目标]](公平 vs 效用)、生命周期([[2025-lhrl-lifecycle-fairness-recommendation]])联立;
与 [[personalization|个性化]]存在根本张力(过度个性化加剧信息茧房与群体极化)。

## 相关页
[[item-side-fairness]]、[[recommender-systems]]、[[multi-objective-optimization]]、[[causal-inference]]、[[reranking]]
