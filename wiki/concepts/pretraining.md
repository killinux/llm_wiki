---
type: concept
subtype: method
tags: [deep-learning, pre-training, self-supervised-learning, transfer-learning, llm]
created: 2026-05-31
updated: 2026-05-31
sources: 0
---

# 预训练 (Pre-training)

预训练是指在大规模无标注（或弱标注）数据上，用自监督目标训练模型参数，使其学到通用的语言/视觉/多模态表示，之后再通过[[fine-tuning]]适配具体下游任务。

## 主要范式

- **自回归语言模型**（GPT 系列）：预测下一个 token，适合文本生成。
- **掩码语言模型**（[[bert]] 系列）：随机遮盖 token 并预测，擅长理解任务。
- **对比学习**（[[clip]]、SimCLR）：拉近正样本对、推远负样本对，常用于视觉/多模态。
- **去噪自编码**（[[bart]]、T5）：corruption → reconstruction。

## 在推荐与 LLM 中的角色

- LLM 本身即预训练产物，规模与数据决定能力上限（[[scaling-laws]]）。
- 推荐领域中，预训练用于物品表示（多模态 embedding）、用户行为序列编码（[[bert4rec]]）、以及基础模型在推荐场景上的适配（[[llm-for-recommendation]]）。

## 相关页

[[self-supervised-learning]]、[[fine-tuning]]、[[transfer-learning]]、[[large-language-models]]、[[bert]]、[[scaling-laws]]
