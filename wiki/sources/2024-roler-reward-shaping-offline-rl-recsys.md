---
type: source
subtype: paper
tags: [offline-rl, recommender-system, reward-shaping, model-based-rl, uncertainty-estimation, world-model]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2407.13163
raw: raw/2407.13163.pdf
authors: [Yi Zhang, Ruihong Qiu, Jiajun Liu, Sen Wang]
year: 2024
---

# ROLeR: Effective Reward Shaping in Offline Reinforcement Learning for Recommender Systems

ROLeR 提出一种非参数(基于聚类/kNN)的 reward shaping 方法与解耦的不确定性惩罚,用以修正 model-based [[offline-rl]] 推荐中 world model 的不准确 reward 估计,在四个 benchmark 上达到 SOTA。

## 问题

[[offline-rl]] 是为真实 [[recommender-system]] 建模用户动态兴趣的有效工具。主流做法是 model-based RL:先从离线日志数据学一个 [[world-model]],再让推荐策略与该 model 交互来学习。但这类方法的效果受限于两点:reward model 估计的准确性,以及 model 的不确定性。根本原因是离线日志数据与真实在线用户交互之间存在巨大分布差异。

作者在 [[kuairec]] 上展示:SOTA 方法 [[dorl]] 的 reward 预测误差在所有 reward 区间都偏高(论文 Figure 1)。在 reward 估计不准的情况下,无论策略保守还是鼓励探索都难以从离线数据中学好。此外,现有方法的不确定性估计通常依赖 [[world-model]] 的 ensemble,把 world model 学习与不确定性惩罚不必要地绑定在一起。

## 方法

ROLeR 沿用 [[dorl]] 的两阶段 model-based 流程(world model 学习 + 在该环境上训练推荐策略),策略学习采用 Advantage Actor-Critic([[actor-critic]] / A2C)。核心贡献是两个相互配合的模块:

- **非参数 reward shaping(训练无关)**:观察到在短时间窗口内相似用户对一组物品的反馈相近,可形成 cluster。用用户的历史交互或 world model 学到的 user embedding 作为 indicator feature(软标签),用 soft-label kNN 在离线数据中检索最近邻用户,再聚合这些邻居对某物品的反馈来修正 reward 估计(论文 Eq.14,平均聚合,距离用 cosine distance)。这是一个简单但有效的聚类式非参数 reward 修正,不需训练。
- **基于聚类质量的不确定性惩罚**:用一个用户与其最近邻之间的距离作为不确定性度量(Eq.15),作为 reward shaping 的互补项。聚类质量差(邻居距离远)即视为高不确定性,从而避免冒险推荐。这一设计**摆脱了对 world model ensemble 的依赖**。

最终用于策略学习的 reward 形如 `r = r̂ × (1 − P̃_U) + λ_E P_E`(Eq.16),其中 P_E 为来自 DORL 的 entropy penalty(对抗 Matthew Effect)。论文还给出了 Performance Lower Bound 的理论分析:在 Lipschitz 连续假设下,证明当用户行为足够形成有意义聚类且离线数据稀疏程度有限时,所学策略的价值函数有下界(Theorem 1)。实现上还把 DORL 的 average state tracker 换成 attention / Transformer state tracker(SASRec 风格)以保留交互顺序信息。

## 结果

- **数据集**:四个 benchmark —— [[kuairand]](KuaiRand-Pure)、[[kuairec]](KuaiEnv)、[[coat]]、[[yahoo-r3]](Yahoo)。
- **基线**:ε-greedy、UCB、SQN、[[bcq]]、[[cql]]、CRR、MBPO、[[mopo]]、[[inverse-propensity-scoring]](IPS)、[[dorl]]、[[cirs]];以及用测试环境 reward 训练的 GT Reward 作为性能上界参考。
- **主指标**:cumulative reward(R_tra),另含 average interaction length 与 single-step reward(R_each)、Majority Category Domination(MCD)。
- **整体表现**:ROLeR 在四个数据集的 cumulative reward 上均显著超过所有基线,逼近 GT Reward 上界。例如 KuaiRec 上 R_tra 约 33.25(GT Reward 约 36.75),KuaiRand 上 R_tra 约 13.46;在 Coat、Yahoo 上同样取得 best。ROLeR 在 KuaiRec/KuaiRand 上能更早、更稳地把 interaction length 推到上界(约 30 步),并取得最接近参考策略的 single-step reward,在 KuaiRec 上 single-step reward 大幅领先(印证 reward 更准)。
- **消融(RQ2)**:reward shaping 与 uncertainty penalty 单独都能提升 cumulative reward;去掉不确定性惩罚或换成 world-model 版本均会下降,reward shaping 的贡献尤其显著。
- **不确定性设计(RQ3)**:对比多种变体(r×λ/d、高斯采样 N(r,λd)、r−λd_min/avg/max、r×(1−d) 等),基于 cosine distance 的 1−d 加权聚合变体在多数数据集上最稳健。
- **鲁棒性(RQ5)**:对最近邻数 k 在较大范围内变化稳定(cumulative reward 变动通常 <2),且不同 k 均稳定超过 SOTA。
- 硬件:NVIDIA RTX A6000(48GB),每个数据集 world model <3 GPU 小时,每次 ROLeR trial ≤2 GPU 小时。发表于 CIKM '24。

## 在本 wiki 中的位置

本文属于 [[reinforcement-learning]] × [[recommender-system]] 交叉方向,具体是 model-based [[offline-rl]] for RecSys 这一支。它直接改进自 SOTA 方法 [[dorl]],与 [[cirs]]、[[mopo]]、[[bcq]]、[[cql]] 等 [[offline-rl]] 方法同属一个评测谱系,并大量使用 [[kuairec]]、[[kuairand]]、[[coat]]、[[yahoo-r3]] 等推荐 benchmark。其核心思想——用基于聚类/kNN 的非参数方法修正 [[world-model]] reward 估计、并用聚类质量替代 ensemble 做不确定性度量——与 wiki 中关于 [[world-model]]、不确定性估计与 reward model 的概念相关,可作为离线 RL 推荐方向中"reward 准确性比策略保守/探索更关键"这一观点的代表性论据。
