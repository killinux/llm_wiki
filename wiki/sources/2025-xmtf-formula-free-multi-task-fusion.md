---
type: source
subtype: paper
tags:
  - recommender-system
  - multi-task-learning
  - reinforcement-learning
  - watch-time
  - actor-critic
title: "xMTF: A Formula-Free Model for Reinforcement-Learning-Based Multi-Task Fusion in Recommender Systems"
arxiv: "2504.05669"
raw: raw/2504.05669.pdf
authors:
  - Yang Cao
  - Changhao Zhang
  - Xiaoshuang Chen
  - Kaiqiao Zhan
  - Ben Wang
year: 2025
created: 2026-05-29
updated: 2026-05-29
---

# xMTF: A Formula-Free Model for Reinforcement-Learning-Based Multi-Task Fusion in Recommender Systems

一句话:xMTF 用「单调融合单元(Monotonic Fusion Cell, MFC)」替代多任务融合(MTF)中预定义的融合公式,把基于 [[reinforcement-learning]] 的 MTF 从「只调几个公式系数」变成「学习任意单调融合函数」,并用两阶段混合(TSH)训练,在 Kuaishou 线上服务超过 1 亿用户。

## 问题

工业级 [[recommender-systems|recommender-system]] 需要优化多种用户反馈(click、like、share、watch time 等)。典型系统分两步:[[multi-task-learning]](MTL)模块预测各类反馈的概率(如 [[ctr]]、like rate),再由 **多任务融合(Multi-Task Fusion, MTF)** 模块把这些预测融合成单一排序分。MTF 直接决定推荐结果,对用户满意度至关重要。

近年来用 [[reinforcement-learning]] 做 MTF 成为热点:把用户视作环境、推荐系统视作 agent、融合权重视作 RL 的 action,以优化 [[watch-time]] / retention 等长期回报。但**现有 RL-based MTF 全是「公式化」(formula-based)方法**:先人为定义一个融合公式 $f(o_1,\dots,o_K; a_1,\dots,a_K)$,RL 只优化其中少数系数 $a_k$。这带来两个缺陷:

- 不同公式给出不同推荐结果,难以确定最优公式,且不同用户可能适配不同公式;
- 预定义公式严重限制了 MTF 的搜索空间,导致性能上限受限。

## 方法

论文提出**无公式(formula-free)** 框架 **eXtreme MTF (xMTF)**:

- **理论基础(Sprecher 表示定理)**:任意「合适的」融合函数 $f(o_{1i},\dots,o_{Ki})$ 都可写成 $g\big(\sum_{k=1}^K h_k(o_{ki})\big)$,即若干单变量单调递增函数 $h_k$ 之和再经外层单调函数 $g$。由于 $g$ 不改变排序结果集,可省略,只需学习每个预测的单调变换 $h_k$。
- **单调融合单元(MFC)**:用可学习的、以用户状态 $s_t$ 为额外输入的函数 $\tilde h_k(o_{ki}, s_t; \theta_k)$ 取代预定义公式,并用一项 pairwise **单调性损失** 显式保证输出对输入预测单调。MFC 因此(1)保留 MTF 内在的单调性结构、可解释;(2)可学习、扩大搜索空间;(3)为不同用户、不同预测提供**个性化融合函数**,而公式化方法只能个性化少数系数。
- **两阶段混合训练(Two-Stage Hybrid, TSH)**:更大的搜索空间使训练困难,现有 RL 方法不能直接用。于是把每个 MFC 拆成两级——
  - **外层(outer stage)**:参数少($a_k$),用 RL 优化长期用户体验。采用 [[actor-critic]] 结构(actor $\mu(s_t;\xi)$ 产生 action,[[critic]] $Q(s_t,a_t;\phi)$ 估计长期回报),与 [[ddpg]]/[[td3]]/[[sac]] 同类。
  - **内层(inner stage)**:参数多([[mlp]]),用监督学习以保证收敛;用外层输出做标签,通过 [[bpr]] pairwise loss 做**知识迁移**,让表达力更强的内层吸收外层学到的长期偏好。
  - MTF 问题被建模为 [[markov-decision-process]],目标是最大化整个 session 的折扣长期回报。

## 结果

- **离线数据集**:KuaiRand([[kuairand]],Kuaishou 公开数据集,含 27,285 用户、32,038,725 items)。MTL 用 [[mmoe]] 生成预测;以 **Total Watch Time(s)** 为评测指标,每实验跑 20 次取均值。
- **离线对比(Table 3,Total Watch Time)**:[[cem]]-1/2 = 897.5 / 931.2;[[td3]]-1/2 = 1088.7 / 1129.1;BatchRL-MTF-1/2 = 1137.3 / 1185.4;TSCAC-1/2 = 1153.3 / 1194.7;MR-MPL-1/2 = 1145.3 / 1189.6;**xMTF = 1279.7**(明显最优)。消融:去掉外层(无 RL 长期建模)= 1092.8,去掉内层(退化为公式化 $z_i=\sum o_{ki}(1+a_k o_{ki})$)= 1106.3,均显著差于完整 xMTF。
- **超参 $\lambda$(单调性损失权重)**:$\lambda=0$(无单调性约束)= 732.8,$\lambda=0.4$(最优)= 1279.7,$\lambda=1$(纯单调性、无监督迁移)= 1103.1,说明单调性与监督迁移都不可或缺。
- **线上 A/B(短视频平台,>1 亿用户,流式持续训练,约两天收敛)**:相对最强基线 [[aitm|UNEX-RL]] 取得 **Daily Watch Time +0.833%**、Play Counts +0.583%、Comment +2.391%、Share +2.205%。论文指出平台上 +0.1% watch time 即统计显著,+0.833% 是当年最大增益之一。已**全量部署上线**。

## 在本 wiki 中的位置

本文位于 [[recommender-systems|recommender-system]] 的「[[multi-task-learning]] → 多任务融合」环节,与 [[rl-based-recsys]] / [[long-term-recommendation]] 强相关:

- 它把 MTF 从「公式 + 调系数」推进到「学习任意单调融合函数」,与同组的 UNEX-RL、BatchRL-MTF、TSCAC 等公式化 RL MTF 工作形成对照,基线还包括 [[cem]]、[[td3]]。
- 训练上结合 [[actor-critic]]([[ddpg]]/[[td3]]/[[sac]] 同族)与监督 [[bpr]] 知识迁移,问题建模为 [[markov-decision-process]],以 [[watch-time]] 为长期回报,呼应 wiki 中以 [[reinforcement-learning]] 优化 [[user-retention]]/长期目标的一类推荐工作。
- 数据集 [[kuairand]]、MTL 骨干 [[mmoe]]([[mixture-of-experts]] 家族)与 [[ple]] 等多任务学习方法相关。

出品方:[[kuaishou]] Technology(与 Peking University 合作)。
