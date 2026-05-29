---
type: concept
subtype: method
tags: [reasoning-trace, synthetic-data, fine-tuning, human-behavior-simulation, process-level-evaluation]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# 合成 reasoning trace

合成 reasoning trace 指为已有的行为/标注数据(如真人点击日志)人工或用模型生成对应的推理过程文本,使模型在微调时不仅学习"做什么动作",还学习"为什么这样做",从而提升对人类逐步行为的拟合能力。

## 在本 wiki 中的出现

- [[2025-can-llm-agents-simulate-human-behavior]]:首个用真实在线购物数据做过程级、动作级定量评测的工作,发现 prompt-only LLM 模拟人类逐步行为的准确率仅约 11.86%,而在真人点击数据加合成 reasoning trace 上微调可显著提升。

## 相关

- [[human-behavior-simulation]]
- [[process-level-evaluation]]
- [[supervised-fine-tuning]]
- [[chain-of-thought]]
