---
type: entity
subtype: model
tags: [model, LLM, OpenAI, GPT-3]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# text-davinci-003

text-davinci-003 是 OpenAI 推出的基于 GPT-3 的指令微调大语言模型,属于 InstructGPT 系列,常被研究工作用作生成与推理任务的基座模型。

## 在本 wiki 中的出现

- 在 [[2023-critic]] 中,text-davinci-003 作为待验证与修正的 LLM 基座之一。CRITIC 让该模型通过与搜索引擎、代码解释器、PERSPECTIVE API 等外部工具交互来自我验证并迭代修正输出,以此论证外部反馈对自我改进的重要性。
- [[2023-recmind-llm-agent-for-recommendation]]:RecMind 是一个由 LLM 驱动的自主推荐 agent,通过规划、记忆与外部工具实现 zero-shot 个性化推荐,并提出 Self-Inspiring 规划算法保留所有已探索状态以增强规划能力。

## 相关

- [[OpenAI]]
- [[GPT-3]]
- [[InstructGPT]]
- [[2023-critic]]
- [[LLM]]
- [[tool-use]]
- [[self-correction]]
