---
type: concept
subtype: method
tags: [llm, agents, reasoning, memory, multi-agent]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# LLM Agents

LLM Agents 指以大语言模型为核心决策器、并通过记忆、规划、工具调用或多实例协作等机制与环境持续交互以完成复杂任务的智能体系统。

## 在本 wiki 中的出现

- [[2023-hyper-actor-critic-recommendation]]:把推荐系统视为序列决策智能体,提出 Hyper-Actor Critic(HAC)框架,将推荐列表生成解耦为 hyper-action 推断与 effect-action 选择两步,并以对齐与监督模块稳定大动作空间下的 RL 推荐策略学习——体现 agent 在巨大离散动作空间中的决策范式。
- [[2023-memorybank]]:为 LLM Agent 设计类人长期记忆机制 MemoryBank,通过存储与分层摘要历史对话、按 Ebbinghaus 遗忘曲线更新记忆、检索相关记忆并构建用户画像,使 agent 具备跨会话的持久记忆能力,并据此实现情感陪伴机器人 SiliconFriend。
- [[2023-multiagent-debate]]:研究 multi-agent 协作范式,让多个 LLM 实例多轮辩论、互相批评彼此答案,在推理(GSM8K 77%→85%)与事实性(MMLU 63.9%→71.1%)任务上显著提升,展示多智能体交互对单体能力的增益。
- [[2023-sotopia-social-intelligence-evaluation]]:SOTOPIA 提出一个开放式社交互动模拟环境与多维评测框架 SOTOPIA-EVAL,交互式地评估 LLM 智能体在目标导向社交场景中的社会智能,发现 GPT-4 在最难子集上的目标完成率显著低于人类。

## 相关

- [[generative-agents]]
- [[react]]
- [[reflexion]]
- [[memory-stream]]
- [[reinforcement-learning]]
- [[llm-planning]]
- [[chain-of-thought]]
- [[hyper-actor-critic]]
- [[recommender-systems]]
- [[multi-agent-systems]]
- [[tool-use]]
- [[social-intelligence]]
- [[agent-evaluation]]
