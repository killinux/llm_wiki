---
type: concept
subtype: method
tags: [text-to-image, fine-tuning, personalization, diffusion]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# DreamBooth

DreamBooth 是一种针对文生图扩散模型的个性化微调方法,通过少量参考图像将特定主体(如某个角色、物体)绑定到一个独有标识符上,从而在新场景中以保持一致性的方式重新生成该主体。

## 在本 wiki 中的出现

- [[2024-unbounded-generative-infinite-game]]:提出"生成式无限游戏"概念并实现一个角色生活模拟系统,游戏机制、叙事与角色/环境图像全部由 LLM 与 text-to-image 模型实时生成;其核心创新是带 Block Drop 的 regional IP-Adapter(保证角色与环境一致性),以及将多 LLM 协作能力蒸馏进 Gemma-2B 的实时游戏引擎。与 DreamBooth 同属"主体/角色一致性生成"问题域。

## 相关

- [[ip-adapter]]
- [[text-to-image]]
- [[diffusion-model]]
- [[subject-consistency]]
