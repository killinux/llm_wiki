---
type: concept
subtype: method
tags: [recommender-systems, video-recommendation, watch-time, ranking, regression]
created: 2026-05-29
updated: 2026-05-29
sources:
  - "[[2024-generative-regression-watch-time-prediction]]"
  - "[[2024-conditional-quantile-estimation-watch-time]]"
  - "[[2025-exponential-gaussian-mixture-network]]"
  - "[[2024-counterfactual-watch-time]]"
  - "[[2024-deconfound-release-interval-bias]]"
  - "[[2025-umre-monotonic-ranking-ensemble]]"
---

# 观看时长预测 (Watch-Time Prediction)

观看时长预测是指在短视频/视频推荐系统中,为给定的"用户-视频"曝光对预测用户将要观看的时长(watch time),并以此作为排序与目标建模的核心信号的一类方法。

## 概述

在短视频推荐中,观看时长是用户兴趣最重要的隐式反馈信号之一,直接关联用户参与度与留存。与点击率(CTR)这类二分类目标不同,watch time 是连续、长尾、且高度依赖于视频时长(duration)的回归目标,因此其预测面临严重的分布偏斜与多种偏差(如时长偏差、曝光/反事实偏差、发布间隔偏差)。围绕这一目标,本 wiki 收录的工作分别从生成式回归、分位数估计、混合分布建模、反事实去偏与单调排序集成等角度提出了不同的建模范式。

## 在本 wiki 中的出现

- [[2024-generative-regression-watch-time-prediction]]:将观看时长预测建模为生成式回归(generative regression)问题,用生成式建模刻画 watch time 的连续长尾分布,而非直接做点估计回归。
- [[2024-conditional-quantile-estimation-watch-time]]:用条件分位数估计(conditional quantile estimation)来预测观看时长,通过估计 watch time 的条件分位数缓解长尾与异方差问题(参见 [[conditional-quantile-estimation]]、[[quantile-regression]])。
- [[2025-exponential-gaussian-mixture-network]]:用指数-高斯混合网络对观看时长的分布建模,以混合分布拟合 watch time 的多峰、长尾特性,提升预测的分布表达能力。
- [[2024-counterfactual-watch-time]]:从反事实(counterfactual)视角处理观看时长预测,纠正"观测到的观看时长"中因曝光/截断带来的偏差,估计更接近真实兴趣的 watch time。
- [[2024-deconfound-release-interval-bias]]:针对发布间隔偏差(release-interval bias)进行去混淆,作为观看时长建模中的一种 [[debiasing]] / [[deconfounding]] 处理,避免该混淆因素污染 watch-time 信号。
- [[2025-umre-monotonic-ranking-ensemble]]:以单调排序集成(monotonic ranking ensemble,UMRE)的方式融合包括观看时长在内的多个排序目标,将 watch-time 预测纳入统一的排序集成框架。

## 相关

- [[watch-time]]
- [[duration-bias]]
- [[video-recommendation]]
- [[micro-video-recommendation]]
- [[conditional-quantile-estimation]]
- [[quantile-regression]]
- [[debiasing]]
- [[deconfounding]]
- [[learning-to-rank]]
- [[ctr]]
- [[user-retention]]
