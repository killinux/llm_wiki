---
type: source
subtype: paper
tags:
  - cross-domain-sequential-recommendation
  - self-attention
  - sequential-recommendation
  - negative-transfer
  - pareto-optimality
  - multi-task-learning
created: 2026-05-29
updated: 2026-05-29
arxiv: "2505.21811"
raw: raw/2505.21811.pdf
authors:
  - Clark Mingxuan Ju
  - Leonardo Neves
  - Bhuvesh Kumar
  - Liam Collins
  - Tong Zhao
  - Yuwei Qiu
  - Qing Dou
  - Sohail Nizam
  - Sen Yang
  - Neil Shah
year: 2025
---

AutoCDSR 重新审视 transformer 自身的 self-attention,把 cross-domain sequential recommendation(CDSR)建模为一个偏好感知的 [[pareto-optimality]] 多目标问题——通过动态最小化 cross-domain attention scores,在不引入任何额外模块的前提下自动完成跨域知识迁移、抑制 negative transfer。

## 问题

[[sequential-recommendation]](SR)预测用户下一步行为,而 cross-domain SR([[cross-domain-sequential-recommendation]], CDSR)需要利用来自多个 domain(如电商不同品类、广告与内容)的行为来预测未来行为。CDSR 面临两大挑战:(i) context length explosion——多域行为显著拉长序列、需要建模复杂长程依赖;(ii) **negative transfer**——跨域信号有时不互补、甚至冲突,naively 把多域行为拼成一条序列再训练单域 SR 模型会引入噪声、损害性能。

作者通过在 KuaiRand-1K 上训练 [[bert4rec]] 验证:在某些样本上单域模型已足够准确,跨域信息反而有害(cross-domain attention 过高导致退化);而在另一些样本上单域模型失败,跨域 attention 与单域更对齐时则带来增益。已有 CDSR 方法大多靠额外的 domain-specific 模块(reweighting、domain-aware module blocks、graph 等)分别处理这两个挑战,却忽视了 transformer 内部本就强大的 self-attention 模块。核心问题:**能否仅靠优化 self-attention 自动完成 CDSR 的跨域知识迁移?**

## 方法

作者提出 AutoCDSR(及增强版 AutoCDSR+),一种 plug-and-play 机制,可嵌入任意基于 transformer 的 SR(如 [[sasrec]]、[[bert4rec]]),几乎不引入额外计算开销、无需重度调参。

- **量化跨域 attention**:定义 a_cd 为不同 domain item 之间的 softmax attention score 之和,用以度量跨域信息交换强度。
- **两目标重构为 MTL**:主任务为推荐损失 L_rec(masked/next-item 预测的 cross-entropy),辅助任务为 cross-domain attention 损失 L_cd-attn = a_cd。整体写作多目标优化 min(L_rec, L_cd-attn),用 [[multi-task-learning]] 框架求解。
- **偏好感知 Pareto 最优**:基于 Multiple Gradient Descent Algorithm(MGDA)求 [[pareto-optimality]] 解,并通过 K+1 个 preference vectors 把 Pareto front 划分为多个子区域,强制模型收敛到偏向推荐任务的子区域——只有当跨域信息真正提升推荐时才增大跨域 attention,从而自动迁移有益知识、抑制 negative transfer。用 Frank-Wolfe 算法近似迭代求解(约 100 次迭代即收敛)。
- **AutoCDSR+**:引入 information bottleneck(IB)tokens 作为跨域信息瓶颈。各单域序列连同 IB tokens 在各自 domain 内处理以捕获域内知识,跨域信息交换**仅经由不同 domain 的 IB tokens**进行,再让域内 item 重新 attend 已更新的 IB tokens,实现结构化、受控的跨域迁移(代价是略增计算与模型复杂度)。

## 结果

- **数据集**:Amazon-Review(Book/Clothing/Video/Toy/Sports 五域)、KuaiRand-1K(以 music type 区分 Type A/B)、以及工业级 Internal 数据集(社媒多 in-app surface,约 5M 用户)。所有实验重复 5 次取均值,指标为 Recall 与 NDCG。
- **平均提升**:AutoCDSR 平均把 [[sasrec]] 和 [[bert4rec]] 的 Recall@10 提升 **9.8%**、NDCG@10 提升 **12.0%/16.7%**(对应不同 backbone)。
- **Amazon-Review**:AutoCDSR 在 20 个 case 中有 12 个(SASRec)/14 个(BERT4Rec)实现超 20% 的 CDSR 提升;增强版 AutoCDSR+(如 BERT4Rec_cd + AutoCDSR+)可与多数 SOTA CDSR 模型持平甚至超越。
- **缓解 negative transfer**:在 KuaiRand-1K 上,对"单域已正确"的样本,AutoCDSR 将 cross-domain attention scores 显著降低约 **17%**;对跨域有益的样本仅小幅降低约 3%,说明选择性保留有益跨域交互。
- **效率**:Table 4 显示 BERT4Rec 基线 10.27 iter/s,+AutoCDSR 仅增 9.34% 开销、+AutoCDSR+ 增 19.96%,而 SOTA 的 SyNCRec 增 75.53%——即作者宣称比 SOTA CDSR 模型快约 4×。
- **鲁棒性**:在 KuaiRand-1K 上人为打乱部分 domain 标签(corruption 10%-50%),AutoCDSR 性能基本稳定;AutoCDSR+ 因依赖准确 domain 标签而对标签噪声更敏感。

## 在本 wiki 中的位置

本文属于 [[recommender-systems|recommender-system]] 中 [[sequential-recommendation]] 与 [[cross-domain-sequential-recommendation]] 的交叉线索,与 [[sasrec]]、[[bert4rec]]、[[gru4rec]] 等 transformer/RNN 序列推荐 backbone 相关。其核心贡献是把 [[negative-transfer]] 处理转化为 [[self-attention]] 上的 [[pareto-optimality]] / [[multi-task-learning]] 优化,可与 [[two-sided-fairness-reranking]]、[[matthew-effect]] 等推荐公平/迁移议题对照阅读,作为"用模型内在机制(而非额外模块)解决跨域迁移"的代表性工作。
