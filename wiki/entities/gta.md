---
type: entity
subtype: benchmark
tags: [benchmark, tool-use, llm-agent, tool-planning]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# GTA

GTA(General Tool Agents)是一个评测 LLM 智能体真实场景下多工具调用与规划能力的基准,常用 AVG(平均得分)等指标衡量智能体在多工具任务上的表现。

## 在本 wiki 中的出现

- [[2026-tooltree-tool-planning]]:免训练的 MCTS 工具规划框架,用执行前/执行后双反馈引导搜索并双向剪枝,在固定预算下提升 LLM 智能体多工具规划的准确率与效率(GTA 66.95 AVG,ToolBench 69.04 AVG)。

## 相关

- [[toolbench]]
- [[tool-use]]
- [[llm-agents|llm-agent]]
- [[monte-carlo-tree-search|mcts]]
