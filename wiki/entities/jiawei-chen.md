---
type: entity
subtype: person
tags: [recommendation, debiasing, doubly-robust, causal-inference, graph-learning, transformer]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Jiawei Chen

Jiawei Chen 是一位从事推荐系统研究的学者,方向涵盖去偏(debiasing)与因果推断、带符号图(signed graph)推荐以及已部署推荐系统的可维护性等问题。

## 在本 wiki 中的出现

- 在 [[2023-conservative-doubly-robust]] 中,作为相关研究工作的作者,该工作提出 CDR(Conservative Doubly Robust),通过审查插补值(imputation)的均值与方差来过滤 Doubly Robust 推荐去偏中的"毒性插补",从而降低偏差与方差并提升性能。
- [[2024-sigformer-sign-aware-graph-transformer]]:用 Transformer 替代 GNN 做 sign-aware 推荐,通过谱编码(SSE)与路径编码(SPE)两种为带符号图设计的 positional encoding 统一利用正负反馈,在 5 个数据集上超越 SOTA。
- [[2024-recommendation-editing]]:提出 recommendation editing 新任务:不重训练、不访问训练数据地修正已部署推荐系统的已知不当推荐,给出形式化定义、ES/EC/EP/EA 评估指标、E-BPR 损失与综合 benchmark。

## 相关

- [[doubly-robust]]
- [[recommendation-debiasing]]
- [[causal-inference]]
- [[2023-conservative-doubly-robust]]
- [[sign-aware-recommendation]]
- [[graph-transformer]]
- [[recommendation-editing]]
- [[recommender-systems]]
