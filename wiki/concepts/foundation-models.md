---
type: concept
subtype: method
tags: [foundation-models, pretraining, transfer-learning, large-models]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# Foundation Models

Foundation Models 指在大规模、广泛数据上预训练、可通过微调或提示适配到多种下游任务的大型模型(如大语言模型、视觉-语言模型等)。

## 在本 wiki 中的出现

- [[2023-causal-inference-for-recommendation]]:这是一篇关于将因果推断引入推荐系统的系统综述,涵盖因果记号、假设、效应与估计方法,以及可解释性、公平性、鲁棒性、uplift 和无偏性等实际问题。在该综述的语境中,Foundation Models 与因果推断推荐方法相对照——前者依赖大规模数据上的相关性学习与预训练范式,后者强调对干预效应与无偏估计的建模;二者在如何处理数据偏差、提升泛化与鲁棒性方面构成互补视角。
- [[2025-drivemlm-autonomous-driving]]:DriveMLM 将 multi-modal LLM 对齐到自动驾驶行为规划模块的离散决策状态,使语言输出可转为车辆控制,在 CARLA Town05 Long 上实现闭环驾驶并取得 DS 76.1、MPI 0.96。
- [[2023-timesfm-time-series-foundation-model]]:Google Research 的 TimesFM:一个在 O(100B) 时间点真实+合成时序上预训练的 decoder-only 时序预测基础模型,zero-shot 表现接近全监督 SOTA。
- [[2023-concordia-generative-agent-based-modeling]]:Google DeepMind 提出的库 Concordia,用 LLM 驱动的生成式 agent 在物理/社会/数字空间中扎根交互,通过 Game Master 控制环境,支持 Generative Agent-Based Modeling 的社会仿真与数字服务评估。

> 说明:上述资料并非专门讨论 Foundation Models 的论文,其对该概念的提及为背景性、对照性的。更具体的角色描述以原文为准。

## 相关

- [[causal-inference]]
- [[recommender-systems]]
- [[pretraining]]
- [[transfer-learning]]
- [[emergent-abilities]]
- [[in-context-learning]]
- [[robustness]]
- [[fairness]]
