---
type: concept
subtype: method
tags: [role-playing, llm-agents, multi-agent, prompting]
created: 2026-05-29
updated: 2026-05-29
sources: 7
---

# 角色扮演智能体

角色扮演智能体(role-playing agent)是指通过 prompt 赋予某个 LLM 一个特定身份或职能(如设计师、程序员、测试员),使其按该角色的视角与职责进行推理、协作和产出的智能体。

## 在本 wiki 中的出现

- [[2023-chatdev]]:ChatDev 用多个 LLM 驱动的角色化软件智能体,通过对话链(chat chain)沿瀑布式流程协作,完成设计、编码、测试、文档的完整软件开发。每个智能体被赋予特定角色,在阶段性对话中分工配合。
- [[2024-sotopia-pi-social-agents]]:通过 behavior cloning 与 self-reinforcement 在 GPT-4 评分过滤的社交对话数据上训练,使 7B LLM 的社交目标完成能力逼近 GPT-4,同时提升安全并保持 MMLU。
- [[2024-generative-agents-self-reports]]:用基于真人深度访谈与问卷自述构建的 generative agents,可对单个个体在多种社会科学结果上做通用模拟,留出题目预测精度接近个体两周后的重测一致性。
- [[2025-opencharacter-role-playing-synthetic-personas]]:用 Persona Hub 大规模合成 persona 造角色对齐 SFT 数据,微调 LLaMA-3 8B 获得 out-of-domain 角色泛化能力,在 PersonaGym 上比肩 GPT-4o。
- [[2025-coser-literary-roleplay-dataset]]:CoSER 从 771 部名著抽取 17,966 个角色的真实多角色对话构建数据集,提出 given-circumstance acting 训练与评测角色扮演 LLM,训练出的 CoSER 70B 在自有评测与多个 RPLA benchmark 上达到 SOTA。
- [[2025-llm-driven-cross-platform-npc]]:一个原型系统,让 LLM 驱动的游戏 NPC 通过云数据库在 Unity 游戏内与 Discord 社交平台间跨平台对话并同步记忆。
- [[2025-memory-os-of-ai-agent]]:借鉴操作系统内存管理,为 AI agent 设计分层(STM/MTM/LPM)、heat 驱动更新的 MemoryOS,统一 Storage/Updating/Retrieval/Generation 四模块,在 LoCoMo 上 F1 平均提升 49.11%、BLEU-1 提升 46.18%。

## 相关

- [[role-playing]]
- [[multi-agent-systems]]
- [[llm-agents|llm-agent]]
- [[chat-chain]]
- [[inception-prompting]]
- [[prompt-engineering]]
