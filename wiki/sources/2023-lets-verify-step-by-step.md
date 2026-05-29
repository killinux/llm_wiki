---
type: source
subtype: paper
tags:
  - process-supervision
  - reward-model
  - reasoning
  - math
  - alignment
created: 2026-05-29
updated: 2026-05-29
arxiv: "2305.20050"
raw: raw/2305.20050.pdf
authors:
  - Hunter Lightman
  - Vineet Kosaraju
  - Yura Burda
  - Harri Edwards
  - Bowen Baker
  - Teddy Lee
  - Jan Leike
  - John Schulman
  - Ilya Sutskever
  - Karl Cobbe
year: 2023
---

OpenAI 的这篇论文系统比较了「过程监督」(process supervision)与「结果监督」(outcome supervision)两种训练奖励模型的方式,证明在多步数学推理上,逐步奖励模型(PRM)显著优于只看最终答案的结果奖励模型(ORM),并开源了人工标注的步骤级数据集 PRM800K。

## 问题

让大语言模型做多步推理时,模型经常出现「逻辑链错误但最终蒙对答案」或「中途某一步出错导致全盘皆错」的情况。传统训练奖励模型/验证器(verifier)的方式是 [[outcome-supervision]]:只根据最终答案是否正确给整条解题轨迹一个标签。这种 [[outcome-supervision]] 信号稀疏,且会奖励到那些「过程错误但答案碰巧正确」的解法,难以引导模型形成可靠的推理链。

本文要回答的核心问题是:相比只监督最终结果,逐步监督推理过程的每一步([[process-supervision]])能否训练出更强、更可靠的奖励模型,从而在数学推理任务上选出更好的解?

## 方法

- 在 [[gpt-4]] 系列基座之上训练两类奖励模型:
  - [[outcome-reward-model]](ORM):仅用最终答案对错作为监督信号。
  - [[process-reward-model]](PRM):对解题过程中的每一步分别给出「正确 / 错误 / 中性」的人工标签,奖励模型学会逐步打分。
- 评测协议采用 best-of-N:对每道题采样 N 条候选解,用奖励模型对每条解打分并选出最优解,比较两类奖励模型选出正确解的能力。对 PRM,整条解的分数由各步骤分数聚合得到。
- 为支撑大规模过程监督,作者收集并开源了 [[prm800k]] 数据集:包含约 80 万条针对 [[math-benchmark]] 题目解题步骤的人工正确性标注。
- 还探讨了「主动学习」式的数据收集策略,优先标注模型容易出错、信息量更大的解题轨迹,以提升标注效率。

## 结果

- 在 [[math-benchmark]] 代表性测试子集(500 题)上做 best-of-1860 选解:PRM 解出 **78.2%**,显著高于 ORM 的 72.4% 和多数投票(majority voting)的 69.6%。随着候选数 N 增大,PRM 相对 ORM 与多数投票的优势进一步拉大。
- 主动学习(active learning)使过程监督的数据效率提升约 **2.6 倍**:优先向标注者展示「看似可信但答案错误」(convincing wrong-answer)的解,标注信息量更大。
- 小规模直接对比(用大 PRM 作为标注预言机监督小模型)显示:在数据规模相同时,过程监督在所有规模下都优于两种结果监督(final-answer checking 与用 PRM_large 做结果监督)。这澄清了与 Uesato et al. (2022) 「两者表现相近」结论的表面冲突——差异主要来自监督规模。
- 分布外(OOD)泛化:在 224 道较新的 STEM 考试题(AP Calculus / AP Chemistry / AP Physics / AMC10/12)上做 best-of-100,PRM 聚合达到 **72.9%**,优于 ORM 的 63.8% 和多数投票的 61.3%,表明 PRM 能容忍一定分布偏移。
- 论文据此提出过程监督带来「负的对齐税」(negative alignment tax):更安全、更可解释的监督方式同时性能更强。
- 作者将完整步骤级标注数据 [[prm800k]](约 80 万标签、覆盖 1.2 万题的 7.5 万条解)开源,以促进相关研究。

## 在本 wiki 中的位置

本文是 [[process-supervision]] 路线的奠基性工作,把奖励建模的粒度从「结果」推进到「过程」,与 [[rlhf]] 中的奖励模型训练、以及后续的推理增强方法(如借助 verifier 的 best-of-N、self-consistency)密切相关。它对 [[reasoning]] 与 [[ai-alignment]] 都有影响:既是提升 LLM 数学/推理能力的实用手段,也是「让监督信号更细粒度、更可解释」这一对齐思路的代表。开源的 [[prm800k]] 与 [[math-benchmark]] 一起构成了研究过程奖励模型(PRM)的重要基础设施。
