---
type: entity
subtype: dataset
tags: [dataset, recommendation, movielens, benchmark]
created: 2026-05-29
updated: 2026-05-29
sources: 8
---

# MovieLens-1M

MovieLens-1M 是由 GroupLens 发布的电影评分数据集,包含约 100 万条用户对电影的评分记录,是推荐系统研究中广泛使用的基准数据集之一。

## 在本 wiki 中的出现

- [[2023-hyper-actor-critic-recommendation]]:作为 Hyper-Actor Critic(HAC)框架的评测数据集之一,用于验证将推荐列表生成解耦为 hyper-action 推断与 effect-action 选择两步、并通过对齐与监督模块稳定大动作空间下 RL 推荐策略学习的效果。
- [[2023-data-heterogeneity-recommendation]]:作为双层聚类方法 BHE 的评测数据集之一,用于挖掘推荐数据中的预测机制异质性与协变量分布异质性;在该数据集上以 NFM 为骨干时,NDCG@20 从 14.01 提升到 22.57。
- [[2023-kuaisim-recommender-simulator]]:面向推荐系统的综合性用户模拟器,提供 multi-behavior 与 cross-session 反馈,统一支持 request 级 list-wise、whole-session 级 sequential 与 cross-session 级 retention 三类 RL 推荐任务并配套 benchmark。
- [[2024-generative-agents-in-recommendation]]:Agent4Rec 用 1000 个 LLM 驱动的生成式 agent(含 profile/memory/action 模块)构建电影推荐用户模拟器,探究其能否忠实模拟真实用户行为并复现 filter bubble 与 popularity bias。
- [[2024-future-impact-decomposition-request-level-recommendation]]:提出 ItemA2C 框架,在 request-level MDP 下将 list-wise reward 分解为 item-wise 信用并用 actor-critic 优化每个 item 的长期未来影响,提升推荐长期效果。
- [[2024-feature-level-bias-ctr]]:自上而下分析揭示 CTR 模型的 feature-level bias 主要源自线性部分,并提出移除/重建线性权重的极简非侵入式去偏策略。
- [[2024-easyrl4rec]]:面向 RL-based 推荐系统的易用代码库,基于五个公开数据集构建轻量 RL 环境,提供四个核心模块与面向长期收益的统一训练/评测流程,并给出经典与近期 RL 方法的对照实验。
- [[2024-robust-recommendation-decision-boundary-gcl]]:提出 RGCL:用决策边界感知的对抗扰动约束 graph contrastive learning 增强视图,平衡语义不变性与对比难度并最大化间隔,在 5 个数据集上一致超越 12 个 baseline(Kuaishou Recall@10 +14.14%)。

## 相关

- [[movielens]]
- [[yelp]]
- [[recommendation-system]]
- [[ndcg]]
- [[reinforcement-learning-for-recommendation]]
