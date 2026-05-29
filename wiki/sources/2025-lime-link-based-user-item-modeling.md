---
type: source
subtype: paper
tags:
  - recommender-system
  - ctr
  - efficient-attention
  - test-time-scaling
  - sequential-recommendation
  - two-tower
created: 2026-05-29
updated: 2026-05-29
arxiv: 2510.18239
raw: raw/2510.18239.pdf
authors:
  - Yunjiang Jiang
  - Ayush Agarwal
  - Yang Liu
  - Bi Xue
year: 2025
---

# LIME: Link-based User-Item Interaction Modeling with Decoupled XOR Attention for Efficient Test Time Scaling

Meta 提出 LIME,通过低秩 "link embeddings" 解耦用户-候选交互并配合 XOR 线性注意力,使大规模推荐排序模型在扩大候选集与延长用户历史时推理成本几乎恒定,实现约 10x 加速并保持与 SOTA Transformer 近乎持平的精度。

## 问题

大规模推荐系统排序面临效率与表达力的根本冲突。两端是两种范式:[[two-tower]] 模型(如 TTSN)用户与物品分别编码、可用 [[approximate-nearest-neighbor-search]] 高效检索,但交互仅限于晚期点积,表达力弱;另一端是 cross-attention Transformer(如 [[sasrec]]、[[hstu]]),通过 [[self-attention]] 编码长用户历史(UIH)并对每个候选做深度交互,精度高但计算昂贵——自注意力对序列长度是二次复杂度 $O(N^2)$,且 cross-attention 对候选数线性增长。这使得在推理时同时扩大候选集、延长用户历史、增大模型容量变得代价过高。混合方法(hybrid)只带来增量改进。

## 方法

LIME(Link-based user-item Interaction Modeling for Efficient inference)针对 [[ctr]] 预测,用全局可学习的中间 "link embeddings" $L \in \mathbb{R}^{\ell \times d}$($\ell \ll N(U)$)作为用户历史与候选物品之间的桥梁:

- **Link Embedding 机制**:link embeddings 先与用户特征经 MLP 上下文化得到 $L^C$,再通过一层 MHA 关注用户完整历史 $E$ 得到个性化 link embeddings $L^P$。关键的候选交互采用 decoupled attention(解耦注意力):候选 $T$ 与 raw、用户无关的 link embeddings $L$ 做 Query-Key 点积 $\phi(TL^t)$,该注意力权重矩阵与用户无关,可对全语料离线预计算并缓存(如用 [[faiss]] 存为 QK Cache)。在线推理时昂贵的矩阵乘退化为查表 + 对 $L^P$ 的加权和,使每候选服务延迟接近常数 $O(1)$。
- **XOR Attention(XORA)**:为把用户历史自注意力从二次降到线性,提出 XOR mask $M_{xor}$ 替代 [[hstu]] 的因果自注意力掩码。它结构性消除昂贵的 history-to-history($E \leftrightarrow E$)交互,只保留 link 与 history 之间的双向 block-wise 注意力($L^C \to E$ 与 $E \to L^C$),复杂度从 $O(N(U)^2 + N(U)\cdot M(U))$ 降为 $O(\ell \cdot N(U))$。
- 两个变体:**LIME-MHA**(单层 MHA 个性化 link)与 **LIME-XOR**(在用户侧堆叠 3 层 HSTU 风格 block 配 XOR mask,加深交互)。
- 三阶段推理流水线:离线物品侧预计算(缓存 QK)、在线用户侧计算(与候选检索并行,延迟被掩盖)、轻量用户-物品交互(查表 + 加权和 + 浅层打分)。

## 结果

- **延迟**:在候选数、用户历史长度、QK 维度三个维度上,MHA 与 [[hstu]] 的延迟随规模激增(对数坐标下爆炸),而两个 LIME 变体延迟近乎恒定,实现约 **10x** 推理加速,适用于 >30k 物品的超长候选场景。
- **工业数据集**(3 天训练 / 6 小时评估):以 TTSN 为 baseline,LIME-XOR 取得 VC NE -1.04%、WT AUC +0.76%,接近 HSTU skyline(-1.06% / +0.77%);在线 A/B LIME-XOR 带来 VC +37.9%、WT +28.6%。LIME-MHA 在线 VC +28.6%、WT +22.1%。32x 序列压缩率下仍保持竞争力。
- **公开数据集**:在 KuaiRand-1K([[kuairand]],12M 交互、最大序列长 256)与 Taobao-Ad(25M 交互、最大序列长 50)上,用 FuxiCTR 统一评估。KuaiRand-1K Click AUC:LIME-MHA 0.7433(+0.60%)、LIME-XOR 0.7448(+0.80%),后者接近 HSTU skyline 0.7444;Taobao-Ad AUC:LIME-MHA 0.6465、LIME-XOR 0.6467,HSTU skyline 0.6475。在相同低秩 $\ell$ 下,LIME 优于 Truncated MHA 与 Linformer 式 LREA 等序列压缩方法,并对比了 [[sasrec]]、[[din]] 等 skyline。
- 生产部署在服务数十亿用户的主平台上,带来最高 **38%** source rate 提升(归因于该排序模型的正向互动占比)。

## 在本 wiki 中的位置

这是一篇高效推荐排序架构论文,核心是用解耦注意力 + 线性化(XOR mask)在 [[recommender-system]] 排序中弥合 [[two-tower]] 的效率与 cross-attention 的表达力。它与 [[sasrec]]、[[din]]、[[hstu]] 等序列推荐模型,以及 [[ctr]] 预测、长序列建模、[[approximate-nearest-neighbor-search]]/[[faiss]] 缓存等条目相关,可作为理解推荐系统中 test-time scaling 与高效注意力的入口。
