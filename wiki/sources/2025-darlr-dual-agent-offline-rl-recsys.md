---
type: source
subtype: paper
tags:
  - offline-rl
  - recommender-system
  - dynamic-reward
  - multi-agent-reinforcement-learning
  - reward-shaping
  - world-model
created: 2026-05-29
updated: 2026-05-29
arxiv: "2505.07257"
raw: raw/2505.07257.pdf
authors:
  - Yi Zhang
  - Ruihong Qiu
  - Xuwei Xu
  - Jiajun Liu
  - Sen Wang
year: 2025
---

DARLR 是一个面向推荐系统的双 agent model-based offline RL 框架,用 selector 与 recommender 两个 RL agent 在策略学习过程中**动态地**精炼 world model 的奖励函数并自适应估计不确定性惩罚,以缓解 frozen reward 带来的不准确性。

## 问题

Model-based [[offline-rl]] 在 [[recommender-systems|recommender-system]] 中很有前景:先用稀疏的离线交互日志训练 [[world-model]](含奖励函数,常用 [[deepfm]] 这类监督模型),再在该 world model 中训练推荐策略。但 world model 的奖励函数往往不准确,尤其对离线日志中罕见的交互。

已有 model-based offline RL for RecSys(如 [[dorl]]、[[rlur]] 即 ROLeR)存在两个主要局限:
1. **deterministic / frozen reward 的直接使用**:把奖励函数当作静态 look-up table,在策略学习中冻结,导致不准确性被放大——高估的 item 在训练中被优先推荐却在测试时不满足用户期望;低估的 item 则被忽略。
2. **static uncertainty penalty**:静态的不确定性惩罚不足以刻画 RecSys 中的决策风险,无法随策略训练中奖励函数与动态的演化而调整。

由于高估与低估的奖励都会损害长期用户满意度,作者主张在策略学习过程中**迭代精炼** world model 的奖励函数。

## 方法

DARLR 包含三大模块:world model、selector、recommender(见原文 Figure 2)。

- **World Model Learning**:用户与 item 从 ID 及特征编码为 embedding,奖励函数通过 [[deepfm]] 等预测模型监督训练;沿用 DORL 的做法对多个 world model 取平均估计奖励 r̂,并加入不确定性惩罚与 entropy penalty(缓解 [[matthew-effect]])。

- **Selector(选择器 agent)**:为当前用户搜索 reference users(参考用户),其直觉是相似用户的偏好可以"动态地代表"当前用户。formulate 为一个 RL 任务,状态包含 recommendation steps 与 selection steps 两部分,用 [[transformer]] 作为 transition 的序列模型。selector 的 intrinsic reward 由三部分组成(Eq.12):单步推荐奖励 r̂、similarity gain(选中用户反馈向量与当前用户的 cosine 相似度)、diversity gain(选中用户之间的差异,保证代表性与信息量)。selector 用 [[actor-critic]] 的 A2C 训练。

- **Dynamic Recommender Reward Modeling**:不同于 ROLeR 的一次性、静态 reward shaping,DARLR 在每个推荐步用 selector 找到的 reference user 集合 u_{S,t} 对奖励做平均(Eq.15),从而沿着学习过程**持续**缓解 world model 的奖励不准确性。

- **Uncertainty Design**:设计了一个简单而有效的相似度感知不确定性惩罚(Eq.16),利用 selector 的 similarity gain 与 diversity gain 来灵活估计当前动作的风险;当奖励预测相对上一轮剧烈变化时,若 similarity/diversity gain 表明选中集合足够有代表性则可接受,否则约束对应动作的选择概率。该惩罚也可随策略学习动态演化(Eq.17),并保留 entropy penalty 鼓励多样性。

- **Recommender(推荐 agent)**:管理用户与 RecSys 的交互,学习提升长期用户参与度的推荐策略;以 item embedding 作为 action,用 Transformer 作为 state tracker(沿用 DORL/ROLeR),A2C 训练。整体训练见 Algorithm 1:前向中双 agent 采样,反向用 TD loss 更新两个 critic、advantage gradient 更新两个 actor。

## 结果

在四个 benchmark 数据集上实验:[[kuairand]]、[[kuairec]]、[[coat]]、Yahoo(Yahoo R3 音乐评分,见 [[yahoo-r3]])。所有方法共享同一个 DeepFM world model。基线分三类:naive(ϵ-greedy、[[ucb]])、model-free RL([[sqn]]、[[bcq]]、[[cql]]、[[crr]])、model-based RL([[ips]]、[[mbpo]]、[[mopo]]、[[dorl]]、ROLeR 即 [[rlur]]),并以 GT (Ideal)(用 ground-truth 奖励训练)作为上界。指标:R_tra(平均累计奖励,反映长期满意度)、R_each(平均单步奖励)、Length(平均交互轨迹长度)、MCD(Majority Category Domination,多样性参考指标,仅适用于 KuaiRand/KuaiRec)。

主要数字(Bold 为最佳,DARLR 标注 Ours;数据集统计:KuaiRand 27285 用户/7551 item 密度 0.697%,KuaiRec 7176 用户/10728 item 密度 16.277%,Coat 290/300 密度 8.046%,Yahoo 15400/1000 密度 2.024%):

- **KuaiRand**:DARLR R_tra = 13.8152(GT 上界 14.3689),优于次优 ROLeR 13.4553;R_each = 0.4670;Length = 29.2028。
- **KuaiRec**:DARLR R_tra = 35.2203(GT 36.7475),显著优于次优 MBPO 12.0426 等;R_each = 1.2600;Length = 27.3526。
- **Coat**:DARLR R_tra = 78.0429(GT 80.0895),优于次优 UCB 73.6713;R_each = 2.6014;Length = 30.0(满)。
- **Yahoo**:DARLR R_tra = 68.5418(GT 68.8791),优于次优 MOPO 65.5098;R_each = 2.2847;Length = 30.0。

结论:DARLR 在四个数据集的累计奖励 R_tra 上全面取得最佳,接近 GT 上界,验证了 dynamic reward shaping 的有效性;并通过收敛曲线显示 dynamic reward 比 static(frozen)reward 收敛更快、更优(原文 Figure 1)。

## 在本 wiki 中的位置

本文属于 RL-based 推荐系统(参见 [[rl-based-recsys]])与 model-based [[offline-rl]] 的交叉,直接承接并改进 [[dorl]] 与 ROLeR([[rlur]])两条工作线:把它们的静态 reward / 一次性 reward shaping 升级为训练过程中的动态精炼,并引入一个 selector agent 形成 [[multi-agent-reinforcement-learning]] 结构。它与本 wiki 中关于 [[world-model]] 不准确性、不确定性惩罚([[mopo]])、[[matthew-effect]] 缓解、长期用户满意度([[long-term-recommendation]]、[[user-retention]])的内容相关,可作为"动态 reward shaping + 双 agent"在 RecSys 中的代表性方案。
