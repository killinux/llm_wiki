---
type: entity
subtype: benchmark
tags: [benchmark, math-reasoning, multi-step-reasoning, evaluation]
created: 2026-05-29
updated: 2026-05-29
sources: 18
---

# GSM8K

GSM8K 是一个由小学水平数学应用题(grade school math word problems)组成的基准数据集,常用于评测大语言模型的多步数学推理能力。

## 在本 wiki 中的出现

- [[2022-chain-of-thought]]:作为 chain-of-thought prompting 的核心评测任务之一。该工作在 few-shot 示例中加入中间推理步骤,显著提升大模型多步推理能力,且增益随模型规模涌现——PaLM 540B 在 GSM8K 上达到 57%。
- [[2022-star-self-taught-reasoner]]:作为 STaR 的评测任务。STaR 用少量 CoT 示例让模型自己生成推理过程,只保留答对的 rationale(并用 rationalization 从答错题反向补全),反复微调自身以 bootstrap 推理能力。
- [[2023-self-refine]]:作为 Self-Refine 评测的任务之一。该方法用同一个 LLM 在测试时迭代"自我反馈→自我修正",无需训练即在 7 个任务上平均提升约 20%。
- [[2023-plan-and-solve-prompting]]:作为 Plan-and-Solve 提示的多步推理评测任务。该工作提出零样本 PS/PS+ 提示,让 LLM 先制定计划再执行子任务,显著改进 Zero-shot-CoT。
- [[2023-critic]]:作为 CRITIC 的评测任务之一。CRITIC 让 LLM 通过与搜索引擎、代码解释器、PERSPECTIVE API 等外部工具交互来自我验证并迭代修正输出,证明外部反馈对自我改进的重要性。
- [[2023-multiagent-debate]]:作为多智能体辩论的推理评测任务。让多个 LLM 实例多轮辩论互相批评彼此答案,在 GSM8K 上从 77% 提升至 85%(事实性任务 MMLU 从 63.9% 提升至 71.1%)。
- [[2023-reasoning-via-planning-rap]]:作为 RAP 的评测任务之一。RAP 把 LLM 同时当作世界模型和推理智能体,用 MCTS 在推理空间里做规划,将 LLM 推理重新表述为带世界模型的规划。
- [[2023-shepherd-critic-for-lm-generation]]:Meta AI 用约 8K 高质量社区+人工反馈数据微调出 7B 的 LLaMA critic 模型 Shepherd,能精确批判 LLM 输出并给改进建议,GPT-4 评估 win-rate 53-87%,与 ChatGPT 媲美。
- [[2023-llms-cannot-self-correct-reasoning-yet]]:本文证明在无外部反馈的"内在自我纠正"设定下,LLM 无法纠正自身推理错误,性能反而往往下降。
- [[2023-agenttuning]]:通过构建跨任务 agent 交互轨迹数据集 AgentInstruct 并与通用指令混合微调,使开源 Llama 2 获得可泛化的 agent 能力且不损害通用能力。
- [[2024-v-star-verifiers-for-self-taught-reasoners]]:V-STaR 在自我提升迭代中复用正确与错误的模型生成解,用 DPO 训练 verifier 在测试时对候选解排序,使 LLaMA2 在数学推理上绝对提升 6%~17%、代码生成 4%~12%。
- [[2024-quiet-star]]:Quiet-STaR 让语言模型在每个 token 前生成隐式 rationale 来更好预测后续文本,以自监督方式从任意文本学会推理,zero-shot 提升 GSM8K(5.9%→10.9%)与 CommonsenseQA(36.3%→47.2%)。
- [[2024-reflection-on-search-trees]]:RoT 让 strong LLM 反思 weak LLM 的历史树搜索经验、对关键状态总结出任务级 guideline 注入后续 prompt,显著提升 BFS/MCTS 等树搜索 prompting 在 Blocksworld、GSM8k、议价任务上的准确率与搜索效率,且任务越难收益越大。
- [[2024-when-can-llms-correct-mistakes]]:批判性综述:细分自我纠错的三类研究问题并提出实验检查清单,论证 LLM 仅凭 prompting 在一般任务上无法可靠自我纠错,瓶颈在于反馈生成,而外部工具/大规模 fine-tuning 可使其奏效。
- [[2024-recursive-introspection-rise]]:RISE 将单轮问题建模为多轮 MDP 并用 reward-weighted regression 迭代微调,让 7B 级 LLM 在无外部反馈下学会跨多轮递归反思并修正答案。
- [[2024-compute-optimal-inference]]:提出 inference scaling laws / compute-optimal inference 研究问题与新型树搜索算法 REBASE,实证表明固定推理算力下小模型配合高级推理策略比大模型更具性价比(Llemma-7B 约省 2× FLOPs 达到 34B 水平)。
- [[2024-megaagent-large-scale-mas-without-sop]]:借鉴操作系统进程/线程模型、无需预定义 SOP、可自动生成数百 agent 并行协作的大规模 LLM 多智能体系统,800 秒内开发五子棋、2991 秒协调 590 个 agent 生成国家政策。
- [[2024-multi-agent-tot-validator]]:将 Tree-of-Thoughts 与多智能体推理结合,新增 Thought Validator agent 过滤无效推理分支后再共识投票,在 GSM8K 上比标准 ToT 平均提升 5.6 个百分点。

## 相关

- [[chain-of-thought]]
- [[multi-step-reasoning]]
- [[math-word-problems]]
- [[mmlu]]
- [[zero-shot-cot]]
- [[palm]]
- [[2022-chain-of-thought]]
- [[2023-multiagent-debate]]
