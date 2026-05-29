---
type: source
subtype: paper
tags: [multi-agent, debate, reasoning, self-reflection, llm, machine-translation]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2305.19118
raw: raw/2305.19118.pdf
authors: [Tian Liang, Zhirui Huang, Yuxuan Wang, Zhangyin Feng, Yujia Zhou, Fandong Meng, Jie Zhou, Shuming Shi, Zhaopeng Tu]
year: 2023
---

提出 Multi-Agent Debate(MAD)框架,让多个 LLM 智能体以"针锋相对"(tit-for-tat)方式辩论、由一个裁判管理流程并给出最终答案,以缓解自我反思中的 Degeneration-of-Thought(DoT)问题、激发发散性思维。

## 问题

像 [[chatgpt]] 这样的现代 LLM 在很多任务上表现出色,但常常依赖 [[chain-of-thought]](CoT)推理,容易产生不忠实的推理步骤、被虚假特征干扰。近期工作(如 Self-Refine、Reflexion)用 [[self-reflection]](自我反思)让模型回看自己的答案再改进。

作者指出自我反思存在 **Degeneration-of-Thought(DoT,思维退化)** 问题:当模型对自己最初的(可能错误的)答案过于自信时,仅靠反思自己之前的回答无法产生真正新颖的想法,会陷入固化的思路而难以纠错。需要一种机制来打破单一智能体的思维定势,引入"发散性思维"。

## 方法

提出 **Multi-Agent Debate(MAD)** 框架,核心由三种角色构成:

- **多个辩论者(debaters)**:多个 LLM 智能体针对同一问题给出各自的论点,并以"针锋相对"(tit-for-tat)的方式互相反驳、提出不同观点,从而引入分歧与发散性思维。
- **裁判(judge)**:管理整个辩论过程。裁判在每一轮判断辩论是否已达成一致(YES/NO);若未达成则继续辩论,最终由裁判从辩论历史中抽取/裁定出最终解。
- **可调节的发散度**:通过设计辩论流程,框架可以在"过度发散"与"过快收敛"之间取得平衡。

关键观察:让来自**不同 LLM** 的裁判参与时,得到正确答案的概率更高;较弱的辩论者搭配强裁判(如 [[gpt-4]])即可显著提升效果。

## 结果

在两个有挑战性的任务上验证:**Commonsense Machine Translation(Common MT,常识机器翻译)** 与 **Counter-Intuitive Arithmetic Reasoning(CA,反直觉算术推理)**。

- MAD 优于已有的自我反思方法,作者将其归因于 MAD 鼓励的发散性思维。
- 当裁判与辩论者来自不同 LLM 时,得到正确答案的概率更高。
- **标志性结果**:在 Common MT 任务上,借助强裁判([[gpt-4]]),较小的 [[vicuna]](Vicuna-13B)可以比 [[gpt-3-5-turbo]] 高出 **6.0%**。
- Common MT 上的 Direct 基线为 ACC 50、BLEU 22.3、COMET 81.0;CA 上的 Direct 基线 ACC 12.0(MAD 在这些指标上带来一致提升)。

作者开源了代码与两份资源(Common MT、CA 数据集),仓库为 Multi-Agents-Debate。

## 在本 wiki 中的位置

本文是 [[multi-agent-debate]] 这一推理增强范式的代表作之一,与 [[self-reflection]] / [[self-refine]]、[[chain-of-thought]] 同属"让 LLM 通过额外推理结构提升正确率"的方向。它由 [[tencent-ai-lab]] 与 [[tsinghua-university]] 合作完成,实验中使用了 [[gpt-4]]、[[gpt-3-5-turbo]]、[[chatgpt]] 与 [[vicuna]] 等模型,可与同期 Du 等人的 multiagent debate 工作对照阅读。
