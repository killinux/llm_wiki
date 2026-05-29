---
type: concept
subtype: method
tags: [watch-time, debias, denoise, video-recommendation, causal-inference]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# D2Co (Debiased and Denoised watch time Correction)

D²Co 是一种从统一因果视角出发的观看时长矫正方法,旨在同时矫正视频推荐中观看时长的时长偏差(duration bias)与噪声观看(noisy watching),从而还原用户对视频的真实兴趣。

## 在本 wiki 中的出现

- [[2023-d2co-watch-time-debias]]:提出 D²Co 方法。该工作从统一的因果视角同时矫正视频推荐中观看时长的时长偏差与噪声观看,以还原用户的真实兴趣。
- [[2024-conditional-quantile-estimation-watch-time]]:提出 CQE,用 quantile regression 与 pinball loss 建模短视频观看时长的完整条件分布,并设计保守/动态组合/条件期望三种推断策略,在 Kuaishou 数亿日活平台上线获显著收益。

## 相关

- [[watch-time-prediction]]
- [[duration-bias]]
- [[causal-inference]]
- [[video-recommendation]]
