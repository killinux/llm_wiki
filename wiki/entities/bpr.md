---
type: entity
subtype: model
tags: [recommendation, ranking, collaborative-filtering]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# BPR

BPR(Bayesian Personalized Ranking,贝叶斯个性化排序)是一种面向隐式反馈的成对排序优化方法,常被用作推荐系统中协同过滤模型的训练目标与基线。

## 在本 wiki 中的出现
- [[2024-recflow-full-flow-recommendation-dataset]]:首个包含工业推荐系统多级漏斗各阶段未曝光样本的大规模全流程数据集,用于研究分布偏移、选择偏差与多阶段联合优化。
- [[2025-fine-grained-skip-micro-video-recommendation]]:将 micro-video 中的 skip 行为细分为 highly positive、less positive、negative 三类,用双层图与分层 BPR ranking loss 建模,在 MVA 与 KuaiRand-Pure 的八项指标上超越 FRAME/LightGT/BM3。
- [[2025-xmtf-formula-free-multi-task-fusion]]:xMTF 用可学习的单调融合单元(MFC)替代多任务融合中的预定义公式,配合 RL 外层 + 监督内层的两阶段混合训练,离线 Total Watch Time 1279.7s 超越全部基线,线上 Daily Watch Time +0.833%,Kuaishou 全量部署服务超 1 亿用户。
- [[2025-tadt-csa-temporal-advantage-decision-transformer]]:面向工业生成式推荐的 Decision Transformer 改进框架,用 Temporal Advantage 信号和对比式状态抽象解决 DT 的轨迹拼接弱与状态空间过大问题。
- [[pairwise-ranking-loss]]
- [[selection-bias]]
- [[multi-task-fusion]]

- [[2023-agentcf-collaborative-learning-agents-recsys]]:把推荐系统中的用户和物品都建模为 LLM agent,通过自主交互与协同反思实现无梯度的协同过滤式优化。
- [[2025-pub-personality-user-behaviour-simulator]]:PUB 是基于 LLM 的用户行为模拟器,将 Big Five 人格特质嵌入用户建模,从行为日志推断人格并生成高保真合成交互,用于推荐系统的离线评估(BPR 作为相关推荐排序方法语境出现)。

## 相关

- [[collaborative-filtering]]
- [[recommender-systems|recommendation-system]]
- [[implicit-feedback]]
