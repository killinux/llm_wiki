---
type: entity
subtype: model
tags: [llm, model, openai, multimodal, gpt]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# GPT-4o

GPT-4o 是 OpenAI 推出的多模态大语言模型,广泛用作 LLM 智能体、推理与记忆系统研究中的基础模型与评测基线。

## 在本 wiki 中的出现

- [[2024-aipatient-simulated-patient-llm-agents]]:AIPatient,一个由六个任务专用 LLM 智能体 + Reasoning RAG + 基于 MIMIC-III 真实病历构建的知识图谱驱动的模拟病人系统,EHR-QA 准确率达 94.15%、NER 知识库 F1=0.89,用户研究中匹配或优于真人模拟病人。
- [[2024-positive-experience-reflection]]:提出 Sweet&Sour:让 LLM agent 在交互式文本环境中不仅从失败、也从成功经验做反思,并配合双缓冲 managed memory,缓解 self-reflection 在初始成功与小模型上失效的问题;ScienceWorld 上 GPT-4o 平均 54.6、Llama 8B 32.5 均超 Reflexion。
- [[2025-agentic-memory-llm-agents]]:受 Zettelkasten 启发的 agentic 记忆系统,通过结构化笔记、自主链接生成与记忆演化为 LLM agent 提供可持续演化的长期记忆。
- [[2025-ab-mcts-adaptive-branching-tree-search]]:提出 AB-MCTS:在推理时树搜索中用 Thompson sampling 自适应决定"向宽采样新候选"还是"向深用外部反馈细化已有答案",统一 repeated sampling 与多轮 refinement,实现更高效的 test-time scaling。

## 相关

- [[openai]]
- [[llm-agent]]
- [[reasoning-rag]]
- [[test-time-scaling]]
- [[llama]]
