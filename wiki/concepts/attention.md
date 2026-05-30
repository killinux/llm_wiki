---
type: concept
subtype: method
tags: [architecture, attention, transformer, deep-learning]
created: 2026-05-30
updated: 2026-05-30
sources: 12
---

# 注意力机制 (Attention)

注意力是一种让模型**按相关性动态加权聚合信息**的机制:对每个查询 (query),根据它与各个键 (key) 的相似度算出权重,
再对相应的值 (value) 做加权求和。它取代了 RNN 的固定隐状态瓶颈,是 [[transformer|Transformer]] 与现代 LLM 的计算核心。

## 标准形式:Scaled Dot-Product Attention
`Attention(Q,K,V) = softmax(QKᵀ / √d_k) · V`
- **Q/K/V** 由输入线性投影得到;`√d_k` 缩放防止点积过大导致 softmax 梯度消失。
- **多头注意力 (Multi-Head)**:并行多组 QKV 投影,各自在不同子空间建模关系,再拼接——增强表达力。

## 变体
- **自注意力 (self-attention)** vs **交叉注意力 (cross-attention)**:Q 与 K/V 同源 / 异源;见 [[self-attention]]。
- **掩码注意力 (causal mask)**:decoder 自回归时只看左侧。
- **效率改进**:[[linear-attention]](O(N)→长序列)、[[flash-attention]](IO 感知、显存友好)、稀疏/局部注意力。
- **位置编码**:注意力本身置换不变,需 [[rope|RoPE]] 等注入位置信息。

## 起源与演化
源于 Bahdanau 2014 为机器翻译 [[seq2seq]] 缓解长程瓶颈;[[transformer]](《Attention Is All You Need》)用纯注意力替代循环,
确立"注意力即一切"。此后注意力被迁移到视觉([[clip]]、[[vision-transformer]])、推荐(自注意力序列推荐 [[bert4rec]]、[[autoint]]、生成式 [[hstu]])等。

## 相关页
[[transformer]]、[[self-attention]]、[[linear-attention]]、[[flash-attention]]、[[rope]]、[[multi-head-attention]]
