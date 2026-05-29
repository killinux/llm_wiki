---
type: concept
subtype: method
tags: [multi-objective-optimization, constrained-optimization, recommendation, trade-off]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# Pareto Optimization

Pareto Optimization 是一类多目标优化方法,寻找无法在不损害任一目标的前提下进一步改进其它目标的解(即 Pareto 最优解),从而刻画多个相互冲突目标之间的权衡边界。

## 在本 wiki 中的出现

- [[2023-two-stage-constrained-actor-critic]]:该工作面向短视频推荐中的多目标权衡问题——在最大化主目标 WatchTime 的同时,需兼顾 Like/Share 等稀疏交互信号。其提出的 TSCAC(两阶段约束式 actor-critic)通过对辅助目标施加软约束来平衡各目标,本质上是在多个冲突目标间寻求权衡,与 Pareto Optimization 所刻画的多目标取舍思想相关;该方法已在快手生产系统全量上线。
- [[2024-llm-tags-vs-classical-text-features]]:在统一协议下对照评估 LLM 生成语义标签与 TF-IDF/LDA/BERT 三类经典文本特征用于短视频推荐用户兴趣建模,发现 LLM 标签下游精度最优(CTR AUC 较 TF-IDF +0.9~1.6 点、SASRec HR@10 +2.1~3.4 点),且因稀疏化在在线成本上 Pareto 支配稠密嵌入,但离线生成贵约 40 倍。
- [[2024-llm-critics-help-catch-llm-bugs]]:OpenAI 用 RLHF 训练 GPT-4 级别的 critic 模型 CriticGPT,让 LLM 写自然语言批评指出代码 bug,以可扩展监督方式帮助人类更准确评估模型生成的代码,体现精度与监督成本之间的权衡。
- [[2025-multi-objective-controllable-decision-transformer]]:提出 MocDT,一种基于 Decision Transformer 的离线 RL 推荐方法,把未来多目标作为控制信号,在推理阶段自回归生成对齐指定目标(累积评分与多样性)的物品序列,无需重训。

## 相关

- [[multi-objective-optimization]]
- [[constrained-optimization]]
- [[actor-critic]]
- [[reinforcement-learning]]
- [[2023-two-stage-constrained-actor-critic]]
