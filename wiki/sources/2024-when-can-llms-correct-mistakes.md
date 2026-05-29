---
type: source
subtype: paper
tags: [self-correction, self-refine, llm-reasoning, survey, feedback, intrinsic-self-correction, external-tools, fine-tuning]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2406.01297
raw: raw/2406.01297.pdf
authors: [Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang]
year: 2024
---

# When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs

一篇关于 LLM [[self-correction]] 的批判性综述:通过细分研究问题并提出实验检查清单,论证 LLM 仅凭自身能力在一般任务上无法可靠地自我纠错,瓶颈在于反馈(feedback)生成。

## 问题

[[self-correction]](自我纠错)指 LLM 在推理(inference)阶段用 LLM 自身来 refine(修正)其响应,反馈来源可以是自我评估、外部工具/知识或 fine-tuning。学界对"LLM 能否纠正自己的错误"无共识:既有正面结果([[self-refine]]、RCI),也有大量负面结果(Huang et al. 2024a、[[critic]] 等)。

作者指出冲突的根源在于:(1) 先前工作往往不精确定义研究问题;(2) 使用了不切实际(unrealistic)或不公平(unfair)的框架;(3) 过度评价(over-evaluate)自我纠错。

论文把研究问题细分为三类:
- RQ1:LLM 能否**仅凭自身固有能力**纠正其 best-possible 初始响应?(对应 intrinsic self-correction)
- RQ2:LLM 能否**借助外部信息**纠正其 best-possible 初始响应?
- RQ3:自我纠错的最终输出是否**优于其他方法**?

## 方法

把自我纠错框架分解为三阶段:初始响应生成、feedback 生成、refinement。并提出新的框架分类法:

- **Realistic vs. Unrealistic**:是否可在真实应用中实现。使用 oracle 信息(如 ground-truth 答案作停止条件,见 RCI、[[reflexion]])的属于 unrealistic,无法验证任何 RQ。
- **Fair vs. Unfair**(在 realistic 之下):是否使用 best-possible 初始响应。"best-possible" 指用上自我纠错模块能访问的全部信息(外部工具/知识/fine-tuning)以最大努力生成的初始响应。
  - Fair-symmetric:[[intrinsic-self-correction]],初始与纠错用同模型同信息。
  - Fair-asymmetric:用额外信息纠错,但也尽量改进初始生成(如用 code interpreter 的 [[critic]]、[[code-execution]] 方法)。
  - Unfair:实用但用了次优初始响应(如仅在纠错阶段用 search engine 而不改进初始生成的 RARR;detoxification 中故意让初始生成不避免有害内容的 [[constitutional-ai]] CAI Revisions、[[self-refine]])。

作者用该分类法逐一审查 RQ1(prompting,§4)、RQ2(外部工具/知识 §5.1、fine-tuning §5.2)、RQ3(强基线 §6),并给出验证各 RQ 所需的实验要求(Table 3/7)与报告负面结果的检查清单(Table 8)。

## 结果

- **RQ1(intrinsic self-correction)**:**没有任何先前工作**证明在一般任务上、仅凭 prompting 生成的反馈能在 fair 设置下成功自我纠错。审查发现这些工作要么用 oracle 信息(unrealistic),要么用弱 prompt 改进初始生成(unfair),从而过度评价。例外:具有 **decomposable responses**(可分解响应)等特殊性质的任务(如 CoVe 验证"列举在纽约出生的政治家")中,intrinsic self-correction 有效,因为验证明显比生成容易。
- **RQ2(外部信息)**:当存在可靠 external feedback 时自我纠错有效(如 code generation 用 code interpreter、可验证任务用 [[tree-of-thoughts]] 式的 generate-and-rank)。Fine-tuning 在**大规模训练数据(常 >100K 标注)**可用时使自我纠错奏效(SelFee、Volcano、[[self-critique]]、REFINER、Self-Edit 等,见 Table 6),但小训练数据下尚未被探索。
- **RQ3(强基线)**:自我纠错常未与足够强的基线([[self-consistency]]、generate-and-rank、pass@k)在可比计算成本下比较,因此能否优于其他方法仍不清楚。
- **核心结论**:**瓶颈在 feedback 生成**。"recognizing errors is easier than avoiding them"(识别错误比避免错误容易)这一假设只对验证极易的任务成立。建议研究直接评估反馈质量(如 error detection accuracy),而非只看 refine 后的下游性能。
- §12 补充 2024 年 6 月后趋势:RL 训练的自我纠错与 [[openai]] o1(用 RL 探索策略、识别并修正自身推理)在 Math Olympiad、竞赛编程等推理任务上超越 SOTA LLM。

涉及任务/benchmark:[[gsm8k]]、[[svamp]]、[[hotpotqa]]、[[mmlu]]、MT-Bench、MiniWoB++、CSQA、detoxification、code generation 等。

## 在本 wiki 中的位置

本文是 [[self-correction]] / [[self-refine]] / [[self-reflection]] 主题的批判性综述与方法论框架,为评估 [[intrinsic-self-correction]]、[[reflexion]]、[[critic]]、[[constitutional-ai]] 等具体方法提供了"fair/unfair/realistic"判定标准。它与 [[test-time-compute]]、[[self-consistency]]、[[process-reward-model]] / [[outcome-reward-model]] 等 inference-time 推理增强方向相关,并把 [[rlhf]] / [[rlaif]] 式 fine-tuning 反馈纳入自我纠错谱系。对理解 [[large-language-models]] 的 [[reasoning]] 能力边界与 [[hallucination]] 的 [[self-critique]] 缓解很有参考价值。作者来自 [[stanford-university]] 之外的 Penn State University 与 University of Illinois Urbana-Champaign(含 [[jiawei-han]])。
