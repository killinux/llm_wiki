---
type: source
subtype: paper
tags:
  - reinforcement-learning
  - recommender-system
  - multi-agent-reinforcement-learning
  - multi-stage-recommender
  - long-term-reward
created: 2026-05-29
updated: 2026-05-29
arxiv: "2401.06470"
raw: raw/2401.06470.pdf
authors:
  - Gengrui Zhang
  - Yao Wang
  - Xiaoshuang Chen
  - Hongyi Qian
  - Kaiqiao Zhan
  - Ben Wang
year: 2024
---

# UNEX-RL: Reinforcing Long-Term Rewards in Multi-Stage Recommender Systems with UNidirectional EXecution

提出 UNEX-RL,一个面向多阶段(matching/pre-ranking/ranking/re-ranking)推荐系统的多智能体强化学习框架,用单向执行(unidirectional execution)对各阶段联合建模以优化长期回报,并通过 cascading information chain (CIC) 解决随之而来的训练难题。

## 问题

工业级 [[recommender-systems|recommender-system]] 普遍采用多阶段(multi-stage)结构:从数千万候选中经过 matching、pre-ranking、ranking、re-ranking 逐级筛选,以低延迟产出推荐。用 [[reinforcement-learning]] 优化用户的 long-term reward(长期回报,如总观看时长、留存)已被证明有效,但单智能体 RL 难以同时优化多个阶段——不同阶段有不同的 observation space(如各阶段候选集的预测/统计不同),无法用单个 agent 建模。

直接套用多智能体强化学习([[multi-agent-reinforcement-learning]])的 CTDE(centralized training with decentralized execution)范式也不行:CTDE 假设所有 agent 的 observation 在训练时从 replay buffer 同时采样,但在多阶段推荐中,上游 agent 的动作哪怕微小变化都会改变下游阶段的候选集,从而改变下游的 observation 与 action,违背 CTDE 假设,导致训练效果退化。

## 方法

- **多阶段建模为 MARL**:N 个阶段建模为 N 个 agent。第 i 阶段 agent 接收 observation τ_t^i,用策略 μ^i 产出动作 a_t^i(如多目标排序的线性融合权重),用该动作从候选集 I_t^i 选出 I_t^{i+1}。目标是最大化 [[markov-decision-process]] 下的长期回报 R_t = Σ γ^{t'-t} r_{t'}。
- **unidirectional execution(单向执行)**:由于第 i 阶段的 v_t^i(本阶段首次获得的预测/统计)必须在候选集 I_t^i 确定后才能得到,各 agent 必须在前一 agent 之后串行执行。这是多阶段推荐区别于传统 MARL 的关键特征,带来两个问题:Observation Dependency (OD)(critic 学习中下游 observation 依赖上游动作)与 Cascading Effect (CE)(某个 actor 策略变化会级联影响下游 agent)。
- **Cascading Information Chain (CIC)**:核心贡献。基于 Theorem 4.1——只需第一阶段 observation τ_t^1 即可重放(replay)整个系统的全部 observation。CIC 迭代地由上游阶段信息推出下游 observation 与 action,只从 τ_t^1 重建 τ_t^{1:N} 和 a_t^{1:N}。用 CIC 改造 critic 学习与 policy gradient,从而同时解决 OD 与 CE,替代传统 CTDE 训练。所有 agent 共享用户反馈 r_t,故只用一个 global critic Q^g。
- **方差缩减技术**:稀疏数据 + 多 agent 去中心动作导致大方差。提出 Stopping Gradient (SG)(在 critic 学习中只保留 Q^g 到 μ^i 的直接梯度,截断 μ^{i+1:N} 到 μ^i 的梯度)与 Category Quantile Rescale (CQR)(将奖励重塑为在相似用户群 G_u、相似物品群 G_i 上的分位数,使其服从均匀分布以压缩取值范围、降方差)。

## 结果

数据集为 [[kuairand]](27,285 用户、32,038,725 物品),并构建 user simulator 模拟用户交互(满足度耗尽即退出会话)。离线只取 matching/pre-ranking/ranking 三阶段。指标为 WatchTime(会话累计观看时长)与 Session Length(会话内观看物品数)。

- 离线总体性能(Table 1):UNEX-RL-CIC 取得最佳,WatchTime 1056.2s、Session Length 24.2;对比 [[ddpg]] 732.6s/18.2、[[td3]] 763.2s/18.9、CEM([[cross-entropy-method]])654.0s/15.3、UNEX-RL-CTDE 887.2s/21.6。说明 MARL 比单 agent 更能释放 RL 在多阶段推荐中的能力,且 CIC 优于 CTDE。
- agent 数量影响(RQ2):agent 数为 1 时 UNEX-RL 退化为 DDPG;随 agent 数增加,UNEX-RL-CIC 与 -CTDE 显著提升,而多个独立 DDPG 因缺乏协作反而更差;CIC 始终优于 CTDE。
- 方差缩减(RQ3):去掉 CQR 性能显著下降;去掉 SG 后 UNEX-RL-CIC 大幅变差,证明 SG 是 CIC 训练的关键。
- 在线 A/B(RQ4,部署于 Kwai/[[kuaishou]],服务超 1 亿用户):相对 CEM,UNEX-RL-CIC 取得 Session WatchTime +0.970%、Daily WatchTime +0.953%(0.1% 即具统计显著);相对 TD3 提升 0.558%。150 天长期在线实验显示部署 UNEX-RL 后有持续显著增益。

## 在本 wiki 中的位置

本文是 [[reinforcement-learning]] 应用于 [[recommender-systems|recommender-system]] 优化长期回报方向的代表工作,由 [[kuaishou]] 提出,首次将 [[multi-agent-reinforcement-learning]] 引入工业级多阶段推荐。其用 actor-critic 与 [[ddpg]]/[[td3]] 类方法做 baseline,数据来自 [[kuairand]],并基于 [[markov-decision-process]] 建模。与同样关注短视频长期参与/留存的工作(如 ResAct、PrefRec、Two-Stage Constrained Actor-Critic)同源,可与本 wiki 中 RL 推荐、watch-time/user-retention 优化相关条目互参。
