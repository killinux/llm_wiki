---
type: source
subtype: paper
tags: [reinforcement-learning, recommender-systems, user-retention, short-video, kuaishou, mdp]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2302.01724
raw: raw/2302.01724.pdf
authors: [Qingpeng Cai, Shuchang Liu, Xueliang Wang, Tianyou Zuo, Wentao Xie, Bin Yang, Dong Zheng, Peng Jiang, Kun Gai]
year: 2023
---

本文(WWW'23)把短视频推荐中的"用户留存"建模为无限时域、以请求为单位的 [[markov-decision-process]],并提出 [[rlur]] 算法,用 [[reinforcement-learning]] 直接优化长期留存(等价于最小化累计回访时间);该算法已在 [[kuaishou]] App 全量上线。

## 问题

短视频平台(TikTok、YouTube Shorts、Kuaishou)的核心目标是提升用户留存(retention),从而拉动 DAU 增长。留存是用户与系统多轮交互后的长期反馈,难以拆解到单个视频或视频列表上,因此传统的 point-wise 模型和 list-wise 模型(只预测即时奖励或即时奖励的组合)无法直接优化留存。强化学习天然面向长期回报,但直接套用现有 RL 算法在留存场景会遇到三大困难:

- **不确定性(Uncertainty)**:留存并非完全由推荐算法决定,受大量系统外因素(如社会事件噪声)影响,方差大。
- **偏差(Bias)**:留存受时间、用户活跃度等因素影响(工作日/周末不同,高活用户天然留存高)。
- **长延迟(Long delay time)**:不同于游戏中即时返回的奖励信号,留存奖励往往要数小时到数天才返回,造成分布漂移大、RL 训练不稳定。

## 方法

将问题建模为**无限时域、以请求为单位的 MDP**:推荐器是 agent,用户是环境;每次请求 agent 输出一个连续动作(对 n 个打分模型的 ranking 权重),ranking 函数据此对候选视频打分并推荐 top 6;即时反馈 I 为观看时长与各类交互(like/follow/comment/share 等)之和;会话结束到下次开 App 的时间间隔即"回访时间(returning time)"T,是延迟奖励。目标是最小化累计回访时间 Σγ^(i-1) T(s_i)(等价于提升开 App 频率与留存)。提出 **RLUR(Reinforcement Learning for User Retention)**,针对三大挑战分别设计:

- **Retention Critic 学习**:用 DDPG 思路学习 critic Q_T 估计累计回访时间;对非末次请求样本折扣因子设为 1,防止回访时间奖励被指数衰减抹掉。
- **延迟奖励**:借助启发式奖励(heuristic reward)和内在激励——用 **RND(Random Network Distillation)** 计算 intrinsic reward 鼓励探索,把即时反馈作为启发式奖励引导策略;并单独学习 immediate reward critic Q_I。
- **不确定性**:用真实回访时间与预测回访时间之比作为归一化留存奖励;训练 session 级分类模型预测回访概率,取 60% 分位数 T_β 作为标签阈值,得到归一化奖励 r=clip(0, T/((1-T')·T_β), α),α=3。
- **偏差**:对高活、低活两个用户群分别学习两套策略 π(·|θ_high)、π(·|θ_low),防止学习被高活用户主导;策略损失为 retention critic 与 immediate critic 的加权和。
- **训练不稳定**:提出新的软正则方法,actor 损失按当前策略与行为策略的高斯密度比加权(分布漂移大的样本权重更小),λ=1.5 控制正则强度。

折扣因子取 0.95,动作为 8 维连续向量 [0,4]^8(对应观看时长、shortview、longview、like、follow、forward、comment、个人页进入 8 个打分模型),actor 损失中两个 critic 权重均为 1.0。

## 结果

离线实验在公开短视频数据集 [[kuairand]] 上搭建模拟器,对比黑盒优化方法 CEM(Cross Entropy Method)与 SOTA RL 方法 TD3,指标为平均回访天数(越低越好)与平均留存(越高越好),报告最后 50 个 episode 平均(Table 1):

- CEM:回访时间 2.036,留存 0.587。
- TD3:2.009 / 0.592。
- RLUR(naive, γ=0):2.001 / 0.596。
- RLUR(naive, γ=0.9):1.961 / 0.601。
- **RLUR(完整):1.892 / 0.618**,在两个指标上均显著优于 TD3 与 CEM,且优于只学回访时间的 naive 变体——说明最小化"多会话累计留存"比单会话更合理。

线上实验在 Kuaishou 十亿级平台进行,test 桶部署 RLUR、base 桶跑 CEM(不上线 TD3 因其训练不稳定)。随部署天数(Day 0→100)RLUR 持续提升回访时间/开 App 频率/留存/DAU:开 App 频率提升收敛到约 0.450%,DAU gap 收敛到 0.2%,1 日留存收敛到 0.053%,7 日留存收敛到 0.063%。论文指出短视频平台中 0.01% 留存提升、0.1% DAU 提升即具统计显著性,故该效果可观,且 RLUR 已长期全量上线。

## 在本 wiki 中的位置

本文是把 [[reinforcement-learning]] 用于工业级推荐系统、直接优化长期留存而非即时点击的代表性工作,联系 [[markov-decision-process]] 建模、[[delayed-reward]] 处理与 [[random-network-distillation]] 探索等概念。它与 LLM 主线相对独立,但其"用 RL 优化长期/延迟目标、用归一化与软正则稳定训练"的思路,与 [[rlhf]]、agent 类长程决策研究在方法论上相通,可作为 RL-for-real-world-systems 的案例节点;同时是 [[kuaishou]] 推荐系统系列(如两阶段约束 Actor-Critic、潜在动作空间正则)中的一篇。
