---
type: concept
subtype: method
tags: [off-policy-evaluation, recommendation, debiasing, offline-evaluation, causal-inference]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# Off-Policy Evaluation

Off-Policy Evaluation (OPE) 指在不实际部署新策略的前提下,利用由另一套(行为)策略收集到的历史日志数据,估计目标策略性能的方法。

## 在本 wiki 中的出现

- [[2022-kuairand]]:KuaiRand 是快手发布的无偏序列推荐数据集,通过在常规推荐流中随机插入视频来收集百万级无偏交互(含 12 种反馈信号、完整的用户/物品 ID 与特征)。其中随机曝光产生的无偏数据可作为 Off-Policy Evaluation 的评估基准,为去偏(debiasing)与离线评估研究提供可信的反事实参照,从而缓解日志数据本身的曝光偏差对策略评估的影响。
- [[2024-edt4rec-max-entropy-decision-transformer]]:EDT4Rec 给 Decision Transformer 加入最大熵探索与基于 CQL Q-function 的 reward relabeling,解决 offline RL 推荐中缺乏 stitching 能力和在线探索不足的问题。
- [[2025-debias-can-be-unreliable]]:揭示用随机曝光数据集传统评估去偏推荐不可靠,提出 URE 方案无偏估计全曝光数据上的 Recall@K。
- [[2025-multiscale-contextual-bandits-long-term]]:提出 MultiScale Policy Learning 框架与 MSBL 算法,用分层 off-policy contextual bandit 在多个时间尺度上协调短期反馈与长期目标,让低尺度数据作为高尺度稀疏数据的 PAC-Bayes 先验。
- [[2025-where-to-explore-reach-cost-aware-unbiased-data]]:提出按用户 scroll-depth 触发、低成本高触达的专用 UI 行("Something Completely Different")来交付随机化探索内容,在不损害短期参与度的前提下大规模收集无偏交互数据,并回灌候选生成提升长期推荐质量(线上 +0.94% 参与度,无偏数据 Gini 0.203 vs 0.494)。

## 相关

- [[debiasing]]
- [[exposure-bias]]
- [[inverse-propensity-scoring]]
- [[offline-evaluation]]
- [[counterfactual-learning]]
- [[sequential-recommendation]]
- [[contextual-bandits]]
- [[pac-bayes]]
- [[2022-kuairand]]
