---
type: concept
subtype: method
tags: [optimization, sampling, reinforcement-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Cross-Entropy Method

Cross-Entropy Method (CEM) 是一种基于采样的随机优化方法,通过迭代地从参数化分布中采样、保留表现最优的"精英"样本、再用这些样本更新分布参数,从而逐步逼近最优解。

## 在本 wiki 中的出现

- [[2024-unex-rl-multi-stage-recommender]]:UNEX-RL 用多智能体 RL 对多阶段推荐系统的各阶段联合建模,以单向执行与 cascading information chain (CIC) 优化长期回报,Kwai 在线提升日观看时长 0.953%。

## 相关

- [[reinforcement-learning]]
- [[multi-stage-recommender-system]]
- [[multi-agent-reinforcement-learning]]
- [[policy-optimization]]
