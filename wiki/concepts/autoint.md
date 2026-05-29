---
type: concept
subtype: method
tags: [recommendation, feature-interaction, attention, ctr]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# AutoInt

AutoInt 是一种基于多头自注意力机制的特征交互建模方法,通过将特征嵌入映射到统一空间并自动学习高阶特征组合,用于点击率预测(CTR)等推荐场景。

## 在本 wiki 中的出现

- [[2023-video-length-debiasing-microvideo-rec]]:VLDRec 通过 play-progress 去偏标注、视频长度条件采样与多任务学习缓解微视频推荐中长视频被偏好的 video-length bias,以 NFM 为基座在 View_Time@120 上较最佳基线提升 1.81%(Kuaishou)与 11.32%(WeChat)。

## 相关

- [[nfm]]
- [[feature-interaction]]
- [[self-attention]]
- [[ctr-prediction]]
