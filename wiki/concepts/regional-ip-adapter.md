---
type: concept
subtype: method
tags: [image-generation, ip-adapter, consistency, text-to-image, diffusion]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Regional IP-Adapter

Regional IP-Adapter 是一种在 text-to-image 扩散模型中按图像区域分别注入参考图像特征的方法,用于在生成过程中同时保持角色与环境等不同元素的视觉一致性。

## 在本 wiki 中的出现

- [[2024-unbounded-generative-infinite-game]]:在"生成式无限游戏"角色生活模拟系统中,作为保证角色与环境一致性的核心创新,采用带 Block Drop 的 regional IP-Adapter,使 LLM 与 text-to-image 模型实时生成的角色/环境图像保持连贯。

## 相关

- [[ip-adapter]]
- [[block-drop]]
- [[2024-unbounded-generative-infinite-game]]
- [[generative-infinite-game]]
- [[text-to-image]]
