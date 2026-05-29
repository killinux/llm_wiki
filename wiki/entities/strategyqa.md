---
type: entity
subtype: benchmark
tags: [benchmark, reasoning, multi-hop, question-answering]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# StrategyQA

StrategyQA 是一个隐式多步推理(multi-hop / implicit reasoning)问答基准,要求模型对开放域问题进行分解并完成多步推理后给出判断式(是/否)答案。

## 在本 wiki 中的出现

- [[2022-chain-of-thought]]:将 StrategyQA 作为评测 chain-of-thought prompting 多步推理能力的常识/隐式推理任务之一。该工作提出在 few-shot 示例中加入中间推理步骤,显著提升大模型的多步推理表现,且增益随模型规模涌现。
- [[2023-plan-and-solve-prompting]]:将 StrategyQA 列入零样本推理评测任务之一,用以验证 Plan-and-Solve (PS/PS+) 提示相对 Zero-shot-CoT 在多步推理上的改进。
- [[2023-fireact-language-agent-fine-tuning]]:提出用多任务、多 prompting 方法(ReAct/CoT/Reflexion)生成的轨迹微调 backbone LM 来构建语言智能体,在性能、鲁棒性、泛化与成本上全面优于 few-shot prompting。

## 相关

- [[chain-of-thought|chain-of-thought-prompting]]
- [[plan-and-solve-prompting]]
- [[multi-hop-reasoning]]
- [[gsm8k]]
- [[zero-shot-cot]]
- [[react]]
- [[reflexion]]
- [[language-agent]]
