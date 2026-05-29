---
type: source
subtype: paper
tags: [reinforcement-learning, recommender-systems, actor-critic, latent-action-space, representation-learning]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2302.03431
raw: raw/2302.03431.pdf
authors: [Shuchang Liu, Qingpeng Cai, Bowen Sun, Yuhao Wang, Ji Jiang, Dong Zheng, Kun Gai, Peng Jiang, Xiangyu Zhao, Yongfeng Zhang]
year: 2023
---

提出 Hyper-Actor Critic(HAC)框架,把推荐列表的生成解耦为「hyper-action 推断 + effect-action 选择」两步,用对齐模块与监督模块来稳定大动作空间下的 RL 推荐策略学习。

## 问题

在推荐系统(RS)中,用户与系统的长期交互可建模为 [[markov-decision-process]],因此 [[reinforcement-learning]] 方法可用于最大化整个会话的累积奖励,比传统 learning-to-rank 更能优化长期收益。但推荐策略的动作是「一个 item 列表」,候选池可能高达数百万且动态变化(每天新增),动作空间 $\mathcal{A}=\mathcal{I}^k$ 极其庞大,使得 tabular 方法(Q-Learning、SARSA)和为固定动作空间设计的方法不适用。

把列表拆成 item-wise 子动作再做 policy gradient 虽缓解了规模问题,但学习仍然困难。本文的核心动机是:引入一个连续的 latent **hyper-action** 空间作为推荐列表的向量化表示,但这会带来 hyper-action 与真正与用户交互的 effect-action(实际推荐列表)之间的**不一致**问题,以及「该在 hyper-action 空间还是 effect-action 空间做探索」的不确定性,从而导致 RL 训练不稳定。

## 方法

提出 **Hyper-Actor Critic (HAC)** 学习框架,以 DDPG 为基础但做了关键改造,包含四个组件:

- **Hyper-Actor / 用户状态生成器**:用 [[sasrec]](基于 Transformer 的序列模型)作为 backbone,把用户交互历史 $x_{1:t}$ 与静态特征 $u$ 经 item kernel function $\Phi$ 编码为用户状态 $s_t$,再用 MLP 推断出向量化的 hyper-action $Z_t = \mathrm{MLP}(s_t)$,其分布设为高斯 $\mathcal{N}(Z_t,\sigma_Z^2)$ 以支持 reparameterization 端到端训练。
- **Scoring Function / effect-action**:在条件独立假设 $P(a_t|s_t,Z_t)=P(a_t|Z_t)$ 下,用打分函数 $\mathrm{score}(i|Z_t)=\Phi(i)^\top Z_t$ 对候选 item 排序,通过 top-$k$ 选择或 categorical sampling 生成最终列表(slate decomposition 风格)。
- **Shared Critic + Inverse Module**:critic 是共享映射 $g:\mathcal{S}\times\mathcal{Z}\to\mathbb{R}$,既能评估 hyper-action $Q(s_t,Z_t)$ 也能评估 effect-action $Q(s_t,a_t)$;再引入 inverse module $\hat{Z}_t=h(a_t)=\mathrm{pooling}(\{\Phi(i)|i\in a_t\})$(item kernel 空间的平均池化)从 effect-action 反推 hyper-action,使两空间共享 critic 并迁移知识。
- **对齐 + 监督**:
  - critic 损失(TD error)只在 effect-action 上计算以保证评估准确:$\mathcal{L}_{TD}=\mathbb{E}[(r+\gamma(1-d)Q(s_{t+1},a_{t+1})-Q(s_t,a_t))^2]$;
  - actor 通过最大化 hyper-action 的 Q 值学习:$\mathcal{L}_{QMax}=\mathbb{E}[Q(s_t,Z_t)]$;
  - **hyper-action 对齐损失** $\mathcal{L}_{Hyper}=\mathbb{E}\|Z_t-\hat{Z}_t\|^2$(L2 正则)避免两空间 mode collapse;
  - **监督损失** $\mathcal{L}_{BCE}$:基于即时用户响应对 effect-action 做 binary cross-entropy 监督,稳定训练。

探索可同时作用于 hyper-action 空间(加高斯噪声,方差 $\sigma_Z^2$)和 effect-action 空间(categorical sampling)。训练采用经验回放(replay buffer)+ target network 的 actor-critic 范式(Algorithm 1)。

## 结果

在三个公开数据集上构建模拟在线环境评测:**RL4RS**($|\mathcal{I}|=283$,k=9)、**MovieLens-1M / ML1M**(6400 用户、3706 item、k=10)、**KuaiRand-1K / KuaiRand**(986 用户、11643 item、k=10)。评测指标:Total Reward(整会话奖励和)、Depth(平均交互轮数)、Reward Variance(跨用户状态的稳定性,越低越好)。$\gamma=0.9$,交互深度上限 20,多数 RL 方法在 50,000 次迭代内收敛。

主结果(Table 2,Total Reward):

| 模型 | RL4RS | ML1M | KuaiRand |
|---|---|---|---|
| Offline SL | 6.721 | 18.559 | 14.394 |
| Online SL | 9.502 | 18.629 | 13.456 |
| A2C | 7.789 | 16.158 | 12.460 |
| DDPG | 8.337 | 17.205 | 11.394 |
| TD3 | 8.553 | 17.545 | 11.777 |
| PG-RA (DDPG-RA) | 8.561 | 18.466 | 10.859 |
| **HAC** | **10.059** | **18.863** | **14.789** |

HAC 在所有数据集的两个长期指标上均最优:相比最强基线,RL4RS 提升约 **6%**、ML1M 约 **1%**、KuaiRand 约 **3%**。HAC Depth 也最高(RL4RS 11.102 / ML1M 18.988 / KuaiRand 15.335)。

其他发现:A2C 表现最不稳定;其它 RL 方法在动作空间更大的 ML1M / KuaiRand 上反而劣于 offline SL,说明它们难以捕捉大 effect-action 空间的模式,而 HAC 能。消融(Fig.8)显示去掉监督 $\mathcal{L}_{BCE}$ 或对齐 $\mathcal{L}_{Hyper}$ 都会降低性能并增大 reward variance;DDPG ≈ "HAC w/o $\mathcal{L}_{BCE}$",表明仅分离 actor/critic 动作空间并加对齐模块不足,HAC 同时需要对齐与监督。超参分析显示 hyper-action 对齐 $\lambda_h=0.1$、effect-action 探索用 top-$k$ greedy(把 hyper-action 噪声设为 0)效果最佳。

## 在本 wiki 中的位置

本文属于「RL 用于推荐 / 大离散动作空间」方向,与本 wiki 主体的 LLM Agent 研究相对独立,但其方法论可与基于 LLM 的 [[llm-agents]] 的动作空间设计相互参照。核心方法是 [[actor-critic]] / [[ddpg]] 的扩展,引入 [[latent-action-space]] 概念,backbone 使用 [[sasrec]]。可与同样讨论序列决策、[[markov-decision-process]] 与 [[reinforcement-learning]] 的工作交叉索引。出自快手([[kuaishou]])与多所高校的合作研究。
