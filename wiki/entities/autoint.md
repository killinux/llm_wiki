---
type: entity
subtype: model
tags: [ctr-prediction, feature-interaction, self-attention, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# AutoInt

AutoInt 是一种用于 CTR(点击率)预测的模型,通过多头自注意力(multi-head self-attention)机制在低维空间中自动学习特征之间的高阶交互。

## 在本 wiki 中的出现

- [[2023-d2co-watch-time-debias]]:该资料提出 D²Co,从统一因果视角同时矫正视频推荐中观看时长的时长偏差(duration bias)与噪声观看(noisy watching),以还原用户真实兴趣;AutoInt 在其语境中作为 CTR / 排序类模型出现(具体角色以原文为准)。
- [[2024-conditional-quantile-estimation-watch-time]]:提出 CQE,用 quantile regression 与 pinball loss 建模短视频观看时长的完整条件分布,并设计保守/动态组合/条件期望三种推断策略,在 Kuaishou 数亿日活平台上线获显著收益。

## 相关

- [[deepfm]]
- [[esmm]]
- [[mmoe]]
- [[ple]]
- [[dupn]]
