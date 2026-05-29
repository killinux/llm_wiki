---
type: source
subtype: paper
tags: [reasoning, planning, tree-search, mcts, reflection, prompting, llm-planning]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2404.05449
raw: raw/2404.05449.pdf
authors: [Wenyang Hui, Kewei Tu]
year: 2024
---

# RoT: Enhancing Large Language Models with Reflection on Search Trees

RoT(Reflection on search Trees)是一个让 LLM 从过往树搜索经验中反思、由 strong LLM 总结出任务级 guideline 来增强 weak LLM 的框架,可显著提升 [[tree-of-thoughts]]、MCTS 等基于树搜索的 prompting 方法在推理与规划任务上的准确率与搜索效率。

## 问题

[[large-language-models]] 与基于树搜索的 prompting 方法(如 BFS、[[monte-carlo-tree-search]])结合后,在需要多步推理与规划的任务(具身规划 [[blocksworld]]、数学推理 [[gsm8k]]、对话策略规划 CraigslistBargain)上表现出色。这类方法把问题分解为多步,逐步尝试 action 引发 state 转移,用 LLM 来(1)生成可用 action、(2)评估 action/state 的 value、(3)预测下一个 state。

但现有方法**忽略了之前的搜索经验**,因此会反复犯同样的错误:错误评估 action、生成低收益的 action、错误预测下一状态。这导致准确率低、搜索效率差,并对错误 action 过度探索(over-exploration)。已有研究指出 value estimation 的准确性对树搜索性能至关重要,而 LLM 的 value estimation 并不可靠。

## 方法

RoT 在不更新参数的前提下,用一个 strong LLM 反思 weak LLM 的历史搜索过程,提炼出自然语言 guideline,再注入到后续搜索的 prompt 中。包含三步:

- **重要状态选择(Important State Selection)**:并非反思整棵树,而是挑出关键状态。状态 s 的重要性定义为其子节点 value 与自身 value 之差的最大值 `Importance(s) = max_{s'∈children(s)} |V(s') − V(s)|`;当 `Importance(s) > λ`(阈值,实验取 0.1)时该状态被选为重要状态,在此类状态做对的决策能大幅改善搜索结果。RoT 同时保存该状态的可用 action、各 action 对应的下一状态及其 value。
- **Guideline 总结(Guideline Summarization)**:对每个重要状态,让 strong LLM 对比反思所有 action 及其后果,先分析每个 action 对下一状态 value 的影响,再总结出 guideline。为避免一次性塞入所有重要状态导致 LLM 顾此失彼、产出过于宽泛的指导,RoT 先对单个重要状态分别生成 guideline,再让 LLM 合并(merge)为一份综合 guideline,附加到生成 action/state/估值的 prompt 的预定位置。
- **迭代改进(Iterative Improvement)**:借鉴 [[expert-iteration]],可迭代地用已有 guideline 生成更优搜索树,再据此总结增强版 guideline。

实验集成两种树搜索方法(BFS、MCTS)和两种非树搜索方法([[chain-of-thought]] / CoT、CoT 自一致性 [[self-consistency]]),baseline 对比近期面向 CoT 的反思方法 LEAP。weak LLM 用 phi-2(2.7B)、Mistral-7B、Mixtral-8x7B;guideline 由 [[gpt-4]] 总结。

## 结果

- **Blocksworld(具身规划)**:RoT 在各模型、各搜索方法上普遍优于 baseline 与 LEAP。例如 Mistral-7B 在 step-8 上 MCTS(1) 从 14.5 提升到 24.5(+69.0%)。MCTS 相对 baseline 的平均相对提升随难度增大:step-2 为 +2.2%,step-8 升至 +27.1%——任务越难,RoT 收益越大。
- **GSM8k(数学推理)**:RoT 在树搜索方法上提升明显,如 Mistral-7B 的 MCTS(1) 从 42.4 提升到 47.3(+11.6%),Mixtral-8x7B 的 MCTS(10) 从 77.4 到 79.2。由于算术计算能力无法靠 guideline 增强,GSM8k 上的提升幅度小于 Blocksworld。
- **CraigslistBargain(对话议价)**:用 mixtral-8x7b、chatgpt、[[gpt-4]] 作为 seller。鼓励利润(profit)设定下 RoT 带来平均绝对 profit 提升约 0.55;同时鼓励达成协议(agreement)的设定下平均 profit 提升约 0.36 且不牺牲达成率。RoT 甚至能让 CoT 的表现追平或超过 MCTS。该任务上 RoT 提升最显著,因为 LLM 对议价较不熟悉。
- **搜索效率**:用迭代-准确率曲线下面积(AUC)衡量,RoT 提升 AUC(如 phi-2 在 Blocksworld step-6 上从 27.2 提升到 33.1),即用更少 MCTS 迭代达到更高准确率,任务越难提升越显著。
- **消融**:在 GSM8k 上,基于重要状态(λ=0.1, 242 个决策)反思取得最佳 47.3,优于用全部经验(45.0)、随机状态(44.2)、仅问题样本(44.7)与无 guideline 的 MCTS(42.4)。

## 在本 wiki 中的位置

本文属于 [[llm-planning]] / [[reasoning]] 方向的 test-time 反思工作,把 [[reflection]] 思想从单样本细化(如 [[self-refine]]、[[reflexion]])推进到对**整棵搜索树的任务级反思**,与基于树搜索的 prompting 方法([[tree-of-thoughts]]、[[reasoning-via-planning-rap]]、[[language-agent-tree-search]])及 [[monte-carlo-tree-search]] 紧密相关。其重要状态选择本质上是在缓解 LLM value estimation 不可靠的问题,可与 [[process-reward-model]]、[[self-consistency]] 等推理增强方法相互参照;迭代改进则呼应 [[expert-iteration]] / [[self-improvement]]。
