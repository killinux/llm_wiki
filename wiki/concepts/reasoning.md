---
type: concept
subtype: method
tags: [reasoning, reasoning-chain, math, supervision]
created: 2026-05-29
updated: 2026-05-29
sources: 13
---

# 推理

推理(reasoning)指模型在得出最终答案前进行的多步中间思考过程,常体现为分步骤地分解、计算并求解复杂问题(如多步数学题)。

## 在本 wiki 中的出现

- [[2023-lets-verify-step-by-step]]:该工作聚焦于多步数学推理任务(MATH 数据集)。OpenAI 证明了过程监督(process supervision,PRM)在多步推理上显著优于结果监督(outcome supervision,ORM)——通过对推理链中的每一步给予奖励信号,best-of-N 选择达到 78.2% 的准确率。论文还开源了步骤级标注数据集 PRM800K,用于训练能够评估推理过程每一步正确性的奖励模型。在此,推理是被监督与验证的核心对象:监督的颗粒度从"最终结果"细化到"推理的每一步"。
- [[2023-chain-of-verification]]:Chain-of-Verification (CoVe) 让 LLM 先生成草稿,再独立回答自我规划的验证问题来核查事实,显著降低幻觉。
- [[2023-llms-cannot-self-correct-reasoning-yet]]:本文证明在无外部反馈的"内在自我纠正"设定下,LLM 无法纠正自身推理错误,性能反而往往下降。
- [[2024-quiet-star]]:Quiet-STaR 让语言模型在每个 token 前生成隐式 rationale 来更好预测后续文本,以自监督方式从任意文本学会推理,zero-shot 提升 GSM8K(5.9%→10.9%)与 CommonsenseQA(36.3%→47.2%)。
- [[2024-self-reflection-llm-agents]]:在 9 个 LLM、1000 道多选题上对比 8 种自我反思类型,证明所有 self-reflection 都能显著提升 LLM agent 的解题准确率(p<0.001)。
- [[2024-recursive-introspection-rise]]:RISE 将单轮问题建模为多轮 MDP 并用 reward-weighted regression 迭代微调,让 7B 级 LLM 在无外部反馈下学会跨多轮递归反思并修正答案。
- [[2024-compute-optimal-inference]]:提出 inference scaling laws / compute-optimal inference 研究问题与新型树搜索算法 REBASE,实证表明固定推理算力下小模型配合高级推理策略比大模型更具性价比(Llemma-7B 约省 2× FLOPs 达到 34B 水平)。
- [[2024-multi-agent-tot-validator]]:将 Tree-of-Thoughts 与多智能体推理结合,新增 Thought Validator agent 过滤无效推理分支后再共识投票,在 GSM8K 上比标准 ToT 平均提升 5.6 个百分点。
- [[2024-score-self-correct-via-rl]]:SCoRe 用完全自生成数据的多轮在线强化学习(两阶段+奖励塑形)训练单个 LLM,在 MATH 上把内在自我纠错 Δ(t1,t2) 从 -11.2% 提到 +4.4%(整体提升 15.6%)、HumanEval 上达 12.2%。
- [[2024-agentic-feedback-loop-recommendation]]:提出 AFL,让 recommendation agent 与 user agent 通过基于 memory 的多轮文本反馈回路相互协作,同时提升推荐(平均 +11.52%)与用户模拟(平均 +21.12%),且不放大流行度/位置偏差。
- [[2024-positive-experience-reflection]]:提出 Sweet&Sour:让 LLM agent 在交互式文本环境中不仅从失败、也从成功经验做反思,并配合双缓冲 managed memory,缓解 self-reflection 在初始成功与小模型上失效的问题;ScienceWorld 上 GPT-4o 平均 54.6、Llama 8B 32.5 均超 Reflexion。
- [[2026-thinkrec-thinking-based-recommendation]]:ThinkRec 通过思考激活(推理数据合成+联合训练)与实例级 LoRA 专家融合,把 LLM 推荐从 System 1 直觉匹配推进到 System 2 推理,在 ML1M/Yelp/Book 上 AUC 平均超 SOTA 7.96%。
- [[2026-orgagent-company-style-mas]]:提出公司式层级多智能体框架 OrgAgent(治理/执行/合规三层),实证表明层级组织在多数推理任务上同时提升效果并大幅降低 token 成本。

## 相关

- [[process-reward-model]]
- [[outcome-reward-model]]
- [[prm800k]]
- [[chain-of-thought]]
- [[best-of-n]]
- [[math-dataset]]
- [[tree-of-thoughts]]
- [[self-correction]]
- [[self-reflection]]
- [[multi-agent-systems|multi-agent]]
- [[reinforcement-learning]]
- [[agent-memory|memory]]
