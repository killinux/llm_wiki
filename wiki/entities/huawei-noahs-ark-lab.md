---
type: entity
subtype: lab
tags: [industry-research, huawei, recommender-systems]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# Huawei Noah's Ark Lab

华为旗下的人工智能与决策推理研究实验室,研究方向涵盖机器学习、推荐系统、自然语言处理与决策优化。

## 在本 wiki 中的出现

- [[2023-multi-task-deep-recommender-systems-survey]]:该综述从任务关系与方法论两个维度为多任务深度推荐系统(MTDRS)建立系统分类体系,梳理代表模型、数据集与未来研究方向;Huawei Noah's Ark Lab 为该工作的署名研究机构之一。
- [[2023-hierrec-scenario-aware-hierarchical-dynamic-network]]:HierRec 用分层 dynamic-weight 网络同时建模显式与隐式场景,在 Ali-CCP/KuaiRand 多场景 CTR 预测上显著超越 MMoE、PLE、STAR 等基线。
- [[2024-bankfair-fluctuating-traffic-reranking]]:BankFair 借鉴破产问题的 Talmud rule,把两侧推荐的曝光分配建模为序列化破产问题并用在线学习求解,在波动用户流量下同时保证短期用户准确性与长期提供方公平性。
- [[2024-counterfactual-watch-time]]:提出 counterfactual watch time (CWT) 与 Counterfactual Watch Model (CWM),从经济学视角建模观看行为以消除视频推荐中的 duration bias。
- [[2024-llm4rerank-auto-reranking-recommendation]]:把推荐 reranking 的 accuracy/diversity/fairness 等目标抽象为全连接图中的 node,让 LLM 以 Chain-of-Thought 多跳方式按用户给定的 "Goal" 自动综合多目标重排候选列表。

## 相关

- [[multi-task-learning]] —— 多任务深度推荐系统(MTDRS)的核心范式
- [[recommender-systems]] —— 实验室相关研究领域
- [[mmoe]]、[[ple]] —— 多任务推荐中的代表性模型架构
- [[multi-scenario-ctr-prediction]] —— HierRec 所属的多场景 CTR 预测方向
- [[reranking]] —— BankFair / LLM4Rerank 涉及的重排序问题
- [[recommendation-fairness]] —— BankFair 关注的提供方公平性
- [[duration-bias]] —— CWM 旨在消除的观看时长偏差
- [[llm-for-recommendation]] —— LLM4Rerank 代表的 LLM 用于推荐方向
