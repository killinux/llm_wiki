---
type: concept
subtype: method
tags: [reinforcement-learning, sequential-decision-making, recommendation, mdp]
created: 2026-05-29
updated: 2026-05-29
sources: 20
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
- [[2024-score-self-correct-via-rl]]:SCoRe 用完全自生成数据的多轮在线强化学习(两阶段+奖励塑形)训练单个 LLM,在 MATH 上把内在自我纠错 Δ(t1,t2) 从 -11.2% 提到 +4.4%(整体提升 15.6%)、HumanEval 上达 12.2%。
- [[2024-llm-powered-user-simulator-for-recommender-system]]:用 LLM 离线蒸馏用户偏好关键词与情感,在线用逻辑+统计集成模型显式推断 like/dislike,构建可解释、低幻觉、低成本的推荐系统用户模拟器。
- [[2025-multi-objective-controllable-decision-transformer]]:提出 MocDT,一种基于 Decision Transformer 的离线 RL 推荐方法,把未来多目标作为控制信号,在推理阶段自回归生成对齐指定目标(累积评分与多样性)的物品序列,无需重训。
- [[2025-value-function-decomposition-mrp]]:提出把在线 RL 推荐中的标准 TD loss 分解为 state TD 与 action TD 两个独立目标,以分离随机策略与随机用户环境两类噪声,获得更准确、更快收敛、对动作探索更鲁棒的价值函数,可通用插入 A2C/DQN/DDPG/HAC/SQN。
- [[2025-policy-guided-causal-state-representation]]:PGCR:面向离线 RL 推荐的两阶段因果状态表示框架,用策略引导的因果特征选择隔离因果相关分量,再用 encoder 学习紧凑状态表示。
- [[2025-xmtf-formula-free-multi-task-fusion]]:xMTF 用可学习的单调融合单元(MFC)替代多任务融合中的预定义公式,配合 RL 外层 + 监督内层的两阶段混合训练,离线 Total Watch Time 1279.7s 超越全部基线,线上 Daily Watch Time +0.833%,Kuaishou 全量部署服务超 1 亿用户。
- [[2025-reward-balancing-revisited]]:提出 R3S,用 diffusion world model 显式建模 reward 不确定性并配合带衰减的多样性惩罚,在 offline RL 推荐中同时平衡 world model 偏差与策略多样性,在 Coat/Yahoo/KuaiRand 上超越 DORL、ROLeR 等 11 个 baseline。
- [[2025-tadt-csa-temporal-advantage-decision-transformer]]:面向工业生成式推荐的 Decision Transformer 改进框架,用 Temporal Advantage 信号和对比式状态抽象解决 DT 的轨迹拼接弱与状态空间过大问题。

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
- [[offline-reinforcement-learning]]
- [[decision-transformer]]
