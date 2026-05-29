---
type: concept
subtype: method
tags: [contextual-bandit, off-policy-learning, reinforcement-learning, policy-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Contextual Bandit

Contextual Bandit(情境老虎机)是一类在线决策方法:在每一步根据观察到的上下文(context)从若干动作中选择一个,并仅获得所选动作的反馈(奖励),目标是学习一个将上下文映射到动作的策略以最大化累计奖励。

## 在本 wiki 中的出现

- [[2025-multiscale-contextual-bandits-long-term]]:提出 MultiScale Policy Learning 框架与 MSBL 算法,用分层 off-policy contextual bandit 在多个时间尺度上协调短期反馈与长期目标,让低尺度数据作为高尺度稀疏数据的 PAC-Bayes 先验。
- [[2025-where-to-explore-reach-cost-aware-unbiased-data]]:提出按用户 scroll-depth 触发、低成本高触达的专用 UI 行("Something Completely Different")来交付随机化探索内容,在不损害短期参与度的前提下大规模收集无偏交互数据,并回灌候选生成提升长期推荐质量(线上 +0.94% 参与度,无偏数据 Gini 0.203 vs 0.494)。
- [[2026-policysim-proactive-policy-optimization]]:PolicySim 是一个基于 LLM 智能体的社会模拟沙盒,用 SFT+DPO 训练用户智能体、用带消息传递的 contextual bandit 自适应优化推荐与曝光控制等平台干预策略,实现部署前的主动评估与优化。

## 相关

- [[off-policy-learning]]
- [[pac-bayes]]
- [[policy-learning]]
- [[reinforcement-learning]]
