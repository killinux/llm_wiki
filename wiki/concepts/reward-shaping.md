---
type: concept
subtype: method
tags: [reinforcement-learning, reward, reward-shaping, alignment, offline-rl]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Reward Shaping

Reward Shaping(奖励塑形)是指在强化学习中通过修改、精炼或补充原始奖励信号,引导智能体更高效、更稳健地学习到期望策略的一类方法。

## 在本 wiki 中的出现

- [[2025-darlr-dual-agent-offline-rl-recsys]]:面向推荐系统的双 agent(selector + recommender)model-based offline RL 框架,在策略学习中用参考用户动态精炼 world model 的奖励并自适应估计不确定性惩罚,在 KuaiRand/KuaiRec/Coat/Yahoo 四个数据集上累计奖励全面领先并接近 ground-truth 上界。
- [[2025-agent-safety-alignment-via-reinforcement-learning]]:首个面向 tool-using agent 的统一安全对齐框架,通过 structured reasoning + sandbox 强化学习,用 benign/malicious/sensitive 三模态分类与 execute-refuse-verify 策略同时抵御用户侧与工具侧威胁。
- [[2026-fairness-begins-with-state-dsrm-hrl]]:DSRM-HRL 用扩散模型把被 popularity bias 污染的用户状态提纯回真实偏好流形,再用分层 RL 解耦长期公平与短期参与,在 KuaiRec/KuaiRand 上实现 accuracy 与 fairness 更优的 Pareto 前沿。

## 相关

- [[reinforcement-learning]]
- [[offline-rl]]
- [[model-based-rl]]
- [[reward-model]]
- [[uncertainty-penalty]]
- [[alignment|safety-alignment]]
