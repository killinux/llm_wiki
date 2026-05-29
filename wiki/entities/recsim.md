---
type: entity
subtype: product
tags: [recommendation, simulation, simulator, reinforcement-learning, user-behavior]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# RecSim

RecSim 是一个用于推荐系统的可配置仿真平台,用于在可控的环境中模拟用户与推荐系统的序列化交互,从而支持(尤其是基于强化学习的)推荐算法的研究与评估。

## 在本 wiki 中的出现

- [[2023-recagent-user-behavior-simulation]]:该论文提出 RecAgent,主张用 LLM-based agent 在沙盒环境中近乎零样本地模拟用户的推荐与社交行为,并研究信息茧房(information cocoons)与从众(conformity)等现象。在这一脉络中,RecSim 作为更早期、基于预设规则/参数化模型的用户行为仿真器,是 LLM-based 用户模拟方法所对照与区别的传统仿真范式之一。
- [[2023-kuaisim-recommender-simulator]]:面向推荐系统的综合性用户模拟器,提供 multi-behavior 与 cross-session 反馈,统一支持 request 级 list-wise、whole-session 级 sequential 与 cross-session 级 retention 三类 RL 推荐任务并配套 benchmark。
- [[2024-lmagent-multimodal-agents-society]]:基于多模态 LLM 的万级规模 agents 社会,在电商场景模拟多用户的购物、社交、直播行为,复现真实 co-purchase 模式与从众等 emergent behavior。
- [[2025-pub-personality-user-behaviour-simulator]]:PUB 是一个基于 LLM 的用户行为模拟器,把 Big Five 人格特质嵌入用户建模,从行为日志推断人格并生成高保真合成交互,用于推荐系统的离线评估。

## 相关

- [[2023-recagent-user-behavior-simulation]]
- [[ai-user-agent]]
- [[generative-agents]]
- [[movielens]]
- [[kuairec]]
