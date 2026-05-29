---
type: concept
subtype: method
tags: [dpo, preference-optimization, alignment, rlhf, fine-tuning]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Direct Preference Optimization

Direct Preference Optimization (DPO) 是一种直接用偏好数据微调语言模型的对齐方法,无需训练显式奖励模型或进行强化学习采样,而是通过一个分类式损失目标直接优化策略,使其偏好被标注为更优的回答。

## 在本 wiki 中的出现

- [[2024-v-star-verifiers-for-self-taught-reasoners]]:V-STaR 在自我提升迭代中复用正确与错误的模型生成解,用 DPO 训练 verifier 在测试时对候选解排序,使 LLaMA2 在数学推理上绝对提升 6%~17%、代码生成 4%~12%。

## 相关

- [[reinforcement-learning-from-human-feedback]]
- [[reward-model]]
- [[self-taught-reasoner]]
- [[verifier]]
