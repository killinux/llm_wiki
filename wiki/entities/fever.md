---
type: entity
subtype: benchmark
tags: [benchmark, fact-verification, evaluation]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# FEVER

FEVER(Fact Extraction and VERification)是一个事实核查基准:给定一条陈述,判断它被证据支持(SUPPORTED)、被反驳(REFUTED),还是信息不足(NOT ENOUGH INFO)。

## 在本 wiki 中的出现

- [[2023-expel]]:作为评估 LLM Agent 决策表现的任务之一。该工作让 LLM Agent 不更新参数,而是从跨任务经验中自主抽取自然语言洞见,并召回相似的成功轨迹来提升决策表现,FEVER 在其中充当检验这种经验抽取与召回方法效果的测试场景。

## 相关

- [[expel]]
- [[hotpotqa]]
- [[fact-verification]]
- [[llm-agent]]
- [[wikipedia]]
