---
type: source
subtype: paper
tags: [self-refinement, iterative-refinement, self-feedback, prompting, in-context-learning, reasoning, code-generation]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2303.17651
raw: raw/2303.17651.pdf
authors: [Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, Shashank Gupta, Bodhisattwa Prasad Majumder, Katherine Hermann, Sean Welleck, Amir Yazdanbakhsh, Peter Clark]
year: 2023
---

SELF-REFINE 提出一种无需训练、仅用同一个 LLM 在测试时通过"自我反馈 → 自我修正"迭代来提升输出质量的方法,在 7 个任务上平均带来约 20% 的绝对提升。

## 问题

大语言模型(LLM)在第一次生成时往往不能给出最优输出,尤其在目标多元(如对话回复生成)或目标难以定义(如提升代码可读性)的任务上。已有的迭代修正方法通常依赖:领域特定的训练数据、外部监督或奖励模型、昂贵的人工标注。这些条件并不总能满足。作者借鉴人类"先起草、再根据自我反馈反复打磨"的写作/编程习惯,想要一种**不需要任何额外训练、监督或强化学习**、可泛化到多种任务的修正方法。

## 方法

[[self-refine]] 用**同一个**模型 M 同时充当生成器、反馈提供者和修正器,基于 [[few-shot-prompting]](in-context learning)实现,流程在三个 prompt(p_gen / p_fb / p_refine)下交替进行:

1. **初始生成**:用 p_gen 生成初始输出 y_0 = M(p_gen ‖ x)。
2. **FEEDBACK**:用 p_fb 让模型对自己的输出生成反馈 fb_t = M(p_fb ‖ x ‖ y_t)。关键要求反馈是 *actionable*(给出可执行的具体改进动作)且 *specific*(指出输出中需修改的具体片段)。
3. **REFINE**:用 p_refine 结合反馈修正输出。为让模型记住历史、避免重复错误,修正时会把过去所有反馈和输出拼接进 prompt:y_{t+1} = M(p_refine ‖ x ‖ y_0 ‖ fb_0 ‖ … ‖ y_t ‖ fb_t)。

FEEDBACK 与 REFINE 交替迭代,直到满足停止条件(指定步数,或从反馈中提取的停止标记/分数),实验中最多迭代 4 次。整个过程不涉及人工介入,仅依赖 few-shot 示例中的监督。

## 结果

在 7 个任务上评测,base LLM 包括 GPT-3.5(text-davinci-003)、ChatGPT(gpt-3.5-turbo)和 [[gpt-4]](OpenAI 2023),代码任务还用了 [[codex]](code-davinci-002)。指标分三类:任务专用自动指标、人类 A/B 偏好、以及用 GPT-4 作为人类偏好的代理(与人类偏好相关性:Sentiment Reversal 82%、Acronym Generation 68%、Dialogue Response 71%)。

SELF-REFINE 在所有任务上一致优于对应 base 模型,绝对提升约 5–40%。GPT-4 + SELF-REFINE 主要结果(Table 1):

- Sentiment Reversal:3.8 → 36.2(↑32.4)
- Dialogue Response:25.4 → 74.6(↑49.2)
- Code Optimization:27.3 → 36.0(↑8.7)
- Code Readability:27.4 → 56.2(↑28.8)
- Math Reasoning:92.9 → 93.1(↑0.2)
- Acronym Generation:30.4 → 56.0(↑25.6)
- Constrained Generation:15.0 → 45.0(↑30.0)

代码生成任务中相对初始生成可提升最多约 13%。Constrained Generation(每句需包含 20–30 个关键词,[[commongen]] 的更难版本)和偏好类任务(对话、情感反转、缩写生成)收益最大。Math Reasoning([[gsm8k]],Cobble et al. 2021)收益最小,原因是 LLM 难以精确定位推理链中的错误;若引入外部信号判断当前答案是否正确,数学任务的提升可增至 5%+。

消融实验(Table 2)表明反馈质量至关重要:具体可执行的反馈 > 通用反馈 > 无反馈。如 Sentiment Reversal 从 43.2(specific)降到 31.2(generic),无反馈时任务直接失败(0)。多次迭代也有效但边际递减,例如 Code Optimization 从初始 22.0 提升到三次迭代后 28.8,Constrained Generation 从 29.0 提升到 49.7。

## 在本 wiki 中的位置

SELF-REFINE 是 [[test-time-compute]] 和 LLM 自我改进方向的代表性工作,与 [[chain-of-thought]] 等推理增强提示互补:CoT 改进单次生成,SELF-REFINE 在生成之后通过迭代反馈进一步打磨。它属于 [[llm-as-judge]] / [[self-critique]] 思路的早期实例(模型评价并修正自身输出),也是后续 [[reflexion]] 等自我反思框架的近邻工作。与依赖外部奖励模型的 [[rlhf]] 不同,SELF-REFINE 不需训练即可在测试时获得收益。
