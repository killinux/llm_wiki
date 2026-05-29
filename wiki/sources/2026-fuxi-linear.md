---
type: source
subtype: paper
tags: [linear-attention, sequential-recommendation, time-aware-recommendation, scaling-law, positional-embedding, recommender-system]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2602.23671
raw: raw/2602.23671.pdf
authors: [Yufei Ye, Wei Guo, Hao Wang, Luankang Zhang, Heng Chang, Hong Zhu, Yuyang Ye, Yong Liu, Defu Lian, Enhong Chen]
year: 2026
---

FuXi-Linear 是一个线性复杂度的时间感知序列推荐模型,通过解耦时间与语义信号、引入可学习核近似相对位置编码,在超长用户行为序列(数千 token)上同时实现推荐质量提升与最高 21× 的推理加速。

## 问题

现代推荐系统主要依赖二次复杂度 O(n²) 的 softmax 注意力(如 [[sasrec]]、HSTU),这限制了其处理长用户序列的能力并拖慢推理。工业场景下用户历史常超过 10⁴ 次交互,使得高容量且高效的建模成为刚需。[[linrec|线性注意力]] 是有前景的替代方案,但现有研究面临三个关键挑战:

1. **时间信号被忽视或被朴素耦合**:多数线性模型忽略交互时间戳,或将时间信号作为标量尺度耦合进语义注意力权重,导致语义信号与时间信号相互干扰,同时忽略行为周期性。
2. **位置信息不足**:现有线性框架提供的位置信息有限。强相对位置编码(RPE、T5-style、Alibi)与线性递归不兼容,而 [[rope|RoPE]] 在推荐任务中表现弱于 RPE。
3. **聚焦短序列与浅层架构**:现有线性推荐研究多局限于短序列(≤100 次交互)和 1-2 层浅层架构,其在超长序列下的可扩展性与容量基本未被验证。

## 方法

FuXi-Linear 由多个堆叠的 FuXi-Linear Block 组成,每个 Block 内输入经过线性多通道注意力(LMCA,含三个通道)再经过多阶段前馈网络(MFFN)。三个通道均支持三种计算形式:**recurrent form**(O(1) 推理)、**parallel form**(并行训练)和 **chunkwise recurrent form**(线性复杂度的并行训练)。

- **Retention Channel(保留通道)**:借鉴 [[retnet|RetNet]] 的简单线性注意力替代全注意力提供语义信息,query/key/value 经 SiLU 激活,query-key 注意力与衰减矩阵 D(D_{i,j}=γ^{i-j})逐元素相乘,扩展到多头,每头有可学习衰减参数 γ_i。

- **Temporal Retention Channel(时间保留通道)**:本文核心创新。仅用时间信息计算周期感知的 Q_t、K_t 与衰减矩阵 D_t,与语义信号解耦,避免互相干扰并捕获周期模式。在复数域建模时间动态:用户兴趣向量按 v' = e^{λΔt}v 演化,λ 写成极坐标形式 r·e^{iθ},通过三角恒等式推导出线性递归形式。采用 H_t 组多尺度时间参数 {(r_h, θ_h)} 建模多面兴趣演化,并引入可学习参数 α、β 自适应平衡历史趋势与当前状态。

- **Linear Positional Channel(线性位置通道)**:用可学习核函数 k 近似相对位置编码 f(x-y)≈k(x)ᵀk(y),将位置投影到 d_p 维空间,从而以线性复杂度获得 RPE 的表达能力,并可重写为递归形式;parallel form 用下三角因果 mask M_causal 实现。

三通道输出经 RMSNorm 归一化后拼接,经门控机制(gating)过滤噪声。模型自回归训练,使用带 N 个负样本的 sampled softmax loss。复杂度分析:并行训练 O(n) 时空复杂度,推理 O(1)。

## 结果

在三个公开数据集(MovieLens-20M、Kuairand-27K、KuaiRec,平均序列长度分别约 144、3556、1746)上评测,指标为 HR@K、[[ndcg|NDCG]]@K(K=10,50)和 MRR。

- **推荐质量**:FuXi-Linear 在所有指标上一致最优。在 Kuairand-27K 与 KuaiRec 长序列数据集上相对 SOTA 平均提升 NDCG@10 9.26%、NDCG@50 7.24%、HR@10 9.01%、HR@50 5.11%、MRR 8.33%。例如 Kuairand-27K 上 NDCG@10=0.0609、HR@10=0.1124、MRR=0.0540,均超过 [[hstu|HSTU]]、FuXi-α、FuXi-β、[[recmamba|Mamba4Rec]]、TTT4Rec、TiM4Rec、RetNet 等基线。

- **效率**:在序列长度 8k 时,Prefill 阶段相对 FuXi-α、FuXi-β、HSTU 加速分别为 10×、3.1×、7.8×;Decode 阶段加速分别为 21×、4.2×、18×。

- **scaling 实验**:固定序列长度 n=1024、头维度 32、d_FFN=4d,仅调整 embedding 维度与层数。FuXi-Linear 展现稳健的幂律 [[scaling-law|scaling]] 性质——参数量从 188K 增至 20M,NDCG@10 从 0.0472 提升到 0.0710、HR@10 从 0.0881 提升到 0.1288,跨两个数量级持续提升。

- **消融**:去掉任一模块均掉点,其中时间通道最关键(移除 Q_t、K_t 掉点最多);位置通道次之;保留通道边际贡献最小但仍有提升。时间编码方法对比中,本文方法以 O(nd) 复杂度超过 HSTU 的 bias(O(n²d))、绝对正弦编码、TiSSD 等。

## 在本 wiki 中的位置

FuXi-Linear 来自 [[university-of-science-and-technology-of-china|中科大]] 与 [[huawei-noahs-ark-lab|华为]] 团队(作者含 [[defu-lian]]、[[enhong-chen]]、[[wei-guo]] 等),延续 FuXi-α / FuXi-β 系列,是将 [[linrec|线性注意力]]、[[retnet|RetNet]]、[[mamba|状态空间模型]] 等高效序列建模技术引入 [[sequential-recommendation|序列推荐]] 的代表工作。它与 [[hstu|HSTU]]、[[sasrec|SASRec]] 等生成式/注意力推荐模型形成对比,核心贡献在于解耦时间与语义信号、用可学习核近似相对位置编码,并首次在 [[recommender-systems|推荐]] 领域验证千长度尺度的幂律 [[scaling-law|scaling]] 性质。评测数据集 [[kuairand]]、[[kuairec]]、[[movielens]] 均为本 wiki 已收录的推荐基准。
