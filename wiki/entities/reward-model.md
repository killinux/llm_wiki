---
type: entity
subtype: model
tags: [reward-model, rlhf, alignment, reinforcement-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# reward model

奖励模型(reward model)是用于为语言模型的输出打分、提供训练信号的模型,常用于 RLHF 等基于强化学习的对齐与微调流程中。

## 在本 wiki 中的出现

- [[2025-llm-collaboration-marl-magrpo]]:把多 LLM 协作建模为合作式 MARL(Dec-POMDP)并提出 Multi-Agent GRPO(MAGRPO),在写作与编码协作上微调多个 LLM;协作产出由奖励信号引导优化,TLDR/arXiv return 达 94.5%/93.1%,HumanEval/CoopHumanEval return 达 86.7%/88.5%。

## 相关

- [[rlhf]]
- [[grpo]]
- [[reinforcement-learning]]
- [[multi-agent-rl]]
