---
type: entity
subtype: model
tags: [video-recommendation, micro-video, embedding-compression, self-attention, foundation-model]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Compressed Video Aggregator (CVA)

CVA 是一种微视频推荐模型,它利用冻结的视觉基础模型提取帧级 embedding,再通过 self-attention 将其聚合压缩为紧凑的视频 embedding,从而在保持精度的同时大幅降低训练开销。

## 在本 wiki 中的出现

- [[2026-compressed-video-aggregator]]:CVA 用冻结视觉基础模型的帧 embedding 加 self-attention 压缩成紧凑视频 embedding,在 MicroLens 与 Short-Video 上提升微视频推荐精度,同时把训练时间与 GPU 显存降低数个数量级。

## 相关

- [[vision-foundation-model]]
- [[self-attention]]
- [[micro-video-recommendation]]
- [[embedding-compression]]
