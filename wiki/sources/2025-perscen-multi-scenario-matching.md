---
type: source
subtype: paper
tags: [recommender-system, multi-scenario-matching, two-tower, graph-neural-network, vector-quantization, personalization]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2506.18382
raw: raw/2506.18382.pdf
authors: [Haotong Du, Yaqing Wang, Fei Xiong, Lei Shao, Ming Liu, Hao Gu, Quanming Yao, Zhen Wang]
year: 2025
---

# PERSCEN: Learning Personalized Interaction Pattern and Scenario Preference for Multi-Scenario Matching

PERSCEN 是首个把"用户个性化建模"直接引入多场景匹配(multi-scenario matching)阶段的两塔召回方法,通过 user-specific 特征图 + 轻量 GNN、向量量化(vector quantization)的场景感知偏好,以及渐进式场景自适应 GLU,在保持高检索效率的同时显著提升召回性能。

## 问题

随着在线平台业务扩张,多场景推荐(multi-scenario recommendation)成为降低维护成本、缓解数据稀疏的主流方案。其匹配(matching/召回)阶段需要从百万级物料中以严格低延迟检索候选,因此普遍采用 [[two-sided-fairness-reranking|两塔]](two-tower,如 [[dpr|DSSM]]、YoutubeDNN)架构。

多场景匹配的关键是同时刻画两类偏好:(1)跨所有场景共享的偏好(preferences shared across scenarios);(2)各场景特有的 scenario-aware 偏好。现有方法(ICAN、ADIN、SASS、M5)依赖注意力、动态加权或 gating 机制,用通用的 scenario context 特征去调制行为序列,但**忽视了 user-specific(用户个性化)建模**:它们对所有用户使用统一的特征交互模式与通用场景上下文,无法捕捉个体用户在不同场景下的细粒度行为差异。论文用例子说明:同一"网格 feed→滚动 feed"的布局切换,User A 从美妆转向美食、User B 从旅行转向电影,场景偏好因人而异。难点在于:user-specific 建模通常计算昂贵,而召回阶段又要求高吞吐、低延迟,二者难以兼顾。

## 方法

PERSCEN(主要设计用户塔,物料塔结构类似)包含三个组件:

- **User-Specific Feature Graph Modeling(用户特定特征图建模)**:受 EmerG 启发,设计 field-wise feature graph generator,为每个用户生成一张独有的特征图——节点是用户特征字段,边由学习得到的 user-specific 邻接矩阵 A_u 表示。每个字段经 MLP 产生 A_u^(1) 的一行;高阶邻接矩阵通过矩阵连乘 A_u^(l) = A_u^(l-1)·A_u^(1) 递归生成,再经归一化/稀疏化/对称化精炼。随后用一个**轻量 GNN**(基于矩阵乘法的链式运算,而非传统消息传递)在该图上捕捉高阶特征交互,得到刻画跨场景共享偏好的用户隐表示 h_u^(L)。这一设计在保留两塔简洁高效的同时引入个性化能力。
- **Scenario-Aware Preference Recognition(场景感知偏好识别)**:对用户在场景 s 的 scenario-specific 行为序列做 pooling+MLP 得到潜表示 z_{u,s},再通过[[variational-autoencoder|向量量化]](vector quantization)在一个**共享 codebook** 中检索最近的 code vector c_j 作为该场景偏好,残差连接得 p_{u,s}=z_{u,s}+c_j。量化不可导,采用 straight-through estimator,并用 VQ loss(codebook loss + commitment loss,带 stop-gradient 与超参 β)优化。共享 codebook 让数据丰富场景学到的偏好可自然迁移到数据稀疏场景。场景上下文经 scenario encoder 得 p_s,最后 MLP 融合得场景感知偏好 p̂_{u,s}。
- **Progressive Scenario Adaptive Transfer(渐进式场景自适应迁移)**:受 GLU/PLE 启发,提出场景感知 GLU,用简单的逐元素乘法(而非 GRU 的 reset/update 复杂门控)实现细粒度、低延迟的信息控制与融合,逐层对 GNN 输出与 p̂_{u,s} 做自适应门控。最终经可学习权重 α 融合得到场景感知用户表示 ê_u(物料侧同理得 ê_v)。

