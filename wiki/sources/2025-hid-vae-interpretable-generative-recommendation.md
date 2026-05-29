---
type: source
subtype: paper
tags:
  - generative-recommendation
  - semantic-id
  - hierarchical-representation
  - disentangled-representation-learning
  - vector-quantization
  - recommender-system
created: 2026-05-29
updated: 2026-05-29
arxiv: 2508.04618
raw: raw/2508.04618.pdf
authors:
  - Dengzhao Fang
  - Jingtong Gao
  - Chengcheng Zhu
  - Yu Li
  - Xiangyu Zhao
  - Yi Chang
year: 2025
---

# HiD-VAE: Interpretable Generative Recommendation via Hierarchical and Disentangled Semantic IDs

HiD-VAE 提出一种层次化监督的量化框架,为 item 学习"可解释 + 解耦"的 semantic ID,既给出可追溯的类别路径(如 Clothing → Topwear → Dress),又用 uniqueness loss 消除 "ID 碰撞",从而提升[[generative-recommendation]]的精度与多样性。

## 问题

[[generative-recommendation]]把传统"检索-排序"流水线统一为端到端的自回归 item ID 生成,其效果高度依赖 [[semantic-id|semantic ID]] 的质量。现有方法(如 [[tiger|TIGER]]、[[lc-rec|LC-Rec]] 基于 [[rq-vae|RQ-VAE]],或 [[vq-rec|VQ-Rec]] 基于 PQ)依赖**无监督向量量化**,存在两个根本缺陷:

1. **语义扁平、不可解释**:学到的层次只是隐式副产品,缺乏显式监督结构,模型成为"黑盒"。
2. **表示纠缠 / ID 碰撞**:不同 item(如 Dress 与 T-Shirt)被映射到相同的离散 ID 序列,损害推荐准确性与多样性。论文测得无监督 baseline 的碰撞率高达 17.8%–22.5%。

## 方法

HiD-VAE 采用"先学表示、再生成"的两阶段设计。

**Stage 1 — 离线层次 ID 学习(HiD-VAE)**:在 [[rq-vae|RQ-VAE]] 的级联量化结构上,引入两类层次化监督损失:
- **Tag Alignment Loss(对比对齐损失)**:把每层累积量化嵌入 z_q 通过层级专属 projector 拉向对应层级的真实标签嵌入,推开其他标签,采用温度 τ=0.07。
- **Tag Prediction Loss(分类损失)**:每层用一个分类器 C_l 预测该层级的类别标签;深层用更大隐藏维与更高 dropout,支持 focal loss(γ=2.0)处理类别不均衡。

**Disentanglement via Uniqueness Loss(解耦/唯一性损失)**:对一个 batch 内被分到相同 semantic ID 序列的 item 对 (i, j),在**量化前的连续 latent** z_0 上施加 margin 惩罚(margin m=0.9),直接惩罚 latent 重叠,鼓励 item→ID 的单射映射,从源头消除 ID 碰撞。总损失为重构 + commitment + β_sup·(align+pred) + β_unique·unique。

**层次标签生成(无标签数据集)**:针对 [[kuairand|KuaiRand]] 等缺乏类别层次的数据集,提出"检索-再分类"流程——先对每层用 sentence encoder 做 Top-K 近邻检索得到候选标签集,再让 LLM 在小候选集内做分类(constrained),避免幻觉,自动生成可靠的层次标签。

**Stage 2 — 在线可解释推荐**:冻结 HiD-VAE 作为 item tokenizer,用一个 Transformer encoder-decoder 自回归预测下一个 item 的 ID 序列。两项设计:
- **Hierarchy-Aware Semantic Embeddings**:每个 token 先映射到对应 tag 文本并编码为语义向量,再与可学习的 ID embedding、层级 type embedding 拼接。
- **Constrained Decoding**:推理时动态屏蔽,仅允许构成"已存在有效前缀"的 token,保证生成的 ID 一定对应真实 item。

## 结果

数据集:Amazon **Beauty**、**Sports and Outdoors**、**KuaiRand-1K**;5-core、leave-one-out,指标 Recall@K 与 [[ndcg|NDCG]]@K(K=5,10)。实现:768 维 Sentence-Transformer 输入,L=3 量化层、codebook 大小 K=256;Stage 2 为 6 层 Transformer、8 头、隐藏 512;NVIDIA 4060、FP16。

**整体性能(RQ1,Table 1)**:HiD-VAE 在三数据集、所有指标上均为最佳,显著优于最强 baseline(多为 [[lc-rec|LC-Rec]])。
- Beauty:Recall@5 相对提升 **+35.07%**(0.0543),NDCG@5 **+33.08%**(0.0358)。
- Sports:NDCG@5 **+32.27%**(0.0332)。
- KuaiRand:NDCG@5 **+18.86%**(0.0479),Recall@5 0.0668。
生成式范式([[tiger|TIGER]]、[[lc-rec|LC-Rec]])整体优于判别式排序模型(GRU4Rec/Caser/HGN/NextItNet/[[sasrec|SASRec]]/[[bert4rec|BERT4Rec]])。

**ID 碰撞率(RQ3,Table 3,越低越好)**:HiD-VAE Full 把碰撞率降到极低 —— Beauty 2.1%、Sports 2.8%、KuaiRand 1.9%,相比最强 baseline [[vq-rec|VQ-Rec]](20%+)在 Sports 上**相对降低 87.6%**。t-SNE 可视化显示 w/o DUL 同类 item 坍缩重叠,加 DUL 后清晰分离。

**消融(RQ2,Table 2)**:
- w/o DUL 性能下降最大(Beauty R@10 0.0698→0.0524),证明 uniqueness loss 是成功的主要驱动;且 DUL 单独已远胜 RQ-VAE 的事后追加整数法。
- 去掉 Tag Prediction(w/o Tag Pred)比去掉 Tag Align 下降更明显,说明分类信号是更强的语义锚点。
- 有趣发现:w/o HS(去掉层次监督)即便保留 DUL,碰撞率仍高于 Full,说明层次监督会间接促进解耦。

**Case study**:对同一用户,RQ-VAE 给出不透明数字码(如 [17,83,152]),而 HiD-VAE 的 ID 可解码为可读路径 "Skincare → Treatments → Serums",提供可追溯推理与更强可控性。

## 在本 wiki 中的位置

本文属于 [[llm-for-recommendation]] 与 [[generative-recommendation]] 方向,核心是改进 [[semantic-id|semantic ID]] 的 tokenization 质量,直接对标 [[tiger|TIGER]]、[[lc-rec|LC-Rec]]、[[vq-rec|VQ-Rec]] 等基于 [[rq-vae|RQ-VAE]]/[[vector-quantization|VQ]] 的方法。它结合 [[variational-autoencoder|VAE]]、[[disentangled-representation-learning|解耦表示学习]] 与 [[hierarchical-representation|层次表示]],并借助 [[large-language-models|LLM]] 为无标签数据生成类别层次。下游用 [[transformer|Transformer]] 做 [[sequential-recommendation|sequential recommendation]],在 [[recommender-system|推荐系统]] 中兼顾精度、多样性与可解释性,可与 [[recommendation-diversity]]、[[recommender-system]] 等条目互链。
