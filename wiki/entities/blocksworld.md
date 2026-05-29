---
type: entity
subtype: benchmark
tags: [planning, reasoning, benchmark]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Blocksworld

Blocksworld 是一个经典的规划(planning)基准任务,要求智能体通过移动积木在初始状态与目标状态之间进行重排,常被用来评估 LLM 的多步推理与规划能力。

## 在本 wiki 中的出现

- [[2023-reasoning-via-planning-rap]]:作为评估 RAP 的任务之一。RAP 把 LLM 同时当作世界模型和推理智能体,用 MCTS 在推理空间里做规划,把 LLM 推理重新表述为带世界模型的规划,Blocksworld 提供了需要多步规划的测试场景。
- [[2024-reflection-on-search-trees]]:RoT 让 strong LLM 反思 weak LLM 的历史树搜索经验、对关键状态总结出任务级 guideline 注入后续 prompt,显著提升 BFS/MCTS 等树搜索 prompting 在 Blocksworld、GSM8k、议价任务上的准确率与搜索效率,且任务越难收益越大。

## 相关

- [[reasoning-via-planning-rap]]
- [[monte-carlo-tree-search|mcts]]
- [[world-model]]
- [[llm-reasoning]]
- [[planning]]
