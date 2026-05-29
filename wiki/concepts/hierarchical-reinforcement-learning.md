---
type: concept
subtype: method
tags: [reinforcement-learning, hierarchical-rl, recommendation, fairness]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# hierarchical reinforcement learning

分层强化学习(Hierarchical Reinforcement Learning, HRL)是一类将复杂决策任务分解为多层子策略的强化学习方法,通过高层策略设定子目标、低层策略执行具体动作,从而解耦不同时间尺度或不同目标维度的优化。

## 在本 wiki 中的出现

- [[2026-fairness-begins-with-state-dsrm-hrl]]:DSRM-HRL 用扩散模型把被 popularity bias 污染的用户状态提纯回真实偏好流形,再用分层 RL 解耦长期公平与短期参与,在 KuaiRec/KuaiRand 上实现 accuracy 与 fairness 更优的 Pareto 前沿。

## 相关

- [[reinforcement-learning]]
- [[diffusion-models]]
- [[recommender-systems|recommendation-systems]]
- [[fairness]]
- [[popularity-bias]]
