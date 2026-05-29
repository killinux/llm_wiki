---
type: concept
subtype: method
tags: [recommender-systems, debiasing, watch-time, causal-inference]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Noisy Watching

Noisy Watching 指在视频推荐场景中,用户的观看时长(watch time)会受到与真实兴趣无关的因素干扰(如自动播放、误触、背景播放等)而产生的噪声,使得观看时长不能可靠地反映用户的真实偏好。

## 在本 wiki 中的出现

- [[2023-d2co-watch-time-debias]]:提出 D²Co,从统一的因果视角同时矫正视频推荐中观看时长的**时长偏差(duration bias)**与 **Noisy Watching(噪声观看)**,以从被污染的观看时长信号中还原用户的真实兴趣。在该工作中,Noisy Watching 被视为需要与时长偏差一并去除的混淆/噪声来源之一。
- [[2026-hesitation-and-tolerance-in-recommender-systems]]:提出并验证推荐系统中介于接受与拒绝之间的 hesitation(犹豫)与 tolerance(容忍)两种中间交互状态,通过问卷、离线日志与线上 A/B 实验论证容忍侵蚀用户留存,并主张将其作为弱正/负信号重新建模。

## 相关

- [[debiasing]]
- [[recommender-systems]]
- [[user-retention]]
- [[causal-inference]]
- [[confounding-bias]]
- [[duration-bias]]
