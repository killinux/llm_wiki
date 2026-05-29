---
type: source
subtype: paper
tags: [recommender-system, micro-video-recommendation, video-recommendation, efficiency, frozen-vision-encoder, sequential-recommendation]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2605.08810
raw: raw/2605.08810.pdf
authors: Yang Xiao, Huiyuan Chen, Kaiyuan Deng, Chao Jiang, Zinan Ling, Ruimeng Ye, Xiaolong Ma, Bo Hui
year: 2026
---

# Compressed Video Aggregator (CVA): 面向高效微视频推荐的内容驱动模块

CVA 是一个轻量级微视频([[micro-video-recommendation]])推荐模块,它把冻结视觉基础模型(frozen VFM)产出的密集帧 embedding 通过 self-attention 压缩成紧凑的视频 embedding(Compact Video Embedding),在保留视频内容语义的同时,把训练时间和 GPU 显存降低数个数量级。

## 问题

短视频(micro-video / short-form video)已成为主流娱乐形式(中国约 10.5 亿用户)。现有视频推荐方法存在两大关键局限:

- **依赖行为信号、忽略内容**:多数工作只用 user-video 交互信号(点击、watch time、dwell time)或视频级属性(标题、封面、点赞、播放量),不建模视频内容本身,无法学习视频的语义关系和时序结构,本质上是在训练集上过拟合,难以泛化到真实场景(尤其 [[cold-start]] 物品)。
- **直接用视频内容算力代价高**:在现代短视频平台(数百万视频、海量用户活动)上应用视频编码器、[[vit]]/VLM 或视频 MLLM 会带来巨大开销——训练时间极长(时序建模需大规模多 GPU 训练)、GPU 显存消耗高(视频模型同时处理多帧)、推理慢(在线推荐无法承担每物品重编码)。

此外,现有微视频数据集的原始帧采样过于粗糙:Short-Video 用 8 帧均匀采样,MicroLens 取每视频中点连续 5 帧,均可能错过最能代表视频整体语义的帧。

## 方法

CVA 把流程解耦为两个阶段(详见原文 Figure 2),并包含可选的语义重采样:

- **Semantic Resampling(可选)**:不用标准均匀/随机采样,而是把原始视频切成 100 个片段抽 100 帧,用 [[clip]] 模型计算帧与视频标题(Title)的相似度,选出语义最相关的 top-N(MicroLens N=5,Short-Video N=8)关键帧并按时间戳排序。实验显示该策略对所有方法都能提升性能。
- **Phase I — Offline Preprocessing(一次性)**:用冻结的视觉基础模型 VFM(如 DINOv3)对关键帧编码成密集特征矩阵 H_v ∈ R^{N×D} 并缓存。冻结编码器避免了反向传播穿过视觉骨干的巨大算力。
- **Phase II — Online Training(CVA 模块)**:CVA 是基于 [[transformer]] 的可学习模块,把变长帧 embedding 蒸馏成定长紧凑向量。
  - **CVA Encoder**:先对 N 帧做 masked mean pooling 压成单向量 Z,经 FFN 投影到 latent 维度,再 Repeat 成 K 个 latent(Z_0);
  - **CVA Self-Attention**:Z_0 过 M 个 Transformer block(Self-Attention + FFN + LN + 残差),做深度推理、过滤噪声、增强语义密度;
  - **CVA Decoder**:对 Z_M 平均后经 FFN 和线性层,得到最终紧凑视频 embedding e_v ∈ R^D。
  - **User Encoding**:把用户历史观看视频的 e_v 序列喂给标准序列推荐 user encoder(如 [[sasrec]]、[[gru4rec]]、[[nextitnet]]),用 dot product 算预测分,用 [[cross-entropy]] 损失(in-batch 负采样)训练。
- 关键架构发现(消融):在 video aggregation 中 **self-attention(对 latent token)是关键组件,而 cross-attention 反而引入噪声**——从 Perceiver IO 出发逐步移除 cross-attention 反而提升性能,而移除所有 attention 则掉点。

## 结果

在 **MicroLens-100K** 和 **Short-Video** 两个基准上评估,报告 HR@10/HR@20、NDCG@10/NDCG@20、训练时间和 GPU 峰值显存:

- **MicroLens-100K**:用 SASRec + CVA(M=8)取得最佳综合性能,HR@10 = 10.007、HR@20 = 14.394,超过重型视频骨干 SlowFast-50(HR@10 = 9.179)和 VideoMAE(HR@10 = 8.373)。同时训练时间约缩短 30 倍(46513s → 1427s)、峰值显存约低 126 倍(143.85GB → 1.14GB)。在 GRU4Rec、NextItNet 等 user encoder 上,CVA 也一致优于 Perceiver IO 和 MLP 基线。
- **Short-Video**:CVA 在多数 user encoder 上稳定优于 Perceiver IO,例如 NARM 上把 HR@10 从 0.346 提升到 1.433;GRU4Rec、FMLPRec、BERT4Rec 等也有一致增益,且训练时间/显存相当或更低。
- **生成描述质量(Table 2)**:相比 Baseline(Mid-5),重采样方法在 Perplexity(168.34 → 65.83)、Diversity(0.7336 → 0.9496)、Avg. Length(103.80 → 165.13)上更优,语义相似度(0.5781 → 0.5518)略降但相当。
- **鲁棒性(Table 7)**:面对 No Title / Noisy Title / Mismatched Title / Masked Title 四种异常标题场景,性能虽下降但 CVA 仍稳健可用,因为压缩后的 latent token 充当"缓冲"过滤噪声。
- **更多帧 → 更好性能**:HR@10 从 9.317(2 帧)升到峰值 10.163(17 帧),NDCG@10 在 20 帧达 5.492,而 GPU 显存因 CVA 在聚合前 pooling 帧 embedding 几乎不变(约 1GB)。
- CVA 是 **VFM-agnostic** 的,可与不同 VFM 配合,其中 DINOv3 综合表现最佳,作为默认骨干。Fully fine-tuning(冻结层=0)在各视觉编码器上均劣于部分冻结,且训练更慢、显存更大。

## 在本 wiki 中的位置

CVA 属于 [[video-recommendation]]/[[micro-video-recommendation]] 中"用冻结视觉骨干 + 轻量聚合模块实现内容感知且高效"的路线,与依赖 ID 与行为信号的传统 [[recommender-systems|recommender-system]] 互补,可缓解 [[cold-start]]。它把 [[clip]] 语义重采样、[[transformer]] self-attention 聚合与标准序列 user encoder([[sasrec]]、[[gru4rec]]、[[nextitnet]])结合,并与 Perceiver IO 等 cross-attention 压缩范式形成对照。可与 [[recommender-systems|recommender-system]]、[[sequential-recommendation]]、[[vit]]、[[clip]]、[[cold-start]] 等页面互链。
