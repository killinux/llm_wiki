---
type: entity
subtype: model
tags: [model, llm, open-source, foundation-model]
created: 2026-05-29
updated: 2026-05-29
sources: 8
---

# LLaMA

LLaMA 是 Meta 推出的一系列开放权重大语言模型(Large Language Model),常被研究者用作构建智能体、推理与微调实验的基础模型。

## 在本 wiki 中的出现

- [[2023-camel-communicative-agents]]:在 CAMEL 的角色扮演框架中,LLaMA 作为可被驱动的底层 LLM 之一,承担 AI User 与 AI Assistant 的角色,在 inception prompting 下自主协作完成任务并生成大规模指令/对话数据。
- [[2023-reasoning-via-planning-rap]]:在 RAP 中,LLaMA 被同时用作世界模型与推理智能体,配合 MCTS 在推理空间内进行规划,从而把 LLM 推理重新表述为带世界模型的规划过程。
- [[2025-drivemlm-autonomous-driving]]:DriveMLM 将 multi-modal LLM 对齐到自动驾驶行为规划模块的离散决策状态,使语言输出可转为车辆控制,在 CARLA Town05 Long 上实现闭环驾驶并取得 DS 76.1、MPI 0.96。
- [[2023-shepherd-critic-for-lm-generation]]:Meta AI 用约 8K 高质量社区+人工反馈数据微调出 7B 的 LLaMA critic 模型 Shepherd,能精确批判 LLM 输出并给改进建议,GPT-4 评估 win-rate 53-87%,与 ChatGPT 媲美。
- [[2023-chain-of-verification]]:Chain-of-Verification (CoVe) 让 LLM 先生成草稿,再独立回答自我规划的验证问题来核查事实,显著降低幻觉。
- [[2023-drivemlm-autonomous-driving]]:DriveMLM 通过将多模态 LLM 的语言决策与模块化 AD 系统的行为规划状态对齐,在 CARLA 仿真器实现闭环自动驾驶,Town05 Long 上 DS 达 76.1,优于 Apollo 4.7 点。
- [[2024-tree-search-for-language-model-agents]]:为 LLM web agent 提出 inference-time best-first tree search,在真实 web 环境中显式做探索与多步规划,把 GPT-4o 在 VisualWebArena 上成功率相对提升 39.7% 至 SOTA 26.4%,并展示 test-time compute scaling 的收益。
- [[2024-large-recommendation-models-scaling]]:华为诺亚与 USTC 的工作,系统评估 large recommendation models 的 scaling law,以生成式推荐模型 HSTU 为代表,在多 backbone、复杂用户行为与 ranking 任务上验证可扩展性及其来源组件。

## 相关

- [[meta]]
- [[large-language-model]]
- [[instruction-tuning]]
- [[mcts]]
- [[world-model]]
- [[ai-agent]]
- [[shepherd]]
- [[drivemlm]]
- [[chain-of-verification]]
- [[gpt-4]]
