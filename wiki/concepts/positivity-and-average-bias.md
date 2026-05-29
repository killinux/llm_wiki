---
type: concept
subtype: method
tags: [user-simulation, llm-bias, evaluation, benchmark]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# positivity-and-average bias

指当前基于 LLM 的用户模拟器在生成用户行为时表现出的一种结构性偏差:倾向于产出过于积极(positivity)且向群体均值收敛(average)的行为,从而难以刻画真实用户的负面反馈与个体异质性。

## 在本 wiki 中的出现

- [[2026-omnibehavior]]:OmniBehavior 是首个完全基于真实工业日志(快手)构建的用户模拟基准,刻画长时程、跨场景、异质行为轨迹,并揭示当前 LLM 模拟器存在"积极且趋均值"的结构性偏差。

## 相关

- [[user-simulation]]
- [[llm-as-simulator]]
- [[behavior-modeling]]
