---
type: entity
subtype: person
tags: [researcher, reasoning, llm]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Eric Zelikman

研究大语言模型推理(reasoning)的研究者,STaR(Self-Taught Reasoner)方法的提出者之一。

## 在本 wiki 中的出现

- 在 [[2022-star-self-taught-reasoner]] 中,他是 STaR 工作的作者。该方法用少量 CoT 示例让模型自己生成推理过程,只保留答对的 rationale(并通过 rationalization 从答错的题反向补全推理),再用这些数据反复微调模型自身,从而 bootstrap 出更强的推理能力。
- [[2024-quiet-star]]:Quiet-STaR 让语言模型在每个 token 前生成隐式 rationale 来更好预测后续文本,以自监督方式从任意文本学会推理,zero-shot 提升 GSM8K(5.9%→10.9%)与 CommonsenseQA(36.3%→47.2%)。

## 相关

- [[chain-of-thought]]
- [[self-taught-reasoner]]
- [[bootstrapping]]
- [[rationalization]]
- [[quiet-star]]
