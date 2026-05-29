---
type: entity
subtype: benchmark
tags: [benchmark, llm-agent, web-navigation, web-agent]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# WebArena

WebArena 是一个用于评测 LLM 智能体在真实网页环境中执行多步任务能力的基准,常被用作网页导航与序列决策类任务的标准测试场景。

## 在本 wiki 中的出现

- [[2024-autoguide-context-aware-guidelines]]:AUTOGUIDE 从离线经验中自动生成并按当前情境检索上下文感知指引,显著提升 LLM 智能体在 ALFWorld、WebShop、WebArena 等序列决策与网页导航任务上的成功率。
- [[2024-tree-search-for-language-model-agents]]:为 LLM web agent 提出 inference-time best-first tree search,在真实 web 环境中显式做探索与多步规划,把 GPT-4o 在 VisualWebArena 上成功率相对提升 39.7% 至 SOTA 26.4%,并展示 test-time compute scaling 的收益。

## 相关

- [[visualwebarena]]
- [[webshop]]
- [[alfworld]]
- [[llm-agent]]
- [[web-navigation]]
