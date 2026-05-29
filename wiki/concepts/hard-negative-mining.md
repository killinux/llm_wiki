---
type: concept
subtype: method
tags: [retrieval, embedding, training, negative-sampling]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Hard negative mining

Hard negative mining 是一种训练负采样策略,通过挑选那些"与正样本高度相似、容易被模型误判为正例"的困难负样本(hard negatives)来构造训练对,从而提升检索/匹配模型对细粒度区分的能力。

## 在本 wiki 中的出现

- [[2023-divide-and-conquer-ebr]]:该工作把推荐召回的 embedding-based retrieval 拆成"物料聚类 + 簇内并行检索 + 可控合并",并采用 prompt-like 多任务适配。在这种 EBR 训练范式中,hard negative mining 通常作为提升表征判别力的关键手段——困难负样本往往就来自与目标 query/物料同簇或语义临近的物料,与该工作的聚类结构天然契合。在公开数据集上 Recall 最高提升约 40%,并已在快手线上部署。
- [[2024-robust-recommendation-decision-boundary-gcl]]:提出 RGCL,用决策边界感知的对抗扰动约束 graph contrastive learning 增强视图,平衡语义不变性与对比难度并最大化间隔,在 5 个数据集上一致超越 12 个 baseline(Kuaishou Recall@10 +14.14%)。

## 相关

- [[embedding-based-retrieval]]
- [[negative-sampling]]
- [[contrastive-learning]]
- [[recall]]
- [[in-batch-negatives]]
