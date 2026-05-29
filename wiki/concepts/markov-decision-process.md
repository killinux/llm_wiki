---
type: concept
subtype: method
tags: [reinforcement-learning, sequential-decision-making, recommendation, mdp]
created: 2026-05-29
updated: 2026-05-29
sources: 12
---

# Markov Decision Process

Markov Decision Process(MDP)是描述序列决策问题的数学框架,由状态、动作、状态转移概率、奖励与折扣因子构成,其核心假设是下一状态与奖励只依赖于当前状态和动作(马尔可夫性),常作为强化学习(reinforcement learning)的建模基础。

## 在本 wiki 中的出现

- [[2023-rlur-user-retention-short-video]]:将短视频用户留存建模为无限时域的请求级 MDP,以此为基础提出 RLUR,用强化学习直接最小化累计回访时间;在 KuaiRand 上优于 TD3/CEM,并在 Kuaishou 全量上线提升留存与 DAU。MDP 在此是问题建模的核心抽象,把"留存"转化为可优化的序列决策目标。
- [[2023-multi-task-recommendations-with-rl]]:RMTL 在 session 级序列上以 actor-critic 强化学习动态生成多任务损失权重,替代固定常数加权;其序列优化天然依赖将推荐过程视为 MDP 的建模视角,从而提升 RetailRocket 与 Kuairand 上 CTR/CTCVR 的 AUC。
- [[2023-hyper-actor-critic-recommendation]]:Hyper-Actor Critic(HAC)框架把推荐列表生成解耦为 hyper-action 推断与 effect-action 选择两步,在 RL 推荐策略学习中处理大动作空间;其策略学习建立在将推荐交互视为 MDP 的基础上,并用对齐与监督模块稳定训练。
- [[2023-multi-task-deep-recommender-systems-survey]]:在为多任务深度推荐系统(MTDRS)建立任务关系与方法论分类体系的综述中,MDP 作为基于强化学习的多任务推荐方法的理论背景被涉及。
- [[2023-kuaisim-recommender-simulator]]:面向推荐系统的综合性用户模拟器,提供 multi-behavior 与 cross-session 反馈,统一支持 request 级 list-wise、whole-session 级 sequential 与 cross-session 级 retention 三类 RL 推荐任务并配套 benchmark。
- [[2023-ts-llm-tree-search-decoding-training]]:TS-LLM:用学习的 value function 的 AlphaZero 风格树搜索,同时指导 LLM 的推理解码与迭代训练,适配任意规模 LLM 并将搜索深度扩展到 64。
- [[2024-unex-rl-multi-stage-recommender]]:UNEX-RL 用多智能体 RL 对多阶段推荐系统的各阶段联合建模,以单向执行与 cascading information chain (CIC) 优化长期回报,Kwai 在线提升日观看时长 0.953%。
- [[2024-future-impact-decomposition-request-level-recommendation]]:提出 ItemA2C 框架,在 request-level MDP 下将 list-wise reward 分解为 item-wise 信用并用 actor-critic 优化每个 item 的长期未来影响,提升推荐长期效果。
- [[2024-easyrl4rec]]:面向 RL-based 推荐系统的易用代码库,基于五个公开数据集构建轻量 RL 环境,提供四个核心模块与面向长期收益的统一训练/评测流程,并给出经典与近期 RL 方法的对照实验。
- [[2024-llm-learnable-planners-long-term-recommendation]]:提出 BiLLP 双层可学习 LLM 规划框架(Planner/Reflector 宏观 + Actor/Critic 微观),在稀疏推荐数据上以 LLM 规划能力做长期推荐,Len 与累积奖励超越从零训练的 RL 与现有 LLM agent 基线。
- [[2024-model-based-multi-agent-short-video-recommender]]:MMRF:协作式多智能体 RL 最大化短视频会话累计 WatchTime,并用 model-based 反馈模拟缓解样本选择偏差,离线 +7.3% GAUC、在线 +0.55% WatchTime,已部署服务数亿用户。
- [[2024-recursive-introspection-rise]]:RISE 将单轮问题建模为多轮 MDP 并用 reward-weighted regression 迭代微调,让 7B 级 LLM 在无外部反馈下学会跨多轮递归反思并修正答案。

## 相关

- [[reinforcement-learning]]
- [[actor-critic]]
- [[td3]]
- [[policy-gradient]]
- [[markov-property]]
- [[reward-function]]
- [[discount-factor]]
- [[user-retention]]
- [[multi-task-learning]]
