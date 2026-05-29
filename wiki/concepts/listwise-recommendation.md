---
type: concept
subtype: method
tags: [recommendation, listwise, ranking, exploration, diversity]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# Listwise recommendation

Listwise recommendation 指以整个推荐列表(而非单个 item)为优化与建模单位的推荐方法,直接面向 list-wise 奖励/效用进行学习与生成,从而在列表层面权衡相关性、多样性与探索。

## 在本 wiki 中的出现

- [[2023-gflownet-listwise-recommendation]]:在该工作(GFN4Rec)中,Listwise recommendation 是核心建模对象。作者用 GFlowNet 的流匹配(flow matching)训练生成器,使得一个推荐列表被生成的概率正比于其 list-wise 奖励,从而在保持高质量的同时显著提升列表多样性,并增强在线探索能力。
- [[2023-kuaisim-recommender-simulator]]:面向推荐系统的综合性用户模拟器,提供 multi-behavior 与 cross-session 反馈,统一支持 request 级 list-wise、whole-session 级 sequential 与 cross-session 级 retention 三类 RL 推荐任务并配套 benchmark。
- [[2024-future-impact-decomposition-request-level-recommendation]]:提出 ItemA2C 框架,在 request-level MDP 下将 list-wise reward 分解为 item-wise 信用并用 actor-critic 优化每个 item 的长期未来影响,提升推荐长期效果。
- [[2024-llm4rerank-auto-reranking-recommendation]]:把推荐 reranking 的 accuracy/diversity/fairness 等目标抽象为全连接图中的 node,让 LLM 以 Chain-of-Thought 多跳方式按用户给定的 "Goal" 自动综合多目标重排候选列表。

## 相关

- [[gflownet]]
- [[flow-matching]]
- [[list-wise-reward]]
- [[recommendation-diversity]]
- [[online-exploration]]
- [[learning-to-rank]]
- [[pointwise-recommendation]]
- [[pairwise-recommendation]]
