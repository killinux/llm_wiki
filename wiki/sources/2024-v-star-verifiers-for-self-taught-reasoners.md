---
type: source
subtype: paper
tags:
  - self-improvement
  - reward-model
  - test-time-compute
  - reasoning
  - code-generation
  - dpo
created: 2026-05-29
updated: 2026-05-29
arxiv: 2402.06457
raw: raw/2402.06457.pdf
authors:
  - Arian Hosseini
  - Xingdi Yuan
  - Nikolay Malkin
  - Aaron Courville
  - Alessandro Sordoni
  - Rishabh Agarwal
year: 2024
---

# V-STaR: Training Verifiers for Self-Taught Reasoners

V-STaR 在 [[self-improvement]] 的迭代过程中**同时利用正确与错误的模型生成解**:用正确解微调 generator,用全部解(含错误解)以 [[direct-preference-optimization]](DPO)训练一个 verifier,在测试时对多个候选解打分排序,从而显著提升 LLM 的数学推理与代码生成表现。

## 问题

诸如 [[star-self-taught-reasoner]](STaR)、[[rejection-sampling-fine-tuning]](RFT)、ReST-EM 这类 [[self-improvement]] 方法,通过在模型自生成的解上迭代 [[fine-tuning]] 来提升问题求解能力。但它们都**只保留正确解、丢弃错误解**——而在困难推理任务上错误解往往占大多数,意味着丢弃了大量可用于学习"对错差异/错误模式"的有价值信息。另一条正交路线是测试时使用学到的 verifier([[reward-model]])对候选解排序选优,以额外的 [[test-time-compute]] 换取更高准确率,但已有 verifier(如 Cobbe 等的 ORM)只从一个固定 generator 采集数据。本文要解决:如何把"被丢弃的错误解"利用起来,迭代地训练出更强的 generator 与 verifier。

## 方法

V-STaR(Verification for Self-Taught Reasoners)的核心是在自我提升的迭代过程中维护两份数据并交替训练 generator 与 verifier:

- **数据采集**:从预训练 LLM Gbase 在原始 DSFT 上微调得到 GSFT;对每个问题采样 k=16 个解,用 ground-truth 答案(数学)或运行 test cases(代码)判定正确性 z。
- **双数据缓冲**:正确解(z=1)加入 generator 数据 DGEN;**正确与错误解都**加入 verifier 数据 DVER(带正确性标签),使 verifier 能从 generator 的错误中学习。
- **迭代**:下一轮用 Gbase 在增广后的 DGEN 上重训得到 Gt,再采样,如此迭代最多 T 轮(实验用 3 轮),逐步获得更优的 generator 与更具挑战性的负例。
- **用 DPO 训 verifier**:把"语言建模 + 二分类"两个目标统一为 offline 偏好学习。将正确解视为 preferred、错误解视为 dispreferred,从 DVER 中正确/错误解的笛卡尔积构造偏好对,以 [[direct-preference-optimization]] 目标(公式 2,β 控制与参考策略 GSFT 的接近度)训练 verifier V。推理时用 V(ŷ|x) 的似然作为打分对候选解排序(Best-of-k)。实验发现 DPO verifier 优于 ORM 风格 verifier。
- **可靠的 Best-of-k 估计**:提出类似 Pass@k 的无偏 Best-of-k 计算公式(公式 3),从固定的 N 个采样中估计 top-1 正确概率,降低方差与成本。

模型:用 [[lora]] 微调 [[llama-2]] 与 CodeLLaMA 的 7B/13B。

## 结果

- **数学推理**:相比 STaR†与 Verification baseline,测试准确率绝对提升 **6%~17%**。
- **代码生成**:绝对提升 **4%~12%**。
- **小模型超越大模型**:7B V-STaR 在 [[gsm8k]] 上超过 base [[llama-2]] 70B(8-shot);在 [[humaneval]] 上接近 CodeLLaMA 34B(zero-shot Pass@1 约 48%),在 [[mbpp]] 上与 CodeLLaMA 34B(zero-shot Pass@1 约 55%)持平。
- **迭代有效**:在同等生成预算下,迭代版优于非迭代 V-STaR[1 Iter]/RFT+Verifier;MBPP 上第 4 轮仅再增 0.3%(收益饱和)。
- **DPO > ORM**:ORM 风格 verifier 在 GSM8K 候选数 >4、MBPP 候选数 >16 时搜索能力明显变差。
- **优于 self-consistency**:在 k≤64 时 V-STaR 排序明显优于多数投票([[self-consistency]]),且可用于代码这类多数投票不适用的任务。
- **指标说明**:generator 报 Pass@1,verifier 方法报 Best-of-64(每题采样 128 个候选)。

评测基准:[[gsm8k]]、[[mbpp]](域内训练),[[math-dataset]] 子集(150 题 Level 1)、[[humaneval]](域外迁移)。

## 在本 wiki 中的位置

V-STaR 处于 [[self-improvement]] / [[star-self-taught-reasoner]] 谱系与 [[test-time-compute]] / verifier 排序两条线的交汇处。相对 [[rejection-sampling-fine-tuning]] 与 [[star-self-taught-reasoner]],它的关键创新是"复用错误解"并以 [[direct-preference-optimization]] 取代 Cobbe 等的 [[outcome-reward-model]](ORM)来训练 verifier。它与 [[process-reward-model]] / [[outcome-supervision]] 的 verifier 路线相关,也与 [[self-consistency]] 作为测试时计算策略形成对比。作者来自 [[mila]]、[[microsoft-research]]、University of Edinburgh 与 [[google-deepmind]]。
