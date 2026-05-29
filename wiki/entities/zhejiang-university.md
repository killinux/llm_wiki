---
type: entity
subtype: lab
tags: [university, china, research-institution, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Zhejiang University

Zhejiang University(浙江大学)是一所位于中国杭州的综合性研究型大学,在本 wiki 中作为相关论文的研究机构出现。

## 在本 wiki 中的出现

- [[2023-conservative-doubly-robust]]:作为研究机构,参与提出 CDR(Conservative Doubly Robust)。该工作通过审查插补值(imputation)的均值与方差来过滤 Doubly Robust 推荐去偏中的"毒性插补"(poisonous imputation),从而降低偏差与方差并提升推荐性能。
- [[2024-sigformer-sign-aware-graph-transformer]]:用 Transformer 替代 GNN 做 sign-aware 推荐,通过谱编码(SSE)与路径编码(SPE)两种为带符号图设计的 positional encoding 统一利用正负反馈,在 5 个数据集上超越 SOTA。
- [[2024-recommendation-editing]]:提出 recommendation editing 新任务:不重训练、不访问训练数据地修正已部署推荐系统的已知不当推荐,给出形式化定义、ES/EC/EP/EA 评估指标、E-BPR 损失与综合 benchmark。

## 相关

- [[doubly-robust]]
- [[selection-bias]]
- [[inverse-propensity-score]]
- [[monte-carlo-dropout]]
- [[graph-neural-networks]]
- [[transformer]]
