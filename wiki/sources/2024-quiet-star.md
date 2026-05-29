---
type: source
subtype: paper
tags: [reasoning, self-improvement, language-models, chain-of-thought, test-time-compute, pretraining]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2403.09629
raw: raw/2403.09629.pdf
authors: [Eric Zelikman, Georges Harik, Yijia Shao, Varuna Jayasiri, Nick Haber, Noah D. Goodman]
year: 2024
---

# Quiet-STaR: Language Models Can Teach Themselves to Think Before Speaking

Quiet-STaR 让语言模型在生成每个 token 之前先生成一段隐式的"思考"(rationale)来更好地预测后续文本,从而以自监督方式在任意网络文本上学会推理,无需任务特定微调即可提升下游推理能力。

## 问题

[[chain-of-thought]] 等以推理为核心的工作通常把推理框定为"回答问题"或"完成 agentic 任务"的方法。但推理其实隐含在几乎所有书面文本里(例如证明步骤之间未写出的中间过程、对话背后的 theory of mind)。

前作 [[eric-zelikman|STaR]](Self-Taught Reasoner)通过在问答任务中从 few-shot 示例推断 rationale、并保留那些能导出正确答案的 rationale 来学习有用的思考。但这是一个高度受限的设定。理想情况下,语言模型应能从任意文本中学会推断那些未被写出的 rationale。把这种能力一般化面临三个核心挑战:

1. 生成续写(continuation)的计算开销;
2. 模型一开始并不知道如何生成或使用内部思考;
3. 需要预测超出单个 next-token 的内容。

## 方法

Quiet-STaR 是 STaR 的一般化,核心是在每个 token 位置都生成 rationale 来解释未来文本。整体流程分为 Think / Talk / Learn 三步反复迭代:

- **Think(并行 rationale 生成):** 提出一种 tokenwise 并行采样算法,通过特制的 attention mask,让每条 thought 只 attend 自身、前文以及起始 thought token,从而在所有 token 位置同时生成 thought,缓解逐位置生成的开销。引入可学习的 `<|startofthought|>` 与 `<|endofthought|>` 特殊 token(用破折号 "---" 的 embedding 初始化)来标记思考的起止。
- **Talk(混合 rationale 前后的预测):** 用一个浅层 MLP 构成的 "mixing head" 产生一个权重,在"有 rationale"与"无 rationale"两种 next-token 预测 logits 之间插值,从而在微调早期缓解分布漂移。
- **Learn(优化 rationale 生成):** 用 [[reinforcement-learning|REINFORCE]] 提升那些有助于预测未来文本的 rationale 的似然;用扩展的 teacher-forcing 技巧把多个未来 token 的 loss 纳入,并减去 baseline(均值)以降低方差。总损失结合了未来 token 的负对数似然项和针对 rationale token 的策略梯度项。

实验以 [[mistral-7b|Mistral 7B]] 为基座,在 OpenWebMath 等互联网文本语料上做 continued pretraining;典型超参为 thought 长度 12 个 token、向前看若干 true token、采样多条 thought。

## 结果

经过 Quiet-STaR continued pretraining 后,在**无任何任务特定微调**的前提下取得 zero-shot 提升:

- [[gsm8k|GSM8K]]:5.9% → 10.9%;
- [[commonsenseqa|CommonsenseQA]]:36.3% → 47.2%;
- 在自然文本上,困难(difficult-to-predict)token 的 perplexity 显著改善。

分析进一步显示:生成的 rationale 不成比例地帮助那些更难预测的 token(即需要推理的 token);更长的 thought 和更多向前看的 token 在一定范围内带来更好效果。这表明该方法学到的是更通用、可扩展的推理能力。

## 在本 wiki 中的位置

Quiet-STaR 属于 [[self-improvement]] / [[reasoning]] 路线,是 STaR([[eric-zelikman]]、[[noah-goodman]] 等)的直接延续与一般化,把推理从结构化问答扩展到任意非结构化文本的自监督学习。它与 [[chain-of-thought]]、[[test-time-compute]]、[[rejection-sampling-fine-tuning]]、[[expert-iteration]] 等"让模型先想再答"的工作相邻;在 [[process-supervision]] / [[outcome-supervision]] 的对照下,它通过下游预测收益隐式地为思考提供监督信号。基座与机构方面关联 [[stanford-university]]。
