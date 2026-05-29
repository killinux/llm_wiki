---
type: concept
subtype: method
tags: [multi-task-learning, optimization, trade-off, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Pareto 最优

Pareto 最优(Pareto optimality)指一种多目标权衡状态:在该状态下,无法在不损害至少一个目标的前提下进一步改善任何其它目标;由所有这类不可被支配解构成的集合称为 Pareto 前沿(Pareto front)。

## 在本 wiki 中的出现

- [[2023-multi-task-deep-recommender-systems-survey]]:在该多任务深度推荐系统(MTDRS)综述中,Pareto 最优作为处理任务间冲突与权衡的优化视角出现。多任务学习需要同时优化多个目标(如点击率、转化率等),不同任务的梯度方向常相互冲突,难以让所有任务同时达到最优;综述据此把"以 Pareto 最优为目标、在任务之间寻求不被支配的折中解"归为应对任务冲突的一类方法论思路。
- [[2024-model-based-multi-agent-short-video-recommender]]:MMRF 采用协作式多智能体 RL 最大化短视频会话累计 WatchTime,并用 model-based 反馈模拟缓解样本选择偏差;离线 +7.3% GAUC、在线 +0.55% WatchTime,已部署服务数亿用户。多智能体在多个相互冲突的目标间寻求协作均衡,体现了 Pareto 最优的权衡思想。

## 相关

- [[pareto]]
- [[multi-objective-optimization]]
- [[multi-task-learning]]
- [[recommender-systems]]
- [[task-conflict]]
- [[gradient-conflict]]
- [[pareto-front]]
- [[multi-agent-reinforcement-learning]]
