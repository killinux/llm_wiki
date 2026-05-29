---
type: concept
subtype: method
tags: [offline-rl, model-based-rl, uncertainty, reward-shaping, recommender-systems]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Uncertainty Penalty

不确定性惩罚是 model-based offline RL 中的一种正则化机制:通过估计 world model 在某状态-动作上的预测不确定性,对奖励进行扣减(惩罚),从而抑制策略在数据分布外、模型不可靠区域的过度乐观行为。

## 在本 wiki 中的出现

- [[2025-darlr-dual-agent-offline-rl-recsys]]:面向推荐系统的双 agent(selector + recommender)model-based offline RL 框架,在策略学习中用参考用户动态精炼 world model 的奖励并自适应估计不确定性惩罚,在 KuaiRand/KuaiRec/Coat/Yahoo 四个数据集上累计奖励全面领先并接近 ground-truth 上界。

## 相关

- [[model-based-offline-rl]]
- [[world-model]]
- [[reward-shaping]]
- [[distribution-shift]]
