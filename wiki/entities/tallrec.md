---
type: entity
subtype: model
tags: [llm, recommendation, lora, instruction-tuning]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# TALLRec

TALLRec 是一个基于 LLM 的推荐对齐框架,通过指令微调(instruction tuning)与 LoRA 高效地把大语言模型适配到推荐任务上。

## 在本 wiki 中的出现

- [[2026-thinkrec-thinking-based-recommendation]]:ThinkRec 通过思考激活(推理数据合成+联合训练)与实例级 LoRA 专家融合,把 LLM 推荐从 System 1 直觉匹配推进到 System 2 推理,在 ML1M/Yelp/Book 上 AUC 平均超 SOTA 7.96%。

## 相关

- [[lora]]
- [[instruction-tuning]]
- [[llm-recommendation]]
- [[thinkrec]]
