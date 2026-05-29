---
type: concept
subtype: method
tags: [text-to-image, image-generation, diffusion, multimodal, generative-model]
created: 2026-05-29
updated: 2026-05-29
sources:
  - "[[2024-unbounded-generative-infinite-game]]"
---

# 文生图 (Text-to-Image / T2I)

文生图(text-to-image)是指以自然语言文本为条件、生成与之语义一致图像的生成式方法,当前主流实现以 diffusion model 为骨干。

## 概述

文生图模型接收一段文本 prompt,经由文本编码器(如 [[clip]])将其映射为条件表示,再驱动一个生成主干(通常是 latent diffusion model)逐步去噪、合成图像。围绕基础 T2I 模型,社区发展出大量可插拔技术:用 [[dreambooth]]/[[lora]] 做主体定制,用 IP-Adapter / [[regional-ip-adapter]] 注入参考图与区域控制,用 [[lcm-lora]] 与 [[latent-consistency-model]] 把多步采样压缩为少步以实现实时生成。在本 wiki 中,文生图主要作为生成式系统(尤其是交互式 / 智能体系统)的视觉渲染后端出现。

## 在本 wiki 中的出现

- [[2024-unbounded-generative-infinite-game]]:Unbounded 把一个 LLM 游戏引擎与一个实时文生图模型耦合,用 T2I 作为画面渲染后端来生成开放、无界的游戏视觉内容;为保证角色 / 场景在多帧间的一致性并满足实时性,它在 T2I 主干上叠加了 [[regional-ip-adapter]](区域化的身份 / 参考注入)与 [[lcm-lora]] / [[latent-consistency-model]](少步快速采样),并借助 [[dreambooth]] 风格的主体定制来锁定角色形象。该论文是本 wiki 中将文生图用作系统级组件的代表案例。

## 相关

- [[latent-consistency-model]] —— 将文生图扩散采样蒸馏为少步推理,使 T2I 接近实时
- [[lcm-lora]] —— 以 [[lora]] 形式为现有 T2I 模型加装少步加速能力的通用插件
- [[regional-ip-adapter]] —— 在文生图中按区域注入参考图特征,实现身份 / 布局控制
- [[dreambooth]] —— 对文生图模型做主体定制(few-shot 个性化)的微调方法
- [[clip]] —— 为文生图提供文本-图像对齐的条件编码
- [[lora]] —— 文生图模型轻量化定制 / 加速的底层参数高效微调技术
- [[generative-infinite-game]] —— 以文生图为视觉后端的生成式无界游戏范式
- [[google]] —— Unbounded 等相关文生图系统工作的来源机构
