---
type: source
subtype: paper
tags: [watch-time, duration-bias, debiasing, recommender-system, quantile-regression, short-video, causal-inference]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2508.11086
raw: raw/2508.11086.pdf
authors: [Emily Liu, Kuan Han, Minfeng Zhan, Bocheng Zhao, Guanyu Mu, Yang Song]
year: 2025
---

# Relative Advantage Debiasing for Watch-Time Prediction in Short-Video Recommendation

ByteDance 提出 RAD(Relative Advantage Debiasing):把观看时长(watch time)映射为「条件经验 CDF 分位数」,用 video ID 与 user ID 两个 umbrella 因子同时纠正多种混淆,得到无偏、有界、同方差的偏好信号,并用两阶段架构把分布估计与偏好建模解耦。

## 问题

在 TikTok / Reels 式沉浸短视频流中,点击、评分等显式反馈稀缺,[[watch-time]] 成为衡量用户兴趣的标准隐式代理。但原始观看时长被一系列与真实偏好无关的混淆因素污染:长视频天然累积更高时长([[duration-bias]]),还有内容流行度([[popularity-bias]])、用户个人观看习惯等。这些 [[confounding-bias]] 会扭曲偏好估计、导致系统过度推荐长视频。

既有工作多只针对 duration bias:按时长分桶后做分位归一化([[d2q]])、残差增益调整([[wtg]]/DVR)、反事实映射([[cwm]])等,对流行度、用户习惯等其它混淆保护有限。更近的 [[conditional-quantile-estimation]](CQE)、AlignPxtr 转而对每个 user-video 对建模完整条件分布,但受「单观测」问题困扰——同一用户极少重看同一视频,导致分布估计噪声大、易过拟合,且把分布拟合与推荐目标耦合在一起。

## 方法

**生成式建模**:把观测时长写成 $S_{u,i}=C_{u,i}+P_{u,i}+\varepsilon_{u,i}$(混淆项 + 真实偏好 + 噪声)。由全方差分解,目标是最小化「偏差方差」$\mathrm{Var}(E[S|C])$,让模型聚焦反映真实偏好的残差变化。

**Umbrella conditioning(伞式条件)**:不逐个纠正混淆,而是利用「许多细粒度混淆都是高层 ID 的确定性函数」——video ID 决定了时长/类别/创作者/流行度,user ID 决定了活跃度/设备/观看习惯。论文证明对 video ID 取条件比对任一单一 video 侧混淆取条件能去掉更多偏差方差(Proposition 1)。

**Conditional Quantile Transformation**:把每个观测时长替换为它在 umbrella 条件经验 CDF 下的分位数 $Q_{u,i}(G)=F_{S|G}(S_{u,i})$。论文证明该分位数标签均值 1/2、方差 1/12、且与混淆因子 $G$ 统计独立(Proposition 2)——即有界、同方差、去偏。

**RAD 两阶段**:
- Stage 1(标签估计):分别得到 video 侧 RAD-V($F_{S|i}$)与 user 侧 RAD-U($F_{S|u,d}$,因 user ID 不含时长信息,先按时长分 D≈4 个等质量桶再估)。
- Stage 2(偏好建模):用 MLP/DCN/DCNv2/GDCN 等 backbone 直接预测 RAD 标签,得到解耦、稳定的训练目标。

**Dual-sided Bayesian evidence fusion**:把两侧分位数经 probit 变换到 z-score 空间,按精度权重 α、β 加权融合再映回分位数(RAD-UV),按各侧统计支持度加权,在 cold-start 等单侧数据稀疏时更鲁棒。

**Learnable distribution embedding**:为在线部署免去存储/查询海量历史时长,把每个 umbrella 因子映射为可学嵌入,经共享 MLP 输出 K=100 个 logits,ReLU + 累加得单调递增分位函数,用 [[quantile-regression]] 训练,推理时无需外部查表。稀疏 cohort 用 K-modes 聚类成 10 组缓解。

## 结果

- **数据集**:[[kuairand]]-Pure(26,592 用户 / 7,146 物品 / 1,384,425 交互)与一个工业离线数据集(超 10 亿 user-video 交互,前 14 天训练、次日测试)。指标:MAE、XAUC、XGAUC。
- **观看时长预测(Table 1)**:RAD 全面优于 VR/PCR/WLR/[[wtg]]/[[d2co]]/[[d2q]]/[[cwm]]/CQE 等基线。以 MLP backbone 为例,MAE 从最优基线 D2Q 的 19.763 降至 RAD-V/RAD-UV 的 18.050;XAUC 从 CWM 的 0.7096 升至 RAD-UV 0.7178;XGAUC 0.6645 → 0.6725。RAD-UV 在各 backbone 上一致取得最优或接近最优。
- **相对偏好建模(Table 2)**:在直接基于 CDF 计算的 User/Video Group XAUC 上,RAD-U 领先 User Group XAUC(MLP 0.7105 vs CQE 0.7050)、RAD-V 领先 Video Group XAUC(MLP 0.6803),RAD-UV 在两侧均匹配或超越。
- **分布匹配(Table 3)**:RAD-U 可学嵌入(MQ+MLP)的平均 1-Wasserstein 距离 2.2793,逼近经验分位下界 2.1500,远优于 CQE 的约 9.1。
- **消融(Table 4)**:两阶段 RAD-U(0.7131/MLP)> RAD-U+MQ 可学嵌入(0.7101)> 一阶段 CQE(0.7044),验证两阶段解耦优于 CQE 的联合估计,且可学嵌入几乎不损失精度。
- **工业数据集(Table 5)**:RAD 在高数据量下仍显著超 CQE(User Group XAUC 0.642 vs 0.623,Video Group 0.631 vs 0.594)。
- **在线 A/B(Table 6)**:三个 RAD 模型相对生产基线均提升用户参与。RAD-UV 最均衡:Active Days +0.0290%、Watch Time +0.3246%、Finish Playing +1.1125%、Skip Rate −0.864%;RAD-U 在 Finish Playing 增益最大(+1.3296%),RAD-V 在 Watch Count 最优(+0.2554%)。

## 在本 wiki 中的位置

本文属于 [[recommender-system]] 中的 [[watch-time]] 去偏一脉,直接对话并超越 [[d2q]]、[[wtg]]、[[d2co]]、[[cwm]]、[[cread]]、[[conditional-quantile-estimation]] 等 [[duration-bias]] / [[popularity-bias]] 纠正方法。其核心工具是 [[quantile-regression]] 与 [[confounding-bias]] 框架(全方差分解、umbrella conditioning),用 [[kuairand]] 公开 benchmark 评测。作者来自 [[bytedance-research]]。文末还指出 RAD 分位标签可作为 [[reinforcement-learning]] 中奖励变换(如 GRPO)与 listwise 推荐的校准信号,为 [[reward-shaping]] 与 [[long-term-recommendation]] 提供接口。
