---
type: entity
subtype: person
tags: [researcher, reasoning, language-models, stanford]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Noah D. Goodman

斯坦福大学计算机科学与心理学教授,研究语言、推理与认知建模,在大语言模型自举推理(bootstrapping reasoning)方面有重要工作。

## 在本 wiki 中的出现

- [[2022-star-self-taught-reasoner]]:论文作者之一。STaR(Self-Taught Reasoner)用少量 chain-of-thought 示例让模型自己生成推理过程,只保留答对的 rationale(并用 rationalization 从答错题反向补全 rationale),再用这些数据反复微调模型自身,从而 bootstrap 出更强的推理能力。
- [[2024-quiet-star]]:Quiet-STaR 让语言模型在每个 token 前生成隐式 rationale 来更好预测后续文本,以自监督方式从任意文本学会推理,zero-shot 提升 GSM8K(5.9%→10.9%)与 CommonsenseQA(36.3%→47.2%)。

## 相关

- [[chain-of-thought]]
- [[bootstrapping-reasoning]]
- [[stanford-university]]
