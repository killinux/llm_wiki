---
type: entity
subtype: model
tags: [model, anthropic, assistant, rlaif]
created: 2026-05-29
updated: 2026-05-29
sources: 7
---

# Claude

Claude 是 Anthropic 开发的大语言模型助手,以"有用、诚实、无害"为目标进行训练。

## 在本 wiki 中的出现

- [[2022-constitutional-ai]]:在 Constitutional AI 的研究中,Claude 是被训练的助手模型。该方法用一套人类书写的原则(constitution)替代人类对有害性的标注,通过模型自我批评与修改、再结合 AI 反馈强化学习(RLAIF),训练出既无害又不回避问题的助手。
- [[2024-self-reflection-llm-agents]]:在 9 个 LLM、1000 道多选题上对比 8 种自我反思类型,证明所有 self-reflection 都能显著提升 LLM agent 的解题准确率(p<0.001)。
- [[2024-aipatient-simulated-patient-llm-agents]]:AIPatient,一个由六个任务专用 LLM 智能体 + Reasoning RAG + 基于 MIMIC-III 真实病历构建的知识图谱驱动的模拟病人系统,EHR-QA 准确率达 94.15%、NER 知识库 F1=0.89,用户研究中匹配或优于真人模拟病人。
- [[2025-llm-agents-cooperate-social-dilemma]]:让 ChatGPT-4o 与 Claude 3.5 Sonnet 为 iterated Prisoner's Dilemma 写出完整策略(而非逐步出招),用 evolutionary game theory / Moran process 模拟 LLM agent 群体演化,发现多数场景下侵略策略劣势、系统倾向合作,但博弈论 prompt 与 self-refine 会增强侵略策略并提高收敛到侵略均衡的风险。
- [[2025-mem0-scalable-long-term-memory]]:Mem0 是一个以记忆为中心的架构,从持续对话中动态抽取、整合与检索关键信息,并提出图记忆变体 Mem0^g,在 LOCOMO 基准上以约 91% 更低延迟和逾 90% token 节省超越多种基线。
- [[2025-emergent-llm-behaviors-data-leakage]]:批判性短文:LLM 多智能体模拟中"自发涌现的社会约定"在观测上等价于 data leakage——模型只是复述预训练中已知的协调博弈知识,而非真正自组织。
- [[2026-self-organizing-llm-agents]]:一项 25,000 任务的大规模实验发现"内生性悖论"——固定智能体顺序但角色自主的混合协议(Sequential)在质量上同时超越中心化(+14%)与完全自主(+44%)协调,但仅当底层模型足够强(存在能力门槛)。

## 相关

- [[anthropic]]
- [[constitutional-ai]]
- [[rlaif]]
- [[rlhf]]
- [[large-language-models|large-language-model]]
- [[ai-assistant]]
- [[llm-agents|llm-agent]]
- [[self-reflection]]
