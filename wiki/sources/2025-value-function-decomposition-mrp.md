---
type: source
subtype: paper
tags:
  - reinforcement-learning
  - recommender-system
  - temporal-difference
  - value-function
  - rl-based-recsys
  - actor-critic
created: 2026-05-29
updated: 2026-05-29
arxiv: 2501.17409
raw: raw/2501.17409.pdf
authors:
  - Xiaobei Wang
  - Shuchang Liu
  - Qingpeng Cai
  - Xiang Li
  - Lantao Hu
  - Han Li
  - Guangming Xie
year: 2025
---

# Value Function Decomposition in Markov Recommendation Process

针对在线 RL 推荐中标准 TD 学习"混合两类随机因素"(随机策略 + 随机用户环境)导致价值函数估计次优的问题,提出把 TD loss 分解为 state TD 与 action TD 两个独立目标,从而得到更准确、收敛更快、对动作探索更鲁棒的价值函数,并可作为通用技术插入 A2C/DQN/DDPG/HAC/SQN 等多种 [[rl-based-recsys]] 骨干。

## 问题

[[recommender-system]] 中的用户-系统交互本质上是长期优化问题,可建模为 [[markov-decision-process]],作者称之为 Markov Recommendation Process(MRP):每个 context-aware 请求编码为用户状态 s_t,策略输出推荐列表(动作 a_t),用户环境给出反馈、即时奖励 r_t 并转移到下一状态。RL 方法的核心是学一个准确的 value function 来逼近长期累计奖励,主流做法是 [[temporal-difference]](TD)学习——用相邻两个状态(Value-based TD,见 [[value-function]])或相邻两个 state-action 对(Quality-based TD,即 Q)之间的差分来更新。

作者指出标准 TD 存在 **Mixing Random Factors(混合随机因素)** 的挑战:MRP 中同时存在两个随机来源——来自随机策略的动作探索(记为 Δ_π)和来自不确定用户环境的反馈(记为 Δ_u),但标准 TD(Eq.3 的 L_VTD、Eq.5 的 L_QTD)没有把二者分开建模。结果是:增大动作探索能更易跳出局部最优,却会引入大方差、破坏价值函数的稳定准确估计;限制探索能稳定估计,却牺牲了探索能力、易陷局部最优。这一 exploration-exploitation 矛盾使得在线 RL 难以得到稳定准确的价值函数。

## 方法

核心思想:把原始 TD 学习分解为两个互不干扰的子目标,各自只承担一种随机因素(见论文 Figure 2-b)。

- **Action TD 目标**(优化 Q,固定 V,stopped gradient):
  L_actionTD = (r(s_t,a_t) + γV(s_{t+1}) − Q(s_t,a_t))^2 (Eq.14)。让 Q 只捕获策略动作带来的差异 Δ_π,通过误差最小化消除用户环境噪声 Δ_u。
- **State TD 目标**(优化 V,固定 Q):
  L_stateTD = (V(s_t) − Q(s_t,a_t))^2 (Eq.15)。让 V 只捕获用户环境带来的 Δ_u,消除随机动作探索 Δ_π 的影响,从而学到不受探索方差污染的状态价值。

两目标联合即 **TD Decomposition** 框架:state 目标用 Q 作为 V 的 label,action 目标用即时奖励 r_t 与 V 作为 Q 的 target。作者论证该分解理论上更准确,并 consistently bounds 原始 TD;附录 A 给出证明。优势包括:去噪后 V/Q 能用更少样本学到更准信号(更快收敛);增大动作探索时 Δ_π 只进入 Q(Eq.14),不影响 V(Eq.15),因此对探索更鲁棒;同时学到 V 与 Q,可适配任何基于 Eq.3 或 Eq.5 的 TD 方法,是通用技术。

此外针对在线 RL 中"采样时的旧策略"与"当前策略"动作分布不一致(action discrepancy)的问题,引入 **debias 项 β = π(a_t|s_t)/p(a_t|s_t)** 得到 L_{β-stateTD} = β(V(s_t)−Q(s_t,a_t))^2 (Eq.18),通过重要性加权把 V 的学习拉向当前策略对应的正确目标 V^*。

