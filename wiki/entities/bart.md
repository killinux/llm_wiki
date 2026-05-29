---
type: entity
subtype: model
tags: [seq2seq, pretraining, denoising-autoencoder, transformer]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# BART

BART 是一种基于 Transformer 的序列到序列(seq2seq)预训练模型,通过"破坏文本再重建"的去噪自编码目标进行预训练。

## 在本 wiki 中的出现

- 在 [[2020-rag]] 中,BART 作为预训练的 seq2seq 生成器,与可检索的 Wikipedia 稠密索引结合,统一微调用于知识密集型 NLP 任务,并取得多项 SOTA。

## 相关

- [[rag]]
- [[seq2seq]]
- [[transformer]]
- [[dense-retrieval]]
- [[wikipedia]]
