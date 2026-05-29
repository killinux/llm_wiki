---
type: concept
subtype: method
tags: [short-video-recommendation, recommender-system, watch-time, user-retention, reinforcement-learning, kuaishou]
created: 2026-05-29
updated: 2026-05-29
sources: 6
---

# 短视频推荐 (Short-Video Recommendation)

短视频推荐:面向 TikTok / YouTube Shorts / Kuaishou 等平台上时长通常为数十秒的短视频信息流的个性化推荐,核心是从 watch-time、skip、点赞等隐式/显式反馈中建模用户兴趣,并优化会话级累计满意度与长期用户留存。

## 概述

短视频场景的典型特征是:用户被动消费、单次会话内连续滑动浏览、以观看时长(watch-time)与各类交互(like/follow/comment/share)作为主要反馈信号。相较一般 [[video-recommendation]] 与 [[micro-video-recommendation]],它更强调会话级序列决策、延迟的长期目标(如 DAU、留存)以及对 watch-time 的去偏处理。方法上既有把会话建模为 [[markov-decision-process]] 并用 [[reinforcement-learning]] 优化长期回报的工业方案,也有针对 skip、watch-time、情感反馈等细粒度信号的建模研究。该方向是本 wiki 中 [[recommender-systems]] 与 RL-for-real-world-systems 的重要落地枢纽。

## 在本 wiki 中的出现

- [[2023-rlur-user-retention-short-video]]:把短视频中的[[user-retention]]建模为无限时域、以请求为单位的 [[markov-decision-process]],提出 RLUR 用 [[reinforcement-learning]] 直接最小化累计回访时间,并在 [[kuaishou]] App 全量上线。本文是把短视频推荐当作长期序列决策、直接优化留存而非即时点击的代表性工作。
- [[2024-model-based-multi-agent-short-video-recommender]]:提出 MMRF,用协作式多智能体 RL 最大化短视频会话的累计 WatchTime,并以 model-based 的反馈模拟缓解工业推荐中的样本选择偏差([[selection-bias]]);离线 +7.3% GAUC、在线 +0.55% WatchTime,已部署服务数亿用户。本文把短视频排序刻画为会话级 MDP 下多偏好维度协作的 actor-critic 问题。
- [[2024-eeg-svrec-eeg-affective-engagement-dataset]]:首个在真实短视频观看场景下采集 EEG 脑电信号并配以六维情感参与度标注(MAES)与行为日志的数据集,用于补充传统行为反馈之外的认知/情感信号,benchmark 显示加入 EEG 特征可提升推荐 AUC。本文从人本评估维度刻画短视频推荐中的用户体验。
- [[2025-fine-grained-skip-micro-video-recommendation]]:针对短视频/micro-video 中被传统方法粗暴二分的 skip 行为,依据 playing time 把交互细分为 highly positive、less positive、negative 三档,用双层图与分层 BPR loss 建模,在 KuaiRand-Pure 与 MVA 上超越多个基线。本文体现短视频场景下"细粒度反馈建模"的脉络。
- [[2024-generative-regression-watch-time-prediction]]:把短视频观看时长预测从回归重构为生成式的逐位 token 序列生成(GRWTP),以序列生成方式预测连续 watch-time。本文聚焦短视频推荐核心信号 watch-time 的建模方式。
- [[2026-vk-lsvd-short-video-dataset]]:由 VK 发布的大规模短视频推荐数据集(VK-LSVD),面向 watch-time 预测与多任务推荐研究,是该场景的公开数据资源。

## 相关

- [[recommender-systems]]
- [[video-recommendation]]
- [[micro-video-recommendation]]
- [[watch-time]]
- [[user-retention]]
- [[reinforcement-learning]]
- [[markov-decision-process]]
- [[selection-bias]]
- [[kuaishou]]
- [[kuairand]]
- [[rlur]]
