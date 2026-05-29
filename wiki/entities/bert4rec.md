---
type: entity
subtype: model
tags: [recommendation, transformer, sequential-recommendation, bert]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# BERT4Rec

BERT4Rec 是一种用于序列推荐的模型,采用双向 Transformer 编码器,通过掩码物品预测(Cloze 任务)从用户历史行为中学习物品表示。

## 在本 wiki 中的出现

- [[2025-multi-objective-controllable-decision-transformer]]:提出 MocDT,一种基于 Decision Transformer 的离线 RL 推荐方法,把未来多目标作为控制信号,在推理阶段自回归生成对齐指定目标(累积评分与多样性)的物品序列,无需重训。
- [[2025-autocdsr-self-attention]]:AutoCDSR 把跨域序列推荐建模为偏好感知的 Pareto 最优多目标问题,通过动态最小化 cross-domain attention scores,仅优化 transformer 内在 self-attention 即可自动迁移有益跨域知识并抑制 negative transfer。
- [[2025-hid-vae-interpretable-generative-recommendation]]:HiD-VAE 用层次化监督量化 + uniqueness loss 学习可解释、解耦的 semantic ID,消除 ID 碰撞并显著提升生成式推荐性能。
- [[2025-grasp-world-knowledge-sequential-recommendation]]:GRASP 用"生成增强检索 + Sigmoid 整体注意力增强"把 LLM 世界知识作为辅助输入(而非监督信号)注入序列推荐,抵抗 LLM 幻觉噪声,在 Beauty/Fashion/Industry-100K 上叠加多种 backbone 均达 SOTA,并通过线上 A/B 验证 GMV +1.71%。
- [[2025-fuxi-gamma-efficient-sequential-recommendation]]:decoder-only 生成式序列推荐框架,用受 Ebbinghaus 遗忘曲线启发的指数幂时间编码器与对角稀疏位置剪枝,在 SOTA 推荐质量下把训练加速最多 4.74×、推理 6.18×。

## 相关

- [[sequential-recommendation]]
- [[transformer]]
- [[decision-transformer]]
- [[generative-recommendation]]
