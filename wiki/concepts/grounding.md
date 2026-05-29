---
type: concept
subtype: method
tags: [grounding, embodied-ai, robotics, llm-planning, closed-loop-feedback]
created: 2026-05-29
updated: 2026-05-29
sources: 7
---

# Grounding

Grounding 指把 LLM 抽象的语言推理与真实环境的状态、可执行动作及其反馈联系起来,使模型的输出受制于现实世界而非仅凭内部先验生成。

## 在本 wiki 中的出现

- [[2022-inner-monologue]]:在该工作中,grounding 通过持续向 frozen LLM 注入自然语言形式的环境反馈(如成功检测、场景描述、人类反馈)来实现,从而让 LLM 形成"内心独白"(inner monologue)。这种反馈使模型的具身推理保持在真实世界的约束内,支撑机器人完成闭环、可重规划的任务执行。
- [[2025-drivemlm-autonomous-driving]]:DriveMLM 将 multi-modal LLM 对齐到自动驾驶行为规划模块的离散决策状态,使语言输出可转为车辆控制,在 CARLA Town05 Long 上实现闭环驾驶并取得 DS 76.1、MPI 0.96。
- [[2023-llms-cannot-self-correct-reasoning-yet]]:本文证明在无外部反馈的"内在自我纠正"设定下,LLM 无法纠正自身推理错误,性能反而往往下降。
- [[2023-self-rag]]:Self-RAG 训练单个 LLM 用 reflection token 实现按需检索与自我反思批判,在推理时可控解码以提升生成质量、事实性与引用准确率。
- [[2023-concordia-generative-agent-based-modeling]]:Google DeepMind 提出的库 Concordia,用 LLM 驱动的生成式 agent 在物理/社会/数字空间中扎根交互,通过 Game Master 控制环境,支持 Generative Agent-Based Modeling 的社会仿真与数字服务评估。
- [[2023-drivemlm-autonomous-driving]]:DriveMLM 通过将多模态 LLM 的语言决策与模块化 AD 系统的行为规划状态对齐,在 CARLA 仿真器实现闭环自动驾驶,Town05 Long 上 DS 达 76.1,优于 Apollo 4.7 点。
- [[2024-aipatient-simulated-patient-llm-agents]]:AIPatient 通过基于 MIMIC-III 真实病历构建的知识图谱与 Reasoning RAG,将六个任务专用 LLM 智能体的输出锚定到真实临床数据上,实现 EHR-QA 准确率 94.15%、NER 知识库 F1=0.89,从而让模拟病人的回答保持与真实病历一致的事实基础;用户研究中其表现匹配或优于真人模拟病人。

## 相关

- [[saycan]]:在 [[2022-inner-monologue]] 中,grounding 直接建立在 SayCan 的 affordance grounding(价值函数衡量技能在当前状态下的可行性)之上
- [[llm-planning]]:grounding 是让 LLM 规划在具身环境中可靠落地的关键机制
- [[closed-loop-feedback]]:grounding 依赖持续的环境反馈来闭合智能体-环境回路
- [[chain-of-thought]]:在反馈较复杂时辅助 LLM 推断目标与已达成状态
- [[vqa]]:主动场景描述中可作为环境反馈的来源之一
- [[hallucination]]:grounding 常被视为缓解 LLM 脱离现实、产生幻觉的手段
- [[retrieval-augmented-generation]]:通过检索外部证据为生成提供事实依据,是文本层面的 grounding
- [[knowledge-graph]]:将输出锚定到结构化知识图谱也是一种 grounding 方式
