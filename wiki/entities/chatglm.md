---
type: entity
subtype: model
tags: [llm, model, chatglm, dialogue]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# ChatGLM

ChatGLM 是基于 GLM 架构的中英双语对话大语言模型,常被用作对话系统与记忆增强等研究中的基础生成模型。

## 在本 wiki 中的出现

- [[2023-memorybank]]:在 MemoryBank 工作中,ChatGLM 作为可适配的底层大语言模型之一被采用。MemoryBank 为 LLM 设计类人长期记忆机制(存储与分层摘要历史对话、按 Ebbinghaus 遗忘曲线更新记忆、检索相关记忆并构建用户画像),并据此构建情感陪伴机器人 SiliconFriend,ChatGLM 在其中承担对话生成的角色。
- [[2023-agenttuning]]:通过构建跨任务 agent 交互轨迹数据集 AgentInstruct 并与通用指令混合微调,使开源 Llama 2 获得可泛化的 agent 能力且不损害通用能力。

## 相关

- [[memorybank]]
- [[siliconfriend]]
- [[large-language-model]]
- [[long-term-memory]]
