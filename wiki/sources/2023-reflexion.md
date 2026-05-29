---
type: source
subtype: paper
tags: [llm, agents, reinforcement-learning, reasoning, self-reflection, prompting]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2303.11366
raw: raw/2303.11366.pdf
authors: [Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao]
year: 2023
---

Reflexion 提出一种用**语言反馈**而非权重更新来强化语言智能体的框架:智能体在每次试验失败后,把环境反馈转化为自我反思的文字,存入记忆,用于改进下一次尝试。

## 问题

传统强化学习需要大量训练样本和昂贵的模型微调来让智能体从试错中学习,这对大语言模型(LLM)既不现实也不高效。能否让 LLM agent 在不更新参数的前提下,从过去失败中"吸取教训"并在后续尝试中表现更好?这要求把稀疏(常常只有成功/失败)的反馈信号转化为对下一次决策有指导意义的信息。

## 方法

Reflexion 将策略优化建模为**语言**层面的自我改进,核心由三个模型组成:

- **Actor(行动者)**:基于 LLM,根据当前状态与记忆生成动作/文本,可采用 [[chain-of-thought]] 或 [[react]] 等方式。
- **Evaluator(评估者)**:对 Actor 产生的轨迹打分,反馈可来自任务自带的成功信号、启发式规则,或 LLM 自身判断。
- **Self-Reflection(自我反思)模型**:这是关键创新——把标量奖励 + 轨迹转化为具体的、口头的(verbal)反思文本,例如分析失败原因并提出下次改进策略。

反思文本被写入**长期记忆**,在下一次试验时与任务一起作为上下文提供给 Actor,从而在多轮试验间实现"语言强化学习"(verbal reinforcement),无需任何梯度更新或微调。框架对决策、推理、编程等不同任务类型通用,只需调整反馈与记忆形式。

## 结果

- **决策任务([[alfworld]])**:在 134 个任务上,Reflexion 将 [[react]] 基线的成功率从 75% 提升到 **130/134 ≈ 97%**(论文报告绝对提升约 22 个百分点)。
- **推理任务([[hotpotqa]])**:相比强基线提升约 **20%**。
- **编程任务([[humaneval]])**:在 Python 代码生成上达到 **91% pass@1**,超过当时 [[gpt-4]] 的 80%,刷新 SOTA;并在 [[mbpp]] 等多种编程基准上验证有效。论文还引入 LeetcodeHardGym 等更难的编程评测。
- 消融实验表明自我反思记忆是性能提升的主因;实验主要基于 [[gpt-3-5]] / [[gpt-4]] 等模型。

## 在本 wiki 中的位置

Reflexion 是 LLM agent 自我改进方向的代表性工作,与 [[react]](行动+推理)互补:ReAct 解决单次试验内的推理-行动交错,Reflexion 在**试验之间**通过语言反馈迭代改进。它体现了"用自然语言代替梯度做强化学习"的思路,与 [[chain-of-thought]]、self-refine 类自我修正方法相关,是理解 [[llm-agents|llm-agent]] 记忆与反思机制的核心论文之一。
