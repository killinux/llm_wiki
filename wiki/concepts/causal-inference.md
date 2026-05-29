---
type: concept
subtype: method
tags: [causal-inference, recommendation, debiasing, confounding, counterfactual]
created: 2026-05-29
updated: 2026-05-29
sources: 8
---

# Causal Inference

Causal Inference(因果推断)是一类从观测数据中估计变量间因果效应、而非仅仅相关关系的方法论,常借助因果记号、可识别性假设、效应定义与估计技术来回答"干预/反事实"问题。

## 在本 wiki 中的出现

- [[2022-deep-causal-reasoning-for-recommendations]]:Deep-Deconf 用深度 VAE 推断 substitute confounders,把推荐建模为 MCMO(multi-cause multi-outcome)因果推断问题,以消除混杂偏差并降低估计方差。在此 Causal Inference 是去混杂推荐建模的核心框架。
- [[2023-causal-inference-for-recommendation]]:一篇系统综述,系统梳理如何将 Causal Inference 引入推荐系统,涵盖因果记号、假设、效应与估计方法,并讨论可解释性、公平性、鲁棒性、uplift 与无偏性等实际问题。Causal Inference 是该综述的主题本身。
- [[2023-idcf-debiasing-recommendation]]:提出 iDCF,借助代理变量(用户特征)与近端因果推断(proximal causal inference),在存在未观测混杂变量时为推荐反事实反馈提供可识别性保证,在 Coat/Yahoo!R3/KuaiRand 上优于现有去混杂方法。Causal Inference 在此为反事实反馈的可识别性提供理论支撑。
- [[2023-d2co-watch-time-debias]]:提出 D²Co,从统一的因果视角同时矫正视频推荐中观看时长的时长偏差(duration bias)与噪声观看(noisy watching),还原用户真实兴趣。Causal Inference 在此为多重偏差的统一矫正提供视角。
- [[2023-video-length-debiasing-microvideo-rec]]:VLDRec 通过 play-progress 去偏标注、视频长度条件采样与多任务学习缓解微视频推荐中长视频被偏好的 video-length bias,以 NFM 为基座在 View_Time@120 上较最佳基线提升 1.81%(Kuaishou)与 11.32%(WeChat)。
- [[2024-generative-agents-in-recommendation]]:Agent4Rec 用 1000 个 LLM 驱动的生成式 agent(含 profile/memory/action 模块)构建电影推荐用户模拟器,探究其能否忠实模拟真实用户行为并复现 filter bubble 与 popularity bias。
- [[2024-edt4rec-max-entropy-decision-transformer]]:EDT4Rec 给 Decision Transformer 加入最大熵探索与基于 CQL Q-function 的 reward relabeling,解决 offline RL 推荐中缺乏 stitching 能力和在线探索不足的问题。
- [[2024-counterfactual-watch-time]]:提出 counterfactual watch time (CWT) 与 Counterfactual Watch Model (CWM),从经济学视角建模观看行为以消除视频推荐中的 duration bias。

## 相关

- [[confounding-bias]]
- [[counterfactual-inference]]
- [[recommendation-debiasing]]
- [[proximal-causal-inference]]
- [[variational-autoencoder]]
- [[uplift-modeling]]
- [[2022-deep-causal-reasoning-for-recommendations]]
- [[2023-causal-inference-for-recommendation]]
- [[2023-idcf-debiasing-recommendation]]
- [[2023-d2co-watch-time-debias]]
