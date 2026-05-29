---
type: entity
subtype: benchmark
tags: [commonsense-reasoning, question-answering, multiple-choice, benchmark, nlp]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# CommonsenseQA

CommonsenseQA 是一个以常识推理为核心的多项选择问答(multiple-choice QA)基准,要求模型在缺乏明确上下文的情况下,依靠对世界的常识知识来从若干选项中选出正确答案。

## 在本 wiki 中的出现

- [[2022-chain-of-thought]]:作为评测 chain-of-thought prompting 的常识推理类基准之一。该论文通过在 few-shot 示例中加入中间推理步骤来提升大模型的多步推理能力,并观察到此类增益随模型规模而涌现。
- [[2022-star-self-taught-reasoner]]:作为 STaR 方法用于 bootstrap 推理能力的评测任务之一。STaR 用少量 CoT 示例让模型自己生成 rationale,只保留答对的推理过程(并以 rationalization 从答错题反向补全),反复微调自身。
- [[2023-plan-and-solve-prompting]]:作为评测零样本 Plan-and-Solve (PS/PS+) 提示的常识推理类任务之一。该方法让 LLM 先制定计划再执行子任务,以改进 Zero-shot-CoT 的多步推理。
- [[2023-llms-cannot-self-correct-reasoning-yet]]:本文证明在无外部反馈的"内在自我纠正"设定下,LLM 无法纠正自身推理错误,性能反而往往下降。
- [[2024-quiet-star]]:Quiet-STaR 让语言模型在每个 token 前生成隐式 rationale 来更好预测后续文本,以自监督方式从任意文本学会推理,zero-shot 提升 GSM8K(5.9%→10.9%)与 CommonsenseQA(36.3%→47.2%)。

## 相关

- [[chain-of-thought|chain-of-thought-prompting]]
- [[in-context-learning]]
- [[commonsense-reasoning]]
- [[gsm8k]]
- [[zero-shot-cot]]
- [[multiple-choice-qa]]
- [[self-correction]]
- [[quiet-star]]
