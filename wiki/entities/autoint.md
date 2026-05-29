---
type: entity
subtype: model
tags: [ctr-prediction, feature-interaction, self-attention, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# AutoInt

AutoInt 是一种用于 CTR(点击率)预测的模型,通过多头自注意力(multi-head self-attention)机制在低维空间中自动学习特征之间的高阶交互。

## 在本 wiki 中的出现
- [[2023-video-length-debiasing-microvideo-rec]]:VLDRec 通过 play-progress 去偏标注、视频长度条件采样与多任务学习缓解微视频推荐中长视频被偏好的 video-length bias,以 NFM 为基座在 View_Time@120 上较最佳基线提升 1.81%(Kuaishou)与 11.32%(WeChat)。
- [[2024-bi-level-user-modeling-deep-recommenders]]:GPRec 提出即插即用的双层用户建模:用可学习分类器与双向(正/负)群体嵌入做群体建模,从 ID 类特征提炼个体偏好并以正交损失解耦,在 ML1M/TenRec/KuaiRand 上稳定提升各类 DRS 主干的 CTR 预测。
- [[2025-self-surrogate-light-feature-selection]]:提出 SELF,用多个 LLM 的世界知识对特征做语义排序、再以轻量 bridge network 融合任务信号,缓解深度推荐系统特征选择对 surrogate model 的依赖。
- [[nfm]]
- [[feature-interaction]]
- [[self-attention]]
- [[ctr-prediction]]

- [[2023-d2co-watch-time-debias]]:该资料提出 D²Co,从统一因果视角同时矫正视频推荐中观看时长的时长偏差(duration bias)与噪声观看(noisy watching),以还原用户真实兴趣;AutoInt 在其语境中作为 CTR / 排序类模型出现(具体角色以原文为准)。
- [[2024-conditional-quantile-estimation-watch-time]]:提出 CQE,用 quantile regression 与 pinball loss 建模短视频观看时长的完整条件分布,并设计保守/动态组合/条件期望三种推断策略,在 Kuaishou 数亿日活平台上线获显著收益。

## 相关

- [[deepfm]]
- [[esmm]]
- [[mmoe]]
- [[ple]]
- [[dupn]]
