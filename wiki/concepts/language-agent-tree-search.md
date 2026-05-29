---
type: concept
subtype: method
tags: [agents, planning, search, mcts, reasoning]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# 语言智能体树搜索 (LATS, Language Agent Tree Search)

一种 [[llm-agents|LLM 智能体]] 框架,把 [[monte-carlo-tree-search|蒙特卡洛树搜索 (MCTS)]]
集成进智能体循环,以**统一推理、行动与规划**。出处:[[2023-lats-language-agent-tree-search]]
(Zhou 等, 2023)。

## 核心思想
不同于只生成单条轨迹的 [[react|ReAct]],LATS 生长出一棵**思考/行动轨迹的搜索树**,用 MCTS
把探索资源分配到更有希望的分支。三种信号引导搜索:
1. **环境反馈**——动作在真实环境中执行,观测结果让搜索"接地"。
2. **价值函数**——由 LLM 给节点打分、估计前景。
3. **自我反思**——对失败做反思(参见 [[reflexion]])并作为上下文回灌。

## 谱系
- 行动来自 [[react|ReAct]]
- 自我反思来自 [[reflexion|Reflexion]]
- 对推理做搜索来自 [[tree-of-thoughts|Tree of Thoughts]]
- LATS = 以上三者 + 有环境支撑的真实交互,全程无梯度(仅靠上下文学习)

## 证据
[[humaneval|HumanEval]] 上 SOTA 92.7% pass@1([[gpt-4]]);[[webshop]] 上平均 75.9(GPT-3.5)。
详见 [[2023-lats-language-agent-tree-search]]。

## 权衡
树搜索成倍增加每个任务的 LLM 调用次数 → 成本/延迟高于单次智能体。好处是规划更审慎、能从
死胡同里恢复。

## 在本 wiki 中的出现

- [[2024-tree-search-for-language-model-agents]]:为 LLM web agent 提出 inference-time best-first tree search,在真实 web 环境中显式做探索与多步规划,把 GPT-4o 在 VisualWebArena 上成功率相对提升 39.7% 至 SOTA 26.4%,并展示 test-time compute scaling 的收益。
- [[2024-rethinkmcts]]:一个面向代码生成的思路搜索框架,用 MCTS 探索写代码的推理过程,并通过 rethink 机制利用块级代码执行反馈直接精炼搜索树中的错误思路。
