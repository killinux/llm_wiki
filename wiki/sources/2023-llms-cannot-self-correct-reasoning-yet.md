---
type: source
subtype: paper
tags: [self-correction, llm-reasoning, intrinsic-self-correction, multi-agent-debate, prompting]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2310.01798
raw: raw/2310.01798.pdf
authors: [Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, Denny Zhou]
title: "Large Language Models Cannot Self-Correct Reasoning Yet"
year: 2023
---

一句话:本文批判性地检验了 LLM 的 [[self-correction]] 能力,通过实验证明在没有外部反馈的"内在自我纠正"(intrinsic self-correction)设定下,LLM 不仅无法纠正自己的推理错误,性能反而往往会下降。

## 问题

[[self-correction]] 被广泛宣传为修补 LLM 输出准确性与可靠性的良方:让模型先给出初始答案,再让它自行审视、批评并修正。许多工作(如 [[self-refine]]、[[reflexion]])声称这种迭代自我修正能显著提升表现。

但本文指出此前许多正面结论存在隐含的"作弊":它们依赖了**外部反馈**(oracle 信息),例如用真实标签来判断答案是否正确、是否需要继续修正。一旦去掉这种 oracle,真正考验的是 LLM 仅凭**自身内在能力**(intrinsic self-correction,无外部反馈、无额外训练)能否纠错。作者聚焦推理任务,系统检验这一更现实的设定。

## 方法

- 定义 **intrinsic self-correction**:模型仅基于自身能力修正初始回答,不使用任何外部反馈(无真实标签、无外部工具、无判别器)。
- 标准流程为三步提示:(1) 生成初始答案;(2) 提示模型"复查上一答案、找出问题";(3) 提示模型据反馈给出修正答案,可迭代多轮。
- 在推理基准上评测,采用 [[gpt-3-5]]([[gpt-3-5-turbo]])与 [[gpt-4]] 等闭源模型。
- 对比 oracle 设定(用真实答案决定何时停止/是否修正)与无 oracle 的内在设定,以揭示既往"提升"主要来自 oracle 标签泄露。
- 进一步分析 [[multi-agent-debate]](多智能体辩论)与 [[self-consistency]] 的关系,论证多智能体辩论的增益本质上更接近自洽投票而非真正的"自我纠错"。

## 结果

- **内在自我纠正会损害推理性能**:在 [[gsm8k]]、[[commonsenseqa]]、[[hotpotqa]] 等推理基准上,去掉 oracle 反馈后,经过自我纠正的准确率不升反降。例如 [[gpt-3-5]] 在 [[gsm8k]] 上初始准确率约 75.9%,一轮自我纠正后下降至约 75.1%,两轮后进一步下降。[[gpt-4]] 也呈现类似的下降趋势。
- 模型常把**原本正确**的答案改错,改对的数量少于改错的数量,净效应为负。
- 此前文献中"自我纠正带来提升"的结论,主要源于使用了 oracle(真实标签)来决定何时停止迭代——这是一种现实中不可得的信息。
- 对 [[multi-agent-debate]] 的分析表明:其相对单纯自我纠正的优势,基本可由 [[self-consistency]](多次采样取多数投票)解释,并非来自模型间真正的批判性纠错。
- 作者据此给出建议:不应高估内在自我纠正;真正有效的纠错需依赖**外部反馈**(如代码执行结果、检索证据、工具、可靠的验证器),并指出何时自我纠正可能有用(如安全/风格类任务,而非需要正确性判定的推理任务)。

## 在本 wiki 中的位置

本文是对 [[self-correction]] / [[self-refine]] / [[reflexion]] 等"自我改进"范式的关键反驳与边界划定,与 [[self-reflection]]、[[self-critique]]、[[self-consistency]] 主题直接相关。它强调 [[grounding]] 与外部反馈([[code-execution]]、[[rag]]、[[reward-model]]/验证器)对可靠纠错的必要性,可作为评估各类 [[reasoning]] 与 [[llm-agents]] 自纠错主张时的批判性参照。作者来自 [[google-deepmind]],通讯/资深作者为 [[denny-zhou]]。
