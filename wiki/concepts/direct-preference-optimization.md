---
type: concept
subtype: method
tags: [dpo, preference-optimization, alignment, rlhf, fine-tuning]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# Direct Preference Optimization

Direct Preference Optimization (DPO) 是一种直接用偏好数据微调语言模型的对齐方法,无需训练显式奖励模型或进行强化学习采样,而是通过一个分类式损失目标直接优化策略,使其偏好被标注为更优的回答。

## 在本 wiki 中的出现

- [[2024-v-star-verifiers-for-self-taught-reasoners]]:V-STaR 在自我提升迭代中复用正确与错误的模型生成解,用 DPO 训练 verifier 在测试时对候选解排序,使 LLaMA2 在数学推理上绝对提升 6%~17%、代码生成 4%~12%。
- [[2024-optima-optimizing-llm-multi-agent]]:OPTIMA 通过生成-排序-选择-训练的迭代范式同时优化 LLM 多智能体系统的通信效率与任务有效性,在重信息交换任务上达成 2.8x 性能提升且 token 用量不到 10%。
- [[2025-llm-collaboration-marl-magrpo]]:把多 LLM 协作建模为合作式 MARL(Dec-POMDP)并提出 Multi-Agent GRPO(MAGRPO),在写作与编码协作上微调多个 LLM;TLDR/arXiv return 达 94.5%/93.1%,HumanEval/CoopHumanEval return 达 86.7%/88.5%。
- [[2026-policysim-proactive-policy-optimization]]:PolicySim 是一个基于 LLM 智能体的社会模拟沙盒,使用 SFT+DPO 训练用户智能体,并用带消息传递的 contextual bandit 自适应优化推荐与曝光控制等平台干预策略,实现部署前的主动评估与优化。

## 相关

- [[reinforcement-learning-from-human-feedback]]
- [[reward-model]]
- [[self-taught-reasoner]]
- [[verifier]]
