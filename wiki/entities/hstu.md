---
type: entity
subtype: model
tags: [recommendation, sequential-recommendation, generative-recommendation, transformer]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# HSTU

HSTU(Hierarchical Sequential Transduction Unit)是一种面向生成式序列推荐的 decoder-only Transformer 架构,将推荐建模为生成式序列转导任务。

## 在本 wiki 中的出现
- [[2026-fuxi-linear]]:线性复杂度的时间感知序列推荐模型,解耦时间与语义信号、用可学习核近似相对位置编码,在数千 token 长序列上提升推荐质量并实现最高 21× 推理加速。
- [[sequence-recommendation]]
- [[linear-attention]]
- [[relative-position-encoding]]

- [[2025-fuxi-gamma-efficient-sequential-recommendation]]:作为生成式序列推荐的代表性架构被提及;该工作提出 decoder-only 生成式序列推荐框架,采用受 Ebbinghaus 遗忘曲线启发的指数幂时间编码器与对角稀疏位置剪枝,在 SOTA 推荐质量下把训练加速最多 4.74×、推理加速 6.18×。

## 相关

- [[dlrm]]
- [[generative-recommendation]]
- [[sequential-recommendation]]
- [[transformer]]
