---
type: concept
subtype: method
tags: [contextual-bandit, off-policy-learning, reinforcement-learning, policy-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Contextual Bandit

Contextual Bandit(情境老虎机)是一类在线决策方法:在每一步根据观察到的上下文(context)从若干动作中选择一个,并仅获得所选动作的反馈(奖励),目标是学习一个将上下文映射到动作的策略以最大化累计奖励。

## 在本 wiki 中的出现

- [[2025-multiscale-contextual-bandits-long-term]]:提出 MultiScale Policy Learning 框架与 MSBL 算法,用分层 off-policy contextual bandit 在多个时间尺度上协调短期反馈与长期目标,让低尺度数据作为高尺度稀疏数据的 PAC-Bayes 先验。

## 相关

- [[off-policy-learning]]
- [[pac-bayes]]
- [[policy-learning]]
- [[reinforcement-learning]]
