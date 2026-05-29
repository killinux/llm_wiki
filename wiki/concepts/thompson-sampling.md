---
type: concept
subtype: method
tags: [thompson-sampling, bandit, exploration-exploitation, bayesian, optimization]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Thompson Sampling

Thompson Sampling 是一种基于贝叶斯后验采样的探索-利用(exploration-exploitation)决策方法:在每一步从各候选动作的奖励后验分布中采样,并选择采样值最优的动作,从而以概率匹配的方式平衡探索与利用。

## 在本 wiki 中的出现

- [[2025-hyperzero-auto-tuning]]:Meta 的端到端超参数自动调优系统 HyperZero,利用推荐系统小时级反馈,通过 semi-i.i.d. delta 信号 + GP/Thompson Sampling 零阶约束优化 + 异步并行,把 value model 权重调优从数周压缩到 2-3 天,合成数据上 Gain 4.951% 远超 Bayesian optimization。
- [[2025-ab-mcts-adaptive-branching-tree-search]]:提出 AB-MCTS:在推理时树搜索中用 Thompson sampling 自适应决定"向宽采样新候选"还是"向深用外部反馈细化已有答案",统一 repeated sampling 与多轮 refinement,实现更高效的 test-time scaling。

## 相关

- [[multi-armed-bandit]]
- [[bayesian-optimization]]
- [[exploration-exploitation]]
- [[monte-carlo-tree-search]]
- [[test-time-scaling]]
