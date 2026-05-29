---
type: entity
subtype: model
tags: [reinforcement-learning, actor-critic, deterministic-policy, deep-rl]
created: 2026-05-29
updated: 2026-05-29
sources: 7
---

# DDPG

DDPG(Deep Deterministic Policy Gradient)是一种面向连续动作空间的无模型 actor-critic 强化学习算法,通过确定性策略梯度结合深度神经网络、经验回放与目标网络来学习策略。

## 在本 wiki 中的出现
- [[2023-hyper-actor-critic-recommendation]]：该工作提出 Hyper-Actor Critic（HAC）框架，将推荐列表生成解耦为 hyper-action 推断与 effect-action 选择两步，并用对齐与监督模块在大动作空间下稳定 RL 推荐策略的学习。DDPG 在这一脉络中代表了将 actor-critic 与连续/高维动作表示相结合的经典思路，HAC 可视为对这类 actor-critic 方法在推荐列表生成这一巨大动作空间场景下的扩展与改造。
- [[2023-kuaisim-recommender-simulator]]：面向推荐系统的综合性用户模拟器，提供 multi-behavior 与 cross-session 反馈，统一支持 request 级 list-wise、whole-session 级 sequential 与 cross-session 级 retention 三类 RL 推荐任务并配套 benchmark。
- [[2024-easyrl4rec]]：面向 RL-based 推荐系统的易用代码库，基于五个公开数据集构建轻量 RL 环境，提供四个核心模块与面向长期收益的统一训练/评测流程，并给出经典与近期 RL 方法的对照实验。
- [[2024-edt4rec-max-entropy-decision-transformer]]：EDT4Rec 给 Decision Transformer 加入最大熵探索与基于 CQL Q-function 的 reward relabeling，解决 offline RL 推荐中缺乏 stitching 能力和在线探索不足的问题。
- [[2025-policy-guided-causal-state-representation]]：PGCR，面向离线 RL 推荐的两阶段因果状态表示框架，用策略引导的因果特征选择隔离因果相关分量，再用 encoder 学习紧凑状态表示。
- [[2025-xmtf-formula-free-multi-task-fusion]]：xMTF 用可学习的单调融合单元（MFC）替代多任务融合中的预定义公式，配合 RL 外层 + 监督内层的两阶段混合训练，离线 Total Watch Time 1279.7s 超越全部基线，线上 Daily Watch Time +0.833%，Kuaishou 全量部署服务超 1 亿用户。
- [[2025-tadt-csa-temporal-advantage-decision-transformer]]：面向工业生成式推荐的 Decision Transformer 改进框架，用 Temporal Advantage 信号和对比式状态抽象解决 DT 的轨迹拼接弱与状态空间过大问题。
- [[reinforcement-learning]]
- [[markov-decision-process]]
- [[ppo]]
- [[reward-model]]
- [[recommender-systems]]
- [[sequential-recommendation]]

- [[2024-unex-rl-multi-stage-recommender]]:UNEX-RL 用多智能体 RL 对多阶段推荐系统的各阶段联合建模,以单向执行与 cascading information chain (CIC) 优化长期回报,Kwai 在线提升日观看时长 0.953%。

## 相关

- [[actor-critic]]
- [[deterministic-policy-gradient]]
- [[multi-agent-reinforcement-learning]]
- [[2024-unex-rl-multi-stage-recommender]]
