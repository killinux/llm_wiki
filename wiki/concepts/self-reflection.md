---
type: concept
subtype: method
tags: [self-reflection, agent, reflexion, self-improvement]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Self-Reflection

Self-Reflection 指 LLM Agent 在完成任务或单步动作后,对自身的输出、轨迹与成败信号进行自我批评与总结,提炼经验并将其反馈到后续决策中,从而在不更新模型参数的情况下实现自我改进。

## 在本 wiki 中的出现

- [[2025-multi-agent-reflexion-mar]]:把 Reflexion 的单 Agent 自我批评换成多 persona 辩论加 judge 合成反思,在 HotPotQA(EM 44→47)与 HumanEval(pass@1 76.4→82.6)上超过单 Agent Reflexion。
- [[2026-experiential-reflective-learning]]:ERL 让 agent 反思单次任务轨迹与成败信号、提炼可迁移启发式存入持久池,新任务时按相关性检索 top-k 注入上下文,无需更新参数即可自我改进,在 Gaia2 上比 ReAct 基线提升 7.8% 成功率。

## 相关

- [[reflexion]]
- [[multi-agent-debate]]
- [[react]]
- [[experiential-learning]]
