---
type: concept
subtype: method
tags: [reinforcement-learning, reward-shaping, offline-rl, recsys, world-model]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Dynamic Reward Shaping

动态奖励塑形是指在策略学习过程中,根据模型对环境(如 world model)的最新理解或不确定性估计,实时、自适应地精炼与调整奖励信号,而非使用一成不变的固定奖励函数。

## 在本 wiki 中的出现

- [[2025-darlr-dual-agent-offline-rl-recsys]]:面向推荐系统的双 agent(selector + recommender)model-based offline RL 框架,在策略学习中用参考用户动态精炼 world model 的奖励并自适应估计不确定性惩罚,在 KuaiRand/KuaiRec/Coat/Yahoo 四个数据集上累计奖励全面领先并接近 ground-truth 上界。

## 相关

- [[reward-shaping]]
- [[model-based-offline-rl]]
- [[world-model]]
- [[uncertainty-penalty]]
- [[recommender-systems]]
