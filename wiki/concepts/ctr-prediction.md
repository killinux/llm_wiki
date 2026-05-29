---
type: concept
subtype: method
tags: [recommendation, ranking, ctr, deep-learning, prediction]
created: 2026-05-29
updated: 2026-05-29
sources: 7
---

# 点击率预估 (CTR Prediction / Click-Through Rate Prediction)

CTR prediction 指给定用户、物品(item)与上下文特征,预测用户点击某次曝光(impression)的概率,是推荐与广告系统中排序(ranking)环节的核心监督学习任务。

## 概述

CTR prediction 通常被建模为一个二分类问题:以用户历史行为、物品属性与场景上下文为输入,输出 [0,1] 的点击概率,常用 AUC、LogLoss 等指标评估(参见 [[evaluation]])。它是工业推荐/广告 pipeline 中精排阶段的代表性目标,大量特征交叉(feature interaction)、多任务与多场景(multi-domain / multi-scenario)建模工作都围绕它展开。由于训练数据来自系统自身的曝光日志,CTR prediction 还天然伴随 selection bias、feature-level bias 等偏差问题,因此与 debiasing 方向紧密相关。

## 在本 wiki 中的出现

- [[2024-feature-level-bias-ctr]]:研究 CTR prediction 模型中的特征级偏差(feature-level bias),将该任务作为分析与去偏(debiasing)的对象。
- [[2023-hierrec-scenario-aware-hierarchical-dynamic-network]]:面向多场景(scenario-aware)的 CTR prediction,用分层动态网络在不同场景下共享与区分排序信号。
- [[2024-scenario-wise-rec]]:以 CTR prediction 为核心任务,提供面向多场景推荐排序的基准与方法。
- [[2024-dfei-large-scale-multi-domain-recommendation]]:在大规模多域(multi-domain)推荐中以 CTR prediction 作为主要排序目标进行特征/表征建模。
- [[2023-multi-task-recommendations-with-rl]]:把 CTR(点击)等行为目标与其他任务一起纳入多任务推荐框架,CTR prediction 是其中的子任务之一。
- [[2024-llm-tags-vs-classical-text-features]]:比较 LLM 生成标签与经典文本特征在下游任务(含 CTR prediction)中的效果,以 CTR 任务衡量特征质量。
- [[2024-merrec-mercari-c2c-recommendation-dataset]]:作为 C2C 推荐数据集,支持包括 CTR prediction 在内的推荐排序任务评测。

## 相关

- [[ctr]]
- [[evaluation]]
- [[debiasing]]
- [[selection-bias]]
- [[factorization-machines]]
- [[deep-interest-network]]
- [[two-tower]]
- [[deepfm]]
- [[autoint]]
- [[mmoe]]
- [[esmm]]
- [[ali-ccp]]
