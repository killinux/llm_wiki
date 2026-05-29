---
type: concept
subtype: method
tags: [recommendation, collaborative-filtering, matrix-factorization, debiasing]
created: 2026-05-29
updated: 2026-05-29
sources: 8
---

# Matrix Factorization

Matrix Factorization 是协同过滤推荐中的经典方法,通过将用户-物品交互矩阵分解为低维的用户隐向量与物品隐向量,以两者内积来预测缺失的评分或交互。

## 在本 wiki 中的出现

- 在 [[2023-data-heterogeneity-recommendation]] 中,Matrix Factorization 作为推荐预测建模的基础范式之一。该工作提出双层聚类方法 BHE,显式挖掘推荐数据中的预测机制异质性与协变量分布异质性,用于多子模型预测与去偏;其方法在不同推荐骨干上验证,在 Yelp/MovieLens-1M 上以 NFM 为骨干时 NDCG@20 从 14.01 提升到 22.57。Matrix Factorization 及其衍生模型(如 NFM)构成此类推荐去偏研究的建模与评测对象。

- 在 [[2023-conservative-doubly-robust]] 中,Matrix Factorization 是推荐去偏所要纠正的基础预测模型背景。该工作提出 CDR(Conservative Doubly Robust),通过审查插补值的均值与方差来过滤 Doubly Robust 去偏中的"毒性插补",从而降低偏差方差并提升性能。Matrix Factorization 风格的预测模型是 Doubly Robust 框架进行偏差校正的典型对象。

- [[2023-kuaisim-recommender-simulator]]:面向推荐系统的综合性用户模拟器,提供 multi-behavior 与 cross-session 反馈,统一支持 request 级 list-wise、whole-session 级 sequential 与 cross-session 级 retention 三类 RL 推荐任务并配套 benchmark。

- [[2024-generative-agents-in-recommendation]]:Agent4Rec 用 1000 个 LLM 驱动的生成式 agent(含 profile/memory/action 模块)构建电影推荐用户模拟器,探究其能否忠实模拟真实用户行为并复现 filter bubble 与 popularity bias。

- [[2023-collaboration-transition-multi-query-self-attention]]:提出 MQSA-TED,用多查询自注意力建模协同信号、并把全局 item 转移模式蒸馏进 embedding,在序列推荐中平衡协同与转移信号。

- [[2024-easyrl4rec]]:面向 RL-based 推荐系统的易用代码库,基于五个公开数据集构建轻量 RL 环境,提供四个核心模块与面向长期收益的统一训练/评测流程,并给出经典与近期 RL 方法的对照实验。

- [[2024-sigformer-sign-aware-graph-transformer]]:用 Transformer 替代 GNN 做 sign-aware 推荐,通过谱编码(SSE)与路径编码(SPE)两种为带符号图设计的 positional encoding 统一利用正负反馈,在 5 个数据集上超越 SOTA。

- [[2024-recommendation-editing]]:提出 recommendation editing 新任务:不重训练、不访问训练数据地修正已部署推荐系统的已知不当推荐,给出形式化定义、ES/EC/EP/EA 评估指标、E-BPR 损失与综合 benchmark。

## 相关

- [[collaborative-filtering]]
- [[neural-factorization-machine]]
- [[doubly-robust]]
- [[recommendation-debiasing]]
- [[ndcg]]
- [[2023-data-heterogeneity-recommendation]]
- [[2023-conservative-doubly-robust]]
