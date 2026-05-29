---
type: entity
subtype: model
tags: [vision-transformer, vit, multimodal, computer-vision]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Vision Transformer

Vision Transformer(ViT)是一种将 Transformer 架构直接应用于图像的视觉模型,通过把图像切分为图块(patch)序列并以自注意力机制建模,从而替代传统卷积网络完成视觉表征学习。

## 在本 wiki 中的出现
- [[2026-compressed-video-aggregator]]:CVA 用冻结视觉基础模型的帧 embedding 加 self-attention 压缩成紧凑视频 embedding,在 MicroLens 与 Short-Video 上提升微视频推荐精度,同时把训练时间与 GPU 显存降低数个数量级。
- [[self-attention]]
- [[visual-foundation-model]]
- [[video-embedding]]

- [[2023-drivemlm-autonomous-driving]]:DriveMLM 通过将多模态 LLM 的语言决策与模块化 AD 系统的行为规划状态对齐,在 CARLA 仿真器实现闭环自动驾驶,Town05 Long 上 DS 达 76.1,优于 Apollo 4.7 点。

## 相关

- [[transformer]]
- [[multimodal-llm]]
- [[clip]]
