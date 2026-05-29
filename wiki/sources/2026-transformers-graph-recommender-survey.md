---
type: source
subtype: paper
tags:
  - transformer
  - graph-recommender-system
  - recommender-system
  - graph-transformer
  - self-attention
  - survey
created: 2026-05-29
updated: 2026-05-29
arxiv: ""
raw: raw/10.1007_s11633-025-1607-8.pdf
authors:
  - Lorenzo Zangari
  - Silvio Raso
  - Andrea Tagarelli
year: 2026
---

# Transformers for Graph-based Recommender Systems: A Survey

首篇系统综述,聚焦把 transformer 引入 graph-based recommender systems(GRS)的研究,提出 graph transformer-based recommender system(GTRS)的形式化定义,并据此建立涵盖 4 大功能类、6 个架构子类的完整分类体系。

## 问题

graph-based recommender systems(GRS)将用户-物品交互建模为图结构,以捕捉复杂的关系模式和高阶连通性,并能缓解 cold-start、data sparsity 与 explainability 等推荐难题。GRS 主流做法基于 graph neural network(GNN)的 message-passing,但 GNN 存在两类局限:

- **over-smoothing(过平滑)**:GNN 类似 low-pass filter,会平滑相连节点的 embedding,模糊推荐排序所需的区分性信号,难以捕捉长程序列依赖。
- **bias 与 noise**:message passing 易受 popularity bias 影响,过度推荐热门物品(positional bias 而非真实相关性),在用户-物品图中形成无关连接,使消息传递变得 noisy。

[[transformer]] 凭借 self-attention(SA)机制可在不预设结构的前提下捕捉节点间长程依赖,在多种图任务上常优于 GNN。然而 transformer 与图结构数据在 GRS 场景的融合尚未被充分探索,且缺少专门面向"在用户偏好学习中引入 transformer 的 GRS"的综述。本文填补这一空白。

## 方法

**形式化定义 GTRS**:给定图 G=(V,E) 与节点特征矩阵 X,模型由四个函数组成:
- R(X, G; Θ_R):计算(可能融入图信息的)topology-aware 输入 embedding;
- M(G; Θ_M):产生 structural prior(如注意力 mask / 邻接矩阵),注入到 SA 计算中;
- T(·; Θ_T):基于 multi-head self-attention(MHSA)的 transformer 主体;
- F(·; Θ_F):处理 transformer 输出、生成最终节点表征 Z;
随后由打分函数 g(z_u, z_i; Θ_g)(通常取内积)预测偏好分 r_{u,i}。模型要成为 GTRS,R、M、F 中至少有一个必须对 G 有非平凡依赖(对 G 的偏导非零)。

**分类体系**(基于"图诱导偏置"出现在何处,用决策树判定 R、M 是否依赖 G):

1. **GUTM(Graph-unaware transformer models)**:transformer 仅处理内容特征(文本/图像),图信息只在下游 F 注入。下设 SM(单模型,串行架构)与 EM(集成模型,并行架构,常配 GNN 分支)。
2. **GATM(Graph-aware transformer models)**:图结构被编码进输入 embedding 后送入 transformer。下设 SIEM(structural input embedding,直接用结构 embedding 初始化)与 ESIEM(enhanced structural input embedding,结构 embedding 与其他信息融合)。
3. **GTSAM(Graph topology-aware self-attention models)**:仅通过把图先验注入 SA block(如邻接 mask / 邻居加权)利用拓扑。下设 MAM(masked SA)与 SMAM(在 mask 基础上加采样)。
4. **HM(Hybrid models)**:同时用 R 和 M 注入图信息,兼具 GATM 与 GTSAM 特性。下设 SHM(单 transformer 栈)与 MHM(多 transformer 栈)。

综述纳入 2018 年至今的文献,在 Table 1 中按推荐任务([[sequential-recommendation]]、session、CTR、multimodal、multi-behavior、POI、conversational、medication 等)、图类型(bipartite/homogeneous/heterogeneous/hypergraph)、transformer 架构与数据集等维度归纳。

## 结果

本文为综述,汇总各代表方法在标准推荐指标(MRR、NDCG、Recall、Hit Rate、Precision、F1、AUC、MAE/RMSE)上的报告结果,要点包括:

- **评测指标**:统一采用 @k 记法,涵盖 MRR@k、NDCG@k、Recall@k、Precision@k、Hit@k,以及 AUC-ROC、MAE、RMSE 等。
- **常用数据集**:[[movielens]]、[[amazon-reviews]](Amazon 多品类)、[[yelp-dataset]](Yelp)、Foursquare、Gowalla、[[retailrocket]]、Diginetica、LastFM、MIMIC-III、REDIAL、KuaiRec、[[kuairand]] 等。
- **代表性数字**:GERL 在 MSN News 上 NDCG@10=0.31;KGTE 在 DBLP/Aminer 上 NDCG@10=0.66;MBHT 在 Taobao/Retailrocket/IJCAI 上 NDCG@5 提升达 52%、HR@10 提升 27%;G-TransRec 在 Taobao/Yelp 上 NDCG@k 平均提升 20%–60%;Hgformer 在 5 个 Amazon/Douban 数据集上相对提升 15%–19%;PREMIER(配 BERT)在 MIMIC-III 上 AUC=0.78。
- **架构权衡**:GUTM 在内容侧信息丰富时有效但对拓扑盲视;SIEM/ESIEM(GATM)继承图归纳偏置与长程注意力,但预计算 embedding 在图 noisy/sparse 时可能次优;GTSAM 直接在 SA 注入拓扑;HM 双重注入,理论上表达力强于单一 GATM 或 GTSAM,但计算与训练成本更高。
- **未来方向**:设计高效的 topology-aware transformer、降低 SA 的计算/内存开销、处理 data sparsity 与边/节点异质性。

## 在本 wiki 中的位置

本文位于 [[transformer]] 架构与 [[recommender-systems|recommender-system]] 的交叉处,系统梳理了 GNN 之外的另一条 GRS 技术路线。它与 wiki 中已有的 [[recommender-systems|recommender-system]]、[[sequential-recommendation]] 等推荐主题,以及 self-attention/transformer 架构脉络相承接,可作为"graph transformer 用于推荐"这一子领域的入口与分类索引。
