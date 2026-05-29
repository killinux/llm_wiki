---
type: concept
subtype: method
tags: [gemma, small-language-model, distillation, on-device]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Gemma-2B

Gemma-2B 是 Google 发布的 Gemma 系列中的轻量级开源大语言模型(约 20 亿参数),因体积小、推理快而常被用作可实时部署、可蒸馏的高效语言模型基座。

## 在本 wiki 中的出现

- [[2024-unbounded-generative-infinite-game]]:提出"生成式无限游戏"概念并实现一个角色生活模拟系统,游戏机制、叙事与角色/环境图像全部由 LLM 与 text-to-image 模型实时生成;核心创新是带 Block Drop 的 regional IP-Adapter(保证角色与环境一致性),以及将多 LLM 协作能力蒸馏进 Gemma-2B 的实时游戏引擎。

## 相关

- [[gemma-2]]
- [[knowledge-distillation]]
- [[ip-adapter]]
- [[text-to-image]]
