---
type: concept
subtype: method
tags: [user-simulation, llm-agent, recommender-systems, social-simulation]
created: 2026-05-29
updated: 2026-05-29
sources: 8
---

# User Behavior Simulation

User Behavior Simulation 是指用计算模型(尤其是 LLM-based agent)在虚拟环境中复现真实用户的行为模式,从而在无需真实用户参与的情况下生成可观测、可分析的交互数据的方法。

## 在本 wiki 中的出现

- [[2023-recagent-user-behavior-simulation]]:提出 RecAgent,把每个用户建模为一个 LLM-based agent,在包含推荐页面与社交媒体的沙盒中近乎零样本(zero-shot)地模拟用户的推荐与社交行为;User Behavior Simulation 是该工作的核心方法,并被用于研究 information cocoon(信息茧房)与 conformity(从众)等涌现现象。
- [[2023-kuaisim-recommender-simulator]]:面向推荐系统的综合性用户模拟器,提供 multi-behavior 与 cross-session 反馈,统一支持 request 级 list-wise、whole-session 级 sequential 与 cross-session 级 retention 三类 RL 推荐任务并配套 benchmark。
- [[2023-agentcf-collaborative-learning-agents-recsys]]:把推荐系统中的用户和物品都建模为 LLM agent,通过自主交互与协同反思实现无梯度的协同过滤式优化。
- [[2024-generative-agents-in-recommendation]]:Agent4Rec 用 1000 个 LLM 驱动的生成式 agent(含 profile/memory/action 模块)构建电影推荐用户模拟器,探究其能否忠实模拟真实用户行为并复现 filter bubble 与 popularity bias。
- [[2023-concordia-generative-agent-based-modeling]]:Google DeepMind 提出的库 Concordia,用 LLM 驱动的生成式 agent 在物理/社会/数字空间中扎根交互,通过 Game Master 控制环境,支持 Generative Agent-Based Modeling 的社会仿真与数字服务评估。
- [[2024-macrec-multi-agent-recommendation]]:清华提出的多 agent 协作推荐框架(SIGIR'24 demo),用 Manager、Analyst、Reflector、Searcher、Task Interpreter 等角色各异的 LLM agent 直接协作完成评分预测、序列推荐、解释生成与对话推荐。
- [[2024-eeg-svrec-eeg-affective-engagement-dataset]]:首个在真实短视频观看场景下采集 EEG 脑电信号并配以六维情感参与度标注(MAES)与行为日志的推荐数据集,benchmark 显示加入 EEG 特征可提升推荐 AUC。
- [[2024-lusifer-llm-user-simulation]]:提出 Lusifer:基于 LLM 的用户模拟环境,在每次交互后增量更新可解释的用户画像,为 RL-based 推荐系统生成动态真实的用户反馈,并在 cold-start 场景超越传统协同过滤基线。

## 相关

- [[llm-agent]]:实现 User Behavior Simulation 的常用技术基础。
- [[recommender-systems]]:User Behavior Simulation 的典型应用场景之一。
- [[social-simulation]]:更广义的社会行为模拟,与用户行为模拟密切相关。
- [[information-cocoon]]:可通过用户行为模拟研究的社会现象。
- [[conformity]]:可通过用户行为模拟研究的社会现象。
