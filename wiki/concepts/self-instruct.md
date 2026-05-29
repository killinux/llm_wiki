---
type: concept
subtype: method
tags: [self-instruct, instruction-tuning, data-generation, llm]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# self-instruct

Self-instruct 是一种让语言模型利用自身生成的指令-输入-输出样本来扩充指令数据集、再用于自我微调以提升指令遵循能力的自举式方法。

## 在本 wiki 中的出现

- [[2023-recommender-ai-agent-interec]]:提出 InteRecAgent,以 LLM 为大脑、传统推荐模型为工具,通过候选总线记忆、plan-first 执行与 actor-critic 反思构建交互式对话推荐 agent,并蒸馏出 7B 的 RecLlama。

## 相关

- [[instruction-tuning]]
- [[knowledge-distillation]]
- [[llm-agents|llm-agent]]
