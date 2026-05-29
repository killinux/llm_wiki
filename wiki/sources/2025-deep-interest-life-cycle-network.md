---
type: source
subtype: paper
tags:
  - recommender-system
  - sequential-recommendation
  - ctr
  - multi-task-learning
  - user-simulation
title: "Interest Changes: Considering User Interest Life Cycle in Recommendation System"
created: 2026-05-29
updated: 2026-05-29
arxiv: "2505.08471"
raw: raw/2505.08471.pdf
authors:
  - Yinjiang Cai
  - Jiangpan Hou
  - Yangping Zhu
  - Yuan Nie
year: 2025
---

# Interest Changes: Considering User Interest Life Cycle in Recommendation System

提出 **DILN(Deep Interest Life-cycle Network)**,显式建模用户兴趣的"生命周期"(emergent / stable / declining 等阶段),并将该特征注入排序模型,在 NetEase Lofter App 线上 A/B 取得 CTR +0.38%、CVR +1.04%、人均时长 +0.25% 的提升。

## 问题

推荐系统中用户兴趣处于持续变化中,典型地经历 **emergent phase(萌发期)→ stable phase(稳定期)→ declining phase(衰退期)** 的"用户兴趣生命周期(user interest life-cycle)"。但已有的兴趣建模工作(如 DIEN、DSIN 以及 [[sim]] 等基于搜索的 [[sequential-recommendation]] 方法)主要关注目标 item 与用户历史行为之间的相关性,忽略了兴趣所处的生命周期阶段:

- emergent 兴趣行为信号稀疏,现有方法难以及时识别和促进;
- declining 兴趣有大量历史行为,排序模型基于行为相关性仍会持续分发,忽视了兴趣的衰退趋势。

作者在 Lofter 上把推荐结果按业务逻辑划分为 Unexplored / Emergent / Long-term / Declining 四类,观察到不同生命周期阶段的分发"效率"(各任务指标)差异显著:emergent 兴趣行为虽少但效率最高,declining 兴趣行为丰富但整体效率下降。由此提出两个挑战:(1) 如何把生命周期特征整合进推荐系统;(2) 如何利用生命周期特征提升兴趣建模精度。

## 方法

DILN 包含两个核心组件:

### Interest Life-cycle Encoder Module(ILEM)

构造并编码兴趣生命周期特征,输出 dense 向量可无缝接入任意排序模型。

- **Feature engineering**:用 General Search Unit(GSU)针对候选 item 检索最相关的近期用户行为 $B^t=[b_1^t,...,b_N^t]$,$t$ 为行为类型(exposure / click / interaction)。限定近 $K$ 个活跃日、$N$ 个搜索结果。对每个活跃日的相关 item 相关性分 $\alpha_{d_i}$ 求和,形成"活跃直方图(active histogram)";soft search 用相关性分作为权重,hard search 固定为 0.1。最终得到长度为 $K$ 的向量,刻画候选兴趣在近 $K$ 个活跃日上的活跃强度分布。
- **Histogram Encoder**:对带时序特性的直方图用多层 1D CNN(kernel size 5/3/2,filter 数 8/16/32)卷积,再经线性层映射为定长向量;选 CNN 而非 [[transformer]] 是出于时间复杂度与效果的平衡。
- **Life-Cycle VQ Cluster**:用 Vector Quantization([[variational-autoencoder]] 离散化思路,VQ-VAE)把所有样本动态划分为 $M$ 个簇,每簇代表一种兴趣生命周期。包含 VQ encoder / VQ search / VQ decoder:对 encoder 压缩向量 $xc_i$ 在码本 $Q\in\mathbb{R}^{M\times d}$ 中找最近簇中心 $c_i$,decoder 重构原始特征,用 MSE 重构损失 $\mathcal{L}_{recon}$ 监督;采用 stop-gradient($sg$)。最终用簇中心 $c_i$ 作为该候选兴趣生命周期的 dense 表示。

### Interest Life-cycle Fusion Module(ILFM)

基于 **MMOE([[mmoe]])** 多任务框架,把生命周期特征显式注入排序模型,动态生成对输入特征与隐层表示的 rescaling 因子(Hadamard product):

- **Feature Recalibrator**:根据样本所处生命周期动态重加权各特征。例如 declining 兴趣下调历史活跃/lifelong sequence 等特征以抑制过度推荐,emergent 兴趣上调短期活跃特征。两层结构,缩放因子 $\gamma$ 设为 2。
- **Neural Fusion Unit**:在 MMOE 各 expert layer 输出与生命周期特征间做层级交互(gating + element-wise),让 expert net 更好捕捉生命周期与具体任务目标间的模式。

总损失 $\mathcal{L}=\mathcal{L}_{recon}+\mathcal{L}_{taskA}+\mathcal{L}_{taskB}$。

## 结果

**离线**(指标 GAUC,baseline = MMOE + [[sim]] Hard Search):

| Method | KuaiRand CTR | KuaiRand CVR | Industry CTR | Industry CVR |
|---|---|---|---|---|
| SIM | 0.6436 | 0.6364 | 0.5832 | 0.6636 |
| SIM+ILEM | 0.6708 | 0.6497 | 0.5921 | 0.6726 |
| DILN | **0.6726** | **0.6512** | **0.5934** | **0.6751** |

仅加 ILEM block 即在 CTR/CVR 上显著提升,再加 ILFM 进一步提升。

- 数据集:[[kuairand]](>27,000 用户、300 万交互,共 30 天;前 20 天构造特征、接 8 天训练、1 天验证、1 天测试);Industry 数据集来自 Lofter(数百万 DAU,10 天曝光日志,>600 万用户、27 亿样本)。超参:GSU 搜索数 $N=100$、直方图长度 $K=20$、VQ 簇数 $M=10$。
- 消融可视化(Figure 4):不同生命周期激活的 VQ 簇分布差异明显(Unexplored 主要激活 cluster 0,emergent 主要激活 cluster 3/4),验证 VQ 聚类能有效分层。

**线上**(Lofter A/B,>3 周,>20% 用户):CTR **+0.38%**、CVR **+1.04%**、人均时长(Duration)**+0.25%**。分阶段曝光调整(Table 2):降低低效兴趣曝光(Unexplored -2.17%、Declining -4.4%),提升 Emergent 曝光(+5.11%);各阶段 CTR/CVR 普遍正向(如 Declining CVR +2.20%、CVR Long-term +1.16%)。DILN 已部署于 Lofter App。

## 在本 wiki 中的位置

本文属于工业界 [[recommender-system]] / [[ctr]] 排序方向,与基于搜索单元建模终身行为序列的 [[sim]]、长短期兴趣融合的 [[sequential-recommendation]] 方法一脉相承,但创新点在于显式建模"兴趣生命周期"并用 VQ 聚类离散化阶段。技术上结合了 [[mmoe]] 多任务架构、VQ-VAE 式离散表示([[variational-autoencoder]])与 [[multi-task-learning]],评测用到公开数据集 [[kuairand]]。可与本 wiki 中其他兴趣演化/兴趣去偏(如 [[debiasing]]、[[duration-bias]])、长期推荐([[long-term-recommendation]])相关条目互参。
