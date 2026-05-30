---
type: entity
subtype: model
tags: [recommender-system, generative-recommendation, llm-for-recommendation, semantic-id, sequential-recommendation]
created: 2026-05-30
updated: 2026-05-30
arxiv: 2311.09049
raw: raw/2311.09049.pdf
authors: [Bowen Zheng, Yupeng Hou, Hongyu Lu, Yu Chen, Wayne Xin Zhao, Ming Chen, Ji-Rong Wen]
affiliations: [Renmin University of China, Tencent WeChat, UC San Diego]
venue: "ICDE 2024"
---

# LC-Rec

LC-Rec(Adapting Large Language Models by Integrating **C**ollaborative Semantics for Recommendation)是一个把**语言语义**与
**协同语义**融合进 [[large-language-models]] 的生成式推荐模型:直接从**整个物品集**生成推荐(不依赖候选集),由 RUC + 腾讯微信团队提出
(arXiv 2311.09049,ICDE 2024)。

## 解决的问题
LLM 与推荐系统间存在**语义鸿沟**:待推荐物品常用 LLM 词表外的离散 **item ID** 索引;LLM 捕捉语言语义,而推荐系统隐含协同语义
([[implicit-feedback|协同信号]]),难以充分发挥 LLM 容量。

## 方法(两大贡献)
- **物品索引 (item indexing)**:基于学习的**向量量化**([[rq-vae]] 路线)+ **uniform semantic mapping**,为每个物品分配有意义且**不冲突**的
  语义 ID([[semantic-id]]),纳入 LLM 词表。
- **对齐微调 (alignment tuning)**:设计一系列专门的微调任务,强制 LLM **深度融合**语言语义与协同语义(由学到的 item index 刻画),实现对推荐任务的有效适配。

## 在本 wiki 中的位置
属于 [[generative-recommendation|生成式推荐]] / [[llm-for-recommendation]] 的 **semantic ID + 单 codebook** 路线,与 [[tiger|TIGER]]、
[[vq-rec|VQ-Rec]] 同族,常被并列对比;后续工作如 [[2025-hid-vae-interpretable-generative-recommendation]]、[[2025-flexcode-dual-codebook-generative-recommendation]]
针对其量化质量/可解释性做改进。连接 [[rq-vae]]、[[hstu]]、[[sequential-recommendation]]。代码:RUCAIBox/LC-Rec。
