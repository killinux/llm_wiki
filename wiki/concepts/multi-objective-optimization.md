---
type: concept
subtype: method
tags: [recommender-system, multi-task-learning, optimization, multi-objective]
created: 2026-05-30
updated: 2026-05-30
sources: 9
---

# 多目标优化 (Multi-Objective Optimization)

多目标优化指**同时优化多个常相互冲突的目标**(如推荐里的点击率 CTR、转化率 CVR、观看时长、留存、多样性、公平性),
追求 **Pareto 前沿**上的解——无法在不损害某一目标的前提下改进另一目标。它是推荐系统排序与重排的核心难题。

## 主流做法
- **标量化 (scalarization)**:加权求和把多目标合成单目标,难点是**权重难调**且非凸前沿会被漏掉;[[2025-xmtf-formula-free-multi-task-fusion]]
  等探索"免公式"的目标融合。
- **多任务学习 (MTL)**:共享底层表示 + 任务专属塔,缓解目标间负迁移——[[esmm]](全曝光空间联合建模 CTR/CVR)、[[mmoe]]/PLE、
  [[2024-residual-multi-task-learner-resflow]]、[[dupn]]。
- **约束优化**:把次要目标设为约束,如 [[2023-two-stage-constrained-actor-critic]] 在时长目标下约束交互。
- **Pareto / 梯度法**:多梯度下降(MGDA)等直接逼近 Pareto 解。
- **可控权衡**:[[2025-multi-objective-controllable-decision-transformer]] 让单模型按偏好向量在前沿上移动。

## 与重排、公平的联系
列表层的多目标平衡常落在 [[reranking|重排]]阶段;当目标涉及多方主体(用户/创作者/平台)时,与
[[item-side-fairness|多边公平]]([[2024-bankfair-fluctuating-traffic-reranking]])交叉。

## 相关页
[[multi-task-learning]]、[[reranking]]、[[recommender-systems]]、[[esmm]]、[[mmoe]]、[[reinforcement-learning-for-recommendation]]
