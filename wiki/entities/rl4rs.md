---
type: entity
subtype: dataset
tags: [recommendation, reinforcement-learning, benchmark, dataset]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# RL4RS

RL4RS 是一个面向推荐系统的强化学习(Reinforcement Learning for Recommender Systems)基准数据集与环境,用于在真实推荐场景下评估和训练 RL 推荐策略。

## 在本 wiki 中的出现

- [[2023-hyper-actor-critic-recommendation]]:该论文提出 Hyper-Actor Critic(HAC)框架,将推荐列表生成解耦为 hyper-action 推断与 effect-action 选择两步,并用对齐与监督模块稳定大动作空间下的 RL 推荐策略学习。在该工作中,RL4RS 作为评估推荐场景下 RL 策略的基准之一。
- [[2023-kuaisim-recommender-simulator]]:面向推荐系统的综合性用户模拟器,提供 multi-behavior 与 cross-session 反馈,统一支持 request 级 list-wise、whole-session 级 sequential 与 cross-session 级 retention 三类 RL 推荐任务并配套 benchmark。

## 相关

- [[2023-hyper-actor-critic-recommendation]]
- [[hyper-actor-critic]]
- [[reinforcement-learning-for-recommendation]]
- [[list-wise-recommendation]]
