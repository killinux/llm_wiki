---
type: concept
subtype: method
tags: [recommendation, filter-bubble, polarization, llm-agent, simulation]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# filter bubble

信息茧房(filter bubble)指推荐系统持续向用户推送与其既有偏好高度一致的内容,导致用户接触的信息范围不断收窄、观点日益同质化的现象。

## 在本 wiki 中的出现

- [[2024-generative-agents-in-recommendation]]:Agent4Rec 用 1000 个 LLM 驱动的生成式 agent(含 profile/memory/action 模块)构建电影推荐用户模拟器,探究其能否忠实模拟真实用户行为并复现 filter bubble 与 popularity bias。
- [[2024-llm-learnable-planners-long-term-recommendation]]:提出 BiLLP 双层可学习 LLM 规划框架(Planner/Reflector 宏观 + Actor/Critic 微观),在稀疏推荐数据上以 LLM 规划能力做长期推荐,Len 与累积奖励超越从零训练的 RL 与现有 LLM agent 基线。
- [[2024-user-creator-feature-polarization]]:提出 user-creator feature dynamics 模型刻画推荐系统对用户与创作者的双向影响,证明非零推荐概率下系统必然极化,并发现 top-k 截断等效率优化反而能抑制极化、而多样性提升方法在动态环境下失效。

## 相关

- [[popularity-bias]]
- [[polarization]]
- [[recommendation-system]]
- [[llm-agent-simulation]]
- [[long-term-recommendation]]
