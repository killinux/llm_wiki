---
type: concept
subtype: method
tags: [loss-function, classification, information-theory]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# cross-entropy

交叉熵衡量预测分布与目标分布之间的差异,是分类与排序模型中最常用的损失函数。

## 在本 wiki 中的出现

- [[2025-gnolr-progressive-implicit-preference]]:提出 GNOLR,用有序标签映射加嵌套优化把多种隐式反馈编码进统一 embedding 空间,既建模用户参与度递进又把多路检索简化为单次最近邻搜索。
- [[2026-compressed-video-aggregator]]:CVA 用冻结视觉基础模型的帧 embedding 加 self-attention 压缩成紧凑视频 embedding,在 MicroLens 与 Short-Video 上提升微视频推荐精度,同时把训练时间与 GPU 显存降低数个数量级。

## 相关

- [[ordinal-regression]]
- [[embedding]]
- [[implicit-feedback]]
