---
type: source
subtype: paper
tags: [sequential-recommendation, recommender-system, temporal-encoder, sparse-attention, efficient-transformer, generative-recommendation]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2512.12740
raw: raw/2512.12740.pdf
authors: [Dezhi Yi, Wei Guo, Wenyang Cui, Wenxuan He, Huifeng Guo, Yong Liu, Zhenhua Dong, Ye Lu]
year: 2025
---

# FuXi-γ: Efficient Sequential Recommendation with Exponential-Power Temporal Encoder and Diagonal-Sparse Positional Mechanism

FuXi-γ 是一个 decoder-only 的生成式[[sequential-recommendation]]框架,用受 [[ebbinghaus-forgetting-curve]] 启发的指数幂时间编码器替代 T5 式 bucket 编码,并对位置注意力做对角稀疏剪枝,在保持 SOTA 推荐质量的同时把训练加速最多 4.74×、推理加速最多 6.18×。

## 问题

生成式推荐模型([[hstu]]、[[fuxi-alpha]] 等)用自回归架构取得了优于传统方法的效果与 scaling 效应,但带来严重的效率瓶颈:

- **时间编码瓶颈**:[[hstu]] 与 [[fuxi-alpha]] 采用 T5 式 bucket 编码([[t5]] 风格),把相对时间间隔做对数变换后离散化为桶索引查表。对长度为 n 的序列,这会产生 n² 次非连续、无结构的内存访问,与并行硬件冲突;且缺乏认知原理支撑、表达力与可解释性受限。FuXi-β 用反比例衰减函数缓解了访存问题,但其固定衰减模式过度偏好近期交互,缺乏适应性。
- **位置编码冗余**:在已有绝对位置 embedding 和时间信号的情况下,[[fuxi-alpha]]、FuXi-β 仍引入一条独立的相对位置注意力通道,复杂度 O(n²),对长序列成为瓶颈。

论文指出 HSTU 相比 [[sasrec]] 把 HR@10 提升 55.18% 但训练慢 3.21×;[[fuxi-alpha]] 相比 HSTU 再提 5.66% HR@10 却又损失 9.63% 效率。如何同时兼顾效果与效率是核心挑战。

## 方法

FuXi-γ 基于 FuXi-β,采用无 query-key 注意力的 decoder-only [[transformer]],由 Embedding 层、L 个 FuXi-γ Block、Prediction 层组成,训练用 sampled softmax loss。核心是两项创新。

**1. 指数幂时间编码器(exponential-power temporal encoder)**
受 [[ebbinghaus-forgetting-curve]](人类记忆随时间指数衰减)启发,对每条序列构造相对时间矩阵 T(T_{i,j}=|t_i − t_j|,仅预处理一次并跨层共享),时间注意力矩阵定义为:

`A_ts = α · γ^{T^β}`,其中 γ ∈ (0,1)

- α 为可学习的基础兴趣强度,β 控制幂变换的非线性度(防止过长间隔信号过弱、长期偏好学不足),γ 为可学习衰减率(小 γ 强调短期、大 γ 保留长期)。
- 全程为标准矩阵运算 + 连续访存,硬件友好。
- **数据类型预转换**:把 int64 的 T 显式预转 float32,避免逐层运行时类型转换。

**2. 对角稀疏位置机制(diagonal-sparse positional mechanism)**
训练后对位置注意力矩阵 W_pos 做半结构化剪枝,分三步:
- **Block Division**:把注意力图切成 s×s 块(s 为可配 stride),不可整除处对上/右边缘 zero-padding(decoder-only 上三角已被 mask 为 0,padding 不损害信息)。
- **Leftmost Importance Scoring**:利用 Toeplitz 矩阵的 persymmetry(同一对角线的块取值相同),只需对最左列的块计算绝对值和作为重要性分数即可覆盖全部对角线(覆盖保证 + 结构感知)。
- **Diagonal-Sliding Selection**:按剪枝比 τ 选出 top-k 个最不重要的块,沿对角线滑动生成最终稀疏 mask(Algorithm 1)。

双通道自注意力层把时间通道 A_ts·V 与位置通道 W_pos·V 拼接后与 U 做 Hadamard 积,再经线性层 + 残差;后接 SwiGLU FFN。整体省去 query-key 注意力、多头扩展等 Transformer 开销。

## 结果

数据集:ML-1M、ML-20M、KuaiRand([[kuairand]])三个公开集 + 一个含数千万月活用户、约 13.1 亿交互的工业级音乐数据集(Industrial)。指标 HR@K、NDCG@K(K=10)、MRR。基线含 LinRec、FLASH、[[gru4rec]]、[[sasrec]]、LRURec、Mamba4Rec、[[llama]]、[[hstu]]、[[fuxi-alpha]]、FuXi-β。

**推荐效果**
- 公开集:8 层配置下,FuXi-γ 平均超过其他自回归模型 3.79% (HR@10)、2.37% (HR@50)、4.46% (NDCG@10)、3.49% (NDCG@50)、4.24% (MRR);2 层浅配置下也取得最优或次优。
- 工业集:相比自回归基线平均 HR@10 高 **25.06%**、NDCG@10 高 **42.86%**;相比最强基线 FuXi-β 取得 HR@10 +6.97%、HR@50 +1.74%、NDCG@10 +12.13%、NDCG@50 +9.25%、MRR +13.70%。

**效率**(KuaiRand,序列长 1000)
- 训练加速:相比 LLaMa/HSTU/FuXi-β 分别 4.74×、4.48×、1.86×;[[fuxi-alpha]] 在该规模 OOM。
- 推理加速:相比 LLaMa/HSTU/FuXi-β 分别 6.18×、6.07×、2.24×。
- 时间编码器单模块在长 1000 序列上相比 bucket 编码器加速最多 **11.00×**;数据类型预转换使该编码器执行时间降 64.82%,整体训练再提速 12.61%、显存降 5.08%,推理提速 15.53%、显存降 6.98%。

**消融与分析**
- 消融(Table 4):时间编码器最关键,去掉后掉点最多;位置编码器为中等贡献;SwiGLU FFN 影响较小。
- 时间编码器平均提升 HR@10/NDCG@10/MRR 各 8.82%、11.16%、11.15%(对比无时间基线),且对 HSTU/FuXi-α/FuXi-β 三种架构均能提升(兼容性,Table 5)。
- 位置剪枝:ML-20M 上 τ=60% 时仍保留 98.92% 原精度,而位置注意力 FLOPs 降 **74.56%**;KuaiRand 上中等稀疏度甚至略增精度;stride s=8 为最佳折中。
- 超参 γ:movie/video 域 γ=0.8 最佳,music 域 γ=0.9 最佳(音乐偏好更长期、更持久)。

## 在本 wiki 中的位置

本文属于"生成式/自回归[[recommender-systems|recommender-system]]的效率优化"脉络,直接承接 [[hstu]]、[[fuxi-alpha]] 与 FuXi-β 的工作线,延续 [[sasrec]]、[[bert4rec]]、[[gru4rec]]、[[tiger]] 等[[sequential-recommendation]]谱系。其贡献在于把认知科学([[ebbinghaus-forgetting-curve]])引入时间衰减建模,并把 LLM 领域常见的 block-sparse 注意力思路迁移到推荐的位置注意力上,与 [[kuairand]] 等真实工业数据集评测结合,代表了"用更便宜的架构换取可部署性"的推荐系统研究方向。作者来自 [[nankai-university]] 与 [[huawei-noahs-ark-lab]]/Huawei,发表于 KDD '26。
