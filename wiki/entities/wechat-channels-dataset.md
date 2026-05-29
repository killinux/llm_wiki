---
type: entity
subtype: dataset
tags: [dataset, recommendation, video, watch-time, debias]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# WeChat Channels Dataset

来自微信视频号(WeChat Channels)场景的视频推荐数据集,记录用户与视频的交互及观看时长等信息,用于研究和评估观看时长(watch-time)相关的推荐建模方法。

## 在本 wiki 中的出现

- 在 [[2023-d2co-watch-time-debias]] 中,该数据集作为实验数据来源之一,用于验证 D²Co 在统一因果视角下同时矫正观看时长的时长偏差(duration bias)与噪声观看(noisy watching)、还原用户真实兴趣的有效性。
- [[2023-video-length-debiasing-microvideo-rec]]:VLDRec 通过 play-progress 去偏标注、视频长度条件采样与多任务学习缓解微视频推荐中长视频被偏好的 video-length bias,以 NFM 为基座在 View_Time@120 上较最佳基线提升 1.81%(Kuaishou)与 11.32%(WeChat)。
- [[2024-counterfactual-watch-time]]:提出 counterfactual watch time (CWT) 与 Counterfactual Watch Model (CWM),从经济学视角建模观看行为以消除视频推荐中的 duration bias。
- [[2024-conditional-quantile-estimation-watch-time]]:提出 CQE,用 quantile regression 与 pinball loss 建模短视频观看时长的完整条件分布,并设计保守/动态组合/条件期望三种推断策略,在 Kuaishou 数亿日活平台上线获显著收益。

## 相关

- [[kuairand]]
- [[watch-time-prediction]]
- [[duration-bias]]
- [[noisy-watching]]
- [[video-recommendation]]
- [[debiasing]]
- [[causal-inference]]
- [[wechat-channels]]
