---
type: concept
subtype: method
tags: [recommendation, ctr-prediction, factorization-machine, deep-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# DeepFM

DeepFM 是一种用于 CTR 预估的端到端推荐模型,将因子分解机(FM)与深度神经网络(DNN)结合,共享同一套特征嵌入,从而同时建模低阶与高阶特征交互,无需人工特征工程。

## 在本 wiki 中的出现

- [[2023-video-length-debiasing-microvideo-rec]]:VLDRec 通过 play-progress 去偏标注、视频长度条件采样与多任务学习缓解微视频推荐中长视频被偏好的 video-length bias,以 NFM 为基座在 View_Time@120 上较最佳基线提升 1.81%(Kuaishou)与 11.32%(WeChat)。

## 相关

- [[factorization-machine]]
- [[nfm]]
- [[ctr-prediction]]
- [[microvideo-recommendation]]
