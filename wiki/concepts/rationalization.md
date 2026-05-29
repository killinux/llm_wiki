---
type: concept
subtype: method
tags: [training, reasoning, bootstrapping]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Rationalization

给模型提供问题的正确答案作为提示,让它反向生成一条能导向该答案的推理过程(rationale),从而为模型自己答错的题目补全可用的训练样本。

## 在本 wiki 中的出现

- [[2022-star-self-taught-reasoner]]:STaR 用少量 CoT 示例让模型自己生成推理过程,只保留答对的 rationale 反复微调自身来 bootstrap 推理能力;对模型答错的题目,则使用 rationalization——把正确答案作为提示喂给模型,反向补全出推理过程,从而覆盖那些仅靠正向采样无法答对的难题,缓解训练数据的偏置。

## 相关

- [[chain-of-thought]]
- [[filtered-rejection-sampling]]
- [[distillation]]
- [[2022-star-self-taught-reasoner]]
