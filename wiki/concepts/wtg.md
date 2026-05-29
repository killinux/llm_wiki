---
type: concept
subtype: method
tags: [watch-time, video-recommendation, debiasing, causal-inference, evaluation]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Watch Time Gain (WTG)

Watch Time Gain (WTG) 是视频推荐场景中用于刻画"用户在某条视频上相对于其基准/期望观看时长的额外观看时长增益"的度量,旨在剥离视频本身时长等因素带来的偏差,从而更真实地反映用户对内容的兴趣。

## 在本 wiki 中的出现

- [[2023-d2co-watch-time-debias]]:该工作提出 D²Co,从统一的因果视角同时矫正视频推荐中观看时长的时长偏差(duration bias)与噪声观看(noisy watching),以还原用户真实兴趣。Watch Time Gain (WTG) 在其中作为去偏后的观看时长信号/度量出现,用于衡量超出时长等混杂因素之外的真实兴趣增益。
- [[2024-conditional-quantile-estimation-watch-time]]:提出 CQE,用 quantile regression 与 pinball loss 建模短视频观看时长的完整条件分布,并设计保守/动态组合/条件期望三种推断策略,在 Kuaishou 数亿日活平台上线获显著收益。

## 相关

- [[2023-d2co-watch-time-debias]]
- [[2024-conditional-quantile-estimation-watch-time]]
- [[quantile-regression]]
- [[duration-bias]]
- [[noisy-watching]]
- [[watch-time]]
- [[causal-inference]]
- [[video-recommendation]]
