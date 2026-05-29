---
type: source
subtype: paper
tags:
  - reasoning
  - chain-of-thought
  - bootstrapping
  - self-improvement
  - few-shot
created: 2026-05-29
updated: 2026-05-29
arxiv: "2203.14465"
raw: raw/2203.14465.pdf
authors:
  - Eric Zelikman
  - Yuhuai Wu
  - Jesse Mu
  - Noah D. Goodman
year: 2022
---

STaR(Self-Taught Reasoner)提出一种用少量带 [[chain-of-thought|链式推理]] 示例引导大模型自己生成 rationale、再用生成的正确推理过程反复微调自身来 bootstrap 推理能力的方法。

## 问题

让语言模型在回答前生成中间推理步骤(rationale / chain-of-thought)能显著提升其在数学、常识推理等复杂任务上的表现,但获得这种能力主要有两条路,都有明显缺陷:

- 构建大规模 rationale 数据集进行微调,成本高、人工标注昂贵;
- 仅靠少样本(few-shot)的 in-context 提示,通常只在超大模型上才有效,且性能往往低于在任务专用数据上直接微调。

论文想解决的核心问题是:能否在**只有极少量 rationale 示例**和一个**没有 rationale 的大答案集**的条件下,让模型自我迭代、逐步学会生成高质量推理过程,从而把推理能力 bootstrap 起来。

## 方法

核心是一个迭代的 **bootstrapping** 循环(STaR):

1. **生成(rationale generation)**:用少量(论文中为 10 个)人写的 rationale 作为 few-shot 提示,让模型对训练集中的每道题生成 rationale + 答案。
2. **过滤(filtering)**:只保留那些**最终答案正确**的 rationale,作为新的微调数据(用正确答案作为是否保留的信号)。
3. **微调(fine-tuning)**:在筛选出的正确 rationale 上微调原始模型。
4. 用微调后的模型重新执行上述步骤,反复迭代。

关键创新是 **rationalization(合理化)**:对于模型答错、因而被过滤掉的题目,把**正确答案作为提示(hint)**反向喂给模型,让它在已知答案的前提下生成一个"事后"的 rationale。这些经过合理化得到的、且最终答案正确的 rationale 也加入训练集。rationalization 让模型能从原本无法解决的难题中学习,加速并稳定了 bootstrapping,避免训练集只覆盖简单题目。每轮迭代都从原始预训练模型重新开始微调,以避免过拟合。

实验主干模型为 GPT-J(6B 参数),任务涵盖算术、常识推理(CommonsenseQA)与小学数学应用题(GSM8K)。

## 结果

- **算术任务(n 位数加法)**:STaR 通过逐步引入合理化,使模型最终能解决多位数加法;带 rationalization 的 STaR 收敛更快且能处理更难的位数。
- **CommonsenseQA**:STaR 将 GPT-J 的准确率提升到 **72.5%**,显著高于 few-shot baseline(约 36.6%)以及直接在答案上微调的 60.0%;其表现接近规模大 30 倍、且使用了完整微调数据的 GPT-3(73.0%),尽管 GPT-J 只有 6B 参数。
- **GSM8K(小学数学)**:STaR(含 rationalization)达到 **10.7%**,优于不带 rationale 的直接微调(5.8%)和 few-shot baseline(3.1%)。
- 消融显示 **rationalization** 在更难的任务上贡献尤为关键,能让模型从原本失败的样本中继续学习,扩大可学习题目的覆盖范围。
- 人工评估表明,STaR 生成的 rationale 质量较高,且模型在没有被显式提供推理监督的情况下学会了产出有意义的推理链。

## 在本 wiki 中的位置

STaR 是 [[chain-of-thought]] 推理路线上的早期代表性工作,把 CoT 从"提示技巧"推进为"可自我迭代提升的训练范式"。它与 [[self-improvement]]、[[bootstrapping]] 思路一脉相承,是后续用模型自生成数据做 [[rejection-sampling-fine-tuning|拒绝采样微调]] 与 reasoning 自训练(如 RFT、自一致性数据蒸馏等)的先声。其在 [[gsm8k]] 与 [[commonsenseqa]] 上的设定也成为后续推理工作的常见对照基准。相关模型见 [[gpt-j]] 与对照的 [[gpt-3]]。作者来自 [[stanford-university|斯坦福]],与 [[noah-goodman]] 等的认知/推理研究方向相关。
