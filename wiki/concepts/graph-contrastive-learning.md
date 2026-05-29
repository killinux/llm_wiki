---
type: concept
subtype: method
tags: [graph-learning, contrastive-learning, self-supervised, recommendation, adversarial]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Graph Contrastive Learning

Graph Contrastive Learning(图对比学习)是一种自监督表示学习方法,通过对图结构生成不同的增强视图,并拉近同一节点不同视图的表示、推远不同节点的表示,从而在缺乏标签的情况下学习鲁棒的图节点/结构嵌入。

## 在本 wiki 中的出现

- [[2024-robust-recommendation-decision-boundary-gcl]]:提出 RGCL:用决策边界感知的对抗扰动约束 graph contrastive learning 增强视图,平衡语义不变性与对比难度并最大化间隔,在 5 个数据集上一致超越 12 个 baseline(Kuaishou Recall@10 +14.14%)。
- [[2025-tadt-csa-temporal-advantage-decision-transformer]]:面向工业生成式推荐的 Decision Transformer 改进框架,用 Temporal Advantage 信号和对比式状态抽象解决 DT 的轨迹拼接弱与状态空间过大问题。

## 相关

- [[contrastive-learning]]
- [[graph-neural-networks]]
- [[self-supervised-learning]]
- [[adversarial-perturbation]]
- [[recommendation-systems]]
