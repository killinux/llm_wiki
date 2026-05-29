---
type: entity
subtype: model
tags: [vision, foundation-model, self-supervised, embedding]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# DINOv3

DINOv3 是一个通过自监督学习训练的视觉基础模型,可作为冻结的特征提取器为图像与视频帧生成通用 embedding。

## 在本 wiki 中的出现

- [[2026-compressed-video-aggregator]]:CVA 用冻结视觉基础模型的帧 embedding 加 self-attention 压缩成紧凑视频 embedding,在 MicroLens 与 Short-Video 上提升微视频推荐精度,同时把训练时间与 GPU 显存降低数个数量级。

## 相关

- [[compressed-video-aggregator]]
- [[micro-video-recommendation]]
- [[self-supervised-learning]]
