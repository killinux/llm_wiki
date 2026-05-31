---
type: concept
subtype: method
tags: [reinforcement-learning, bandits, recommender-system, exploration-exploitation, online-learning]
created: 2026-05-30
updated: 2026-05-31
sources: 9
---

# 上下文老虎机 (Contextual Bandits)

上下文老虎机是介于**监督学习**与**完整强化学习**之间的在线决策框架:每一步先观察一个**上下文 (context)**(如用户特征),
从若干**臂 (arm / action)** 中选一个,只观察被选臂的**奖励**(bandit feedback),目标是最小化累计 **regret**。它没有完整 RL 的
状态转移 / 长期信用分配,因此更易上线、样本效率更高。

## 核心问题:探索-利用权衡
- **利用 (exploit)**:选当前估计收益最高的臂;**探索 (explore)**:试不确定的臂以改进估计。
- 经典算法:**ε-greedy**、**UCB**(上置信界)、**Thompson Sampling**(后验采样);线性假设下的 **LinUCB**。

## 在推荐 / 内容分发中的应用
是冷启动与新内容探索的主力工具——用最小代价为新 item / 新用户收集反馈。
- 长期视角:[[2025-multiscale-contextual-bandits-long-term]] 把 bandit 扩到多尺度、面向长期收益。
- 与**完整 RL 推荐**的分界:当决策有显著的跨期影响(留存、生态)时需升级到 [[reinforcement-learning-for-recommendation]]
  (如 [[2023-rlur-user-retention-short-video]]、[[2023-dorl-matthew-effect-offline-rl-recommendation]]);bandit 是其"无状态转移"特例。

## 在推荐/策略中的具体应用

- [[2025-multiscale-contextual-bandits-long-term]]：提出 MultiScale Policy Learning 框架与 MSBL 算法，用分层 off-policy contextual bandit 在多个时间尺度上协调短期反馈与长期目标，让低尺度数据作为高尺度稀疏数据的 PAC-Bayes 先验。
- [[2025-where-to-explore-reach-cost-aware-unbiased-data]]：提出按用户 scroll-depth 触发、低成本高触达的专用 UI 行来交付随机化探索内容，在不损害短期参与度的前提下大规模收集无偏交互数据（线上 +0.94% 参与度，无偏数据 Gini 0.203 vs 0.494）。
- [[2026-policysim-proactive-policy-optimization]]：PolicySim 用带消息传递的 contextual bandit 自适应优化推荐与曝光控制等平台干预策略。

## 相关页
[[reinforcement-learning]]、[[reinforcement-learning-for-recommendation]]、[[recommender-systems]]、[[exploration-exploitation]]、[[online-item-cold-start-popularity-aware-meta-learning]]、[[off-policy-learning]]、[[pac-bayes]]、[[policy-learning]]
