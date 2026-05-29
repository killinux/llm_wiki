---
type: source
subtype: paper
tags:
  - rlhf
  - instruction-tuning
  - alignment
  - llm
created: 2026-05-29
updated: 2026-05-29
arxiv: 2203.02155
raw: raw/2203.02155.pdf
authors:
  - Long Ouyang
  - Jeff Wu
  - Xu Jiang
  - Diogo Almeida
  - Carroll L. Wainwright
  - Pamela Mishkin
  - Chong Zhang
  - Sandhini Agarwal
  - Katarina Slama
  - Alex Ray
  - Ryan Lowe
  - et al. (OpenAI)
year: 2022
---

InstructGPT 通过基于人类反馈的强化学习([[rlhf]])对 [[gpt-3]] 进行微调,使语言模型更好地遵循用户指令、更真实、毒性更低;一个 1.3B 参数的 InstructGPT 在人类评测中胜过 175B 的 GPT-3。

## 问题

大型语言模型(如 [[gpt-3]])仅以预测下一个 token 为目标进行训练,这一目标与"有帮助地、安全地遵循用户的指令"并不一致。模型常常会编造事实、生成有偏见或有毒的内容,或者根本不照用户意图行事。简单地把模型做大并不能解决这种**对齐(alignment)**问题。论文要回答的核心问题是:如何让语言模型的行为符合用户的真实意图(包括显式意图如"遵循指令"与隐式意图如"真实、无害")。

## 方法

论文提出用 [[rlhf]] 对齐模型,整体分为三步:

1. **监督微调(SFT)**:招募约 40 名标注员,收集人工撰写的 prompt 与示范回答,用这些 (prompt, response) 演示数据对 [[gpt-3]] 做有监督微调。prompt 主要来自提交到 OpenAI API Playground 的真实用户请求,以及标注员编写的任务(generation、open QA、brainstorming、chat、rewrite、summarization、classification 等)。
2. **训练奖励模型(RM)**:对同一个 prompt 采样模型的多个输出,让标注员按质量**排序**;用这些比较数据训练一个奖励模型([[reward-model]]),预测人类更偏好哪个回答。RM 基于 6B 规模模型。
3. **用 [[ppo]] 做强化学习**:将 SFT 模型作为初始策略,以 RM 输出作为奖励信号,用近端策略优化(PPO)进一步微调模型,使其生成更受人类偏好的输出。为缓解在公开 NLP 数据集上的性能回退("alignment tax"),还引入了混合预训练梯度的变体 **PPO-ptx**。

得到的模型即 InstructGPT,提供 1.3B、6B、175B 三种规模。评测同时使用人类偏好对比和公开 benchmark(如 [[truthfulqa]]、[[realtoxicityprompts]] 等)。

## 结果

- **人类偏好**:在 API prompt 分布上,标注员明显更偏好 InstructGPT 的输出。**1.3B 的 InstructGPT 输出比 175B 的 [[gpt-3]] 更受偏好**,尽管参数量小了 100 多倍。175B InstructGPT(PPO-ptx)相对于 175B GPT-3 的胜率约为 85%±3%,相对于 few-shot 提示的 GPT-3 约为 71%±4%。
- **真实性**:在 [[truthfulqa]] 上,InstructGPT 生成真实且有信息量回答的比例约为 GPT-3 的两倍。
- **毒性**:在 [[realtoxicityprompts]] 上,当提示模型保持尊重时,InstructGPT 生成的毒性内容比 GPT-3 减少约 25%;但在偏见(bias)指标上没有明显改善。
- **性能回退缓解**:直接做 RLHF 会在部分公开 NLP 数据集上造成性能下降;通过 PPO-ptx(混入预训练梯度)可以在保持对齐收益的同时,大幅减小这种 alignment tax。
- **泛化**:InstructGPT 能泛化到训练标注员之外的"held-out"标注员偏好,也能遵循训练分布之外的指令(如非英语任务、代码相关任务),尽管这类数据在训练中很少。
- 仍存在简单错误:模型有时会照做带有错误前提的指令,或在简单问题上过度对冲。

## 在本 wiki 中的位置

本文是 [[openai]] 提出的对齐工作,是 [[rlhf]] 在大语言模型上的代表性实践,直接奠定了 [[chatgpt]] 的训练范式(SFT → [[reward-model]] → [[ppo]])。它把 [[instruction-tuning]] 与人类反馈结合,展示了"对齐 > 单纯扩大规模"的关键经验,是理解 [[gpt-3]] 之后 instruction-following 模型与 [[alignment]] 主题的核心入口。
