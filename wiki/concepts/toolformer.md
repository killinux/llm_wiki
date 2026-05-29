---
type: concept
subtype: method
tags: [tool-use, llm, self-supervised, api]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Toolformer

Toolformer 是一种通过自监督方式让语言模型学会自主调用外部工具(如计算器、搜索引擎、问答系统、翻译系统、日历等)API 的方法,模型可以自行决定何时调用哪个工具、传入什么参数,并把返回结果融入后续生成。

## 在本 wiki 中的出现

- [[2023-critic]]:作为"让 LLM 借助外部工具来增强能力"这一研究方向的代表性工作之一。CRITIC 与 Toolformer 同属让模型与外部工具交互的脉络,但侧重点不同——Toolformer 关注模型学会在生成中主动调用工具,而 CRITIC 让 LLM 通过与搜索引擎、代码解释器、PERSPECTIVE API 等外部工具交互来自我验证并迭代修正输出,强调外部反馈对自我改进的关键作用。
- [[2023-recmind-llm-agent-for-recommendation]]:RecMind 是一个由 LLM 驱动的自主推荐 agent,通过规划、记忆与外部工具实现 zero-shot 个性化推荐,并提出 Self-Inspiring 规划算法保留所有已探索状态以增强规划能力。
- [[2023-agenttuning]]:通过构建跨任务 agent 交互轨迹数据集 AgentInstruct 并与通用指令混合微调,使开源 Llama 2 获得可泛化的 agent 能力且不损害通用能力。

## 相关

- [[2023-critic]]
- [[tool-use]]
- [[self-supervised-learning]]
- [[react]]
- [[in-context-learning]]
