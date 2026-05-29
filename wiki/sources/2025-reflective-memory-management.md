---
type: source
subtype: paper
tags: [llm-long-term-memory, dialogue-agent, memory-module, retrieval-augmented-generation, reinforcement-learning, personalization]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2503.08026
raw: raw/2503.08026.pdf
authors: [Zhen Tan, Jun Yan, I-Hung Hsu, Rujun Han, Zifeng Wang, Long T. Le, Yiwen Song, Yanfei Chen, Hamid Palangi, George Lee, Anand Iyer, Tianlong Chen, Huan Liu, Chen-Yu Lee, Tomas Pfister]
year: 2025
---

# In Prospect and Retrospect: Reflective Memory Management (RMM)

提出 **Reflective Memory Management (RMM)**,为长期个性化对话 agent 设计一套"前瞻反思 + 回溯反思"的外部记忆机制:用主题(topic)为粒度组织记忆,并用 LLM 引用(attribution)信号在线 RL 地精炼检索,在 LongMemEval 上比无记忆基线提升 10% 以上准确率。

## 问题

[[large-language-models]] 本质上是无状态(stateless)的,无法在跨会话的长期交互中保留并召回相关信息,这限制了它们在需要持续个性化场景(客服、虚拟助手、教育平台等)的效果。已有的外部 [[memory-module]] / [[llm-long-term-memory]] 机制存在两个关键缺陷:

1. **固定记忆粒度**:现有系统按预设边界(turn / session / 时间间隔)切分对话历史,无法对齐对话本身的语义结构(如话题切换),导致记忆碎片化、信息不完整。
2. **固定检索器**:依赖静态 retriever,无法适应不同对话领域与个体用户的交互模式;而为个性化检索器收集标注数据成本高昂,阻碍规模化。

任务形式化为**多会话(multi-session)对话**:agent 跨多个 session 与用户交互,每个 session 由若干 turn(用户 query + agent 回复)组成,agent 仅靠一个外部记忆库存储历史信息,目标是结合当前上下文与检索到的历史生成个性化回复。挑战在于平衡"全面存储"与"精确检索"——无关上下文会干扰 LLM 并降低回复质量。

## 方法

RMM 框架由四个组件构成:**memory bank**(每条记忆是 (topic summary, raw dialogue) 对,topic summary 作为检索 key)、**retriever**、**reranker**(轻量可学习模块)、**LLM**(生成回复 + 反馈信号)。核心是两个互补的反思机制(完整流程见 Algorithm 1):

- **Prospective Reflection(前瞻反思,基于主题的记忆组织)**:在每个 session 结束时执行。先用 LLM 把 session 按不同话题**分解并摘要**(memory extraction),topic 是可跨一个或多个 turn 的语义连贯单元(从细粒度意图到宽泛主题);再对每条抽取记忆检索 Top-K 最相似的已有记忆,由 LLM 决定**直接添加(add)**新话题还是**合并(merge)**到已有记忆中更新。这样记忆库围绕有意义的主题结构组织,摆脱了固定 turn/session 边界。

- **Retrospective Reflection(回溯反思,基于 LLM 引用的检索精炼)**:
  - **Reranker 设计**:对 retriever 返回的 Top-K 记忆 embedding,通过带残差的线性层做 embedding adaptation(q' = q + W_q q),点积算相关性分数,再用 **Gumbel Trick** 做可微的随机采样(加 Gumbel 噪声后 softmax,温度 τ 控制探索)选出 Top-M。Reranker 不改动 retriever 本身,可适配任意预训练检索模型。
  - **LLM Attribution as Rewards**:在生成回复的同一次 LLM 调用中,让 LLM 对上下文中每条记忆生成引用(citation),被引用记为 +1(Useful)、未引用记为 -1(Not Useful),作为奖励信号。citation 在 response 之后生成,比 prior/post-hoc citation 更有效。
  - **Reranker Update**:用 **REINFORCE** 算法以二元奖励在线更新 reranker(Δφ = η·(R−b)·∇log P),无需昂贵的标注数据即可在对话推进中持续适配。

实现:generator 用 **Gemini-1.5-Flash**(并评估 Gemini-1.5-Pro);默认 retriever 为 Contriever,另测 Stella、GTE;无 reranker 时 Top-K=5,有 reranker 时 Top-K=20、Top-M=5。

## 结果

在 **MSC** 与 **LongMemEval** 两个个性化对话基准上评测(MSC 用 METEOR / BERTScore,LongMemEval 用 Recall@5 / Accuracy,3 次平均):

- **主结果(Table 1)**:RMM 全面超越 No History、Long Context、RAG、MemoryBank、LD-Agent 等基线。配 GTE 时 RMM 在 MSC 达 **33.4% METEOR / 57.1% BERT**,在 LongMemEval 达 **69.8% Recall@5 / 70.4% Accuracy**;配 Contriever 也有 61.2% Accuracy,显示鲁棒性。相比之下最强 RAG(GTE)为 27.5 METEOR / 63.6 Acc。摘要所称"比无记忆基线 +10% 以上准确率",对应 No History 在 LongMemEval 为 0.0% Acc。Oracle 检索上限为 100% Recall / 90.2% Acc。
- 记忆对回复质量的贡献:MSC 上 86% 的回复因记忆而改善,LongMemEval 上为 100%。
- **消融(Table 2)**:在 RAG(24.8 METEOR / 54.3 Recall)基础上,+PR(前瞻反思)提升到 28.6 / 57.4;直接 RL 微调 retriever(+RR 无 reranker)反而退化(20.3 / 34.2);加上 reranker(+RR)恢复到 27.5 / 58.8;完整 RMM 达 **30.8 METEOR / 60.4 Recall@5 / 61.2 Acc**(Contriever)。
- **Citation 分数验证(Table 3)**:用 Gemini-1.5-Pro 评判,useful memory 识别的 Precision/Recall/F1 整体为 87.6 / 85.8 / 86.7,证明引用奖励有效。
- **不同 LLM(Table 4)**:Long-Context 设定下 Gemini-1.5-Pro 略优;但在 RMM 下 Gemini-1.5-Flash 反而优于 Pro(可能因更强模型对个人信息更倾向拒答,源于对齐/隐私调优)。
- **粒度与离线预训练分析**:Prospective Reflection 得到的 PR 粒度接近"逐实例最优(best)"oracle 粒度,优于固定 turn/session/mix;少量标注做离线监督预训练(对比学习)可进一步提升 retriever 的 recall 与 accuracy。

论文被 ACL 2025 接收。

## 在本 wiki 中的位置

本文属于 [[llm-long-term-memory]] 与 [[memory-module]] 主题下面向**长期个性化对话 agent** 的工作,与 [[memorybank]](Ebbinghaus 遗忘曲线驱动的记忆更新)、[[siliconfriend]]、[[memory-stream]]、[[agent-memory]] 等记忆机制相关,可视为它们在"自适应粒度 + 在线检索精炼"方向上的改进。方法上结合了 [[retrieval-augmented-generation]] 的检索范式、[[reinforcement-learning]] 的 REINFORCE 在线更新,以及类似 [[reflexion]] / [[self-refine]] 的反思(reflection)思想,但反思对象是**记忆组织与检索器**而非推理链。LLM 引用作为奖励信号与 [[llm-as-judge]] / attribution 评估相关。出自 [[google-deepmind]] 体系的 Google Cloud AI Research(作者含 [[tianlong-chen]]、[[huan-liu]] 等),generator 使用 Gemini-1.5 系列。
