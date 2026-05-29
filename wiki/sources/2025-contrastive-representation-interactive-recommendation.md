---
type: source
subtype: paper
tags: [interactive-recommendation, contrastive-learning, deep-reinforcement-learning, recommender-system, sample-efficiency, representation-learning]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2412.18396
raw: raw/2412.18396.pdf
authors: [Jingyu Li, Zhiyong Feng, Dongxiao He, Hongqi Chen, Qinghang Gao, Guoli Wu]
year: 2025
---

# Contrastive Representation for Interactive Recommendation (CRIR)

本文提出 CRIR,用一个并行的对比学习辅助任务(PRCL)从用户-物品交互中抽取高层偏好排序特征,以增强 [[interactive-recommendation]] 中 [[deep-reinforcement-learning]] agent 的状态表示,从而显著提升其样本效率(sample efficiency)。

## 问题

[[interactive-recommendation]](IR)将推荐建模为序列决策问题,用 [[reinforcement-learning]] / [[deep-reinforcement-learning]](DRL)求解,以捕捉用户动态兴趣并平衡长短期目标(类似 ChatGPT 中的 [[rlhf]] 机制)。但 DRL 用于 IR 时存在严重的**样本低效**(sample inefficiency)问题:动作空间大、需在线训练且高维观测难以训练好,导致 agent 难以在有限的在线交互内学到理想策略,无法快速吸引用户、维持活跃用户数。

作者把改善 IR 样本效率的工作分为三类:(i) 改进 DRL 功能组件;(ii) 增强 reward 信号;(iii) 增强状态表示。本文属于第三类,但不同于前馈式处理(pooling / 神经网络),而是借鉴传统推荐中的自监督 [[contrastive-learning]] 范式。其核心动机被命名为 **DRL Representation Consensus**:若 agent 能从高维观测中获得高质量语义表示,则建立其上的 DRL 推荐方法应当显著更省样本。直接套用传统对比学习面临三个问题:(i) IR 交互历史无法提供足够对比样本;(ii) 大动作空间下对比计算开销巨大;(iii) IR 在线推荐与离线训练同时进行,对比学习能否稳定训练尚未充分研究。

## 方法

CRIR 由一个**状态表示网络**(State Representation Network)和提出的 **Preference Ranking Contrastive Learning (PRCL)** 组成,二者通过 Interest Weight(兴趣权重)连接,以并行辅助任务(Auxiliary Mechanism)方式训练。

- **状态表示网络**:借鉴 [[deep-interest-network]](DIN)的 weighted sum attention,为交互历史中每个行为(物品特征+用户反馈)计算兴趣权重(activation unit + Dice 激活);同时并行 average pooling 保留基础状态信息并稳定收敛。最终状态表示见式(1)。
- **PRCL**:针对问题 (i),充分利用用户在不同时刻对不同已交互物品的偏好度量;针对问题 (ii),用兴趣权重生成近似高层用户表示的 interest weights,避免在整个潜在动作集上做对比计算。
  - **Data Augmentation**:Sampling(replay buffer 随机采样 + 下一轮 DRL 训练用的 PER 采样,合称 **Mixed Mechanism**)、Weighting(用兴趣权重表示对各行为的关注度)、Ranking(按兴趣权重对交互历史排序,取前 ⌊n/2⌋ 为候选正样本,随机选 (h1,hk) 为正对,后半部分为负对,每个 transition 得 1 正对 + ⌊n/2⌋ 负对)。
  - **Positional Weighted InfoNCE Loss**(式 6):在标准 InfoNCE 基础上引入排名位置系数 1/√(R_u(h_k)) 来平滑不同对比对的判别强度,使排名位置度量该对比对的重要性。
- **DRL backbone**:用 [[ddpg]] + Priority Experience Replay(PER),采用生成式推荐范式。PRCL 与主 DRL 任务分开但同步进行(Auxiliary Mechanism)。

## 结果

在 [[virtual-taobao]] 仿真环境与基于 [[movielens-1m]](ML-1M)构建的仿真器上做实验,**全冷启动设置**(所有表示参数随机初始化)。

- **评测指标**:Cumulative Reward(一回合内 Σr_t)与 Click Through Rate(CTR,正 reward 占比);用折线图按 episode 展示样本效率,每条曲线重复 5 次取 95% 置信区间。
- **Baseline**:[[sac]]、[[crr]](Critic Regularized Regression)、[[ppo]]、[[drr]]、[[nicf]](Neural Interactive Collaborative Filtering),以及消融版 **CRIR w/o CL**。
- **RQ1(整体性能与消融)**:Virtual-Taobao 上 CRIR 的 cumulative reward 领先,约在第 **8000** episode 找到好策略,其他方法在 20000 episode 内均未达此水平。CTR 上多数模型最终升至约 **0.8**,但 CRIR 取得更多高 reward 动作。CRIR w/o CL 早期优于其他 baseline 但后期回落,说明状态表示网络与 PRCL 各有贡献。ML-1M 仿真器上 CRIR 同样最优,NICF/PPO 等在连续动作环境表现差。
- **RQ2-1(PRCL 频率)**:PRCL 频率 ∈ {0,0.25,0.5,0.75,1.0},频率越高样本效率越高但非线性,0.25→0.5 的提升远大于 0.5→0.75,且 PRCL 对 episode reward 这类"难"指标的提升大于 CTR。
- **RQ2-2(系数策略)**:判别系数 1/√(R_u(h_k)) 优于均匀 balanced 系数(≈0.3183),验证位置加权的有效性。
- **RQ3(采样/训练机制)**:Mixed Mechanism 优于 Divided / Combined;Auxiliary Mechanism 优于把 PRCL 作为 value function 约束的 Constrained Mechanism(γ∈{0,0.5,1.0} 影响很小),说明辅助式训练策略更有效。

## 在本 wiki 中的位置

本文属于**强化学习推荐 / 交互式推荐**方向,核心贡献是把 [[contrastive-learning]] 作为辅助任务来提升 [[deep-reinforcement-learning]] agent 的状态表示与样本效率,可与 [[rl-based-recsys]]、[[interactive-recommendation]]、[[drr]]、[[nicf]] 等节点关联。它使用 [[virtual-taobao]] 与 [[movielens-1m]] 作为仿真评测环境,与 IR 样本效率、表示学习相关工作形成对照。
