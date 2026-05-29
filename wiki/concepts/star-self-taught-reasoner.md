---
type: concept
subtype: method
tags: [reasoning, self-improvement, bootstrapping, chain-of-thought]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# STaR (Self-Taught Reasoner)

STaR 是一种自举式推理训练方法:让语言模型为问题生成带推理链(rationale)的答案,保留答案正确的推理链(对错误样本可用正确答案做"反向提示"补全),再用这些自生成的推理链微调模型,迭代提升其推理能力。

## 在本 wiki 中的出现

- [[2024-v-star-verifiers-for-self-taught-reasoners]]:V-STaR 在自我提升迭代中复用正确与错误的模型生成解,用 DPO 训练 verifier 在测试时对候选解排序,使 LLaMA2 在数学推理上绝对提升 6%~17%、代码生成 4%~12%。

## 相关

- [[chain-of-thought]]
- [[self-improvement]]
- [[verifier]]
- [[dpo-direct-preference-optimization]]
- [[rejection-sampling-fine-tuning]]
