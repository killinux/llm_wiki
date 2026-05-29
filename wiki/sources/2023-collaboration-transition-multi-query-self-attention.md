---
type: source
subtype: paper
tags:
  - sequential-recommendation
  - recommender-system
  - self-attention
  - knowledge-distillation
created: 2026-05-29
updated: 2026-05-29
arxiv: "2311.01056"
raw: raw/2311.01056.pdf
authors:
  - Tianyu Zhu
  - Yansong Shi
  - Yuan Zhang
  - Yihong Wu
  - Fengran Mo
  - Jian-Yun Nie
year: "2023"
---

本文提出 MQSA-TED(Multi-Query Self-Attention with Transition-Aware Embedding Distillation),通过多查询自注意力建模用户协同信号、并把全局 item-to-item 转移模式蒸馏进 item embedding,从而在序列推荐中同时捕捉协同信号与转移信号并平衡二者。

## 问题

现代 [[sequential-recommendation]] 模型(如 [[sasrec]])依赖 self-attention 建模动态用户兴趣,但在捕捉序列中的"协同信号"(collaborative signals,用户交互序列之间的相似性)与"转移信号"(transitional signals,物品对之间的转移频率)上都存在局限:

- self-attention 用单个物品(最近一个)的 embedding 作为 attention query,难以捕捉协同信号,本质上是一个被注意力增强的一阶马尔可夫链,对缺乏观测转移的测试样本泛化差。
- 这类方法通常遵循 auto-regressive 框架,无法学习全局的 item-to-item 转移模式。
- 作者在 Amazon Beauty/Sports 上的前置实验(Figure 1)显示:在转移频率为 0 的测试样本上 LightGCN(协同)优于 SASRec;在转移频率高的样本上 Item Transition(纯转移)优于 SASRec,说明 SASRec 两类信号都没用好。

## 方法

MQSA-TED 包含两个主要模块:

- **Multi-Query Self-Attention(MQSA)用于用户协同建模**:提出 L-query self-attention,用最近 L 个物品(而非单个物品)的 mean-pooling 表示作为 attention query(公式 7),L 控制历史上下文范围以权衡 bias-variance。再用 multi-query 把 short-query(L=1,类似 SASRec)与 long-query(较大 L)自注意力按超参 α 组合:ê_t = α·ê_t^short + (1−α)·ê_t^long(公式 8),平衡长短期兴趣。
- **Transition-Aware Embedding Distillation(TED)用于物品转移建模**:构建带权有向的 item transition graph(边权为时间跨度 k 内的转移频率,默认 k=1),用行归一化与温度 τ 生成 pseudo-label(公式 9);student 用一个简单的 factorization 模型(self-attention 层之前的 item embedding 点积)预测转移分布(公式 10),用交叉熵把全局转移模式蒸馏进 embedding(L_kd,公式 11)。
- 总损失 L = L_rec + λ_kd·L_kd + λΘ·||Θ||₂²(公式 12)。两个模块通过 dual supervision 实现解耦:self-attention 之前的 item embedding 捕捉转移信号,之后的表示捕捉协同信号。可类比为 retrieval(转移)+ re-ranking(协同)。

## 结果

- 在四个真实数据集 Beauty、Sports、Toys(Amazon Review)、Yelp 上评测,指标为 HR@N 与 NDCG@N(N=5/10/20),baseline 含 POP、[[matrix-factorization]] 系、FPMC、Caser、GRU4Rec、SASRec、BERT4Rec、FMLP-Rec、LightGCN。
- MQSA-TED 在几乎所有指标上取得最佳:相比最优 baseline 平均 HR@20 提升 6.24%、NDCG@20 提升 7.64%(论文摘要/RQ1)。例如 Beauty HR@5=0.0752(提升 7.23%)、NDCG@5=0.0534;Sports NDCG@5=0.0320(提升 11.34%);Yelp NDCG@5=0.0205(提升 11.74%)。
- 消融(RQ2):L 在 [2,4] 时表现好;α≈0.5 取得最佳 bias-variance 权衡,α=1 退化为 SASRec+TED;λ_kd≈0.1 最佳,λ_kd=0 退化为纯 MQSA 并显著掉点;蒸馏温度 τ=0.05 或 0.1 最佳(需相对硬的 pseudo-label)。
- RQ3:TED 优于图正则方法 GraReg、GES(graph-based embedding smoothing)。RQ4:TED 作为 domain adapter 也能提升 LightGCN、FMLP-Rec 等多种 backbone,但在 Yelp 上提升有限(该数据集序列性弱)。RQ5(Figure 5):MQSA 在缺乏转移的样本上提升明显,TED 作为 calibrator 让 MQSA-TED 在高转移频率样本上更好,二者结合在两类信号间取得平衡。

## 在本 wiki 中的位置

本文属于"self-attention 序列推荐 + 知识蒸馏"方向,直接改进 [[sasrec]],与 wiki 中的 [[sequential-recommendation]]、[[recommender-systems|recommender-system]]、[[matrix-factorization]] 等主题相连,展示了如何用 multi-query attention 与 transition distillation 在协同信号与转移信号之间解耦并平衡,可与图卷积推荐(如 [[recommender-systems|recommender-system]] 下的 LightGCN 路线)互为参照。
