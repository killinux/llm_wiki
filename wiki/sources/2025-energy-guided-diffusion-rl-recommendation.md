---
type: source
subtype: paper
tags: [diffusion-model, offline-rl, rl-based-recsys, recommender-system, actor-critic, long-term-recommendation, energy-guided-sampling]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2510.12815
raw: raw/2510.12815.pdf
authors: [Xiaocong Chen, Siyu Wang, Lina Yao]
year: 2025
---

# DAC4Rec:面向长期用户行为预测的能量引导扩散采样(RL 推荐)

一句话:DAC4Rec(Diffusion-enhanced Actor-Critic for Offline RL4RS)用[[diffusion-model]]表示离线 RL 推荐中表达力更强的行为策略,结合 Q 值引导的策略改进与能量引导采样(energy-guided sampling),在六个真实数据集与 VirtualTaobao 在线模拟上更好地建模长期用户偏好。

## 问题

基于强化学习的推荐系统([[rl-based-recsys]],文中称 RL4RS)能动态适应用户偏好,但依赖在线交互导致数据效率低。[[offline-rl]]通过预收集轨迹缓解这一问题,但既有离线 RL4RS 方法(如基于 [[decision-transformer]] 的 DT4Rec、CDT4Rec、EDT4Rec)存在两大缺陷:

- **行为策略表达力不足**:它们依赖对行为策略(behavior policy)的模仿,而行为策略本身偏向短期兴趣,缺乏刻画多样、长期演化偏好的表达力。作者在 VirtualTB 上验证(Figure 1):随着交互历史变长,CDT4Rec 与 EDT4Rec 的 CTR 显著下降,说明它们难以泛化到更长轨迹。
- **次优轨迹与噪声**:离线数据中的历史行为受难以观测的因素影响,常常并非最优动作,直接当作专家示范([[behavior-cloning]])会把策略约束在狭窄区域,导致收敛到次优策略。
- 评估阶段的随机性:扩散策略需从分布中采样动作,缺乏对统计量的直接访问,导致采样噪声大、推荐质量不稳定。

## 方法

DAC4Rec 建立在 [[actor-critic]] 结构上,核心由三部分组成:

1. **扩散作为策略(Diffusion as a Policy)**:用条件扩散模型的反向过程(reverse process)参数化行为策略 μ。相比传统两步法,基于 [[ddpm]] 的扩散策略能直接表征行为策略的多模态、偏斜等复杂分布,且其基于采样的正则只需从数据集随机采样,独立于精确行为策略。训练目标为条件 ε-model 的去噪损失 L_d(θ)。
2. **Q 值引导的策略改进**:将 Q-learning 集成进训练管线,最终目标为行为克隆项与策略改进项的加权和 L=L_d+L_q。改进项有两种实现——Direct Policy Optimization(反传 Q 网络梯度,适用于 [[ddpg]]/[[td3]] 等确定性策略)与 Likelihood-based(借助 Advantage Weighted Regression 加权,如 [[iql]]);因扩散似然不可解,作者用 DDPM 下界并以一步去噪近似动作 â⁰ 来简化策略改进。
3. **能量引导采样(Guided Sampling)**:评估阶段提出针对 RL4RS 的能量引导机制,避免传统 score function 依赖额外 classifier 的开销。把策略 μ₀ 与按 e^{Q(s,a)} 加权的目标 π₀ 同时扩散到同一噪声分布,定义中间能量函数 E_t(s,a_t),并训练一个能量模型 f_ψ 估计目标 score function,以能量梯度引导反向扩散,从而降低采样随机性、稳定推荐质量。

整体训练分两步(Algorithm 1):先训练扩散行为策略并交替更新 Q 网络,再训练能量模型用于引导采样。框架可无缝嵌入任意含 Q 值的 RL 算法(Q-learning、[[sac]]、DDPG/TD3)。

## 结果

在五个真实离线数据集([[coat]]、[[yahoo-r3]]、[[movielens-1m]]、[[kuairec]]、[[kuairand]],经 EasyRL4Rec 转为 RL 环境)与在线模拟平台 [[virtual-taobao]](VirtualTB)上评估,指标为累积奖励 R_cumu、单步平均奖励 R_avg、轨迹长度 Length 与 CTR。

- **总体对比(RQ1)**:无论用 [[gru4rec]](GRU)还是 [[sasrec]](SASRec)作 state encoder,DAC4Rec(Ours)在几乎所有数据集上取得最高 R_cumu 与 R_avg。例如 Table 1 中 Coat 上 R_cumu=90.42、R_avg=2.88;MovieLens 上 R_avg=4.26;KuaiRec R_avg=1.08;在 VirtualTB 上 R_cumu=81.53、R_avg=6.15,均优于 DDPG/SAC/TD3/DT/DT4Rec/CDT4Rec/EDT4Rec。
- **长期偏好(RQ2)**:Table 3 按交互长度 11–20 / 21–30 / 31+ 比较平均 CTR,DAC4Rec 在 31+ 长交互上 CTR=0.702,显著高于 EDT4Rec(0.587)、CDT4Rec(0.564)、DT4Rec(0.545),且随交互变长衰减最小,表明更强的长期偏好建模与稳定性。
- **超参(RQ3)**:扩散步数 N∈{20,50,100,200},N 越大性能越稳、方差越小;N=100 在精度与计算开销间最优(N=200 提升边际)。
- **消融(RQ4)**:去除能量引导(DAC4Rec-E)或动作近似(DAC4Rec-A)均掉点;action approximation 贡献显著,energy guidance 对随机策略(如 SAC)增益更大、对确定性策略(TD3)提升有限。
- **可迁移性(RQ5,Table 4)**:对 DDPG,+Diffusion 提升 Avg.CTR 至 0.8665,+Diffusion+Energy 达 0.8771;对 SAC,+Diffusion+Energy 达 0.8455,能量引导对随机策略 SAC 的正向作用强于确定性的 DDPG,印证其"降低随机性"的设计目标。

## 在本 wiki 中的位置

本文属于 [[rl-based-recsys]] / [[offline-rl]] 与 [[diffusion-model]] 交叉方向,延续 [[kuaisim-recommender-simulator]]、DT4Rec/CDT4Rec/EDT4Rec 等离线 RL4RS 研究,但用扩散策略替代 [[decision-transformer]] 的行为建模,以增强表达力并缓解 [[behavior-cloning]] 导致的次优收敛。其能量引导采样与 [[classifier-free-guidance]]、score-based 引导相关,是 [[diffusion-models-in-recommendation-survey]] 所综述方向在 RL 推荐中的具体实例,聚焦 [[long-term-recommendation]] 与 [[user-retention]] 目标。
