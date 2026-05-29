---
type: entity
subtype: lab
tags: [university, china, research-institution, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 6
---

# Zhejiang University

Zhejiang University(浙江大学)是一所位于中国杭州的综合性研究型大学,在本 wiki 中作为相关论文的研究机构出现。

## 在本 wiki 中的出现

- [[2023-conservative-doubly-robust]]:作为研究机构,参与提出 CDR(Conservative Doubly Robust)。该工作通过审查插补值(imputation)的均值与方差来过滤 Doubly Robust 推荐去偏中的"毒性插补"(poisonous imputation),从而降低偏差与方差并提升推荐性能。
- [[2024-sigformer-sign-aware-graph-transformer]]:用 Transformer 替代 GNN 做 sign-aware 推荐,通过谱编码(SSE)与路径编码(SPE)两种为带符号图设计的 positional encoding 统一利用正负反馈,在 5 个数据集上超越 SOTA。
- [[2024-recommendation-editing]]:提出 recommendation editing 新任务:不重训练、不访问训练数据地修正已部署推荐系统的已知不当推荐,给出形式化定义、ES/EC/EP/EA 评估指标、E-BPR 损失与综合 benchmark。
- [[2024-diit-domain-invariant-information-transfer]]:DIIT 通过 gating 域级聚合 + 对抗表示对齐双抽取器和 multi-spot 知识蒸馏迁移器,把多个 source domain 模型的 domain-invariant 信息注入 target domain 模型,实现推理只需 target 模型的高效工业跨域推荐。
- [[2025-multi-objective-controllable-decision-transformer]]:提出 MocDT,一种基于 Decision Transformer 的离线 RL 推荐方法,把未来多目标作为控制信号,在推理阶段自回归生成对齐指定目标(累积评分与多样性)的物品序列,无需重训。
- [[2026-thinkrec-thinking-based-recommendation]]:ThinkRec 通过思考激活(推理数据合成+联合训练)与实例级 LoRA 专家融合,把 LLM 推荐从 System 1 直觉匹配推进到 System 2 推理,在 ML1M/Yelp/Book 上 AUC 平均超 SOTA 7.96%。

## 相关

- [[doubly-robust]]
- [[selection-bias]]
- [[inverse-propensity-score]]
- [[monte-carlo-dropout]]
- [[graph-neural-networks]]
- [[transformer]]
- [[decision-transformer]]
- [[offline-reinforcement-learning]]
- [[cross-domain-recommendation]]
- [[knowledge-distillation]]
- [[llm-recommendation]]
- [[lora]]
