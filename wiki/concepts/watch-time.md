---
type: concept
subtype: method
tags: [watch-time, recommendation, interest-signal, debias, video]
created: 2026-05-29
updated: 2026-05-29
sources: 8
---

# Watch Time as Interest Signal

把视频推荐中用户的观看时长(watch time)当作其真实兴趣的隐式反馈信号来建模与优化的方法。

## 在本 wiki 中的出现

- [[2023-d2co-watch-time-debias]]:把 watch time 作为兴趣信号是该工作的核心前提,但作者指出直接使用观看时长存在两类偏差——**时长偏差(duration bias)** 与 **噪声观看(noisy watching)**。论文提出 D²Co,从统一的因果视角同时矫正这两种偏差,从被污染的观看时长信号中还原用户的真实兴趣。
- [[2023-video-length-debiasing-microvideo-rec]]:VLDRec 通过 play-progress 去偏标注、视频长度条件采样与多任务学习缓解微视频推荐中长视频被偏好的 video-length bias,以 NFM 为基座在 View_Time@120 上较最佳基线提升 1.81%(Kuaishou)与 11.32%(WeChat)。
- [[2024-future-impact-decomposition-request-level-recommendation]]:提出 ItemA2C 框架,在 request-level MDP 下将 list-wise reward 分解为 item-wise 信用并用 actor-critic 优化每个 item 的长期未来影响,提升推荐长期效果。
- [[2024-touch-the-core-hybrid-targets-recommendation]]:首次研究"离散转化任务 + 连续核心目标(如 watch time)"的 hybrid targets 多任务学习,提出 HTLNet 用 label embedding 显式传递任务依赖并设计梯度调整策略稳定优化。
- [[2024-eeg-svrec-eeg-affective-engagement-dataset]]:首个在真实短视频观看场景下采集 EEG 脑电信号并配以六维情感参与度标注(MAES)与行为日志的推荐数据集,benchmark 显示加入 EEG 特征可提升推荐 AUC。
- [[2024-model-based-multi-agent-short-video-recommender]]:MMRF 用协作式多智能体 RL 最大化短视频会话累计 WatchTime,并用 model-based 反馈模拟缓解样本选择偏差,离线 +7.3% GAUC、在线 +0.55% WatchTime,已部署服务数亿用户。
- [[2024-counterfactual-watch-time]]:提出 counterfactual watch time (CWT) 与 Counterfactual Watch Model (CWM),从经济学视角建模观看行为以消除视频推荐中的 duration bias。
- [[2024-conditional-quantile-estimation-watch-time]]:提出 CQE,用 quantile regression 与 pinball loss 建模短视频观看时长的完整条件分布,并设计保守/动态组合/条件期望三种推断策略,在 Kuaishou 数亿日活平台上线获显著收益。

## 相关

- [[duration-bias]]
- [[noisy-watching]]
- [[causal-inference]]
- [[implicit-feedback]]
- [[video-recommendation]]
- [[short-video-recommendation]]
- [[duration-debias]]
- [[reinforcement-learning-recommendation]]
- [[multi-task-learning]]
- [[quantile-regression]]
- [[user-engagement]]