**优化**:匹配分 ŷ=σ(⟨ê_u, ê_v⟩)(内积);视作二分类,随机负采样;总损失 L_PERSCEN = L_task(BCE) + L_VQ。代码已开源(github.com/LARS-research/PERSCEN)。

## 结果

数据集:**KuaiRand-Pure**(来自快手,4 场景 K1–K4,24,122 用户 / 7,583 物料 / 650,283 交互)与 **Alimama**(阿里妈妈广告,4 场景 A1–A4,138,622 用户 / 846,811 物料 / 933,633 交互)。指标 Recall@K 与 Hits@K(K 取约总物料 1%:KuaiRand K∈{50,100},Alimama K∈{500,1000})。基线含单场景 YoutubeDNN-S/DSSM-S 与多场景 YoutubeDNN-M/DSSM-M/ICAN/ADIN/SASS/M5。硬件 RTX 3090Ti。

- **召回性能**:PERSCEN 在两数据集所有场景上均优于全部基线。例如 KuaiRand K1(占 84% 数据)R@50=18.74、K2 R@50=30.69、K3 R@50=19.60、K4 R@50=21.39;Alimama A1 R@500=12.72、A2 R@500=12.66、A3 R@500=12.34、A4 R@500=12.63,均为最佳或并列最佳。
- **稀疏场景增益显著**:在数据稀疏场景(如 KuaiRand K4 占 3%、Alimama A4 占 10%),ICAN/ADIN 等多场景模型甚至不如单场景模型(优化被数据丰富场景主导),而 PERSCEN 凭共享 codebook 的偏好迁移取得明显提升。
- **效率/复杂度**(Table 2):PERSCEN 参数量与 FLOPs 处于合理范围——KuaiRand 上 4.30 MB / 8.52 GFLOPs(SASS 仅 3.27 MB,M5 高达 43.87 GFLOPs);Alimama 上 39.80 MB / 12.84 GFLOPs。约 10 GFLOPs 落在工业部署可接受区间。
- **推理延迟**(Table 3,Alimama batch=4096):PERSCEN 平均 4.83 ms,优于 ICAN(3.19 ms 但性能差)以外的多数,显著低于其 GRU 变体(5.02 ms),印证场景感知 GLU 迁移更高效。
- **消融**(Table 5,Alimama):去掉 GNN("w/o GNN")性能大幅下降,证明 GNN 建模特征交互优于简单 MLP;"w/ shared graph"(共享而非 user-specific 邻接矩阵)变差,凸显个性化特征图价值;"w/o spec sequence""w/o VQ""w/o GLU" 均不及完整模型,验证各组件必要性,尤其 VQ 在稀疏场景缓解数据不平衡。

## 在本 wiki 中的位置

本文属于 [[recommender-system]] 中的 [[candidate-generation|匹配/召回]] 方向,聚焦 multi-scenario matching,沿用 [[dpr|两塔/DSSM]] 范式并以高效率为约束。技术上融合了 [[graph-contrastive-learning|GNN]] 类特征交互(field-wise feature graph)、[[variational-autoencoder|向量量化]](VQ,与离散 codebook 思想相关)与 GLU 门控迁移。其"user-specific 个性化建模"主线与 [[personalized-ranking]]、[[cold-start]]/数据稀疏迁移议题相通;场景间共享 codebook 的迁移机制与 [[multi-task-learning]]、跨域推荐形成对照(论文强调多场景无场景间优劣层级,目标是所有场景同时提升)。作者来自[[tsinghua-university|清华大学]](Quanming Yao)、Northwestern Polytechnical University 与美团(Meituan),发表于 KDD 2025。
