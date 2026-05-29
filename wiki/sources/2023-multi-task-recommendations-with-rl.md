---
type: source
subtype: paper
tags: [multi-task-learning, recommender-systems, reinforcement-learning, actor-critic, ctr-prediction, ctcvr]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2302.03328
raw: raw/2302.03328.pdf
authors: [Ziru Liu, Jiejie Tian, Qingpeng Cai, Xiangyu Zhao, Jingtong Gao, Shuchang Liu, Dayou Chen, Tonghao He, Dong Zheng, Peng Jiang, Kun Gai]
year: 2023
---

RMTL 用 actor-critic 强化学习框架,把推荐系统的多任务损失按 session 级序列动态加权组合,取代固定常数权重的线性加权,在 RetailRocket 与 Kuairand 两个公开数据集上提升了 CTR/CTCVR 预测的 AUC。

## 问题

[[multi-task-learning]](MTL)在推荐系统中广泛用于同时学习多个目标(如 CTR 与 CTCVR),但现有 MTL 推荐模型存在两个被忽视的问题:

- **数据层面:item-wise 而非 session-wise。** 现有方法的输入大多是基于单个 item 的特征嵌入与 user-item 交互,忽略了真实推荐场景中更普遍的 session 级序列模式。比如短视频/电商中点击与转化往往发生在同一 session 内、带有时序相关性。
- **损失加权:固定常数权重。** 多目标损失函数通常用线性标量化(linear scalarization)把各任务损失按固定常数权重相加,这种 item-wise 多目标损失难以保证全局最优收敛,且任务间可能存在冲突,预测性能受限。

本文聚焦电商/短视频中的 CTR/CTCVR 预测(K=2),提出用 RL 动态生成损失权重来解决上述两点。

## 方法

提出 **RMTL(Reinforcement-enhanced MTL)** 框架,核心是把多任务推荐建模成 [[markov-decision-process]](MDP)并用 [[actor-critic]] 框架训练:

- **Session MDP 构建。** 按 session id 组织交互记录:state 为 user-item 组合特征,action 为两个任务的连续预测值 (a_1,t, a_2,t) ∈ [0,1]^2(分别对应 CTR 与 CTCVR),reward 用负 BCE 定义 r_k,t = y log(a) + (1-y) log(1-a),transition 沿用户交互序列、概率为 1,折扣 γ = 0.95。
- **Actor 网络(策略)。** 采用兼容现有 MTL 模型的 two-tower 多任务骨干作为 actor,输出每个任务的确定性预测值。整体损失为各任务 BCE 的加权和,权重由 critic 生成。
- **Critic 网络(权重生成)。** 设计共享一个 bottom 层的双 MLP critic,为每个任务输出 Q 值;损失权重通过对 Q 值做线性变换(带 punish 变量 λ)得到:ω_k,t = 1 − λ·Q(s_t, a_k,t; φ_k),从而沿改善策略决策的方向反向调整目标损失权重。
- **稳定训练。** 借鉴 DDPG,引入 target actor / target critic 网络,用 TD error 更新 estimation critic、用平均 Q 值梯度更新 actor,并对 target 网络做软更新(soft update rate β = 0.2)。先用预训练 MTL 参数初始化并冻结到 critic 收敛,再重训。

RMTL 与多数现有 MTL 模型兼容,文中在 ESMM、[[mmoe]]、[[ple]] 三种主流 MTL 骨干上实现。默认 λ = 0.7,actor/critic 学习率分别为 1e-3 与 0.001。

## 结果

数据集:RetailRocket(电商,点击+购买序列标签)与 Kuairand-1K(短视频),按时间戳 6:2:2 划分,评估指标为 AUC、Logloss、s-Logloss(session 级 Logloss)。基线含 Single Task、Shared Bottom、ESMM、MMoE、PLE 及 RL 基线 D-PLE。

- 每个 RMTL 版本(RMTL-ESMM/MMoE/PLE)在 AUC 与 Logloss 上均优于对应非 RL 基线。RetailRocket 上 RMTL 相对对应基线获得约 **0.003-0.005 的 AUC** 提升。
- RetailRocket CTR:RMTL-MMoE AUC 0.7350(MMoE 基线 0.7309);RMTL-PLE AUC 0.7339。RetailRocket CTCVR:RMTL-PLE AUC **0.7419**(PLE 基线 0.7387)。
- Kuairand CTR:RMTL-PLE AUC **0.7053**(PLE 基线 0.7026)。Kuairand CTCVR:RMTL-ESMM AUC 0.7377(ESMM 基线 0.7350)。
- 多数提升通过双侧 t 检验(p < 0.05)达到统计显著。s-Logloss 改善幅度小于 0.001。
- **可迁移性研究:** 从 ESMM/MMoE/PLE 预训练得到的 critic 网络可迁移到其他 MTL 基线,显著提升其 AUC、降低 Logloss。
- **消融研究(RetailRocket):** 对比 CW(常数权重)、WL(标签×Q 值加权)、NLC(直接用负 Q 值、不做线性变换)三种变体,完整 RMTL-PLE 表现最佳(CTR AUC 0.7339,CTCVR AUC 0.7419),验证了线性组合权重设计与 critic 网络的有效性。

## 在本 wiki 中的位置

本文是把强化学习引入推荐系统多任务损失加权的代表工作,出自 WWW 2023,由 City University of Hong Kong 与 [[kuaishou]] 合作完成。它把 actor-critic 与 ESMM/MMoE/PLE 等经典 MTL 架构结合,提供了一个可插拔的损失权重动态调整方案。可与 [[multi-task-learning]]、[[mmoe]]、[[ple]]、[[actor-critic]]、[[markov-decision-process]] 等条目交叉参考。
