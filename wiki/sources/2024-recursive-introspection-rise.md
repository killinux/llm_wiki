---
type: source
subtype: paper
tags:
  - self-improvement
  - self-correction
  - test-time-compute
  - reinforcement-learning
  - math-reasoning
  - fine-tuning
created: 2026-05-29
updated: 2026-05-29
arxiv: "2407.18219"
raw: raw/2407.18219.pdf
authors:
  - Yuxiao Qu
  - Tianjun Zhang
  - Naman Garg
  - Aviral Kumar
year: 2024
---

# Recursive Introspection: Teaching Language Model Agents How to Self-Improve

通过把单轮问题建模为多轮 MDP 并用 reward-weighted regression 做迭代微调,RISE 让 7B 级 LLM 学会在没有外部反馈的情况下跨多轮递归地反思并修正自己的答案。

## 问题

智能体的一个核心能力是 [[self-correction]]:在多轮交互中能反思自己的推理、发现并改正错误,并随着更多 [[test-time-compute]] 的投入持续提升答案质量。然而即便是最强的专有 [[large-language-models]],也几乎不具备这种顺序自我改进的能力——哪怕被明确告知自己出错了。

先前工作多依赖 prompting 让模型自我批判与修订(如 [[self-refine]]、[[self-critique]]、[[reflexion]]),但多项研究表明:在缺乏外部反馈(verifier、编译器或人类)时,LLM 无法有意义地对推理错误进行 [[self-correction]],强行 prompting 自纠反而常常降低性能。本文据此提出疑问:能否通过**训练**而非 prompting,让模型仅利用自身前几轮输出就实现跨轮自我改进?

## 方法

作者提出 **RISE (Recursive IntroSpEction)**,一种赋予模型多轮顺序自我改进能力的微调方法,包含两大组件:

- **将单轮问题转为多轮 MDP**:给定 prompt 数据集 `D = {(xᵢ, yᵢ*)}`,初始状态即 prompt `x`,动作是模型的回答,下一状态拼接 prompt、上一轮回答与一条固定的"反思并重试"指令,reward 是答案正确性 `r(x, ŷ) ∈ {0,1}`(对照 oracle 答案),horizon 固定为最大轮数。该构造借鉴了 online imitation learning 与 [[reinforcement-learning]] 的思想。

- **多轮 rollout 数据收集**:对每个 prompt 滚动 k 轮,轮间插入反思指令,每轮采样 N 个候选回答。监督目标有两种构造方式:
  - **Distillation**:用更强的 teacher 模型(如 [[gpt-3-5]])在已见失败尝试的上下文下给出正确回答。
  - **Self-distillation**:从模型自身采样 N 个回答,取其中最好的(若有正确者)作为监督目标,无需更强 teacher,可从模型自身 bootstrap 出该能力。

- **策略改进**:用 **reward-weighted regression (RWR)** 在收集的多轮数据上微调,按指数化 reward 加权,上调成功回答、下调失败回答。整个过程可迭代多轮(用最新模型重新收集数据再训练)。

- **推理**:两种模式——带 oracle(由环境判断是否在某轮已得到正确答案而终止);不带 oracle(固定轮数后用 [[self-consistency]] / majority voting 聚合各轮答案)。

## 结果

在数学推理 benchmark [[gsm8k]] 与 [[math-dataset]] 上,以 [[llama-2]]-7B、[[llama-3]]-8B、Mistral-7B 为 base 模型评测:

- **主结果(GSM8K,5 轮 introspection)**:RISE 让 LLaMa3-8B 提升 8.2%、Mistral-7B 提升 6.6%(全部仅用自身数据);LLaMa2-7B 提升 17.7%(超过第一轮的 parallel sampling),Mistral-7B 提升 23.9%。对比之下 [[gpt-3-5]] 自身在 5 轮内仅提升 4.6%。base/instruction-tuned 模型顺序运行多轮往往不升反降,RISE 则呈单调上升。
- **主结果(MATH,5 轮)**:RISE 让 LLaMa2-7B 提升 4.6%、Mistral-7B 提升 11.1%。
- **对比 prompting 自纠**:即便 [[gpt-3-5]] 与 [[gpt-4]] 被 prompt 做自纠(intrinsic self-correction),也无法表现出 RISE 训练模型那样稳定的顺序提升;RISE 的 7B 模型在等量推理算力下优于自身的 [[self-refine]] 基线与标准单轮微调基线。
- **对比并行采样**:在匹配推理预算下,RISE 的顺序多轮改进 + majority voting 优于第一轮抽取等量 i.i.d. 样本(best-of-N / maj@N),说明顺序自纠带来的收益超出单纯多采样。
- **OOD 泛化**:在 GSM8K 上用 RISE 训练可迁移到 [[svamp]] 等数据集的提升。
- **迭代效果**:多轮迭代微调进一步增强自改进行为,但收益递减。
- **不损单轮能力**:RISE 不显著降低 1 轮性能,即多轮能力的获得未以牺牲原始单轮能力为代价。

## 在本 wiki 中的位置

RISE 属于 LLM **self-improvement / self-correction** 与 **test-time scaling** 的交叉方向。与依赖 prompting 的 [[self-refine]]、[[reflexion]]、[[self-critique]] 不同,它通过 [[fine-tuning]] 把自纠能力**内化**进模型权重;与 [[self-consistency]]、best-of-N 等并行扩展 [[test-time-compute]] 的方法不同,它强调**顺序**修订。方法论上把单轮 prompt 建模为多轮 [[markov-decision-process]] 并用类 [[reinforcement-learning]] 的 reward-weighted regression 训练,是 [[self-improvement]] 与 [[reasoning]] 研究的代表性工作之一。作者 Aviral Kumar 等来自 [[carnegie-mellon-university]] 与 UC Berkeley。
