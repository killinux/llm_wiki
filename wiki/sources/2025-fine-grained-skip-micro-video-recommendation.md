---
type: source
subtype: paper
tags:
  - recommender-system
  - micro-video-recommendation
  - graph-neural-network
  - lightgcn
  - skip-behavior
  - bpr
created: 2026-05-29
updated: 2026-05-29
arxiv: 2504.03107
raw: raw/2504.03107.pdf
authors:
  - Sanghyuck Lee
  - Sangkeun Park
  - Jaesung Lee
year: 2025
---

# Exploiting Fine-Grained Skip Behaviors for Micro-Video Recommendation

一句话:针对 micro-video 推荐中被传统方法粗暴二分(正/负)的 skip 行为,本文提出基于双层图(dual-level graph)与分层 ranking loss 的方法,将交互细分为 highly positive、less positive、negative 三类,在两个公开数据集的八项指标上超越三个 baseline。

## 问题

micro-video(通常时长不足三分钟的短视频)推荐中,用户在观看前几秒后才决定是否继续观看或滑走,因此视频的前几秒承载强烈信号。作者通过对 [[2022-kuairand]] 的 KuaiRand-Pure 与 MVA(Micro-video-A)数据集的统计观察发现:大多数 skip 都发生在视频前 5 秒内。

传统方法(如 FRAME)仅依据是否发生 skip 把交互简单地二分为正样本或负样本,过度简化了 skip 行为。具体而言,延迟发生的 skip(用户先看了一段时间再滑走)其实携带"较弱的正向兴趣",而前 5 秒内的快速 skip 才代表强烈的负向信号。把这两者混为一谈会损失信息。

## 方法

核心是"双层正向图构建 + 双路径正向图学习 + 分层 ranking loss"。

- **交互三分**:依据 Duration/Playing Time 与 Playing Time 阈值(5 秒)把全部交互划分为:
  - Highly Positive(Duration/Playing Time ≥ 1.0,即完整观看)
  - Less Positive(Duration/Playing Time < 1.0 但 Playing Time ≥ 5s,即延迟 skip)
  - Negative(Duration/Playing Time < 1.0 且 Playing Time < 5s,即快速 skip)
- **Dual-Level Positive Graph Construction**:用 highly positive 与 less positive 信号分别构建两个 user-video 二部交互图(交互矩阵 $R^h$、$R^l$),并用对称归一化(沿用 [[lightgcn]] 的归一化方式)得到邻接矩阵 $\bar{A}^h$、$\bar{A}^l$。negative 交互不进入图构建,而是参与损失优化。
- **Dual-Path Positive Graph Learning**:借鉴 GCN 高阶传播,分别在两条路径上做两跳 embedding propagation,得到 highly/less positive 的 user/video embedding,再 mean pooling 融合两层,得到统一的 $H_u$、$H_v$。
- **Preference Prediction Layer**:拼接用户与视频 embedding,经两层带非线性激活的权重矩阵输出偏好得分 $\hat{z}_{u,v}$。
- **分层 ranking loss(BPR)**:扩展传统 [[bpr]],对每条交互采样得到 highly/less/negative 三元组,计算两组 BPR 损失:$\mathcal{L}_{\text{BPR},h,l}$(highly vs less positive)与 $\mathcal{L}_{\text{BPR},h,n}$(highly vs negative),取平均;其中快速 skip 被视为强负信号。
- **BCE 监督损失**:把"是否被 skip"作为二分类(y=1 未被 skip),用 binary cross-entropy 作为补充监督。
- **组合损失**:$\mathcal{L}_{\text{combined}} = \lambda \mathcal{L}_{\text{BPR}} + (1-\lambda)\mathcal{L}_{\text{BCE}}$,实验中 $\lambda=0.5$。

视觉特征由预训练 CNN 逐帧提取后平均为 128 维向量(KuaiRand-Pure 无视频特征,改用可学习 embedding)。

## 结果

- **数据集**:MVA(12,739 users / 58,291 videos / 342,694 interactions);KuaiRand-Pure(27,285 users / 7,583 videos / 1,186,059 interactions)。
- **Baselines**:FRAME、LightGT(两个多模态 micro-video 模型)、BM3(多媒体推荐模型)。
- **评测指标**:Precision/Recall/MAP/[[ndcg]] @{3,5},共八项;MVA 重复 10 次、KuaiRand-Pure 重复 7 次,paired t-test(p=0.01)。
- **MVA 表现**(Proposed,全部带显著性 *):Precision@3=0.573,Recall@3=0.623,MAP@3=0.739,NDCG@3=0.790;Precision@5=0.540,Recall@5=0.882,MAP@5=0.731,NDCG@5=0.812。次优 BM3 的 NDCG@5=0.787,FRAME=0.784,LightGT=0.760。
- **KuaiRand-Pure 表现**(Proposed):Precision@3=0.279,Recall@3=0.632,MAP@3=0.545,NDCG@3=0.591;Precision@5=0.234,Recall@5=0.760,MAP@5=0.565,NDCG@5=0.637。次优 FRAME 的 NDCG@5=0.604,BM3=0.495,LightGT=0.402。
- **消融实验**:
  - 图构建方式对比(Total Interactions vs Only Highly Positives vs Proposed):双层图在所有指标最优,例如 MVA 上 NDCG@3 从 0.772(highly only)/0.768(total)提升到 0.790。
  - 损失对比(BPR with Unseen Interactions vs 提出的分层 BPR):提出的 BPR 更优,如 NDCG@3 从 0.783 提升到 0.791,说明快速 skip 作为强负信号相对于完整观看有明确的相对排序。

作者指出局限是对 5 秒阈值的依赖,未来希望摆脱固定阈值(如 [[kuairec]] 中 10 秒后仍有大量 skip),并引入 attention 机制。

## 在本 wiki 中的位置

本文属于 [[recommender-system]] / micro-video 推荐方向,与本 wiki 中已有的 micro-video 数据集与方法相邻:数据集层面与 [[2022-kuairand]]、[[2023-microlens-micro-video-recommendation-dataset]] 同源;方法层面建立在 [[lightgcn]] 的 GCN 归一化传播之上,并扩展了 [[bpr]] 损失。其核心贡献——用 watch-time / playing-time 把交互细分为多档信号——与本 wiki 中关于 watch-time debias 的工作(如 [[2023-d2co-watch-time-debias]])及 [[recommendation-with-negative-feedback]] 主题相呼应,是"细粒度反馈建模"这一脉络在 micro-video 场景的图神经网络实例。
