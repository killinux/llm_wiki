---
type: concept
subtype: method
tags: [reinforcement-learning, model-based, offline-rl, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# Model-based RL

Model-based RL 是一类强化学习方法,它显式地学习一个环境模型(状态转移与奖励),并利用该模型进行规划或生成模拟交互数据,从而提升样本效率。

## 在本 wiki 中的出现

- [[2023-dorl-matthew-effect-offline-rl-recommendation]]:该工作以 model-based offline RL 为基础框架,在其悲观惩罚(pessimistic penalty)之上额外引入熵惩罚,用以缓解交互式推荐中的马太效应(Matthew effect),进而提升用户的长期满意度。在此场景下,model-based RL 通过学习到的用户响应模型支撑离线策略优化,而其固有的悲观惩罚机制正是 DORL 进行改造与扩展的对象。
- [[2023-ts-llm-tree-search-decoding-training]]:TS-LLM 用学习到的 value function 进行 AlphaZero 风格的树搜索,同时指导 LLM 的推理解码与迭代训练,适配任意规模 LLM 并将搜索深度扩展到 64。
- [[2024-model-based-multi-agent-short-video-recommender]]:MMRF 用协作式多智能体 RL 最大化短视频会话累计 WatchTime,并通过 model-based 反馈模拟缓解样本选择偏差,离线 +7.3% GAUC、在线 +0.55% WatchTime,已部署服务数亿用户。
- [[2025-caserec-counterfactual-augmentation-system-exposure]]:CaseRec 用 Decision Transformer 式 offline RL 建模完整 system exposure 序列,并通过 user simulator 驱动的反事实数据增强发掘未见用户兴趣,改进 sequential recommendation 并缓解 exposure bias。
- [[2025-reward-balancing-revisited]]:提出 R3S,用 diffusion world model 显式建模 reward 不确定性并配合带衰减的多样性惩罚,在 offline RL 推荐中同时平衡 world model 偏差与策略多样性,在 Coat/Yahoo/KuaiRand 上超越 DORL、ROLeR 等 11 个 baseline。

## 相关

- [[reinforcement-learning]]
- [[world-model]]
- [[offline-rl]]
- [[recommender-system]]
- [[markov-decision-process]]
- [[matthew-effect]]
- [[tree-search]]
- [[value-function]]
- [[multi-agent-rl]]
