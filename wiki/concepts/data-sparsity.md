---
type: concept
subtype: method
tags: [recommender-system, graph-learning, contrastive-learning, data-sparsity]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Data Sparsity

数据稀疏性(Data Sparsity)指在推荐、图学习等场景中,用户与物品的交互记录相对于全部可能交互的比例极低,导致大量节点或样本缺乏足够监督信号,从而损害模型表征质量与泛化能力的问题。

## 在本 wiki 中的出现

- [[2024-robust-recommendation-decision-boundary-gcl]]:提出 RGCL,用决策边界感知的对抗扰动约束 graph contrastive learning 增强视图,在交互稀疏的图上平衡语义不变性与对比难度并最大化间隔,在 5 个数据集上一致超越 12 个 baseline(Kuaishou Recall@10 +14.14%)。
- [[2025-multi-objective-controllable-decision-transformer]]:提出 MocDT,一种基于 Decision Transformer 的离线 RL 推荐方法,把未来多目标作为控制信号,在推理阶段自回归生成对齐指定目标(累积评分与多样性)的物品序列,无需重训。

## 相关

- [[graph-contrastive-learning]]
- [[cold-start]]
- [[collaborative-filtering]]
- [[lightgcn]]
- [[margin-maximization]]
- [[adversarial-robustness]]
- [[decision-transformer]]
- [[offline-reinforcement-learning]]
