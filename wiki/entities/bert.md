---
type: entity
subtype: model
tags: [nlp, pre-training, transformer, masked-language-model, google]
created: 2026-05-31
updated: 2026-05-31
sources: 0
---

# BERT

BERT（Bidirectional Encoder Representations from Transformers）是 Google 于 2018 年提出的双向 Transformer 编码器预训练模型。通过**掩码语言模型（MLM）**和**下一句预测（NSP）**两个自监督目标在大规模语料上预训练，再在下游任务上微调，刷新了当时 11 项 NLP 基准。

## 核心设计

- **双向上下文**：与 GPT 系列的自回归（左到右）不同，BERT 同时利用左右两侧上下文，通过随机遮盖 15% 的 token 让模型预测被遮盖位置。
- **两阶段范式**：预训练 → 微调（pre-train → fine-tune），奠定了后续 NLP 预训练模型的标准流程。
- **规模**：BERT-Base（110M 参数，12 层）/ BERT-Large（340M 参数，24 层）。

## 影响与后续

BERT 直接催生了 RoBERTa、ALBERT、DistilBERT、ELECTRA 等改进变体，也影响了推荐领域的 [[bert4rec]]（将 MLM 思想用于序列推荐）。在 LLM 时代，BERT 编码器架构被 decoder-only 架构（[[gpt-4]] 等）逐渐取代，但其预训练-微调范式仍是基础范型。

## 相关页

[[transformer]]、[[large-language-models]]、[[fine-tuning]]、[[self-supervised-learning]]、[[bert4rec]]、[[google]]
