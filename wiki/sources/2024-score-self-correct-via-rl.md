---
type: source
subtype: paper
tags:
  - self-correction
  - reinforcement-learning
  - reasoning
  - large-language-models
created: 2026-05-29
updated: 2026-05-29
arxiv: "2409.12917"
raw: raw/2409.12917.pdf
authors:
  - Aviral Kumar
  - Vincent Zhuang
  - Rishabh Agarwal
  - Yi Su
  - John D. Co-Reyes
  - Avi Singh
  - Kate Baumli
  - Shariq Iqbal
  - Colton Bishop
  - Rebecca Roelofs
  - Lei M. Zhang
  - Kay McKinney
  - Disha Shrivastava
  - Cosmin Paduraru
  - George Tucker
  - Doina Precup
  - Feryal Behbahani
  - Aleksandra Faust
year: 2024
---

# SCoRe:通过多轮在线强化学习训练 LLM 自我纠错

SCoRe(Self-Correction via Reinforcement Learning)是 [[google-deepmind]] 提出的方法,用完全自生成数据的多轮在线 [[reinforcement-learning]] 训练单个模型,使其无需外部反馈即可显著提升内在 [[self-correction]] 能力。

## 问题

[[large-language-models]] 在被要求 [[intrinsic-self-correction]](即仅凭模型自身、不依赖外部反馈或验证器去修正自己的回答)时表现很差,常常无法改善甚至会把正确答案改错。

作者发现,先前依赖监督微调(SFT)的自我纠错方案存在两类根本缺陷:
- **分布偏移(distribution shift)**:在离线/他人生成的纠错轨迹上做 SFT,训练分布与模型自身在测试时产生的回答分布不匹配。
- **行为坍缩(behavior collapse)**:SFT 容易让模型学到一种"最小编辑"的偏好——第二轮几乎照抄第一轮答案(即对第一轮答案几乎不做修改),从而学不到真正的纠错行为。

核心目标是只用模型自生成的数据,训练出在第二轮真正能把错误答案改对、同时不破坏已正确答案的能力。

## 方法

SCoRe 把自我纠错建模为一个多轮 [[markov-decision-process]],用在线 [[reinforcement-learning]]([[ppo]] 风格的策略梯度)在模型自己生成的轨迹上训练,分两个阶段:

- **阶段一(Stage I,初始化)**:针对第二轮(纠错后)的回答做 RL 优化以最大化正确率,同时用 KL 约束把第一轮回答拉近基座模型的分布(即让第一轮基本不变),目的是先得到一个"第二轮会做出实质性修改"的良好初始化策略,缓解行为坍缩。
- **阶段二(Stage II,多轮 RL + reward shaping)**:对两轮联合做多轮 RL,并加入**奖励塑形(reward shaping)**奖励项,显式激励"从第一轮到第二轮发生正向改变"——对把错答案改对的行为给予额外奖励、对把对答案改错的行为施加惩罚,从而引导模型学到非平凡(non-trivial)的自我纠错策略,而非退化为不修改。

整个流程不使用任何外部反馈、外部验证器或多模型,仅靠单个模型的自生成数据训练。

## 结果

数学任务用 [[gemini]] 1.5 Flash、代码任务用 Gemini 1.0 Pro 微调评测:

- 在 [[math-dataset]](MATH,在 MATH500 上报告)推理基准上,SCoRe 将基座模型的内在自我纠错能力提升了 **15.6%**(绝对值)。具体地(Table 2):Acc@t1 从 52.6% 提到 **60.0%**,Acc@t2 从 41.4% 提到 **64.4%**,自我纠错增量 Δ(t1,t2) 从基座的 **-11.2%** 变为 **+4.4%**(首个显著为正的内在自我纠错结果)。把错答案改对的比例(Δ^{i→c})从 4.6% 升到 5.8%,把对答案改错的比例(Δ^{c→i})从 15.8% 降到 1.4%。
- 在 [[humaneval]] 代码生成基准上,内在自我纠错增量 Δ(t1,t2) 达 **12.2%**(Table 3),比基座(3.0%)高约 9.1%(虽只在 MBPP 上训练却能泛化到 HumanEval)。Acc@t2 达 **64.6%**。在离线修复任务 MBPP-R 上从 47.3% 提升到 **60.6%**,接近 GPT-3.5(43%)与 GPT-4(63.2%)之间的水平。
- 对比基线:Self-Refine、STaR、Pair-SFT 在 MATH 上的 Δ(t1,t2) 分别为 -1.0%、0.4%、1.8%,均接近零或为负(把答案越改越差),验证了先前 SFT/提示方法无法实现真正的内在自我纠错。
- 推理时计算扩展([[test-time-compute]]):在每题 32 个样本预算下,纯并行采样([[self-consistency]])带来 7.4% 增益,而把部分预算用于顺序自我纠错可达 10.5% 增益。
- 消融实验(Table 4)表明:去掉多轮训练 Δ(t1,t2) 变为 -2.4%;去掉 Stage I 降到 2.2%;去掉奖励塑形降到 2.6%;Stage II 用 STaR 代替 REINFORCE 降到 2.2%——两阶段训练、奖励塑形以及在线(on-policy)RL 各自都对避免行为坍缩、获得真正纠错收益至关重要。

## 在本 wiki 中的位置

本文属于用 [[reinforcement-learning]] 提升 LLM [[reasoning]] 与 [[self-correction]] 的方向,可与基于提示/迭代精炼的方法如 [[self-refine]]、[[reflexion]]、[[self-consistency]] 对照——SCoRe 强调的是用 RL 把纠错能力直接训进权重,而非靠推理时提示。它也与 [[star-self-taught-reasoner]]、[[rejection-sampling-fine-tuning]] 等自生成数据训练范式相关,并与 [[process-reward-model]] / [[outcome-reward-model]] 及 [[test-time-compute]] 等 [[test-time-scaling]] 工作互补。
