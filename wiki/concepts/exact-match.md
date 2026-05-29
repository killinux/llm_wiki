---
type: concept
subtype: method
tags: [evaluation, metric, qa]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Exact Match

Exact Match(EM)是一种评估指标,要求模型预测的答案与标准答案在归一化后完全一致才算正确,常用于问答与代码生成等任务的准确率衡量。

## 在本 wiki 中的出现

- [[2025-multi-agent-reflexion-mar]]:把 Reflexion 的单 Agent 自我批评换成多 persona 辩论加 judge 合成反思,在 HotPotQA(EM 44→47)与 HumanEval(pass@1 76.4→82.6)上超过单 Agent Reflexion。

## 相关

- [[reflexion]]
- [[hotpotqa]]
- [[pass-at-k]]
