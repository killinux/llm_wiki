---
type: concept
subtype: method
tags: [recommender-systems, offline-rl, world-model, reward-shaping, uncertainty]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Reference User Selection

Reference User Selection 是一种在基于模型的离线强化学习推荐框架中,通过动态挑选"参考用户"来精炼 world model 奖励信号、并据此自适应估计不确定性惩罚的方法。

## 在本 wiki 中的出现

- [[2025-darlr-dual-agent-offline-rl-recsys]]:面向推荐系统的双 agent(selector + recommender)model-based offline RL 框架,在策略学习中用参考用户动态精炼 world model 的奖励并自适应估计不确定性惩罚,在 KuaiRand/KuaiRec/Coat/Yahoo 四个数据集上累计奖励全面领先并接近 ground-truth 上界。

## 相关

- [[model-based-offline-rl]]
- [[world-model]]
- [[uncertainty-penalty]]
- [[recommender-systems]]
- [[dual-agent-framework]]
