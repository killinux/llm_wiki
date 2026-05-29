---
type: concept
subtype: method
tags: [reinforcement-learning, recommendation, actor-critic, policy-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Hyper-Actor Critic (HAC)

Hyper-Actor Critic(HAC)是一种面向推荐系统的强化学习框架,通过将推荐列表生成解耦为 hyper-action 推断与 effect-action 选择两步,来稳定大动作空间下的策略学习。

## 在本 wiki 中的出现

- [[2023-hyper-actor-critic-recommendation]]:提出 HAC 框架。该工作把推荐列表生成解耦为 hyper-action 推断与 effect-action 选择两个步骤,并引入对齐(alignment)与监督(supervision)模块,以在大动作空间下稳定 RL 推荐策略的学习。

## 相关

- [[actor-critic]]
- [[reinforcement-learning-for-recommendation]]
- [[list-wise-recommendation]]
- [[large-action-space]]
- [[policy-gradient]]
