---
type: source
subtype: paper
tags: [recommender-system, watch-time, short-video, mixture-distribution, recsys]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2508.12665
raw: raw/2508.12665.pdf
authors: [Xu Zhao, RuiBo Ma, Jiaqi Chen, Weiqi Zhao, Ping Yang, Yao Hu]
year: 2025
---

# Multi-Granularity Distribution Modeling for Video Watch Time Prediction via Exponential-Gaussian Mixture Network

EGMN 把短视频观看时长(watch time)建模为一个 **Exponential-Gaussian Mixture(EGM)分布**,用指数分量刻画粗粒度的偏态(快划/quick-skip),用多个高斯分量刻画细粒度的多模态多样性,并以神经网络端到端参数化该分布。

## 问题

在 TikTok、KuaiShou、小红书等短视频平台上,观看时长是衡量用户满意度的核心指标,准确预测它对 [[recommender-systems|recommender-system]] 的推荐质量至关重要。作者通过对真实工业数据的系统分析,发现观看时长分布存在两个跨粒度难题:

- **粗粒度偏态(coarse-grained skewness)**:大量 quick-skip(用户快速划走)导致观看时长在 0 附近高度集中、强偏态。
- **细粒度多样性(fine-grained diversity)**:不同用户(挑剔型 vs 包容型)和不同视频(美妆视频呈双峰、影视合集呈多峰)的观看时长分布形态差异巨大,呈现多模态。

已有方法多绕开这两个难题:label normalization 损失绝对时长信息;task transformation(把回归转成一系列分类,如 [[d2q]]、[[cread]]、[[tpm]])引入离散化/重构误差;[[wtg]](Value Regression / [[mse]])假设高斯分布,与真实强偏态长尾不符;[[d2co]] 用 GMM 分离噪声观看但忽略 quick-skip 等丰富交互。这些方法对观看时长概率分布 $p(t)$ 做了过强或不当假设。

## 方法

**问题定义**:给定 user-video 对的嵌入特征向量 $\mathbf{x}$,学习 $f(\mathbf{x})$ 预测观看时长 $t$,核心是直接对 $p(t)$ 建模而非套用任意度量。

**EGM 分布**:假设 $p(t)$ 为一个指数分布与 $K$ 个高斯分布的混合:
$p(t)=\omega_0 f_{exp}(t\mid\lambda)+\sum_{k=1}^{K}\omega_k f_{gauss}(t\mid\mu_k,\sigma_k^2)$,权重满足 $\sum\omega_k=1$。指数分量利用无记忆性与零点附近的质量集中刻画 quick-skip;高斯混合作为复杂多模态分布的相合估计器刻画多样性。

**EGMN 架构**(见论文 Figure 2):

1. **Hidden Representation Encoder**:融合用户特征(画像、历史行为)、视频特征(内容、duration、类别、创作者)、上下文特征(时段、设备),经嵌入层与 backbone $g_{backbone}$ 得到共享隐表示 $\mathbf{h}$。backbone 与具体网络无关,可用 DCN/DIN/SENet/[[transformer]] 等。
2. **Mixture Parameter Generator**:从 $\mathbf{h}$ 分支生成各分量参数——指数率 $\lambda$、高斯均值 $\mu_k$、方差 $\sigma_k^2$(均用 softplus 保正)、混合权重 $\omega$(softmax)。为保证可辨识性(identifiability),约束高斯均值大于指数分量的均值。

**训练目标**(三损失组合,$\mathcal{L}=\mathcal{L}_{MLE}+\alpha\mathcal{L}_{entropy}+\beta\mathcal{L}_{reg}$):

- $\mathcal{L}_{MLE}$:对观测观看时长做最大似然估计,使模型对真实时长赋予高概率密度。
- $\mathcal{L}_{entropy}$:对混合权重做熵最大化正则,防止坍缩到单一分量,保持多模态能力。
- $\mathcal{L}_{reg}$:对 EGM 期望值与真实时长做 MAE 回归,保证绝对值预测精度。

**推理**:以 $p(t\mid\mathbf{x})$ 的期望值 $\hat t=\omega_0/\lambda+\sum\omega_k\mu_k$ 作为最终预测;同时可输出 quick-skip 识别、特定区间的累积概率、分位数估计等。

## 结果

**离线对比(Table 1,四数据集:工业集 Indust、[[kuairec]]、WeChat、CIKM;指标 MAE↓ / XAUC↑)**:EGMN 平均提升 14.11% MAE、7.76% XAUC。Indust 上 MAE 22.24 / XAUC 0.6563,相对次优(多为 CREAD)提升 6.75% MAE、5.09% XAUC;KuaiRec MAE 4.204、XAUC 0.6093;WeChat MAE 18.88、XAUC 0.6692;CIKM MAE 0.6209、XAUC 0.7751。

**在线 A/B(Table 2,小红书,7 天,10% 流量,排序阶段 backbone 为 MMOE)**:相较 CREAD,Watch Time +0.681%、Video Views +0.189%,Engage Actions -0.055%(无显著负向);在线 MAE 31.37(-2.030%)、XAUC 0.6912(+1.260%)、KL 散度 0.1012(-19.94%)。

**Quick-skip 识别(RQ2,Figure 3,Indust)**:在 2s/4s/6s 三个阈值上 EGMN 的二分类 AUC 均最高;移除指数分量(EGMN w/o exp)在所有阈值上 AUC 下降超 6%,证实指数分量主导偏态捕获。

**消融(Table 3)**:去掉指数分量在 KuaiRec 上 MAE +18.55%;去掉高斯分量 KuaiRec MAE +9.71%;去掉 $\mathcal{L}_{MLE}$ 在 Indust MAE +3.73%;去掉 $\mathcal{L}_{entropy}$ +3.19%;去掉 $\mathcal{L}_{reg}$ +3.24%。高斯分量数量在 8–12 时最佳(XAUC 峰值约 0.611),过多导致过拟合。

**分布拟合(RQ5)**:KL 散度上仅 EGMN 与 D2Q < 1.0(EGMN 收敛到约 0.5,D2Q 约 0.1),但 D2Q 的 MAE 在第 6 个 epoch 后急剧上升,而 EGMN 在 KL 与 MAE 上同步单调下降,更好地平衡分布建模与值回归;在 duration 级与 user-video 级均能拟合双峰/多峰真实分布。代码开源于 GitHub(BestActionNow/EGMN)。

## 在本 wiki 中的位置

本文属于 [[recommender-systems|recommender-system]] 中 watch-time 预测方向,直接对标并改进 [[wtg]]、[[d2q]]、[[cread]]、[[tpm]]、[[d2co]] 等观看时长建模方法,关联 [[kuairec]] 等 RecSys 数据集与 [[mse]]、[[transformer]] 等基础组件。它将观看时长回归重构为概率分布(混合密度网络思路)建模,可与本 wiki 中 [[watch-time]]、[[duration-bias]]、[[debiasing]] 等条目互参。
