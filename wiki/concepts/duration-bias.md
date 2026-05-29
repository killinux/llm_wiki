---
type: concept
subtype: method
tags: [duration-bias, debiasing, recommendation, causal-inference, watch-time]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Duration Bias

Duration Bias 指在视频推荐中,观看时长(watch time)会系统性地受到视频本身时长(duration)的影响——时长更长的视频天然更容易积累更高的观看时长,从而使观看时长无法忠实反映用户的真实兴趣,造成对推荐模型的偏差。

## 在本 wiki 中的出现

- [[2023-d2co-watch-time-debias]]:该论文将 Duration Bias 作为核心矫正对象之一。它提出 D²Co,从统一的因果视角同时矫正观看时长中的 Duration Bias 与 noisy watching(噪声观看),以从被污染的观看时长信号中还原用户的真实兴趣。
- [[2024-counterfactual-watch-time]]:提出 counterfactual watch time (CWT) 与 Counterfactual Watch Model (CWM),从经济学视角建模观看行为以消除视频推荐中的 duration bias。
- [[2024-conditional-quantile-estimation-watch-time]]:提出 CQE,用 quantile regression 与 pinball loss 建模短视频观看时长的完整条件分布,并设计保守/动态组合/条件期望三种推断策略,在 Kuaishou 数亿日活平台上线获显著收益。

## 相关

- [[debiasing]]
- [[confounding-bias]]
- [[exposure-bias]]
- [[recommender-systems]]
- [[user-retention]]
- [[causal-inference]]
- [[inverse-propensity-score]]
