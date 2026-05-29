---
type: concept
subtype: method
tags: [test-time-compute, inference, reasoning, self-improvement]
created: 2026-05-29
updated: 2026-05-29
sources: 10
---

# Test-time Compute

Test-time Compute 指在推理(inference)阶段、而非训练阶段额外投入计算资源以提升模型输出质量的一类方法,例如多次采样、迭代修正或搜索,而无需更新模型参数。

## 在本 wiki 中的出现

- [[2023-self-refine]]:Self-Refine 是一种典型的 Test-time Compute 方法。它用同一个 LLM 在测试时迭代执行"自我反馈(self-feedback)→自我修正(self-refinement)"循环,不依赖任何额外训练或监督数据,即在 7 个任务上平均提升约 20%。这体现了 Test-time Compute 的核心思想:用推理阶段的额外计算换取更高的输出质量。
- [[2023-memgpt-llms-as-operating-systems]]:MemGPT 借鉴操作系统的分层内存与虚拟内存分页,用函数调用让 LLM 自主管理上下文内外的多级存储,在固定上下文模型上制造"无限上下文"的假象。
- [[2024-v-star-verifiers-for-self-taught-reasoners]]:V-STaR 在自我提升迭代中复用正确与错误的模型生成解,用 DPO 训练 verifier 在测试时对候选解排序,使 LLaMA2 在数学推理上绝对提升 6%~17%、代码生成 4%~12%。
- [[2024-quiet-star]]:Quiet-STaR 让语言模型在每个 token 前生成隐式 rationale 来更好预测后续文本,以自监督方式从任意文本学会推理,zero-shot 提升 GSM8K(5.9%→10.9%)与 CommonsenseQA(36.3%→47.2%)。
- [[2024-when-can-llms-correct-mistakes]]:批判性综述:细分自我纠错的三类研究问题并提出实验检查清单,论证 LLM 仅凭 prompting 在一般任务上无法可靠自我纠错,瓶颈在于反馈生成,而外部工具/大规模 fine-tuning 可使其奏效。
- [[2024-tree-search-for-language-model-agents]]:为 LLM web agent 提出 inference-time best-first tree search,在真实 web 环境中显式做探索与多步规划,把 GPT-4o 在 VisualWebArena 上成功率相对提升 39.7% 至 SOTA 26.4%,并展示 test-time compute scaling 的收益。
- [[2024-recursive-introspection-rise]]:RISE 将单轮问题建模为多轮 MDP 并用 reward-weighted regression 迭代微调,让 7B 级 LLM 在无外部反馈下学会跨多轮递归反思并修正答案。
- [[2024-compute-optimal-inference]]:提出 inference scaling laws / compute-optimal inference 研究问题与新型树搜索算法 REBASE,实证表明固定推理算力下小模型配合高级推理策略比大模型更具性价比(Llemma-7B 约省 2× FLOPs 达到 34B 水平)。
- [[2024-score-self-correct-via-rl]]:SCoRe 用完全自生成数据的多轮在线强化学习(两阶段 + 奖励塑形)训练单个 LLM,在 MATH 上把内在自我纠错 Δ(t1,t2) 从 -11.2% 提到 +4.4%(整体提升 15.6%)、HumanEval 上达 12.2%。
- [[2025-ab-mcts-adaptive-branching-tree-search]]:提出 AB-MCTS,在推理时树搜索中用 Thompson sampling 自适应决定"向宽采样新候选"还是"向深用外部反馈细化已有答案",统一 repeated sampling 与多轮 refinement,实现更高效的 test-time scaling。

## 相关

- [[self-refine]]
- [[self-feedback]]
- [[iterative-refinement]]
- [[chain-of-thought]]
- [[verifier-models]]
- [[tree-search]]
- [[inference-scaling-laws]]
- [[self-correction]]
