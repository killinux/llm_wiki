---
type: entity
subtype: model
tags: [model, language-model, open-source]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# GPT-J

GPT-J 是一个开源的自回归 Transformer 语言模型,常被研究工作用作可微调的基础模型。

## 在本 wiki 中的出现

- [[2022-star-self-taught-reasoner]]:STaR 使用 GPT-J 作为待 bootstrap 的基础模型。该方法以少量 CoT 示例提示模型自行生成推理过程(rationale),只保留得出正确答案的 rationale(并通过 rationalization 从已知答案反向补全做错的题目),再用这些数据反复微调模型自身,从而逐步增强其推理能力。

## 相关

- [[chain-of-thought]]
- [[2022-star-self-taught-reasoner]]
- [[transformer]]
- [[language-model]]
