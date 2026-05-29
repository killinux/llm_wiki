---
type: source
subtype: paper
tags:
  - offline-rl
  - recommender-system
  - decision-transformer
  - reward-relabeling
  - max-entropy
created: 2026-05-29
updated: 2026-05-29
arxiv: 2406.00725
raw: raw/2406.00725.pdf
authors:
  - Xiaocong Chen
  - Siyu Wang
  - Lina Yao
year: 2024
---

# Maximum-Entropy Regularized Decision Transformer with Reward Relabelling for Dynamic Recommendation (EDT4Rec)

EDT4Rec 是一个面向动态推荐的 offline RL 模型,通过给 [[decision-transformer]] 引入最大熵探索策略和基于 Q-function 的 reward relabeling,解决其在推荐场景中缺乏 stitching 能力、在线探索不足的问题。

## 问题

基于 RL 的 [[recommender-systems|recommender-system]](RLRS)能利用用户反馈作为 reward 持续优化推荐策略,但在线 RL 存在数据效率低、依赖仿真环境的问题。Offline RL 用预收集数据训练可缓解此问题,[[decision-transformer]](DT)是其中代表,已有 CDT4Rec([[causal-inference]] 估计 reward)、DT4Rec 等实现。但直接把 DT 用于推荐有两个核心缺陷:

1. **缺乏 stitching 能力**:推荐场景 offline 数据高度稀疏,可能没有足够的 expert(最优且 dense)轨迹。vanilla DT 无法从 sub-optimal 轨迹中学习,即无法把多条次优轨迹拼接(stitching)成更优轨迹。例如三条点击序列轨迹,reward 为 0 的轨迹被视为次优,但其中片段可与正 reward 片段组合成新的高 reward 轨迹。
2. **在线探索不足**:DT 认为 offline 数据已覆盖所有可能,在 fine-tuning 在线环境时会放弃探索;而用户兴趣是动态变化的,offline 数据无法完整反映用户意图,需要持续探索。

## 方法

EDT4Rec 以 causal [[decision-transformer]] 为骨干,受 SAC([[reinforcement-learning]] 中的 Soft Actor-Critic)启发,做两处关键改造:

- **Max-Entropy Enhanced Exploration(最大熵增强探索)**:把 DT 的确定性策略改为随机策略(连续动作空间用对角协方差的多元高斯分布),训练目标从 MSE 改为最小化负对数似然(NLL)。在此基础上加入策略熵约束 $H_\theta^\mathcal{T}[a|s,g] \ge \beta$,通过 Lagrangian 对偶求解,交替优化策略参数 $\theta$ 与温度变量 $\lambda$。与 SAC 的区别:其熵在序列层面(对 K 个连续 timestep 取平均)而非 transition 层面计算;损失基于 NLL 而非 discounted return,本质是在受控偏差下逼近观测数据分布。
2 个全连接层在输出端分别预测策略的均值和 log 方差。

- **RTG Relabeling(return-to-go 重标注)**:不再用整条轨迹 reward 之和做条件,而是用学到的 Q-function 重标注 RTG,从而让 reward conditioning 也能利用次优轨迹中的优质片段,获得 stitching 能力。Q-function 用 [[cql]](Conservative Q-Learning)学习其下界估计,只在 RTG 低于 CQL 估计的下界值时才替换(选择性 relabel),并通过 reward recursion $R_{t-1}=r_{t-1}+R_t$ 向前传播。为避免 relabel 破坏 reward 与 RTG 的一致性,设计了 Algorithm 1 的两步重标注(先 relabel $R_T$,再考虑一致性重算 $\hat R_T$)。论文引用 CQL 的 Lower Bound 定理论证 relabel 后的 RTG 更接近最优值函数。

训练时在线 goal $g_{online}$ 和 context length $K$ 都设为 2。在线 fine-tuning 时维护 replay buffer,按轨迹长度比例采样(Algorithm 2)。

## 结果

在 6 个公开 offline 数据集([[kuairand]] Kuairand-1k-15policies、LibraryThing、[[movielens]] MovieLens-20M、GoodReads、Netflix、Book-Crossing)和 VirtualTB 在线仿真平台上评测,指标为 Recall / Precision / nDCG(offline)和 CTR(online)。Baseline 包括 [[ddpg]]、[[sac]](确定性版)、[[td3]]、[[decision-transformer]](DT)、DT4Rec、CDT4Rec。

- **offline 全面领先**(Table 1,均在 95% 置信区间下显著):Kuairand-1k 上 EDT4Rec Recall 31.256、Precision 31.322、nDCG 31.321,优于次优的 CDT4Rec(30.322 / 30.014 / 30.525)。LibraryThing 上 Recall 16.021 vs CDT4Rec 14.768。MovieLens-20M 上 Recall 20.314、nDCG 18.234。GoodReads 上 Recall 14.144。Book-Crossing 上 Recall 10.345。Netflix 上 Recall 16.541。
- DT 类方法整体优于传统 RL(DDPG/SAC/TD3),归因于 transformer 的高表达力;DT、DT4Rec、CDT4Rec 均弱于 EDT4Rec,印证 DT 缺乏探索能力、预训练阶段接近 behavior cloning 的论断。
- **online(VirtualTB,Figure 3a)**:EDT4Rec 的 CTR 显著优于所有 baseline。超参研究显示 $g_{online}$ 和 $K$ 均设为 2 时性能最佳。
- **消融实验(Figure 4)**:EDT4Rec-E(去掉在线探索)早期因纯利用略优,但随着遇到陌生状态而性能下滑;EDT4Rec-R(去掉 reward relabeling)CTR 显著下降,印证两个组件的必要性,也支持"DT 缺乏 stitching"的主张。

## 在本 wiki 中的位置

本文属于 [[offline-rl]] 与 [[recommender-systems|recommender-system]] 的交叉工作,把 [[decision-transformer]] 范式扩展到动态推荐。它与同系列的 CDT4Rec(用 [[causal-inference]] 估 reward)、DT4Rec(vanilla DT 用于推荐)、研究 [[matthew-effect]] 的工作同属 RLRS 方向。其核心技术借鉴了 [[sac]] 的最大熵思想与 [[cql]] 的保守 Q-learning 下界,reward relabeling 思路与 [[off-policy-evaluation]] / [[doubly-robust]] 等 debiasing/value 估计方法相关。stitching 与 sub-optimal trajectory 学习是 [[offline-rl]] 的经典议题。
