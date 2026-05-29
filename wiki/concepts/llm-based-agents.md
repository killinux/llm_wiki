---
type: concept
subtype: method
tags: [llm, agents, multi-agent, autonomy, tool-use]
created: 2026-05-29
updated: 2026-05-29
sources: 9
---

# LLM-based Agents

LLM-based Agents 是以 large language model 为推理与决策核心的自主系统,能够根据目标进行规划、调用工具、与环境或其它 agent 交互,并迭代完成复杂任务。

## 在本 wiki 中的出现

- [[2023-metagpt]]:MetaGPT 将 LLM-based Agents 组织为一个多智能体软件开发框架。它把人类的 SOP(Standard Operating Procedure)编码进 prompt,为各个 agent 赋予专业化角色,并通过结构化输出在 agent 之间传递信息以减少错误累积。该框架在 HumanEval/MBPP 上达到 SoTA。这里 LLM-based Agents 既是被组织协作的基本单元,也是承载角色专业化与结构化协作流程的载体。
- [[2023-recmind-llm-agent-for-recommendation]]:RecMind 是一个由 LLM 驱动的自主推荐 agent,通过规划、记忆与外部工具实现 zero-shot 个性化推荐,并提出 Self-Inspiring 规划算法保留所有已探索状态以增强规划能力。
- [[2023-agentcf-collaborative-learning-agents-recsys]]:把推荐系统中的用户和物品都建模为 LLM agent,通过自主交互与协同反思实现无梯度的协同过滤式优化。
- [[2024-generative-agents-in-recommendation]]:Agent4Rec 用 1000 个 LLM 驱动的生成式 agent(含 profile/memory/action 模块)构建电影推荐用户模拟器,探究其能否忠实模拟真实用户行为并复现 filter bubble 与 popularity bias。
- [[2024-hiagent-hierarchical-working-memory]]:HiAgent 用 subgoal 作为 memory chunk 分层管理 LLM agent 的 working memory(汇总过去 observation、按需检索明细轨迹),在五个长程任务上成功率约翻倍(21→42)、context 减少 35%。
- [[2024-aipatient-simulated-patient-llm-agents]]:AIPatient,由六个任务专用 LLM 智能体 + Reasoning RAG + 基于 MIMIC-III 真实病历构建的知识图谱驱动的模拟病人系统,EHR-QA 准确率达 94.15%、NER 知识库 F1=0.89,用户研究中匹配或优于真人模拟病人。
- [[2025-multi-agent-collaboration-mechanisms-survey]]:系统综述,沿 actors、types、structures、strategies、coordination protocols 五个维度刻画基于 LLM 的多 agent 系统协作机制,并梳理其跨领域应用与挑战。
- [[2025-agentcf-plus-plus]]:通过双层记忆架构、两步融合机制与兴趣组共享记忆增强 AgentCF 用户模拟器,在跨域推荐中减少无关信息并显式建模流行度因素。
- [[2025-llm-agent-evaluation-survey]]:SAP Labs 的 LLM agent 评测综述,提出"评测目标 × 评测过程"二维分类法,并强调企业落地中的可靠性、合规与 RBAC 等挑战。

## 相关

- [[multi-agent-systems]]
- [[large-language-models]]
- [[prompt-engineering]]
- [[role-playing]]
- [[tool-use]]
- [[code-generation]]
- [[metagpt]]
- [[humaneval]]
- [[mbpp]]
- [[planning]]
- [[memory]]
- [[llm-for-recommendation]]
- [[user-simulation]]
- [[retrieval-augmented-generation]]
- [[agent-evaluation]]
