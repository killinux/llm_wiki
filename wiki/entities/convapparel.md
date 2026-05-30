---
type: entity
subtype: dataset
tags: [dataset, user-simulator, llm-evaluation, conversational-shopping, realism-gap]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# ConvApparel

ConvApparel 是 Google 提出的人-AI 服装购物对话数据集,包含 4,146 段对话,采用双 agent good/bad 协议生成并带有逐轮第一人称标注,用于量化 LLM user simulator 与真实用户之间的 realism gap。

## 在本 wiki 中的出现

- [[2026-convapparel-user-simulator-validation]]:Google 提出 ConvApparel(4,146 段人-AI 服装购物对话、双 agent good/bad 协议、逐轮第一人称标注)及 PLSA+HLS+counterfactual validation 三支柱框架,系统量化 LLM user simulator 的 realism gap,发现所有 simulator 平均 HLS 仅 0.004,但 ICL/SFT 在反事实泛化上优于纯 prompting。

## 相关

- [[user-simulator]]
- [[hls-human-likeness-score]]
- [[plsa]]
- [[counterfactual-validation]]
- [[agent-evaluation|llm-evaluation]]
