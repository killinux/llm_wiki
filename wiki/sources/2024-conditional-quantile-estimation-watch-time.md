---
type: source
subtype: paper
tags:
  - recommender-system
  - watch-time
  - quantile-regression
  - duration-bias
  - short-video
created: 2026-05-29
updated: 2026-05-29
arxiv: 2407.12223
raw: raw/2407.12223.pdf
authors:
  - Chengzhi Lin
  - Shuchang Liu
  - Chuyuan Wang
  - Yongqi Liu
year: 2024
---

# Conditional Quantile Estimation for Uncertain Watch Time in Short-Video Recommendation

CQE 用 quantile regression 建模短视频 [[watch-time]] 的完整条件分布(而非单点期望),并据此设计三种推断策略适配不同推荐场景,在 [[kuaishou]] 数十亿日活平台上线取得显著收益。

## 问题

[[watch-time]](观看时长)是短视频推荐衡量用户兴趣与参与度的核心指标,准确预测它对优化推荐至关重要。但现有方法多只预测观看时长的**条件期望** E[W|x](单一平均值),忽略了用户行为内在的不确定性与异质性:

- 同一 user-video pair 在真实场景下几乎不可能在相同条件下被多次观测,无法直接估计真实条件分布。
- 单点平均值无法刻画不同 user-video pair 之间差异巨大的观看分布形态(峰位、离散度各异),限制了推荐性能。
- 论文用 interquartile range(IQR)在线上数据量化了这种分布离散度与预测精度的关系:窄分布(IQR ∈ [0.0, 0.1])预测准(UAUC 0.721,MAE 0.105),宽分布(IQR ∈ [0.5, 1.0])则差很多(UAUC 0.536,MAE 0.305)。

## 方法

提出 **Conditional Quantile Estimation(CQE)** 模型:

- **建模整个条件分布**:不再回归期望,而是用 [[quantile-regression]] 同时估计 N 个分位点 {τ₁,…,τ_N}(默认 N=100)对应的观看时长 {t_τ₁,…,t_τ_N}。
- **单调性架构**:网络 φ 输出经 ReLU 得到非负向量 d,再做累加求和 t_τᵢ = Σ_{j≤i} d_j,天然保证分位数估计的有序约束 t_τ₁ ≤ … ≤ t_τ_N。
- **训练目标**:对每个分位点用 **pinball loss**(分位回归损失,τ≠0.5 时非对称),聚合所有分位点损失 L_QR = Σ L_τᵢ。计算开销相比传统点估计仅略增。
- **三种推断策略(inference strategies)**,把多分位输出转化为最终预测:
  1. **Conservative Estimation(CSE)**:取较低分位(如 τ_low=0.25),用于看重用户满意度、过估代价高的场景,降低用户失望/流失风险。
  2. **Dynamic Quantile Combination(DQC)**:按上下文(用户 churn 风险、视频新颖度)用混合参数 k 在低/高分位间加权 ŷ = k·t_τlow + (1−k)·t_τhigh;高流失风险/新内容偏保守,反之偏激进。
  3. **Conditional Expectation(CDE)**:对相邻分位线性插值近似分布,恢复整体期望;N→∞ 时理论最优,用于以最大化总参与度为目标的全局优化。

CQE 还能与现有 [[duration-bias]] 去偏方法(如 [[d2q]]、[[d2co]]、[[wtg]])无缝集成。

## 结果

**在线 A/B(RQ1,[[kuaishou]] 数亿日活平台,各组 ≥10% 流量,运行 >1 周,CQE 接入排序阶段 MLP):**
- CSE:Average Watch Time per User +0.008%,Total Play Count **+0.346%**,active days +0.033%,active users +0.031%(在数亿日活下统计显著)。
- DQC:Watch Time +0.106%,Play Count +0.177%,并提升两项多样性指标。
- CDE:Watch Time **+0.165%**(显著),但 Play Count −0.088%(加深单视频参与、略减交互广度)。

**离线实验(RQ2/RQ3):**
- 观看时长预测(Table 6):在 [[kuairec]]/Kuaishou 与 CIKM16 数据集上,以 MAE 与 XAUC 评估,CQE_CDE 全面优于 WLR、[[d2q]]、OR、TPM、DML、CREAD —— Kuaishou MAE 4.437(最优)、XAUC 0.610;CIKM16 MAE 0.823、XAUC 0.694。
- 用户兴趣预测(Table 5/7):在 [[wechat-channels-dataset]](WeChat)与 [[kuairand]](KuaiRand-pure)上,以 GAUC 与 nDCG@k 评估,backbone 用 [[deepfm]]、[[autoint]]、DCNV2,标签设计用 PCR/[[wtg]]/[[d2co]]。CQE_CDE 在所有组合下均优于 MSE 与 CE 基线(如 DeepFM+D2Co+CQE_CDE 在 KuaiRand 上 GAUC 0.662、nDCG@1 0.452)。
- 分位数量消融(RQ3):观看时长预测中性能随 N 增大而提升;用户兴趣预测中 N>10 后趋稳(约 0.663)。

代码开源:https://github.com/justopit/CQE 。

## 在本 wiki 中的位置

本文是 [[kuaishou]] 出品的短视频 [[recommender-system]] 工作,聚焦 [[watch-time]] 预测,与本 wiki 中一系列 watch-time 去偏研究紧密相关:它对比并可叠加 [[d2q]](backdoor adjustment 去 [[duration-bias]])、[[d2co]](去偏去噪)、[[wtg]](Watch Time Gain)等方法,并复用 [[kuairand]]、[[kuairec]]、[[wechat-channels-dataset]] 等数据集与 [[deepfm]]、[[autoint]] 等 backbone。

值得注意的方法学桥接:CQE 用的 [[quantile-regression]] 与 pinball loss,正是分布式 [[reinforcement-learning]](distributional RL)以及 LLM [[rlhf]] 中分布式 [[reward-model]](论文引用了 Dorka 2024 的 quantile regression for distributional reward models in RLHF)所共享的工具——把"预测一个标量"升级为"预测整个分布",从而显式建模不确定性。这条线索把推荐系统的观看时长建模与 LLM 对齐中的奖励建模联系起来。
