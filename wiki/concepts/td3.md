---
type: concept
subtype: method
tags: [reinforcement-learning, actor-critic, off-policy, continuous-control]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# TD3

TD3(Twin Delayed Deep Deterministic Policy Gradient)是一种面向连续动作空间的 off-policy actor-critic 强化学习算法,通过双 Q 网络取最小值抑制过估计、延迟更新策略网络以及目标策略平滑等技巧改进 DDPG,在 RL-based 推荐系统中常作为经典基线方法被采用。

## 在本 wiki 中的出现

- [[2023-kuaisim-recommender-simulator]]:面向推荐系统的综合性用户模拟器,提供 multi-behavior 与 cross-session 反馈,统一支持 request 级 list-wise、whole-session 级 sequential 与 cross-session 级 retention 三类 RL 推荐任务并配套 benchmark。
- [[2024-easyrl4rec]]:面向 RL-based 推荐系统的易用代码库,基于五个公开数据集构建轻量 RL 环境,提供四个核心模块与面向长期收益的统一训练/评测流程,并给出经典与近期 RL 方法的对照实验。
- [[2024-edt4rec-max-entropy-decision-transformer]]:EDT4Rec 给 Decision Transformer 加入最大熵探索与基于 CQL Q-function 的 reward relabeling,解决 offline RL 推荐中缺乏 stitching 能力和在线探索不足的问题。

## 相关

- [[ddpg]]
- [[actor-critic]]
- [[off-policy-rl]]
- [[decision-transformer]]
- [[cql]]
- [[rl-based-recommendation]]
