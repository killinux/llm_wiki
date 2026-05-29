---
type: concept
subtype: method
tags: [verifier, reasoning, test-time-compute, reward-model, evaluation]
created: 2026-05-29
updated: 2026-05-29
sources:
  - "[[2023-lets-verify-step-by-step]]"
  - "[[2024-v-star-verifiers-for-self-taught-reasoners]]"
  - "[[2024-compute-optimal-inference]]"
---

# 验证器 (Verifier)

验证器是一个独立于生成器(generator)的模型,用于判断 LLM 生成的候选解(及其推理过程)是否正确,并据此对多个候选进行打分、排序或筛选。

## 概述

在推理任务中,LLM 的单次采样往往不可靠,但其正确答案常常已存在于多个采样之中。验证器的作用是把"生成"与"判断"解耦:让生成器负责产生多样化的候选解,再由验证器评估每个候选的正确性,从而从中选出最优答案。验证器既可以是只看最终结果的结果型(outcome verifier),也可以是逐步评估推理链中每一步的过程型(process verifier);实现上常等同于一个 [[reward-model]],推理时通过 best-of-N 或加权投票来选解。它是 [[test-time-compute]] 扩展的核心组件:更强的验证器能在不改动生成器的前提下显著提升整体准确率。

## 在本 wiki 中的出现

- [[2023-lets-verify-step-by-step]]:把训练验证器(verifier)的奖励建模粒度从"结果"推进到"过程"。该工作对比了只看最终答案的结果监督(得到 [[outcome-reward-model]] 式验证器)与对推理链逐步打标的过程监督(得到 [[process-reward-model]] 式验证器),发现在 best-of-N 选解中,过程监督训练出的验证器更可靠,是本 wiki 中该概念最核心的奠基来源,并开源了步骤级数据集 PRM800K。
- [[2024-v-star-verifiers-for-self-taught-reasoners]]:在 [[star-self-taught-reasoner]] 的自训练流程之上引入验证器(标题即 "Training Verifiers")。它不仅用自生成的正确解微调生成器,还把通常被丢弃的错误解与正确解配对、用 [[direct-preference-optimization]] 训练验证器;推理时以验证器的似然 V(ŷ|x) 对多个候选打分排序(Best-of-k),并指出 DPO 风格验证器优于 Cobbe 等的 ORM 风格验证器。
- [[2024-compute-optimal-inference]]:把验证器置于测试时算力分配的框架中考察。它证明在没有 oracle verifier 时,单纯采样的 majority/weighted voting 准确率会收敛到由模型输出分布与 reward model 决定的上限(diminishing returns),从而论证需要更强的验证器与搜索算法(如其提出的 REBASE,用 [[process-reward-model]] 引导树搜索)来实现计算最优推理。

## 相关

- [[process-reward-model]]:逐步打分的过程型验证器实现。
- [[outcome-reward-model]]:只评估最终结果的结果型验证器实现。
- [[reward-model]]:验证器在概念上与奖励模型高度重叠,常以奖励模型形式实现。
- [[process-supervision]] / [[outcome-supervision]]:训练验证器所用的两类监督信号。
- [[test-time-compute]]:验证器是测试时扩展中分配额外算力(best-of-N、引导搜索)的主要载体。
- [[self-consistency]]:不训练独立验证器、改用多数投票筛选答案的替代路线。
- [[self-verification]] / [[llm-as-judge]]:让模型自身或另一 LLM 充当验证器的相关范式。
- [[critic]]:与验证器相邻的"指出错误"式评审范式。
- [[rejection-sampling-fine-tuning]]:用验证器筛选出的正确样本回灌训练生成器。
- [[tree-search]] / [[monte-carlo-tree-search]]:用验证器分数引导搜索方向的推理策略。
