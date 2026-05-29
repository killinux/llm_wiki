---
type: source
subtype: paper
tags: [sequential-recommendation, state-space-model, mamba, lifelong-sequence, long-sequence-modeling, efficiency, recommender-system]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2403.16371
raw: raw/2403.16371.pdf
authors: [Jiyuan Yang, Yuanzi Li, Jingyu Zhao, Hanbing Wang, Muyang Ma, Jun Ma, Zhaochun Ren, Mengqi Zhang, Xin Xin, Zhumin Chen, Pengjie Ren]
year: 2024
---

# Uncovering Selective State Space Model's Capabilities in Lifelong Sequential Recommendation

本文提出 [[recmamba]],用带选择机制的状态空间模型 [[mamba]] 替换 Transformer 层来建模"终身"(lifelong,长度 >=2k)用户行为序列,在保持与 [[sasrec]] 相当的推荐效果的同时,大幅降低训练时长(约 70%)和显存占用(约 80%)。

## 问题

[[sequential-recommendation]] 旨在从用户的序列化交互中建模其动态兴趣。随着用户在线参与度提高,平台积累了海量的终身(lifelong)用户行为序列,但现有序列推荐模型难以处理这类超长序列,主要瓶颈有二:

- **计算复杂度**:基于 self-attention 的 [[sasrec]] 在序列长度上是二次复杂度,且显存需求巨大,长序列下易 OOM;多数现有研究只允许模型接受约 200 条交互记录,无法真正表征"终身"兴趣。
- **长程依赖建模能力**:Markov Chain 类方法假设下一次交互只依赖前一(或前几)次,难以刻画长程 item 转移;[[gru4rec]] 等 RNN 方法存在信息遗忘与梯度消失问题。

核心研究问题:i) 如何高效处理超长用户行为序列(兼顾数据稀疏与计算复杂度);ii) 如何捕获序列内的长程 item 转移依赖。论文聚焦序列长度 >=2k 的真实场景(如微视频用户每天观看数十上百个视频)。

## 方法

[[mamba]] 是一种引入了数据相关(data-dependent)选择机制的状态空间模型([[state-space-model]], SSM),目标是在达到 Transformer 建模能力的同时实现序列长度上的线性扩展,并通过硬件感知的并行循环算法高效处理长序列。

- **RecMamba 框架**:将序列推荐模型中的 Transformer 层替换为 Mamba block,以选择性地建模终身用户序列、捕获随时间演化的用户偏好。
- **与 Mamba4Rec 的区别**:Mamba4Rec 是首个将 Mamba 用于高效序列推荐的工作,其做法是用 Mamba block 替换 self-attention block;而 [[recmamba]] 替换的是整个 Transformer 层,从而进一步提升处理终身序列的效率。
- **实验设置**:在两个真实数据集 [[kuairand]](来自 [[kuaishou]] 微视频平台,含随机曝光物品以保证无偏,平均序列长 11,811)与 [[lfm-1b]](Last.FM 音乐平台,超十亿次收听交互,平均序列长 9,043)上评测;采用 leave-one-out 划分,指标为 Recall 与 NDCG;对比基线包括 attention 类 [[sasrec]]、RNN 类 [[gru4rec]] 与线性 attention 类 [[linrec]];在 NVIDIA A800 80G 上训练 500 epoch,序列长度取 2k 与 5k。

## 结果

- **效果(Table 2)**:RecMamba 与 SASRec 显著优于 LinRec 和 GRU4Rec。在 2k 长度上 RecMamba 略逊于 SASRec(次优);但在 5k 长度上多数情况下超过 SASRec。例如 KuaiRand(5k) 上 RecMamba 取得 Recall@5=0.7004、NDCG@5=0.5713,均优于 SASRec 的 0.6422/0.5224。
- **效率(Table 3)**:在 LFM-1b(2k) 上,相比 SASRec,RecMamba 训练时长减少约 **73%**、推理时间减少约 **61%**、显存占用减少约 **80%**(SASRec 39.85G → RecMamba 7.60G)。摘要中概括为训练时长降低约 70%、显存降低 80%。
- **可扩展性**:在 5k 长度下,SASRec 出现 OOM(需把 batch size 从 256 降到 32 仍不行),而 RecMamba 仍能正常运行,且其效率优势随序列长度增长而更显著。
- **长序列收益(RQ1)**:在两个数据集上,序列越长 RecMamba 效果越好,印证引入更长序列有助于建模用户兴趣。

## 在本 wiki 中的位置

本文是 [[mamba]] / [[state-space-model]] 在 [[recommender-systems|recommender-system]] 领域的早期落地工作之一,与同期的 Mamba4Rec 并列,主张用线性复杂度的 SSM 解决 [[sequential-recommendation]] 中长序列的效率与长程依赖难题。它与 wiki 中 [[sasrec]]、[[lifelong-learning]] 以及 [[kuairand]]、[[lfm-1b]] 等推荐数据集条目直接相关,可作为"序列推荐的高效长序列建模"这一脉络的参考。
