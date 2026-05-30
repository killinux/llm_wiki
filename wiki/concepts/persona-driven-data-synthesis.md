---
type: concept
subtype: method
tags: [data-synthesis, persona, role-playing, synthetic-data, sft, alignment]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Persona-Driven Data Synthesis

一种以"人物画像（persona）"为驱动条件来大规模合成训练数据的方法：通过预先构建或采样海量多样化的 persona 描述，引导 LLM 围绕每个 persona 生成对应的指令、对话或角色对齐样本，从而获得覆盖面广、风格多样、可扩展的合成数据集。

## 在本 wiki 中的出现

- [[2025-opencharacter-role-playing-synthetic-personas]]：用 Persona Hub 大规模合成 persona 造角色对齐 SFT 数据，微调 LLaMA-3 8B 获得 out-of-domain 角色泛化能力，在 PersonaGym 上比肩 GPT-4o。

## 相关

- [[persona-hub]]
- [[synthetic-data-generation]]
- [[role-playing-llm]]
- [[personagym]]
- [[supervised-fine-tuning|sft]]
