---
type: concept
subtype: method
tags: [react, llm-agent, reasoning, acting, planning, tool-use]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# ReAct

ReAct(Reasoning and Acting)是一种让大语言模型在解决任务时交替进行"推理(生成思考链)"与"行动(调用工具/与环境交互)"的范式,使模型能基于观测结果迭代调整计划。

## 在本 wiki 中的出现

- [[2024-tree-search-for-language-model-agents]]:为 LLM web agent 提出 inference-time best-first tree search,在真实 web 环境中显式做探索与多步规划,把 GPT-4o 在 VisualWebArena 上成功率相对提升 39.7% 至 SOTA 26.4%,并展示 test-time compute scaling 的收益。
- [[2024-hiagent-hierarchical-working-memory]]:HiAgent 用 subgoal 作为 memory chunk 分层管理 LLM agent 的 working memory(汇总过去 observation、按需检索明细轨迹),在五个长程任务上成功率约翻倍(21→42)、context 减少 35%。

## 相关

- [[llm-agent]]
- [[tree-search]]
- [[working-memory]]
- [[test-time-compute-scaling]]
- [[tool-use]]
