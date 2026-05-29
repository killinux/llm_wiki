---
type: entity
subtype: model
tags: [recommendation, graph-neural-network, collaborative-filtering, lightgcn]
created: 2026-05-29
updated: 2026-05-29
sources: 6
---

# LightGCN

LightGCN 是一种轻量化的图卷积网络协同过滤模型,通过去除特征变换与非线性激活、仅保留邻域聚合来学习用户与物品的嵌入表示,是推荐系统中常用的基线模型。

## 在本 wiki 中的出现

- [[2025-segment-level-user-interest-modeling]]:把短视频拆成时间片段,用混合表示+多模态用户-视频编码器+片段兴趣解码器建模用户沿时间线动态演变的片段级兴趣,用于 video-skip 预测与推荐。
- [[2025-simuser-llm-user-simulation-recsys]]:基于 LLM 的 agent 框架,用从历史数据推断的 persona、记忆、感知与决策模块构建可信合成用户来低成本评估推荐系统。
- [[2025-bankfair-plus-regret-aware-reranking]]:BankFair+(BankFair 的扩展期刊版)把 regret theory 的非线性满意度函数与 fuzzy programming 引入推荐重排,在保证供给侧最低曝光公平与用户平均精度的同时,显著提升被忽视的用户个体公平(KuaiRand-1K 上 MMR 0.741 vs BankFair 0.493)。
- [[2026-thinkrec-thinking-based-recommendation]]:ThinkRec 通过思考激活(推理数据合成+联合训练)与实例级 LoRA 专家融合,把 LLM 推荐从 System 1 直觉匹配推进到 System 2 推理,在 ML1M/Yelp/Book 上 AUC 平均超 SOTA 7.96%。
- [[2025-pub-personality-user-behaviour-simulator]]:PUB 是一个基于 LLM 的用户行为模拟器,把 Big Five 人格特质嵌入用户建模,从行为日志推断人格并生成高保真合成交互,用于推荐系统的离线评估。
- [[2025-mitigating-unwanted-recommendations-conformal-risk-control]]:一个 post-hoc、模型无关、distribution-free 的方法,用 conformal risk control 给推荐中"不想要内容"的比例提供可证明上界,并以用户曾看过的安全重复内容替换有害项以保住推荐质量。

## 相关

- [[graph-neural-network]]
- [[collaborative-filtering]]
- [[recommendation-system]]
- [[matrix-factorization]]
