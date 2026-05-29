---
type: concept
subtype: method
tags: [recommendation, micro-video, multimodal, video-embedding]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Micro-video Recommendation

微视频推荐(Micro-video Recommendation)指为短时长视频内容(如 MicroLens、Short-Video 等场景中的短视频)预测并推荐用户可能感兴趣条目的推荐任务,通常依赖从原始视频帧中提取的视觉/多模态表征来建模物品。

## 在本 wiki 中的出现

- [[2026-compressed-video-aggregator]]:CVA 用冻结视觉基础模型的帧 embedding 加 self-attention 压缩成紧凑视频 embedding,在 MicroLens 与 Short-Video 上提升微视频推荐精度,同时把训练时间与 GPU 显存降低数个数量级。

## 相关

- [[video-embedding]]
- [[multimodal-recommendation]]
- [[vision-foundation-model]]
