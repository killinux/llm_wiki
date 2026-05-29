---
type: entity
subtype: product
tags: [llm, chatbot, openai, rlhf, dialogue]
created: 2026-05-29
updated: 2026-05-29
sources: 13
---

# ChatGPT

ChatGPT 是 OpenAI 发布的基于大语言模型的对话式 AI 产品,通过指令微调与人类反馈强化学习对齐,以自然语言对话形式完成问答、写作、推理等任务。

## 在本 wiki 中的出现

- [[2022-instructgpt]]:作为 ChatGPT 的技术前身与方法基础。该工作用 RLHF(SFT → 奖励模型 → PPO)对齐 GPT-3,使 1.3B 的 InstructGPT 在人类偏好上胜过 175B 的 GPT-3,并更真实、毒性更低;这套对齐范式正是 ChatGPT 的核心训练思路。
- [[2023-memorybank]]:将 ChatGPT 作为可接入长期记忆机制的 LLM 之一。MemoryBank 为 LLM 设计类人长期记忆(存储与分层摘要历史对话、按 Ebbinghaus 遗忘曲线更新记忆、检索相关记忆并构建用户画像),并据此实现情感陪伴机器人 SiliconFriend。
- [[2023-multiagent-debate]]:将 ChatGPT 作为参与多智能体辩论的 LLM 实例。让多个 LLM 实例多轮辩论、互相批评彼此答案,在推理(GSM8K 77%→85%)与事实性(MMLU 63.9%→71.1%)任务上显著提升。
- [[2023-multi-agent-debate]]:将 ChatGPT 用作辩论框架中的智能体与/或裁判。该工作提出 Multi-Agent Debate(MAD)框架,用多个 LLM 智能体"针锋相对"辩论加裁判仲裁,缓解自我反思的 Degeneration-of-Thought 问题并激发发散性思维。
- [[2023-shepherd-critic-for-lm-generation]]:Meta AI 用约 8K 高质量社区+人工反馈数据微调出 7B 的 LLaMA critic 模型 Shepherd,能精确批判 LLM 输出并给改进建议,GPT-4 评估 win-rate 53-87%,与 ChatGPT 媲美。
- [[2023-recmind-llm-agent-for-recommendation]]:RecMind 是一个由 LLM 驱动的自主推荐 agent,通过规划、记忆与外部工具实现 zero-shot 个性化推荐,并提出 Self-Inspiring 规划算法保留所有已探索状态以增强规划能力。
- [[2023-chain-of-verification]]:Chain-of-Verification (CoVe) 让 LLM 先生成草稿,再独立回答自我规划的验证问题来核查事实,显著降低幻觉。
- [[2023-agentcf-collaborative-learning-agents-recsys]]:把推荐系统中的用户和物品都建模为 LLM agent,通过自主交互与协同反思实现无梯度的协同过滤式优化。
- [[2024-generative-agents-in-recommendation]]:Agent4Rec 用 1000 个 LLM 驱动的生成式 agent(含 profile/memory/action 模块)构建电影推荐用户模拟器,探究其能否忠实模拟真实用户行为并复现 filter bubble 与 popularity bias。
- [[2023-self-rag]]:Self-RAG 训练单个 LLM 用 reflection token 实现按需检索与自我反思批判,在推理时可控解码以提升生成质量、事实性与引用准确率。
- [[2024-llm-critics-help-catch-llm-bugs]]:OpenAI 用 RLHF 训练 GPT-4 级别的 critic 模型 CriticGPT,让 LLM 写自然语言批评指出代码 bug,以可扩展监督方式帮助人类更准确评估模型生成的代码。
- [[2025-llm-agents-cooperate-social-dilemma]]:让 ChatGPT-4o 与 Claude 3.5 Sonnet 为 iterated Prisoner's Dilemma 写出完整策略(而非逐步出招),用 evolutionary game theory / Moran process 模拟 LLM agent 群体演化,发现多数场景下侵略策略劣势、系统倾向合作,但博弈论 prompt 与 self-refine 会增强侵略策略并提高收敛到侵略均衡的风险。
- [[2025-mem0-scalable-long-term-memory]]:Mem0 是一个以记忆为中心的架构,从持续对话中动态抽取、整合与检索关键信息,并提出图记忆变体 Mem0^g,在 LOCOMO 基准上以约 91% 更低延迟和逾 90% token 节省超越多种基线。

## 相关

- [[gpt-3]]
- [[instructgpt]]
- [[openai]]
- [[rlhf]]
- [[ppo]]
- [[llm]]
- [[multi-agent-debate]]
- [[memorybank]]
- [[siliconfriend]]
