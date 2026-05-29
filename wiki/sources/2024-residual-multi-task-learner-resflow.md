---
type: source
subtype: paper
tags:
  - multi-task-learning
  - recommender-system
  - learning-to-rank
  - e-commerce
  - residual-learning
created: 2026-05-29
updated: 2026-05-29
arxiv: "2411.09705"
raw: raw/2411.09705.pdf
authors:
  - Cong Fu
  - Kun Wang
  - Jiahua Wu
  - Yizhou Chen
  - Guangda Huzhang
  - Yabo Ni
  - Anxiang Zeng
  - Zhiming Zhou
year: 2024
---

# ResFlow:用于应用排序的残差多任务学习器

ResFlow 是一个轻量的[[multi-task-learning]]框架,通过在不同任务网络的**对应层之间建立残差连接**来实现高效的跨任务信息传递,部署于 Shopee Search 的 pre-rank 模块,线上 A/B 测试带来 OPU(order-per-user)1.29% 的提升且无额外延迟。

## 问题

现代电商平台的[[recommender-systems]]与搜索引擎依赖建模多种用户反馈(点击 CTR、点击转化 CTCVR 等)来提供个性化服务,[[multi-task-learning]](MTL)因此成为排序系统的核心。但真实大规模电商排序有两大难点:

- **效率约束**:大规模排序采用多阶段级联(match → pre-rank → rank),早期阶段(如 pre-rank)需在 150ms 内从百万级候选中快速筛选,无法使用过重的模型。
- **序列依赖与稀疏性**:用户行为天然有序(只有先点击才能下单),且高承诺行为极度稀疏(CTCVR 常仅 0.1% 量级),带来样本选择偏差与稀疏问题。

现有方法各有局限:[[mmoe]]、[[ple]] 等基于专家网络共享信息,但缺乏对任务关系的显式建模,性能相对偏弱;[[aitm]] 用注意力模块顺序传递信息但计算量大,不适合 pre-rank;[[esmm]] 及其因果去偏变体(ESCM2、DCMT)建模序列依赖,但在扩展到两个以上任务时面临高方差、数值不稳定(NaN)等问题。

## 方法

ResFlow 的核心是在**链式相关任务网络的对应层之间**引入残差连接(generalized residual connection,跨网络而非 [[lstm]]/ResNet 那种网络内部),以逐元素相加的方式把前序任务(如"click",反馈更稠密)的信息加性地传给后序任务(如"order",更稀疏)。

- **残差学习器视角**:若第 k 个任务的第 l 个 block 残差连接到第 (k-1) 个任务,则 o^l_k = o^l_{k-1} + f^l_k(o^{l-1}_k),即 f^l_k 只需学习相对于前序任务的"残差",而稠密任务已学好的特征使稀疏任务的学习更容易。
- **加性 vs 乘性**:与 [[esmm]] 通过概率相乘间接建模 CTCVR 不同,ResFlow 直接建模 CTCVR,残差在 logit 上的加法相当于对条件概率的"加性编码"。实验显示直接建模 + 加性融合优于条件概率相乘。
- **非递增约束**:序列依赖任务的概率应沿依赖链非递增,实验发现多数场景训练后自然满足,无需额外正则;需要时用 min(logit, 0) 强制残差 logit 非正最稳定。
- **轻量与通用**:残差连接是唯一额外引入的结构,计算开销极小,可用于任意"前序任务信息有益于后序任务"的联合学习,并可扩展到更长的渐进链(view → like → forward)、twin-tower 架构以及回归任务。

此外针对线上线下指标错配,论文提出离线指标 **Weighted Recall@K(WR@K)**,用 W_k(订单数等集体反馈)加权,与线上 OPU 对齐良好;并提出排序打分时用**加性融合**多任务分数(Score = α·CTR + β·CTCVR)替代传统乘性融合(CTR^α × CVR^β)。

## 结果

- **离线 CTCVR AUC(Table 4)**:在 S0/S1/[[ali-ccp]]、AliExpress AE 各国子集、Shopee 等数据集上,ResFlow 一致优于 [[mmoe]]、[[ple]]、[[aitm]]、[[esmm]]、ESCM2-IPW/DR、DCMT 等全部基线,CTCVR AUC 相对最佳基线平均提升 **1.54%**。例如 AE-RU 0.913、Shopee-3 0.910、Shopee-2 0.902。
- **消融(Table 5)**:特征残差(FR)与最终 logit 残差(LR)单独均有提升,二者结合(NSE + FR + LR)效果最好(AE-RU 0.913 vs NSE 基线 0.869);高层(logit)残差比低层残差更关键。
- **更一般场景**:在 KuaiRand-Pure-S1 视频交互(valid view/like/follow/comment/forward)上 ResFlow 全面最优(Table 6);任务拓扑实验显示按样本稀疏度从稠密到稀疏链接(topo1)最佳(Table 7)。
- **回归即渐进多任务(Table 8)**:把回归离散化为渐进多任务后,Progressive + ResFlow 在 KuaiRand-Pure-S1 上 MSE 1658.44,优于 Traditional 的 1719.92 和 Progressive + NSE 的 1720.12。
- **指标对齐(Table 10)**:WR@100 与线上 OPU 的 Pearson 相关系数高达 0.788(2 targets)/ 0.867(3 targets),远高于 Recall@K、NDCG、List AUC。
- **线上 A/B(Shopee Search pre-rank)**:相比此前部署的 ESMM,3-target ResFlow 取得 OPU **+1.29%**、GMV +0.88%、买家数 +0.84%、线上 CTR +0.25%、线上 CTCVR +1.37%,且坏例率与系统延迟无上升(平均/P99 延迟 110ms/147ms,与 ESMM 的 110ms/146ms 相当)。ResFlow 已全量部署于 Shopee Search pre-rank。

## 在本 wiki 中的位置

ResFlow 是 MTL 在工业级 [[recommender-systems]] / [[learning-to-rank]] 中的应用工作,直接对标 [[mmoe]]、[[ple]]、[[aitm]]、[[esmm]] 等多任务排序方法,聚焦序列依赖任务(CTR → CTCVR)与样本稀疏问题。它把残差学习思想从网络内部推广到跨任务网络,并解决了线上线下指标对齐(WR@K)与分数融合等部署难题。涉及数据集 [[ali-ccp]]、[[kuairand]]、[[movielens-1m]],出自 Shopee/南洋理工([[anxiang-zeng]] 等)。
