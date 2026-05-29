---
type: concept
subtype: method
tags: [diffusion, lora, acceleration, text-to-image, distillation]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# LCM LoRA

LCM LoRA(Latent Consistency Model LoRA)是一种通过 LoRA 适配器形式蒸馏一致性模型(Consistency Model)的加速模块,使预训练的潜空间扩散模型(如 Stable Diffusion)能够以极少的采样步数(通常 1~4 步)生成图像,从而实现接近实时的 text-to-image 推理。

## 在本 wiki 中的出现

- [[2024-unbounded-generative-infinite-game]]:提出"生成式无限游戏"概念并实现一个角色生活模拟系统,游戏机制、叙事与角色/环境图像全部由 LLM 与 text-to-image 模型实时生成;核心创新是带 Block Drop 的 regional IP-Adapter(保证角色与环境一致性)与将多 LLM 协作能力蒸馏进 Gemma-2B 的实时游戏引擎,实时图像生成依赖少步采样加速技术。

## 相关

- [[latent-consistency-model]]
- [[lora]]
- [[ip-adapter]]
- [[text-to-image]]
- [[diffusion-models|diffusion-model]]
