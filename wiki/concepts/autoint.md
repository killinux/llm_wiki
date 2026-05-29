---
type: concept
subtype: method
tags: [recommendation, feature-interaction, attention, ctr]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# AutoInt

AutoInt 是一种基于多头自注意力机制的特征交互建模方法,通过将特征嵌入映射到统一空间并自动学习高阶特征组合,用于点击率预测(CTR)等推荐场景。

## 在本 wiki 中的出现

- [[2023-video-length-debiasing-microvideo-rec]]:VLDRec 通过 play-progress 去偏标注、视频长度条件采样与多任务学习缓解微视频推荐中长视频被偏好的 video-length bias,以 NFM 为基座在 View_Time@120 上较最佳基线提升 1.81%(Kuaishou)与 11.32%(WeChat)。
- [[2024-bi-level-user-modeling-deep-recommenders]]:GPRec 提出即插即用的双层用户建模:用可学习分类器与双向(正/负)群体嵌入做群体建模,从 ID 类特征提炼个体偏好并以正交损失解耦,在 ML1M/TenRec/KuaiRand 上稳定提升各类 DRS 主干的 CTR 预测。
- [[2025-self-surrogate-light-feature-selection]]:提出 SELF,用多个 LLM 的世界知识对特征做语义排序、再以轻量 bridge network 融合任务信号,缓解深度推荐系统特征选择对 surrogate model 的依赖。

## 相关

- [[nfm]]
- [[feature-interaction]]
- [[self-attention]]
- [[ctr-prediction]]
