---
type: concept
subtype: method
tags: [fine-tuning, training, adaptation, LLM]
created: 2026-05-29
updated: 2026-05-29
sources: 7
---

# 微调

微调(fine-tuning)指在预训练模型的基础上,使用特定任务或领域的数据继续训练以更新模型参数,使其适应目标任务的方法。

## 在本 wiki 中的出现

- [[2023-expel]]:作为对照基线被有意回避。ExpeL 让 LLM Agent **不**更新参数(即不做微调),转而从跨任务经验中自主抽取自然语言洞见,并召回相似的成功轨迹来提升决策表现,以此说明无需微调也能积累与复用经验。
- [[2023-shepherd-critic-for-lm-generation]]:Meta AI 用约 8K 高质量社区+人工反馈数据微调出 7B 的 LLaMA critic 模型 Shepherd,能精确批判 LLM 输出并给改进建议,GPT-4 评估 win-rate 53-87%,与 ChatGPT 媲美。
- [[2023-ts-llm-tree-search-decoding-training]]:TS-LLM:用学习的 value function 的 AlphaZero 风格树搜索,同时指导 LLM 的推理解码与迭代训练,适配任意规模 LLM 并将搜索深度扩展到 64。
- [[2023-fireact-language-agent-fine-tuning]]:提出用多任务、多 prompting 方法(ReAct/CoT/Reflexion)生成的轨迹微调 backbone LM 来构建语言智能体,在性能、鲁棒性、泛化与成本上全面优于 few-shot prompting。
- [[2023-agenttuning]]:通过构建跨任务 agent 交互轨迹数据集 AgentInstruct 并与通用指令混合微调,使开源 Llama 2 获得可泛化的 agent 能力且不损害通用能力。
- [[2024-v-star-verifiers-for-self-taught-reasoners]]:V-STaR 在自我提升迭代中复用正确与错误的模型生成解,用 DPO 训练 verifier 在测试时对候选解排序,使 LLaMA2 在数学推理上绝对提升 6%~17%、代码生成 4%~12%。
- [[2024-recursive-introspection-rise]]:RISE 将单轮问题建模为多轮 MDP 并用 reward-weighted regression 迭代微调,让 7B 级 LLM 在无外部反馈下学会跨多轮递归反思并修正答案。

## 相关

- [[in-context-learning]]
- [[prompt-engineering]]
- [[retrieval-augmented-generation]]
- [[llm-agent]]
- [[reinforcement-learning]]
