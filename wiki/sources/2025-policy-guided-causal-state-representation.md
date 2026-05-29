---
type: source
subtype: paper
tags:
  - offline-rl
  - rl-based-recsys
  - causal-inference
  - state-representation
created: 2026-05-29
updated: 2026-05-29
arxiv: 2502.02327
raw: raw/2502.02327.pdf
authors:
  - Siyu Wang
  - Xiaocong Chen
  - Lina Yao
year: 2025
---

PGCR(Policy-Guided Causal Representation):一个面向离线 RL 推荐系统的两阶段框架,通过策略引导的因果特征选择隔离状态中"因果相关分量(CRC)",再用 encoder 学习只保留 CRC 的紧凑状态表示。

## 问题

在离线 [[rl-based-recsys]](offline RLRS)中,学习有效的状态表示对捕捉影响长期奖励的用户偏好至关重要。但原始状态表示往往是高维、含噪、并包含与奖励**因果无关**的分量;同时离线数据中缺失的转移(missing transition)使得难以准确识别与用户满意度最相关的特征。基于 [[world-model]] 思路的 bisimulation 方法(如 Zhang 等)在离线设置下会因缺失转移而违反 bisimulation 原则,导致状态表示不准。因此需要从状态空间中**隔离出因果相关分量**,而非简单压缩。

## 方法

把 [[markov-decision-process]] 从因果建模视角重新表述,用确定性结构方程加外生噪声变量(exogenous noise)构造 [[structural-causal-model]](SCM),并把状态 $s_t$ 分解为因果相关分量(CRC)与因果无关分量(CIRC)。框架分两个阶段:

- **因果特征选择策略(Causal Feature Selection Policy)**:对动作 $a_t$ 做原子干预 $do(a_t := a_t^T)$,生成只保留 CRC、改变 CIRC 的修改状态 $s_t^I$。基于 [[do-calculus]] 推导干预后的奖励分布,用一阶 **Wasserstein distance** 度量原始奖励分布与干预后奖励分布的差异,并据此设计奖励 $r_t = \exp(-\lambda W_1(\cdot))$($\lambda \in (0,1]$),激励策略保留对用户兴趣有直接影响的 CRC。论文给出 Proposition 1,用 back-door criterion 证明 $a_t$ 对 $s_{t+1}$ 因果效应的**可识别性**。训练时借助一个预训练的 expert policy(可用任意 RL 算法,实现中用 [[ddpg]])收集原始与干预后的奖励分布。
- **策略引导的状态表示(Policy-Guided State Representation)**:用 encoder $\phi$ 把原始状态 $s_t$ 与其干预版本 $s_t^I$ 编码为 latent $z_t, z_t^I$,通过最小化二者潜在表示的 MSE 损失 $J = \|\phi(s_t) - \phi(s_t^I)\|_2^2$,迫使 encoder 聚焦 CRC、忽略 CIRC。Proposition 2 论证基于该 latent 表示的最优策略与完整状态等价。干预生成的修改状态同时起到**数据增广**作用,缓解离线数据缺失转移问题。
- **整合学习流程**:离线数据集 + 因果特征选择策略生成 $s_t^I$ → 训练 encoder → 用 latent 表示 $z_t$ 训练推荐策略 $\pi_{Re}$。

## 结果

在 [[movielens-1m]]、[[coat]]、[[kuairec]]、[[kuairand]] 四个离线数据集(按 [[easyrl4rec]] 转为 RL 环境)上,把 PGCR 接入 [[ddpg]]、[[sac]]、[[td3]] 三种 backbone:

- PGCR 版本在 cumulative reward 与 average reward 上一致优于原始算法。例如 KuaiRec 上 PGCR-SAC 的 cumulative reward 达 15.3726,而 SAC 为 10.5235;MovieLens-1M 上 PGCR-TD3 cumulative reward 14.1281 vs TD3 的 10.1620;Coat 上 PGCR-SAC cumulative reward 20.4272 vs SAC 17.5432。interaction length 基本稳定或略增,且 PGCR 版本方差更低。
- 在线模拟平台 **VirtualTaobao** 上以 1-step CTR 为指标,PGCR 在三种 backbone 上均显著提升 CTR(图 2)。
- **消融实验**:把因果 agent 换成随机采样状态得到 PGCR-C,PGCR 在所有数据集/算法上的 cumulative/average reward 均优于 PGCR-C,验证因果 agent 的必要性。
- **超参数研究**:奖励平衡参数 $\lambda$ 在 0.1–0.2 区间各模型 CTR 达峰值,$\lambda > 0.2$ 后性能下降(PGCR-DDPG 降幅最大)。实现细节:actor 学习率 $10^{-4}$、critic $10^{-3}$、$\gamma=0.95$、soft update $\tau=0.001$、hidden size 128、replay buffer $10^6$,训练 100,000 timesteps。

## 在本 wiki 中的位置

本文属于 [[causal-inference]] 与 [[offline-rl]] 在 [[recommender-system]] 交叉处的工作,核心是 [[state-representation]] 学习。它与 [[deep-deconf]]、[[idcf]] 等推荐去偏(debiasing)工作共享因果视角,但聚焦点是离线 RLRS 的状态表示而非 [[selection-bias]] 校正。方法上依赖 [[structural-causal-model]]、[[do-calculus]]、[[potential-outcome-framework]] 的可识别性论证,并借鉴 bisimulation([[world-model]] 式状态抽象)思路但用 Wasserstein 因果效应度量替代。相关工作包括 InvRec、CDT4Rec、CIDS(并发工作,用 conditional mutual information 做在线 RLRS 因果状态学习)及 [[matthew-effect]] 缓解的 counterfactual exploration。可作为 [[easyrl4rec]] 基准生态下的因果增强方法参考。
