---
type: entity
subtype: model
tags: [model, openai, llm]
created: 2026-05-29
updated: 2026-05-29
sources: 11
---

# GPT-3.5

OpenAI 推出的大型语言模型系列,是 GPT-3 的改进版本,经过指令微调以更好地遵循自然语言指令,广泛用作对话与智能体应用的基础模型。

## 在本 wiki 中的出现

- [[2023-reflexion]]:作为 LLM 智能体的基础模型之一,用于验证以语言化自我反思反馈(而非梯度更新)来强化智能体、使其从失败中迭代改进的效果。
- [[2023-chatdev]]:作为驱动角色化软件智能体的 LLM,支撑 ChatDev 中多个智能体通过对话链沿瀑布式流程协作完成设计、编码、测试与文档的完整软件开发。
- [[2023-ts-llm-tree-search-decoding-training]]:TS-LLM 用学习的 value function 的 AlphaZero 风格树搜索,同时指导 LLM 的推理解码与迭代训练,适配任意规模 LLM 并将搜索深度扩展到 64。
- [[2023-llms-cannot-self-correct-reasoning-yet]]:证明在无外部反馈的"内在自我纠正"设定下,LLM 无法纠正自身推理错误,性能反而往往下降。
- [[2023-fireact-language-agent-fine-tuning]]:提出用多任务、多 prompting 方法(ReAct/CoT/Reflexion)生成的轨迹微调 backbone LM 来构建语言智能体,在性能、鲁棒性、泛化与成本上全面优于 few-shot prompting。
- [[2023-sotopia-social-intelligence-evaluation]]:SOTOPIA 提出开放式社交互动模拟环境与多维评测框架 SOTOPIA-EVAL,交互式评估 LLM 智能体在目标导向社交场景中的社会智能,发现 GPT-4 在最难子集上的目标完成率显著低于人类。
- [[2023-agenttuning]]:通过构建跨任务 agent 交互轨迹数据集 AgentInstruct 并与通用指令混合微调,使开源 Llama 2 获得可泛化的 agent 能力且不损害通用能力。
- [[2023-drivemlm-autonomous-driving]]:DriveMLM 通过将多模态 LLM 的语言决策与模块化 AD 系统的行为规划状态对齐,在 CARLA 仿真器实现闭环自动驾驶,Town05 Long 上 DS 达 76.1,优于 Apollo 4.7 点。
- [[2024-recursive-introspection-rise]]:RISE 将单轮问题建模为多轮 MDP 并用 reward-weighted regression 迭代微调,让 7B 级 LLM 在无外部反馈下学会跨多轮递归反思并修正答案。
- [[2024-limits-of-agency-in-agent-based-models]]:提出 LLM archetypes——为少数代表性 agent 类型查询 LLM 行为再概率采样到个体,从而在百万级 ABM 仿真(NYC 840 万人 COVID-19)中保持规模的同时引入 LLM 自适应行为。
- [[2024-stateact-self-prompting-state-tracking]]:StateAct 通过 self-prompting 与 chain-of-states 状态跟踪增强 LLM base agent,纯 in-context learning 即在 Alfworld/Webshop/Textcraft 上比 ReAct 提升 7%-30%。

## 相关

- [[gpt-4]]:同为 OpenAI 的 GPT 系列模型,GPT-4 是其后继的更强版本。
- [[openai]]:GPT-3.5 的开发与发布方。
- [[chatgpt]]:基于 GPT-3.5 等模型构建的对话产品。
- [[llm-agents|llm-agent]]:GPT-3.5 常被用作 LLM 智能体的基础模型。
