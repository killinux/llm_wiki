---
type: concept
subtype: method
tags: [agent, self-reflection, self-improvement, reasoning]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Reflexion

Reflexion 是一种让语言模型 Agent 通过对自身行动结果进行语言化的自我反思,并把反思内容存入记忆以指导后续尝试,从而在不更新模型权重的情况下迭代提升任务表现的方法。

## 在本 wiki 中的出现

- [[2025-multi-agent-reflexion-mar]]:把 Reflexion 的单 Agent 自我批评换成多 persona 辩论加 judge 合成反思,在 HotPotQA(EM 44→47)与 HumanEval(pass@1 76.4→82.6)上超过单 Agent Reflexion。

## 相关

- [[self-refine]]
- [[chain-of-thought]]
- [[react]]
- [[multi-agent-debate]]
