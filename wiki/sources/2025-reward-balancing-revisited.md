---
type: source
subtype: paper
tags: [offline-rl, recommender-system, world-model, diffusion-model, reward-shaping, interactive-recommendation, matthew-effect]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2506.22112
raw: raw/2506.22112.pdf
authors: [Wenzheng Shu, Yanxiang Zeng, Yongxiang Tang, Teng Sha, Ning Luo, Yanhua Cheng, Xialong Liu, Fan Zhou, Peng Jiang]
year: 2025
---

# Reward Balancing Revisited: Enhancing Offline Reinforcement Learning for Recommender Systems

提出 R3S(Reallocated Reward for Recommender Systems),用 diffusion world model 显式建模 reward 预测的固有不确定性,并配合带衰减的多样性惩罚,在 offline RL 推荐中同时平衡 world model 内在偏差与策略多样性。

## 问题

[[offline-rl]] 已成为真实世界 [[recommender-system]] 的主流方法,可从历史日志学习策略并捕捉用户偏好。但在 offline RL 中,reward shaping 面临核心难题:offline 静态数据集与动态学习策略之间存在分布失配(distributional mismatch)。这一失配来自两方面:(1)由于 state-action 覆盖不全、策略优化过度保守导致的 world model collapse;(2)推荐多样性不足引发的 [[matthew-effect]]。

既有 offline RL 方法(如 [[bcq]]、[[cql]]、[[mopo]])主要通过对未见 state-action 施加保守/悲观估计,往往忽略数据分布内在的交互关系。近期工作(如 [[dorl]]、ROLeR)虽利用 world model 提升 reward 的多样性与不确定性,但仅依赖先验经验来处理 reward shaping。论文指出关键空白:无法**同时**平衡 world model 的内在偏差与策略推荐的多样性。

## 方法

R3S 基于 A2C(actor-critic)框架,分两阶段:(a)从 offline 日志构建 world model;(b)通过与 world model 交互训练推荐策略。整体建模为 MDP `<S, A, T, r, γ>`。

- **Inherent Diffusion Uncertainty(固有扩散不确定性)**:以 DiffRec(Diffusion Recommender Model)为骨干重构 world model。Forward 过程对稀疏 reward 加 Gaussian 噪声;以 user/item embedding 的拼接 `c = e_u ⊕ e_i` 作为条件,训练去噪网络(由 [[deep-neural-network]] 参数化)。Reverse Sampling 阶段进行 M 次采样得到一系列 reward 矩阵,取均值作为预测 reward `r_D`,并直接由预测分布导出不确定性信号 `P_D`(各采样与均值的方差),无需训练额外的 world model 集成。
- **Diversity Strategy(多样性策略)**:沿用 DORL 提出的 entropy penalty `P_E`(behavior policy 与 uniform 分布间的负 KL 散度)缓解 Matthew Effect;并提出新的 interactive penalty `P_I`——保留 `P_E` 的计算结构,但把第 i 步的 k 阶熵从连续子序列 `[i-k, i-1]` 改为在 `[0, i-1]` 内随机采样 k 个位置,以捕捉长程依赖。
- **Diversity Attenuation(多样性衰减)**:引入指数衰减函数 `ω(l) = α(e^{-ξl}+1)`(α=5e-1,ξ=1.0),在早期迭代用 `P_E` 促进多样性,后期由 `P_I` 捕捉长程上下文依赖。
- **最终 reward 范式**:`r̂ = r_D − λ1·P_D(UNCERTAIN) + λ2·[(1−ω(l))·P_I + ω(l)·P_E](DIVERSITY)`。

## 结果

在 3 个真实数据集上评测:[[coat]](购物)、[[yahoo-r3]](音乐)、[[kuairand]](短视频),沿用 [[easyrl4rec]] 的设置。对比 11 个 RL baseline,包括 bandit 类 UCB、ε-greedy;model-free 的 SQN、CRR、[[cql]]、[[bcq]];model-based 的 [[mbpo]]、IPS([[inverse-propensity-score]])、[[mopo]]、[[dorl]]、ROLeR。指标为 R_tra(累计 reward)、R_each(每步 reward)、Length(交互距离)。

主要结果(R_tra / R_each):
- **Coat**:R3S = 78.224 / 2.607,优于次优 ROLeR(76.160 / 2.539)与 DORL(71.399 / 2.380);Length 均达上限 30.000。
- **Yahoo**:R3S = 69.223 / 2.307,优于 ROLeR(68.364 / 2.279);Length 30.000。
- **KuaiRand**:R3S = 14.087 / 0.488,R_tra 高于 ROLeR(13.455)与 DORL(11.850);R_each 最高(0.488),即使 Length(28.841)未达最大交互距离。

消融(Table 2,Coat / KuaiRand 的 R_tra):去掉 diffusion uncertainty(w/o U)降至 72.369 / 12.136;去掉 diversity(w/o D)降至 74.208 / 11.252;去掉 P_E 为 75.433 / 13.641;去掉 P_I 为 76.243 / 13.228。结论:Coat 这类稀疏小数据上 diffusion 增益更大、P_E 更优;KuaiRand 这类复杂交互上 P_I 更擅长;P_E 因约束更强,平均交互长度更长。

## 在本 wiki 中的位置

本文属于 [[rl-based-recsys]] / [[interactive-recommendation]] 方向,直接延续 Kuaishou 系工作 [[dorl]](缓解 offline RL 推荐中的 Matthew Effect)与 ROLeR 的 reward shaping 思路,创新点在于把 [[world-model]] 换成 [[diffusion-model]]([[recommendation-simulator]] 式的 DiffRec)来显式量化 reward 不确定性,并把多样性惩罚扩展为带时间衰减的 interactive penalty。与 [[model-based-rl]]([[mopo]]、[[mbpo]])、[[offline-rl]] 保守估计方法([[cql]]、[[bcq]])形成对照,评测复用 [[easyrl4rec]] 与 [[kuairand]]/[[coat]]/[[yahoo-r3]] 标准基准。作者主要来自 [[kuaishou]] 与电子科技大学(UESTC),通讯作者 [[peng-jiang]]。
