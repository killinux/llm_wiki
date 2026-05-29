---
type: concept
subtype: method
tags: [exposure-bias, debiasing, recommendation, sequence-modeling]
created: 2026-05-29
updated: 2026-05-29
sources: 7
---

# Exposure Bias

Exposure Bias 指模型只能从"已被曝光/呈现给用户的样本"中学习,而无法观测到未曝光样本的真实反馈,导致训练数据并非来自真实分布、从而使学习与评估产生系统性偏差。

## 在本 wiki 中的出现

- [[2022-kuairand]]:快手发布的无偏序列推荐数据集。它通过在常规推荐流中**随机插入视频**来获取一批不受推荐系统曝光策略影响的无偏交互,正是为了对抗 Exposure Bias——常规日志中物品是否被用户看到由推荐系统决定,使得观测数据有偏。该随机曝光数据为去偏(debiasing)建模与可靠的离线评估提供了基准。
- [[2023-chain-of-verification]]:Chain-of-Verification (CoVe) 让 LLM 先生成草稿,再独立回答自我规划的验证问题来核查事实,显著降低幻觉。
- [[2024-feature-level-bias-ctr]]:自上而下分析揭示 CTR 模型的 feature-level bias 主要源自线性部分,并提出移除/重建线性权重的极简非侵入式去偏策略。
- [[2024-fairness-recommendation-missing-labels]]:证明大规模推荐系统在缺失标签下 REO 公平性指标不可识别,提出用小比例 random traffic 无偏估计公平性指标并给出误差上界,首次公开 TikTok 公平性数据集。
- [[2025-debias-can-be-unreliable]]:揭示用随机曝光数据集传统评估去偏推荐不可靠,提出 URE 方案无偏估计全曝光数据上的 Recall@K。
- [[2024-generative-regression-watch-time-prediction]]:提出 Generative Regression (GR),把短视频 watch time 预测从 ordinal regression 重构为 token 序列生成任务,配合 dynamic quantile 词表与 CLEM(curriculum learning + embedding mixup),在 KuaiRec/CIKM16/工业数据集及 Kuaishou 线上 A/B 上超过 SOTA,并可迁移到 LTV 预测。
- [[2025-caserec-counterfactual-augmentation-system-exposure]]:CaseRec 用 Decision Transformer 式 offline RL 建模完整 system exposure 序列,并通过 user simulator 驱动的反事实数据增强发掘未见用户兴趣,改进 sequential recommendation 并缓解 exposure bias。

## 相关

- [[selection-bias]]
- [[debiasing]]
- [[counterfactual-learning]]
- [[sequential-recommendation]]
- [[offline-evaluation]]
