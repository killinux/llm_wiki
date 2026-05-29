---
type: concept
subtype: method
tags: [rope, position-encoding, attention, transformer]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# RoPE

旋转位置编码(Rotary Position Embedding),一种通过对 query 和 key 向量按位置施加旋转变换、从而在注意力计算中隐式注入相对位置信息的位置编码方法。

## 在本 wiki 中的出现

- [[2026-fuxi-linear]]:线性复杂度的时间感知序列推荐模型,解耦时间与语义信号、用可学习核近似相对位置编码,在数千 token 长序列上提升推荐质量并实现最高 21× 推理加速。

## 相关

- [[relative-position-encoding]]
- [[attention]]
- [[linear-attention]]
