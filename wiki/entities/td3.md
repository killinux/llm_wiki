---
type: entity
subtype: model
tags: [reinforcement-learning, actor-critic, off-policy, baseline]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# TD3

TD3(Twin Delayed Deep Deterministic policy gradient)是一种面向连续动作空间的 off-policy actor-critic 强化学习算法,通过双 Q 网络、延迟策略更新和目标策略平滑来缓解 DDPG 的价值高估问题。

## 在本 wiki 中的出现
- [[2026-lerl-llm-enhanced-rl-long-term-recommendation]]:分层框架 LERL 用 LLM 做高层语义类别规划、用 RL(PPO)做低层细粒度物品选择,在 KuaiSim 模拟器上优化交互式推荐的长期用户满意度并缓解 filter bubble。
- [[2026-fairness-begins-with-state-dsrm-hrl]]:DSRM-HRL 用扩散模型把被 popularity bias 污染的用户状态提纯回真实偏好流形,再用分层 RL 解耦长期公平与短期参与,在 KuaiRec/KuaiRand 上实现 accuracy 与 fairness 更优的 Pareto 前沿。
- [[ppo]]
- [[hierarchical-rl]]
- [[2023-kuaisim-recommender-simulator]]:面向推荐系统的综合性用户模拟器,提供 multi-behavior 与 cross-session 反馈,统一支持 request 级 list-wise、whole-session 级 sequential 与 cross-session 级 retention 三类 RL 推荐任务并配套 benchmark。
- [[2024-easyrl4rec]]:面向 RL-based 推荐系统的易用代码库,基于五个公开数据集构建轻量 RL 环境,提供四个核心模块与面向长期收益的统一训练/评测流程,并给出经典与近期 RL 方法的对照实验。
- [[2024-edt4rec-max-entropy-decision-transformer]]:EDT4Rec 给 Decision Transformer 加入最大熵探索与基于 CQL Q-function 的 reward relabeling,解决 offline RL 推荐中缺乏 stitching 能力和在线探索不足的问题。
- [[2025-policy-guided-causal-state-representation]]:PGCR:面向离线 RL 推荐的两阶段因果状态表示框架,用策略引导的因果特征选择隔离因果相关分量,再用 encoder 学习紧凑状态表示。
- [[2025-xmtf-formula-free-multi-task-fusion]]:xMTF 用可学习的单调融合单元(MFC)替代多任务融合中的预定义公式,配合 RL 外层 + 监督内层的两阶段混合训练,离线 Total Watch Time 1279.7s 超越全部基线,线上 Daily Watch Time +0.833%,Kuaishou 全量部署服务超 1 亿用户。
- [[off-policy-rl]]
- [[decision-transformer]]
- [[cql]]
- [[rl-based-recommendation]]

- [[2023-rlur-user-retention-short-video]]:作为对比基线(baseline)出现。该工作将短视频用户留存建模为无限时域请求级 MDP,提出 RLUR 用强化学习直接最小化累计回访时间;在 KuaiRand 数据集上,RLUR 的表现优于 TD3 与 CEM,并在 Kuaishou 全量上线后提升了留存与 DAU。
- [[2024-unex-rl-multi-stage-recommender]]:UNEX-RL 用多智能体 RL 对多阶段推荐系统的各阶段联合建模,以单向执行与 cascading information chain (CIC) 优化长期回报,Kwai 在线提升日观看时长 0.953%。

## 相关

- [[ddpg]]
- [[reinforcement-learning]]
- [[actor-critic]]
- [[cem]]
- [[multi-agent-rl]]
- [[2023-rlur-user-retention-short-video]]
