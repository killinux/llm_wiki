---
type: entity
subtype: model
tags: [lora, peft, fine-tuning, low-rank-adaptation]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# LoRA

LoRA(Low-Rank Adaptation,低秩适配)是一种参数高效微调方法,通过向预训练模型的权重注入可训练的低秩矩阵,在冻结原始权重的情况下以极少的额外参数适配下游任务。

## 在本 wiki 中的出现

- [[2024-unbounded-generative-infinite-game]]:提出"生成式无限游戏"概念并实现一个角色生活模拟系统,游戏机制、叙事与角色/环境图像全部由 LLM 与 text-to-image 模型实时生成;核心创新是带 Block Drop 的 regional IP-Adapter(保证角色与环境一致性)与将多 LLM 协作能力蒸馏进 Gemma-2B 的实时游戏引擎。

## 相关

- [[ip-adapter]]
- [[text-to-image]]
- [[gemma-2b]]
- [[knowledge-distillation]]
- [[peft]]
