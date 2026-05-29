---
type: source
subtype: paper
tags: [reasoning, planning, search, world-model, mcts, llm]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2305.14992
raw: raw/2305.14992.pdf
authors: [Shibo Hao, Yi Gu, Haodi Ma, Joshua Jiahua Hong, Zhen Wang, Daisy Zhe Wang, Zhiting Hu]
year: 2023
---

RAP(Reasoning via Planning)把 LLM 同时当作"推理智能体"和"世界模型",并用蒙特卡洛树搜索(MCTS)在巨大的推理空间里做有策略的规划,从而把语言模型的推理重新表述为"带世界模型的规划"问题。

## 问题
[[chain-of-thought]] 等方法让 LLM 逐步生成中间推理,显著提升了推理能力,但 LLM 在一些对人类很容易的任务上仍然吃力:例如为环境中的任务生成可执行的动作计划,以及复杂的数学、逻辑、常识推理。

作者认为根本缺陷在于:LLM 缺少一个内部的**世界模型**(world model)来预测世界状态(环境状态、中间变量取值)并模拟动作的长期后果。这使得 LLM 无法像人脑那样进行**有意识的规划**——探索多条候选推理路径、预判未来状态与奖励、并迭代地修正已有的推理步骤。CoT 这类方法本质上是"一条路走到黑"的自回归生成,缺乏前瞻和回溯。

## 方法
RAP 把 LLM 复用为两个角色:
- **世界模型**:给定当前状态和一个候选动作,LLM 预测下一个状态(如 Blocksworld 中积木的新摆放、数学题中的中间子问题答案)。
- **推理智能体**:LLM 提出候选动作,逐步构建一棵推理树。

在世界模型和**任务专属奖励**(task-specific reward)的引导下,RAP 用基于 [[monte-carlo-tree-search]] 的规划算法在推理树上做探索,平衡探索(exploration)与利用(exploitation),高效地找到一条高奖励的推理路径。奖励信号可来自动作的似然、状态置信度、自我评估等。论文还提出 **RAP-Agg** 变体,聚合多次 MCTS 迭代的结果来估计奖励。

与 [[tree-of-thoughts]] 相比,RAP 的关键区别在于显式引入"世界模型"来预测状态转移,并用带奖励的 MCTS 做规划,而不仅是树搜索 + 自评。

## 结果
主干实验基于 [[llama]](LLaMA-33B),覆盖三类任务:

- **计划生成(Blocksworld)**:在按最少动作数分组的测试集上(2 步 30 例、4 步 57 例、6 步 114 例),CoT-LLaMA-33B 几乎无法生成正确计划(4 步设定仅约 1%),RAP-LLaMA-33B 在 4 步达到 64% 成功率、6 步达到 42%。在完整 [[blocksworld]] 数据集上,RAP-LLaMA-33B 比 CoT 版本的 [[gpt-4]] 高出约 33%(绝对值)。
- **数学推理([[gsm8k]])**:4-shot 提示下,单条推理轨迹的 RAP(10) 准确率 48.6%(摘要正文记为 48.8%),加上 RAP-Aggregation 后达 51.6%;相比 CoT(29.4%、CoT+SC(10) 46.8%)与 Least-to-Most(25.5%、+SC 42.5%)均更优。
- **逻辑推理([[prontoqa]])**:RAP 预测准确率 94.2%、证明(proof)准确率 78.8%,相比 CoT(87.8/64.8)证明准确率高 14%,相比 CoT+SC(89.8 预测)预测准确率高 4.4%。

整体表明:用同一个 LLM 充当世界模型 + 规划,可在较小模型上超过更大模型的 CoT 基线。

## 在本 wiki 中的位置
RAP 属于"LLM 推理增强"中**搜索/规划**一脉,与 [[tree-of-thoughts]] 同期且思路相近,都把推理建模为在状态空间上的搜索;RAP 的差异化在于显式的**世界模型**与 [[monte-carlo-tree-search]] 规划,因此也连接到 [[world-model]] 与 agent 规划方向。它是 [[chain-of-thought]] 的进阶替代,可与 self-consistency 等推理方法对比阅读。项目对应开源库 llm-reasoners。
