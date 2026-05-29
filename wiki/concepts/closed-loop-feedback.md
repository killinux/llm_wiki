---
type: concept
subtype: method
tags: [closed-loop, feedback, embodied-reasoning, planning, llm]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Closed-Loop Feedback

Closed-Loop Feedback 指系统在执行过程中持续接收环境/任务反馈,并据此调整后续决策与规划,从而形成"行动—感知—再规划"的闭环,而非一次性地开环执行预设计划。

## 在本 wiki 中的出现

- [[2022-inner-monologue]]:将多种来源的自然语言环境反馈(如成功检测、场景描述、人类回应等)持续注入 frozen LLM 的提示中,让模型形成"内心独白"(inner monologue)式推理。借助这种 closed-loop feedback,LLM 无需额外训练即可在机器人具身任务中实现闭环、可重规划的推理,在动作失败或环境变化时重新规划。

## 相关

- [[inner-monologue]]
- [[grounded-language-feedback]]
- [[llm-planning]]
- [[embodied-reasoning]]
- [[re-planning]]
- [[frozen-llm]]
