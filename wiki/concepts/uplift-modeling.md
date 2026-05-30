---
type: concept
subtype: method
tags: [causal-inference, recommender-system, marketing, treatment-effect]
created: 2026-05-30
updated: 2026-05-30
sources: 6
---

# 增益建模 (Uplift Modeling)

增益建模估计**干预 (treatment) 对个体结果的因果增量效应**(ITE/CATE),即"对这个用户做 vs 不做某动作的收益之差",
而非预测绝对结果。用于优惠券/推送/曝光等场景:把资源投给**被干预才会转化**的"可说服者 (persuadables)",而非本就会转化的人。

## 与传统预测的区别
- response model 预测 P(转化 | 干预);uplift 预测 **P(转化|干预) − P(转化|不干预)**。
- 四象限人群:persuadables(增益正)、sure things、lost causes、**do-not-disturb**(干预反而流失)。只有 persuadables 值得投放。

## 方法
- **Meta-learners**:S-/T-/X-learner 用基学习器组合估 CATE。
- **因果树/森林**:causal tree、causal forest 直接按增益分裂。
- **直接优化**:uplift 专用损失;与 [[causal-inference|因果推断]] 的反事实框架同源。

## 在本 wiki 的关联
与推荐去偏/反事实一脉相承——曝光是干预,未观测混杂导致偏差,见 [[2022-deep-causal-reasoning-for-recommendations]]、[[deconfounder]]、
[[2024-counterfactual-watch-time]];长期价值视角下与 [[reinforcement-learning-for-recommendation]] 的信用分配互补。

## 相关页
[[causal-inference]]、[[recommender-systems]]、[[counterfactual-reasoning]]、[[deconfounder]]
