---
type: concept
subtype: method
tags: [self-improvement, bootstrapping, reasoning, agent, in-context-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 9
---

# Self-Improvement

Self-Improvement 指 LLM(或基于 LLM 的 Agent)在很少甚至不依赖额外人工标注的情况下,利用自身生成的产物(推理过程、轨迹、经验)反复优化自己的能力,从而不断提升表现的方法。

## 在本 wiki 中的出现

- [[2022-star-self-taught-reasoner]]:STaR 是 Self-Improvement 在**推理能力训练**上的代表。它用少量 CoT 示例引导模型自己生成 rationale,只保留得出正确答案的推理过程(并通过 rationalization 从答错的题目反向补全 rationale),再用这些数据反复微调模型自身,从而 bootstrap 出更强的推理能力。这里 Self-Improvement 体现为"用自己生成、自己筛选的数据来更新自身参数"的闭环。

- [[2023-expel]]:ExpeL 是 Self-Improvement 在 **Agent 层面、无参数更新**形态的代表。LLM Agent 不更新参数,而是从跨任务的经验中自主抽取自然语言洞见(insights),并在面对新任务时召回相似的成功轨迹,从而提升决策表现。这里 Self-Improvement 体现为"通过经验积累与召回在 in-context 层面变强",而非梯度更新。

- [[2023-ts-llm-tree-search-decoding-training]]:TS-LLM:用学习的 value function 的 AlphaZero 风格树搜索,同时指导 LLM 的推理解码与迭代训练,适配任意规模 LLM 并将搜索深度扩展到 64。

- [[2024-metacognition-generative-agents]]:为 generative agents 引入元认知(metacognition)模块,让 agent 观察并反思自身思考与行动以动态调整策略,在僵尸末日等目标导向场景中显著提升表现。

- [[2024-v-star-verifiers-for-self-taught-reasoners]]:V-STaR 在自我提升迭代中复用正确与错误的模型生成解,用 DPO 训练 verifier 在测试时对候选解排序,使 LLaMA2 在数学推理上绝对提升 6%~17%、代码生成 4%~12%。

- [[2024-llm-learnable-planners-long-term-recommendation]]:提出 BiLLP 双层可学习 LLM 规划框架(Planner/Reflector 宏观 + Actor/Critic 微观),在稀疏推荐数据上以 LLM 规划能力做长期推荐,Len 与累积奖励超越从零训练的 RL 与现有 LLM agent 基线。

- [[2024-sotopia-pi-social-agents]]:通过 behavior cloning 与 self-reinforcement 在 GPT-4 评分过滤的社交对话数据上训练,使 7B LLM 的社交目标完成能力逼近 GPT-4,同时提升安全并保持 MMLU。

- [[2024-quiet-star]]:Quiet-STaR 让语言模型在每个 token 前生成隐式 rationale 来更好预测后续文本,以自监督方式从任意文本学会推理,zero-shot 提升 GSM8K(5.9%→10.9%)与 CommonsenseQA(36.3%→47.2%)。

- [[2024-recursive-introspection-rise]]:RISE 将单轮问题建模为多轮 MDP 并用 reward-weighted regression 迭代微调,让 7B 级 LLM 在无外部反馈下学会跨多轮递归反思并修正答案。

## 相关

- [[chain-of-thought]]
- [[rationalization]]
- [[bootstrapping]]
- [[llm-agent]]
- [[in-context-learning]]
- [[experience-replay]]
- [[self-training]]
- [[verifier]]
- [[reflection]]
- [[tree-search]]
