---
type: source
subtype: paper
tags:
  - recommender-system
  - graph-transformer
  - signed-graph
  - collaborative-filtering
  - negative-feedback
created: 2026-05-29
updated: 2026-05-29
arxiv: "2404.11982"
raw: raw/2404.11982.pdf
authors:
  - Sirui Chen
  - Jiawei Chen
  - Sheng Zhou
  - Bohao Wang
  - Shen Han
  - Chanfei Su
  - Yuqing Yuan
  - Can Wang
year: 2024
---

# SIGformer: Sign-aware Graph Transformer for Recommendation

SIGformer 用 Transformer 架构替代 GNN 来做 sign-aware 推荐,通过两种为带符号图(signed graph)量身设计的 positional encoding,统一利用正/负反馈中的协同信息。

## 问题

[[recommender-systems|recommender-system]] 中的图方法(如 LightGCN)大多只用用户的正反馈(点击、高评分),而忽略了同样普遍且有价值的负反馈(低评分、点"踩"、快速划走)。把正、负反馈合成一张**带符号图**能更完整地刻画用户偏好,但现有少数 sign-aware 工作存在两个局限:

1. **正负反馈被分开处理**:通常分别构建正图和负图、各自学表示再融合,无法整体利用 signed graph 中的协同信息(例如跨正负边的高阶路径)。
2. **用 MLP / GNN 抽取负图信息可能无效**:大多数为推荐设计的 GNN(如 LightGCN)基于同质性(homophily)假设——相连节点相似,但这对负图并不成立;MLP 又难以利用图结构且在稀疏推荐数据上难训练。

作者主张需要一种能整体利用完整 signed graph 的新架构,并发现 Transformer 与 [[collaborative-filtering]] 的本质高度契合(先估计用户/物品相似度,再据此聚合相似实体的信息)。

## 方法

SIGformer 把传统图推荐范式中的 GNN 替换为 Transformer,核心是两个 sign-aware 的 positional encoding:

- **Sign-aware Spectral Encoding (SSE)**:把正图与负图的 Laplacian 组合为 L = 1/(1-α)·(L⁺ - αL⁻),取其最小的若干特征值对应的低频特征向量作为位置编码。理论上,带 SSE 的 Transformer 等价于一个**低通滤波器**——拉近有正反馈的用户-物品对的 embedding,推远有负反馈的对(论文给出 Lemma 1 及证明)。超参 α 控制负图影响,作者将其取值范围放宽到包含负值 (-1, 1),因为"负反馈未必真的负,只是相对没那么正"。
- **Sign-aware Path Encoding (SPE)**:枚举长度不超过阈值 L_p 的所有路径类型(按长度和边的符号区分,总数 N_p = 2(2^{L_p} - 1)),为每种路径类型学习一个表示节点亲和度的参数 φ。不同于只编码最短路径的图 Transformer,SPE 考虑全部路径关系,给出节点关系的整体视图。
- **Transformer 主干**:每层把 Q=K=V 设为上一层 embedding(省去 W_Q/W_K/W_V 投影矩阵),注意力 = 0.5·(softmax(QKᵀ/√d + P_s) + softmax(P_p))·V;两个编码用各自的 softmax 以缓解量级差异。最后聚合各层 embedding,用内积做预测,以 BPR loss 优化。
- **采样加速**:用 signed graph 上的随机游走(non-cyclic random walk)采样邻居并记录路径类型,把注意力复杂度降到 O((n+m)·d·N̂),效率可与 LightGCN 相当。

## 结果

在 5 个含正负反馈的真实数据集上评测,指标为 Recall@20 与 NDCG@20:

- **数据集**:Amazon-CDs、Amazon-Music、Epinions(评分类,高于 3.5 视为正),以及 [[kuairec]]、[[kuairand]](短视频,按观看时长比 / is_click 划分正负);7:1:2 划分。
- **整体**:SIGformer 在几乎所有数据集上超过所有 baseline(含 unsigned 图方法 LightGCN/LightGCL/XSimGCL/GFormer、sign-aware 方法 SiReN/SiGRec/PANE-GNN、signed graph embedding 方法 SBGNN/SLGNN、图 Transformer SGFormer/SignGT)。在 KuaiRand 上 Recall@20 相对最优 baseline 提升达 **15.61%**(0.1494),NDCG@20 提升 3.33%(0.0722);Amazon-Music 上 Recall@20 0.3091(+5.81%)、NDCG +5.87%。仅在 Epinions 上略逊于 GFormer(Recall -0.41%)。多数提升带 p < 0.05 显著性标记。
- **消融(Table 3)**:去掉负反馈(w/o-Neg)、去掉 SSE 或 SPE 都会一致下降,验证负反馈与两种编码各自有效。
- **超参 α**:多数数据集最优 α 落在小的负值;KuaiRec 因负反馈(快速划走)表达强烈厌恶,结论不同——说明 α 能灵活调节负反馈作用。
- **效率(RQ5)**:基于随机游走的 SIGformer 计算开销不重,效率与 SiGRec、LightGCN 相当,远快于 SiReN、PANE-GNN、GFormer。

## 在本 wiki 中的位置

本文属于 [[recommender-systems|recommender-system]] / 图推荐方向,核心贡献是把 Transformer 引入 **sign-aware** 推荐,并用谱与路径两类 positional encoding 统一利用正负反馈。它与只用正反馈的图方法(LightGCN 等)形成对照,也区别于把正负图分开处理的 sign-aware 方法。与 [[collaborative-filtering]]、[[matrix-factorization]] 等经典协同过滤思想一脉相承,实验用到了快手系数据集 [[kuairec]]、[[kuairand]]。通讯作者为浙江大学的 [[jiawei-chen]]([[zhejiang-university]])。与本 wiki 中以 LLM 为中心的推荐/agent 工作相比,本文是纯结构化推荐模型,可作为图推荐架构演进(GNN→Transformer)的参考节点。
