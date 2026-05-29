---
type: source
subtype: paper
tags:
  - recommender-system
  - interactive-recommendation
  - fairness
  - reinforcement-learning
  - diffusion-model
  - hierarchical-reinforcement-learning
  - popularity-bias
  - state-representation
created: 2026-05-29
updated: 2026-05-29
arxiv: 2603.03820
raw: raw/2603.03820.pdf
authors:
  - Yun Lu
  - Xiaoyu Shi
  - Hong Xie
  - Xiangyu Zhao
  - Mingsheng Shang
year: 2026
---

# Fairness Begins with State: Purifying Latent Preferences for Hierarchical Reinforcement Learning in Interactive Recommendation

提出 DSRM-HRL:先用扩散模型把被 popularity bias 污染的用户状态"提纯"回真实偏好流形,再用分层 RL 解耦长期公平与短期参与,从而把交互推荐中的公平问题从"reward shaping"重构为"state estimation"问题。

## 问题

交互式推荐系统(Interactive Recommender Systems, IRS)普遍用 [[reinforcement-learning]] 优化长期累积收益,但 RL 会放大 "rich-get-richer" 现象,导致 item-side 的 [[exposure-bias]](热门物品被反复曝光,长尾物品得不到公平曝光)。

作者指出,现有 [[fairness]]-aware 方法存在一个根本性疏忽:它们都假设观测到的 user state 是真实偏好的忠实表示,因而只在 decision level 做干预(给 reward 加 fairness penalty,或对 policy 输出加约束)。但实际中 implicit feedback 被 [[popularity-bias]] 噪声严重污染(epistemic uncertainty),观测状态是被扭曲的状态,误导 RL agent。因此 accuracy 与 fairness 的持续冲突"不是 reward 设计问题,而是 state estimation 失败"。

实现这一思路面临三个挑战:
- C1 非线性 bias 重建:popularity bias 不是高斯白噪声,而是偏好流形上的系统性非线性结构,传统 denoising autoencoder / 线性滤波会导致 "information collapse"。
- C2 信号保留 vs. 噪声消除:过度去噪会抹掉个性化所需的细粒度行为信号。
- C3 多目标的时间冲突:item-side fairness 是长期轨迹目标,而 accuracy 是即时短期目标,单层 agent 同时处理二者会产生梯度干扰与训练不稳定。

## 方法

整体框架 DSRM-HRL 分两阶段:latent state purification + decoupled hierarchical constrained control。

实证动机(第 3 节,三个发现):
- Observation 1(spurious feedback loop):item 流行度与平均 reward 存在强线性相关(R² > 0.85),系统学到的是"曾经强制曝光给用户看的东西",而非用户真正喜欢的。
- Observation 2(input-side bottleneck):仅对 state 做提纯、不改 policy/reward,即可同时提升 accuracy 与 equity。
- Observation 3(manifold collapse):用 t-SNE 分析,raw state 空间里用户按 popularity 聚类,而 interest 类别高度纠缠不可分。

DSRM(Denoising State Representation Module),解决 C1/C2:把 state purification 建模为 conditional generative 问题,学习算子 Π_θ: ℝ^d → M 把污染状态映射回 latent preference manifold。
- 假设真实偏好位于低维流形 M,观测状态 s̃_t = M(s*_t) + ζ_pop(structured epistemic noise)。
- Forward process:对编码后的 state 在 K 步内逐步注入高斯噪声(模拟极端曝光偏置下的偏好信号退化)。
- Reverse process:用 [[diffusion-model]] 的反向去噪过程做"iterative probabilistic manifold projection",迭代恢复低熵偏好表示,得到提纯状态 ŝ_t = Π_θ(s̃_t)。
- state 编码用 [[transformer]] 对历史交互序列(含 position/history embedding)做编码。

HRL(Hierarchical Constrained Control),解决 C3:用 [[hierarchical-reinforcement-learning]] 把宏观公平调控与微观参与优化解耦。
- High-level Manager(fairness regulation):输出策略控制变量 z_t = [ω_acc, ω_fair],动态定义当前 fairness 约束;优化生态系统级目标 r^h_t = r_t + λ·Fair(L_t),其中 Fair(·) 用负 Gini 系数衡量长期曝光公平。
- Low-level Worker(utility optimization):在可行 fairness 流形内最大化即时参与,对候选 item i 计算 Ψ(i; ŝ_t, z_t) = ω_acc·Sim(ŝ_t, e_i) − ω_fair·log(pop_i);形式上是约束优化 max E[R_acc] s.t. E[R_fair] ≥ z_t。

联合优化(Purify-then-Decouple):
- Stage I:先预训练 DSRM,用 noise reconstruction loss L_DSRM = E‖ε − ε_θ(s^(k), k, s̃_t)‖²。
- Stage II:固定 DSRM,用 [[ppo]] 联合训练两个分层 policy,梯度分离缓解学习干扰。

