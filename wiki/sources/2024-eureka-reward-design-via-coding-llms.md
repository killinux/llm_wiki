---
type: source
subtype: paper
tags:
  - reward-design
  - reinforcement-learning
  - code-generation
  - llm-agent
  - robotics
  - evolutionary-search
created: 2026-05-29
updated: 2026-05-29
arxiv: "2310.12931"
raw: raw/2310.12931.pdf
authors:
  - Yecheng Jason Ma
  - William Liang
  - Guanzhi Wang
  - De-An Huang
  - Osbert Bastani
  - Dinesh Jayaraman
  - Yuke Zhu
  - Linxi "Jim" Fan
  - Anima Anandkumar
year: 2024
---

# Eureka: Human-level Reward Design via Coding Large Language Models

Eureka 用编码 LLM(GPT-4)零样本生成可执行的奖励函数代码,并结合进化搜索与「奖励反思」迭代改进,在 29 个 RL 环境上达到人类专家级别的奖励设计,首次让模拟 Shadow Hand 学会转笔。

## 问题

奖励函数对 [[reinforcement-learning]] 至关重要,但以难以设计著称:文中引用的一项调查显示 92% 的 RL 研究者/从业者依赖人工试错设计奖励,89% 认为自己设计的奖励是次优的并会导致非预期行为。[[large-language-models]] 已被证明是出色的高层语义规划器,但能否用于学习复杂的低层操控技能(如灵巧的转笔)仍是开放问题——现有方法需要大量领域专家知识来构造任务 prompt,或只能学到简单技能。本文提出一个核心问题:能否用 state-of-the-art 编码 LLM(如 [[gpt-4]])构建一个**通用**的奖励编程算法,在无需任务特定 prompt、无需预定义奖励模板的情况下,自动化繁琐的试错过程,并与人类监督兼容以保证安全与对齐。

## 方法

Eureka(Evolution-driven Universal REward Kit for Agent)由三个算法组件构成:

- **Environment as Context(环境作为上下文)**:直接把未经修改的环境源代码(不含奖励代码)与自然语言任务描述喂给编码 LLM,使其零样本生成可执行的 Python 奖励函数。仅给出极少的通用指令(如要求把各奖励分量以 dictionary 形式暴露出来),无需任务特定的奖励模板或 few-shot 示例。
- **Evolutionary Search(进化搜索)**:每轮从 LLM 独立采样 K 个奖励候选;由于生成是 i.i.d. 的,全部都有 bug 的概率随采样数指数下降(实验中每环境采样 16 个即至少有一个可执行)。然后基于上一轮表现最好的奖励,通过 in-context **reward mutation**(变异 prompt)生成改进版本。变异形式自由,包括修改超参数、改变奖励分量的函数形式、引入新的奖励分量。每环境跑 5 次独立 run,每次搜索 5 个 iteration,K=16。
- **Reward Reflection(奖励反思)**:把策略训练动态用文本总结出来,作为反馈输入 LLM。具体是追踪每个奖励分量及任务 fitness 函数 F 在训练中间检查点的标量值并列出。这弥补了 fitness 函数本身缺乏 credit assignment 信息的问题,使奖励编辑更有针对性。

奖励质量由 fitness 函数 F(任务真实评估指标,可能稀疏)评估;奖励生成问题即输出使 F(策略) 最大化的奖励代码。中间奖励评估借助 IsaacGym 的 GPU 加速分布式 RL,带来最高三个数量级的策略学习加速。整体形式化基于 Singh et al. (2010) 的 Reward Design Problem。

此外 Eureka 还支持一种 gradient-free 的 in-context [[rlhf]]:无需修改算法,可把人类奖励函数当作第一轮输出(Human Init.),或把人类的文本反馈作为 reward reflection 输入(Eureka-HF),从而生成更对齐、更安全的奖励,且无需模型更新。

## 结果

- **环境与基线**:29 个任务、10 种机器人形态,基于 IsaacGym 实现——9 个原始 Isaac 环境 + 20 个 Bidexterous Manipulation(Dexterity)双手操控任务。后端 LLM 用 `gpt-4-0314`。两个 benchmark 都在 GPT-4 知识截止(2021 年 9 月)之后或同期发布。基线包括 L2R(两阶段模板化 prompting)、Human(任务作者手工设计的奖励)、Sparse(即 fitness 函数 F)。策略统一用 PPO 训练。
- **超越人类奖励**:在 Isaac 所有任务上达到或超过人类水平,在 Dexterity 20 个任务中 15 个超过人类。总体在 **83%** 的任务上超过人类专家奖励,平均归一化提升 **52%**。L2R 在低维任务(如 CartPole、BallBalance)与之相当,但在高维任务上明显落后。
- **进化搜索不可或缺**:消融 Eureka w.o. Evolution(32 Samples)在两个 benchmark 上 2 个 iteration 后均被原始 Eureka 超过;Eureka 性能随 iteration 持续提升并最终超过人类。
- **生成新颖奖励**:Eureka 奖励与人类奖励大多弱相关,且任务越难相关性越低;少数情况下甚至负相关却表现显著更好,说明能发现违反人类直觉的奖励设计原则。
- **Reward Reflection 重要性**:去掉 reward reflection(No Reward Reflection)使 Isaac 平均归一化分数下降 **28.6%**,高维任务退化更明显。
- **课程学习实现转笔**:把转笔拆解为子任务,先用 Eureka 奖励预训练定向重定位策略,再 fine-tune 到目标转笔配置。Fine-Tuned 策略能连续转笔多个 cycle,而 from-scratch 与仅预训练(zero-shot)策略一个 cycle 都完不成。首次在模拟拟人五指 Shadow Hand 上实现快速转笔。
- **Eureka from Human Feedback**:Eureka (Human Init.) 在所测 Dexterity 任务上一致优于 Human 与原始 Eureka,说明其 in-context 改进能力与基奖励质量基本无关(支持假设:人类擅长识别相关状态变量,但不擅长用它们设计奖励)。Eureka-HF(纯文本反思)在 Humanoid 任务上被 20 名用户中 **15/20** 偏好(对比原始 Eureka),获得更安全更稳定的步态(尽管前向速度 5.58 略低于 Eureka 的 7.53)。
- GPT-4 换成 GPT-3.5 后性能下降,但在多数 Isaac 任务上仍达到或超过人类水平,表明方法可迁移到不同质量的编码 LLM。

## 在本 wiki 中的位置

这是一篇把 [[code-generation]]、[[large-language-models]] 与 [[reinforcement-learning]] 奖励设计结合的代表性工作,属于「用 LLM 辅助/自动化奖励工程」方向。它与 [[rlhf]] 相关但提出了 gradient-free、无需模型更新的变体。方法上的 [[evolutionary-search]] / reward mutation 与 self-improvement 类 [[llm-agents|llm-agent]](如 [[reflexion]]、[[voyager]])的 in-context 迭代改进思路相通,文中也引用了这些工作作为可行性依据。机构上来自 [[nvidia]]、UPenn、Caltech、UT Austin,作者包括 [[linxi-fan]] 与 [[anima-anandkumar]]。
