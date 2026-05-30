---
type: concept
subtype: method
tags: [architecture, encoder-decoder, nlp, transformer, generation]
created: 2026-05-30
updated: 2026-05-30
sources: 7
---

# 序列到序列 (Sequence-to-Sequence, Seq2Seq)

Seq2Seq 是把**一个变长序列映射为另一个变长序列**的建模范式(如翻译、摘要、问答),经典实现是 **encoder-decoder** 结构:
编码器把输入压成表示,解码器**自回归**地逐 token 生成输出。

## 演化
- **RNN 时代**:Sutskever et al. 2014 用 LSTM encoder-decoder;Bahdanau **attention** 缓解长序列信息瓶颈,是 [[attention]] 机制的起点。
- **Transformer 时代**:[[transformer]](《Attention Is All You Need》)用全注意力替代 RNN,encoder-decoder 成为机器翻译标准;
  [[t5]] 把所有 NLP 任务统一为 "text-to-text" seq2seq;[[bart]] 用去噪自编码预训练 seq2seq。
- **Decoder-only 的兴起**:[[gpt-3]] 等 decoder-only 自回归 LM 把"输入"也当作待续写的前缀,在很多任务上取代了显式 encoder-decoder,
  但 seq2seq 的"条件生成"思想被保留。

## 在本 wiki 的延伸
seq2seq 的"自回归生成"被迁移到非 NLP 领域:[[decision-transformer]] 把 RL 重构为序列建模;生成式推荐(如 [[hstu]]、[[2024-generative-regression-watch-time-prediction]])
把推荐 / 回归重构为 token 序列生成;[[rag]] 用可检索知识增强 seq2seq 生成。

## 相关页
[[transformer]]、[[attention]]、[[t5]]、[[bart]]、[[rag]]、[[decision-transformer]]