实验在模拟在线环境中进行(传统离线评估不适合在线 RL):数据集为 [[movielens-1m]]、[[amazon-book]](Amazon book)与 [[kuairand]](KuaiRand1K);仿真器参照 [[kuaisim]],click 奖励 +1.0、miss 为 −0.2,最大 episode 深度 20,由 temper-based user leave 模型控制离开。指标含 average total reward、session depth、minimum reward 与 reward variance;所有方法 30,000 步内收敛,取最后 100 步均值,5 个随机种子。baseline 含 Supervision(Non-RL)、[[a2c]]、[[dqn]]、[[ddpg]]、[[hac]](Hyper-Actor-Critic)、[[sqn]] 与 Dueling DQN(D-DQN)。

## 结果

- TD Decomposition 在 4 个可分解骨干(A2C / DQN / DDPG / HAC)和 3 个数据集上 **一致优于** 原始 TD,KuaiRand 与 Amazon 上的提升 student-t 检验显著(p<0.05)。
- Table 1(Total Reward,数值为均值±std)节选:
  - **KuaiRand**:A2C 11.91→**15.91**(+33.59%);DQN 10.74→13.44(+25.14%);DDPG 12.86→13.78(+7.15%);HAC 12.47→**16.89**(+35.45%);SQN 11.22→15.42(+37.43%)。
  - **ML1M**:A2C 17.19→17.62(+2.50%);DQN 15.95→16.14(+1.19%);DDPG 13.52→17.05(+26.11%);HAC 16.89→17.76(+5.15%);SQN 16.33→16.88(+3.37%)。
  - **Amazon**:A2C 11.24→13.11(+16.64%);DQN 10.36→11.94(+15.25%);DDPG 10.99→11.58(+5.37%);HAC 12.17→13.31(+9.37%);SQN 6.94→11.74(+69.16%)。
- TD 分解的整体提升在 KuaiRand 上最大,作者推测短视频平台用户交互动态性更强,是更难的推荐环境。
- **更鲁棒**:在 KuaiRand 中当探索幅度 σ>0.1 时原始 TD 会 crash,而 TD 分解仍能学到准确价值并随探索增大获得更多收益(Figure 1、Figure 5);ML1M 中 σ 增至 1 时分解仍稳定,原始 TD 逐渐退化。
- **更快收敛**:A2C 与 HAC 的学习曲线显示分解版在前期 reward 提升更快、收敛点更优(Figure 3/4/6)。
- **debias 消融**:去掉 β 项会在两环境上产生次优表现(Figure 7);Table 2 给出不同 σ 下 β 与动作分布差异 α 的关系——探索幅度越大,旧/新策略分布越接近(β 越大、α 越小)。
- Dueling DQN 虽分离了 V 与 Advantage,但未分解 TD 学习以解决混合随机因素,表现弱于其他先进 RL 方法。

## 在本 wiki 中的位置

本文属于 [[rl-based-recsys]] / [[reinforcement-learning]] for recommendation 主题,聚焦 [[temporal-difference]] 学习中 [[value-function]] 估计的偏差与方差问题,提出的 TD 分解是一项可叠加到 [[actor-critic]] 及 value-based 方法上的通用技术,与 [[hac]]、[[a2c]]、[[ddpg]]、[[dqn]]、[[sqn]] 等骨干互补。它建立在 [[markov-decision-process]] 的推荐建模(MRP)之上,实验依托 [[kuaisim]] 模拟器与 [[movielens-1m]]、[[amazon-book]]、[[kuairand]] 数据集,可与本 wiki 中 [[long-term-recommendation]]、[[off-policy-evaluation]]、[[easyrl4rec]] 等条目关联。研究由 [[kuaishou]]([[qingpeng-cai]] 等)与 [[peking-university]] 合作完成,发表于 WWW '25。
