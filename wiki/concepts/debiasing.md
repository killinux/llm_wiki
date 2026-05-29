---
type: concept
subtype: method
tags: [debiasing, recommendation, causal-inference, bias, unbiased-evaluation]
created: 2026-05-29
updated: 2026-05-29
sources: 9
---

# Debiasing

Debiasing 指在推荐系统等场景中,识别并矫正由数据收集或反馈机制引入的各类偏差(如曝光偏差、选择偏差、时长偏差等),以还原用户真实兴趣并获得无偏估计的一系列方法。

## 在本 wiki 中的出现

- [[2022-kuairand]]:作为支撑去偏研究的数据基础。该数据集通过在推荐流中随机插入视频收集百万级无偏交互(含 12 种反馈信号、完整用户/物品 ID 与特征),为 debiasing 与离线评估提供随机曝光数据。
- [[2023-idcf-debiasing-recommendation]]:提出 iDCF,借助代理变量(用户特征)与近端因果推断,在存在未观测混杂变量时为推荐反事实反馈提供可识别性保证,代表基于因果推断的 debiasing 路线,在 Coat/Yahoo!R3/KuaiRand 上优于现有去混杂方法。
- [[2023-d2co-watch-time-debias]]:提出 D²Co,从统一因果视角同时矫正视频推荐中观看时长的时长偏差(duration bias)与噪声观看,是面向 watch-time 的具体 debiasing 方法。
- [[2023-video-length-debiasing-microvideo-rec]]:VLDRec 通过 play-progress 去偏标注、视频长度条件采样与多任务学习缓解微视频推荐中长视频被偏好的 video-length bias,以 NFM 为基座在 View_Time@120 上较最佳基线提升 1.81%(Kuaishou)与 11.32%(WeChat)。
- [[2024-feature-level-bias-ctr]]:自上而下分析揭示 CTR 模型的 feature-level bias 主要源自线性部分,并提出移除/重建线性权重的极简非侵入式去偏策略。
- [[2024-fairness-recommendation-missing-labels]]:证明大规模推荐系统在缺失标签下 REO 公平性指标不可识别,提出用小比例 random traffic 无偏估计公平性指标并给出误差上界,首次公开 TikTok 公平性数据集。
- [[2024-counterfactual-watch-time]]:提出 counterfactual watch time (CWT) 与 Counterfactual Watch Model (CWM),从经济学视角建模观看行为以消除视频推荐中的 duration bias。
- [[2024-llm4rerank-auto-reranking-recommendation]]:把推荐 reranking 的 accuracy/diversity/fairness 等目标抽象为全连接图中的 node,让 LLM 以 Chain-of-Thought 多跳方式按用户给定的 "Goal" 自动综合多目标重排候选列表。
- [[2024-deconfound-release-interval-bias]]:将 release interval 识别为短视频推荐中的 confounder,提出模型无关的因果框架 LDRI,通过 backdoor adjustment 阻断后门路径并按视频自身 recency sensitivity 个性化去偏。

## 相关

- [[exposure-bias]]
- [[selection-bias]]
- [[duration-bias]]
- [[causal-inference]]
- [[counterfactual-learning]]
- [[unbiased-evaluation]]
- [[sequential-recommendation]]
- [[watch-time-prediction]]
- [[backdoor-adjustment]]
- [[fairness]]
- [[ctr-prediction]]
- [[recommendation-reranking]]
