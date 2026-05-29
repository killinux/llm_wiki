---
type: concept
subtype: method
tags: [recommendation, watch-time, causal-inference, debiasing, quantile]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Duration-Deconfounded Quantile (D2Q)

Duration-Deconfounded Quantile (D2Q) 是一种用于视频推荐观看时长建模的方法,通过将观看时长转换为以视频时长分组的分位数(quantile)来消除视频时长(duration)作为混淆因子(confounder)带来的偏差,从而更公平地刻画用户的真实观看兴趣。

## 在本 wiki 中的出现

- [[2023-d2co-watch-time-debias]]:作为对照/前驱方法被提及。该论文提出 D²Co,从统一因果视角同时矫正视频推荐中观看时长的时长偏差(duration bias)与噪声观看(noisy watching),还原用户真实兴趣。D2Q 在此语境下代表仅针对时长偏差进行去混淆的分位数建模思路。
- [[2024-counterfactual-watch-time]]:提出 counterfactual watch time (CWT) 与 Counterfactual Watch Model (CWM),从经济学视角建模观看行为以消除视频推荐中的 duration bias,与 D2Q 同属时长偏差去混淆方向。
- [[2024-conditional-quantile-estimation-watch-time]]:提出 CQE,用 quantile regression 与 pinball loss 建模短视频观看时长的完整条件分布,并设计保守/动态组合/条件期望三种推断策略,在 Kuaishou 数亿日活平台上线获显著收益;其分位数建模思路与 D2Q 一脉相承。

## 相关

- [[2023-d2co-watch-time-debias]]
- [[watch-time-prediction]]
- [[duration-bias]]
- [[causal-inference]]