## 结果

环境用高保真模拟器 [[kuaisim]],基于真实数据集 [[kuairec]](train 7,176 users / 10,728 items / 12,530.8k interactions;test 1,411 / 3,327 / 4,676.5k)和 [[kuairand]]-Pure(train 26,285 / 7,551 / 1,436.6k;test 27,285 / 7,583 / 1,186.1k)。引入 popularity-based grouping(top 20% popular vs. 余下 80% long-tail)与 fairness-aware abandonment(反复推热门则会话提前终止)。Max Len 设 30 和 50。

评测指标:Interaction Length(Len,长期留存)、Cumulative Reward(R_cum)、Single-step Reward(R_each,短期相关性)、Absolute Difference(AD,组间曝光差,越低越公平)。

Baselines:general RL(A2C、[[td3]]、[[bcq]])与 fairness-aware RL(MOFIR、DORL、DNaIR、SAC4IR)。结果跑 3 个随机种子取平均。

主要结果(RQ1,Table 2):
- KuaiRec(Max Len = 30):DSRM-HRL 平均 interaction length 达 26.600,比最强 fairness baseline SAC4IR(21.967)高 21.1%,比最强 general RL baseline BCQ(20.800)高 27.9%;同时取得最高 R_each(0.917)和有竞争力的 AD(0.008)。
- KuaiRand-Pure(Max Len = 30):Len 24.067、R_each 0.849、R_cum 19.750、AD 0.011,综合最优。
- BCQ 虽 AD 很低(保守策略),但 Len 远不及本方法。A2C/TD3 等 AD 偏高(曝光失衡),会话提前终止。

消融(RQ2,Table 3):
- FLAT(DSRM + 单层 RL)在 KuaiRec(Max Len=30)Len 仅 24.333,低于完整版 26.600。
- HRL(无 denoising)Len 23.167,低于完整版,说明分层控制单独不够。
- HRL + 启发式去噪(+RCE/+TCE/+BOD)严重退化,如 KuaiRec 上 HRL+RCE 仅 15.167,远低于 23.167,说明传统去噪靠刚性假设、会扭曲 state。完整 +DSRM 版本最佳。

扩散步数敏感(RQ3):步数在 10~30 附近最优;增到 100/500 出现 over-smoothing(KuaiRec 上 Len 在 500 步降到 14.7),去噪过度会连个性化信号一起抹掉,得到低熵但信息贫乏的表示。

计算效率(RQ4,Table 4,KuaiRec Max Len=30 / Episode=20,000):DSRM-HRL 训练 15,909 秒,约为 DNaIR 的 2.1×、SAC4IF 的 2.3×,但远低于启发式去噪 RCE(29,919 秒);因为扩散在 compact latent state 而非 raw feature 上操作,推理仍适合部署。

收敛与稳定性(RQ5,Figure 7):DSRM-HRL 在两个数据集上收敛更平滑、方差更低,Interaction Length 单调上升且更早饱和,AD 快速下降并保持低位,说明 fairness 约束被分层控制内化,而非靠不稳定外部惩罚强加。

另:第 3.2 节报告,在 DNaIR policy 上仅加 DSRM 去噪即在 KuaiRec 上 AD 改善 88%、interaction length 提升 18.4%。

## 在本 wiki 中的位置

本文属于 [[rl-based-recsys]] 与 [[interactive-recommendation]] 中的公平性方向,核心论点是把 [[provider-fairness]] / item-side [[exposure-bias]] 问题从 [[reward-shaping]] 重新定位到 state 表示的提纯。

- 与 [[popularity-bias]]、[[matthew-effect]]、[[filter-bubble]] 等推荐偏差主题直接相关;用 negative Gini(AD)度量曝光公平,呼应 [[two-sided-fairness-reranking]] / [[minimum-exposure-guarantee]] 等公平方法,但走的是 state-purification 路线。
- 方法上把 [[diffusion-model]] 当作 representation purifier(而非生成器),与 [[dreamrec]]、[[diffusion-models]] 在推荐中的生成式用法形成对比;state 编码用 [[transformer]]。
- RL 侧采用 [[hierarchical-reinforcement-learning]] 解耦长期/短期目标,用 [[ppo]] 训练,与 [[constrained-mdp]]、[[lagrangian-relaxation]] 等约束优化思路相关;baselines 覆盖 [[td3]]、[[bcq]] 等 [[offline-rl]] 方法。
- 实验生态对接 [[kuaisim]] 模拟器与 [[kuairec]]、[[kuairand]] 数据集([[kuaishou]] 短视频场景),与 [[dorl]]、[[cirs]] 等同一评测体系下的 [[long-term-recommendation]] / [[user-retention]] 工作可比较。
