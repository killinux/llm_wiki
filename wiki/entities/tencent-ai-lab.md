---
type: entity
subtype: lab
tags: [lab, industry-research, china, tencent, llm, multi-agent]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# Tencent AI Lab

Tencent AI Lab 是腾讯旗下的企业人工智能研究机构,研究方向涵盖机器学习、自然语言处理与大语言模型(LLM)等领域。

## 在本 wiki 中的出现

- [[2023-multi-agent-debate]]:作为该论文中提出 Multi-Agent Debate(MAD)框架的研究机构。MAD 用多个 LLM 智能体以"针锋相对"的方式进行辩论,并由裁判进行仲裁,从而缓解自我反思中的 Degeneration-of-Thought 问题,并激发模型的发散性思维。
- [[2023-agentcf-collaborative-learning-agents-recsys]]:把推荐系统中的用户和物品都建模为 LLM agent,通过自主交互与协同反思实现无梯度的协同过滤式优化。
- [[2024-crocodile-cross-experts-covariance]]:Crocodile 用多嵌入架构 + cross-experts covariance loss(CovLoss)解耦各 expert 表示,并以 Prior Informed Element-wise Gating(PEG)路由,平衡多域推荐中"保持域差异性"与"充分学习参数"的两难,公开数据集与 Tencent 线上 A/B 均取得提升。
- [[2025-opencharacter-role-playing-synthetic-personas]]:用 Persona Hub 大规模合成 persona 造角色对齐 SFT 数据,微调 LLaMA-3 8B 获得 out-of-domain 角色泛化能力,在 PersonaGym 上比肩 GPT-4o。
- [[2025-memory-os-of-ai-agent]]:借鉴操作系统内存管理,为 AI agent 设计分层(STM/MTM/LPM)、heat 驱动更新的 MemoryOS,统一 Storage/Updating/Retrieval/Generation 四模块,在 LoCoMo 上 F1 平均提升 49.11%、BLEU-1 提升 46.18%。

## 相关

- [[multi-agent-debate]]
- [[degeneration-of-thought]]
- [[large-language-model]]
- [[multi-agent-system]]
- [[self-reflection]]
- [[recommendation-system]]
- [[multi-domain-recommendation]]
- [[collaborative-filtering]]
- [[persona-hub]]
- [[personagym]]
- [[memory-os]]
- [[locomo]]
- [[llama-3]]
