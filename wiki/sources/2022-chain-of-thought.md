---
type: source
subtype: paper
tags:
  - prompting
  - reasoning
  - in-context-learning
  - emergent-abilities
  - llm
created: 2026-05-29
updated: 2026-05-29
arxiv: "2201.11903"
raw: raw/2201.11903.pdf
authors:
  - Jason Wei
  - Xuezhi Wang
  - Dale Schuurmans
  - Maarten Bosma
  - Brian Ichter
  - Fei Xia
  - Ed H. Chi
  - Quoc V. Le
  - Denny Zhou
year: 2022
---

本文提出 **Chain-of-Thought (CoT) prompting**:在 few-shot 示例中给出"中间推理步骤"链条,引导大模型在给出最终答案前先生成一系列自然语言推理步骤,从而显著提升其在算术、常识与符号推理任务上的表现。论文发表于 NeurIPS 2022,作者来自 Google Research / Brain Team。

## 问题

现代 NLP 已被大语言模型革新,扩大模型规模(scaling)带来了诸多收益,但**仅靠扩大规模并不足以解决**算术、常识、符号推理这类具有挑战性的任务。已有两类思路各有局限:

- **rationale-augmented 训练 / 微调**(如 Ling et al. 2017、[[cobbe-gsm8k]] 的 verifier 方法)需要大量高质量的推理标注,成本高昂。
- 传统 [[few-shot-prompting]](Brown et al. 2020 推广)在需要推理的任务上表现差,且性能往往**不随模型规模显著提升**。

如何在不更新模型参数的前提下,让 LLM 具备多步推理能力,是本文要解决的核心问题。

## 方法

核心思想:**chain-of-thought prompting**。在 in-context 示例(exemplars)中,不再只提供 ⟨输入, 答案⟩ 二元组,而是提供 ⟨输入, chain of thought, 答案⟩ 三元组,其中 chain of thought 是一连串导向最终答案的自然语言中间推理步骤。

- 这是一种纯 **prompting** 方法,**不微调、不更新模型权重**,只改变提示中的少量示例(算术任务用一组手写的 **8 个** CoT 示例,AQuA 用 4 个)。
- 模型在测试时被引导先"逐步思考"生成中间推理过程,再输出最终答案;实验采用 greedy decoding。
- 作者强调 CoT 是一种 [[emergent-abilities]](涌现能力):只有当模型规模达到约 **100B 参数** 以上时 CoT 才带来增益;在较小模型上,CoT 生成的推理链流畅但不合逻辑,反而损害性能。
- 在五个大模型上验证:[[gpt-3]](text-ada/babbage/curie/davinci-001 等)、[[lamda]](最大 137B)、[[palm]](8B/62B/540B)、[[ul2]] 20B 与 [[codex]]。
- 涵盖三类任务:算术推理([[gsm8k]]、SVAMP、ASDiv、AQuA、MAWPS)、常识推理([[commonsenseqa]]、[[strategyqa]]、BIG-bench 的 Date/Sports、[[saycan]])、符号推理(末位字母拼接、硬币翻转)。
- 还做了消融:equation only、variable compute only(输出等量的点 "...")、chain of thought after answer,三者都接近 baseline,说明收益来自"以自然语言表达的中间推理步骤"本身。

## 结果

- **算术推理**:在 [[gsm8k]] 上,[[palm]] 540B + CoT 达到约 **57%** 解题率(达到当时 SOTA),超过 prior best 55% 与 finetuned [[gpt-3]] 175B 的 33%;标准 prompting 仅 18%。对最大的 GPT 与 PaLM 模型,CoT 使 GSM8K 性能比标准 prompting **翻倍以上**。PaLM 540B + CoT 在 SVAMP、MAWPS 上也取得新 SOTA,在 AQuA、ASDiv 上接近 SOTA(差距 2% 以内)。
- **规模依赖(涌现)**:在小模型上 CoT 几乎无增益甚至负向,仅在约 100B 参数以上的大模型(如 [[palm]] 540B、[[gpt-3]] 175B、[[lamda]] 137B)上出现明显跃升。
- **常识推理**:[[palm]] 540B + CoT 在 [[strategyqa]] 上达 **75.6%**(prior SOTA 69.4%),在 Sports Understanding 上达 **95.4%**(超过非专家人类 84%);在 [[commonsenseqa]] 上增益较小。
- **符号推理**:在末位字母拼接、硬币翻转上,[[palm]] 540B + CoT 接近 **100%** in-domain 解题率,并展现出对更长、超出示例长度的输入的 **length generalization**(长度泛化,OOD)能力;标准 prompting 在 OOD 上失败。
- **鲁棒性**:不同标注者、不同示例集、不同示例顺序与数量下,CoT 均稳定优于标准 prompting,表明效果不依赖特定语言风格。

## 在本 wiki 中的位置

本文是 [[prompt-engineering]] 与 LLM 推理研究的奠基性工作之一,确立了"通过提示激发中间推理步骤"这一范式,直接启发了后续大量工作,包括 [[zero-shot-cot]]("Let's think step by step")、[[self-consistency]](对多条推理链投票)、[[least-to-most-prompting]]、[[tree-of-thoughts]] 等。它与 [[in-context-learning]] 和 [[emergent-abilities]] 的讨论紧密相关,是理解现代 LLM reasoning 能力的关键入口。
