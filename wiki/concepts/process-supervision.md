---
type: concept
subtype: method
tags: [process-supervision, reward-model, reasoning, math, alignment]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# 过程监督

过程监督(process supervision)是一种对推理过程中的每一步给予反馈的训练/评估方法,与只对最终结果给予反馈的结果监督(outcome supervision)相对,常用于训练步骤级奖励模型(Process Reward Model, PRM)。

## 在本 wiki 中的出现

- [[2023-lets-verify-step-by-step]]:OpenAI 在该工作中系统性地比较了过程监督与结果监督,证明过程监督训练出的 PRM 在 MATH 多步数学推理上显著优于结果监督训练的 ORM,best-of-N 选择下达到 78.2% 的求解率,并开源了步骤级人工标注数据集 PRM800K。
- [[2024-quiet-star]]:Quiet-STaR 让语言模型在每个 token 前生成隐式 rationale 来更好预测后续文本,以自监督方式从任意文本学会推理,zero-shot 提升 GSM8K(5.9%→10.9%)与 CommonsenseQA(36.3%→47.2%)。

## 相关

- [[process-reward-model]]
- [[outcome-supervision]]
- [[outcome-reward-model]]
- [[prm800k]]
- [[best-of-n]]
- [[chain-of-thought]]
- [[math-benchmark]]
- [[reward-model]]
- [[rlhf]]
