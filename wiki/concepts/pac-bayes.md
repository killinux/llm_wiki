---
type: concept
subtype: method
tags: [generalization-bound, learning-theory, bayesian, off-policy]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# PAC-Bayes

PAC-Bayes 是一类学习理论框架,通过引入先验分布与后验分布之间的 KL 散度,为随机化预测器(或策略)的泛化误差给出高概率上界,从而把贝叶斯式的先验知识与 PAC 风格的泛化保证结合起来。

## 在本 wiki 中的出现

- [[2025-multiscale-contextual-bandits-long-term]]:提出 MultiScale Policy Learning 框架与 MSBL 算法,用分层 off-policy contextual bandit 在多个时间尺度上协调短期反馈与长期目标,让低尺度数据作为高尺度稀疏数据的 PAC-Bayes 先验。

## 相关

- [[contextual-bandits]]
- [[off-policy-learning]]
- [[generalization-bound]]
- [[kl-divergence]]
