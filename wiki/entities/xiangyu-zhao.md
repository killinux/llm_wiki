---
type: entity
subtype: person
tags: [researcher, recommender-systems, multi-task-learning, deep-learning, reinforcement-learning, llm, reranking, feature-selection, multi-scenario-recommendation, benchmark]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# Xiangyu Zhao

研究者,工作涉及多任务深度推荐系统(MTDRS)、强化学习推荐、用户模拟、深度推荐系统的特征选择、多场景推荐基准建设以及大语言模型在推荐(如自动重排)中的应用。

## 在本 wiki 中的出现

- 在 [[2023-multi-task-deep-recommender-systems-survey]] 中,作为该综述的作者之一参与撰写。该综述从任务关系与方法论两个维度为多任务深度推荐系统(MTDRS)建立系统分类体系,梳理了代表模型、数据集与未来研究方向。
- [[2023-kuaisim-recommender-simulator]]:面向推荐系统的综合性用户模拟器,提供 multi-behavior 与 cross-session 反馈,统一支持 request 级 list-wise、whole-session 级 sequential 与 cross-session 级 retention 三类 RL 推荐任务并配套 benchmark。
- [[2024-llm4rerank-auto-reranking-recommendation]]:把推荐 reranking 的 accuracy/diversity/fairness 等目标抽象为全连接图中的 node,让 LLM 以 Chain-of-Thought 多跳方式按用户给定的 "Goal" 自动综合多目标重排候选列表。
- [[2025-self-surrogate-light-feature-selection]]:提出 SELF,用多个 LLM 的世界知识对特征做语义排序、再以轻量 bridge network 融合任务信号,缓解深度推荐系统特征选择对 surrogate model 的依赖。
- [[2024-scenario-wise-rec]]:首个面向多场景推荐(MSR)的开源 benchmark,整合 6 个公开数据集、12 个基线模型与统一的数据处理/训练/评测流水线,并在工业广告数据集上验证。

## 相关

- [[multi-task-learning]]
- [[recommender-system]]
- [[deep-learning]]
- [[reinforcement-learning-recommendation]]
- [[llm-for-recommendation]]
- [[reranking]]
- [[user-simulator]]
- [[feature-selection]]
- [[multi-scenario-recommendation]]
