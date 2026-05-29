---
type: source
subtype: paper
tags: [llm, agents, planning, reasoning, mcts, search]
created: 2026-05-29
updated: 2026-05-29
arxiv: "2310.04406"
raw: raw/2310.04406v3.pdf
authors: [Andy Zhou, Kai Yan, Michal Shlapentokh-Rothman, Haohan Wang, Yu-Xiong Wang]
published: 2023-10-06
revised: 2024-06-06
---

# LATS：语言智能体树搜索,统一 LLM 的推理、行动与规划

一句话:提出 [[language-agent-tree-search]]——把 LLM 套进 [[monte-carlo-tree-search|蒙特卡洛树搜索]]
里,让 [[llm-agents|LLM 智能体]] 能够借助环境反馈、价值估计和自我反思,**有意识地在
"推理 + 行动"轨迹空间中搜索**。

- **作者**:Andy Zhou, Kai Yan, Michal Shlapentokh-Rothman, Haohan Wang, Yu-Xiong Wang
- **arXiv**:[2310.04406](https://arxiv.org/abs/2310.04406) · 2023-10-06 提交,2024-06-06 最后修订 · cs.AI / cs.CL / cs.LG(亦含 cs.CV)
- **本地原文**:`raw/2310.04406v3.pdf`
- **代码**:https://github.com/lapisrocks/LATS

## 问题
LLM 在决策类任务上有潜力,但它们依赖**简单的"行动"流程**,限制了作为自主智能体的部署。
诱导逐步推理与自我评估的提示方法有帮助,但**无法在任务内做有意识的探索或回溯**。

## 方法
LATS 被称为**首个统一 LLM 推理、行动、规划三种能力的通用框架**。它仅利用 LLM 的上下文
学习能力(无梯度更新),将 [[monte-carlo-tree-search|MCTS]] 与以下三者结合:
- **LLM 价值函数**——由 LLM 给节点打分,引导探索方向。
- **自我反思**——对失败轨迹做反思(类似 [[reflexion|Reflexion]]),把反思作为后续分支的上下文。
- **引入环境获取外部反馈**——动作在环境中真实执行,观测结果回流,提供比纯自我评估更
  审慎、更具适应性的信号(论文称之为"关键特性")。

定位上是 [[react|ReAct]](行动)、[[reflexion|Reflexion]](自我反思)、
[[tree-of-thoughts|Tree of Thoughts]](对推理做搜索)三者的综合,并在树搜索之上加入了
有环境支撑的真实交互。

## 结果
- **编程**——在 [[humaneval|HumanEval]] 上用 [[gpt-4]] 取得 SOTA **92.7% pass@1**。
- **网页导航**——在 [[webshop]] 上用 GPT-3.5 取得 **平均分 75.9**(无梯度,与基于梯度的
  微调相当)。

## 备注 / 待解问题
- MCTS 意味着**每个任务要调用很多次 LLM** → 相比单次提示存在成本/延迟权衡(等再 ingest
  更多"智能体 + 搜索"类论文后,值得单独建一页做对比)。
- 与 [[tree-of-thoughts]] 的区别:ToT 只对推理步骤搜索、没有真实环境;LATS 额外加入了
  行动 + 观测 + 反思。
