---
type: concept
subtype: method
tags: [diffusion, distillation, fast-sampling, image-generation, text-to-image]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Latent Consistency Model

一句话定义:Latent Consistency Model(LCM)是一种在隐空间上训练的一致性模型,通过学习扩散概率流 ODE 的解映射,实现仅需极少步数(1-4 步)即可从噪声直接生成高质量图像的快速采样方法,常用于需要实时响应的 text-to-image 生成场景。

## 在本 wiki 中的出现

- [[2024-unbounded-generative-infinite-game]]:提出"生成式无限游戏"概念并实现一个角色生活模拟系统,游戏机制、叙事与角色/环境图像全部由 LLM 与 text-to-image 模型实时生成;核心创新是带 Block Drop 的 regional IP-Adapter(保证角色与环境一致性)与将多 LLM 协作能力蒸馏进 Gemma-2B 的实时游戏引擎。其对实时图像生成的需求与 LCM 类快速采样方法高度相关。

## 相关

- [[consistency-model]]
- [[diffusion-model]]
- [[text-to-image]]
- [[ip-adapter]]
- [[knowledge-distillation]]
