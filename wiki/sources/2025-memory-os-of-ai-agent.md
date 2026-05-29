---
type: source
subtype: paper
tags:
  - agent-memory
  - llm-agent
  - long-term-memory
  - personalization
  - memory-management
created: 2026-05-29
updated: 2026-05-29
arxiv: 2506.06328
raw: raw/2506.06326.pdf
authors:
  - Jiazheng Kang
  - Mingming Ji
  - Zhe Zhao
  - Ting Bai
year: 2025
---

# Memory OS of AI Agent (MemoryOS)

借鉴操作系统的内存管理原理,为 [[llm-agent|AI agent]] 设计一套分层的"内存操作系统"MemoryOS,通过 Storage / Updating / Retrieval / Generation 四个模块统一管理长期对话记忆,从而提升长对话中的连贯性与个性化。

> 注:本文件对应 raw 中的 PDF(`raw/2506.06326.pdf`),但其正文标题页与参考文献显示该工作的 arXiv 编号为 2506.06328(Memory OS of AI Agent)。frontmatter 的 arxiv 字段按论文自报编号填写。

## 问题

[[large-language-models]] 受限于固定长度的 context window 与薄弱的记忆机制,在存在大时间跨度的多轮对话中难以维持连贯性,常出现事实不一致、个性化不足。作者把现有 [[agent-memory|LLM 记忆机制]]归为三类:

- **Knowledge-organization**:把中间推理状态组织成语义网络/笔记,如 A-Mem、Think-in-Memory(TiM)。
- **Retrieval mechanism-oriented**:用外部记忆库 + 检索增强,如 [[memorybank|MemoryBank]](结合 [[ebbinghaus-forgetting-curve|遗忘曲线]]刷新记忆)、EmotionalRAG。
- **Architecture-driven**:改变核心控制流来显式管理 context,如 [[2023-memgpt-llms-as-operating-systems|MemGPT]] 的 OS 式分层读写、Self-Controlled Memory(SCM)。

这些方法各自只覆盖单一维度(存储结构、检索机制或更新策略),缺少一个统一、系统的"内存操作系统"。

## 方法

MemoryOS 把记忆组织成"逻辑段(对话主题)再细分为页"的层级结构,并用 heat(热度)做优先级管理,包含四个模块:

- **三级分层存储(Memory Storage)**:
  - **Short-Term Memory(STM)**:以 dialogue page = {Q, R, T} 存实时对话;为每页构造 dialogue chain,LLM 两步生成 meta(判断与前页是否语义连续、汇总链上各页)。
  - **Mid-Term Memory(MTM)**:Segmented Paging 架构,同主题页聚成 segment;用 `F_score = cos(e_s, e_p) + F_Jacard(K_s, K_p)`(语义相似度 + 关键词 Jaccard)判断页归属,超过阈值 θ 则并入。
  - **Long-term Personal Memory(LPM)**:存 User Persona(User Profile 静态属性 + User KB 事实库 + 90 维 User Traits)与 Agent Persona(Agent Profile + Agent Traits)。
- **Memory Updating**:
  - STM→MTM:固定长度队列,按 [[2023-memgpt-llms-as-operating-systems|FIFO]] 把最旧页迁入 MTM。
  - MTM→LPM:基于 heat 的 segment 删除与升迁,`Heat = α·N_visit + β·L_interaction + γ·R_recency`,其中 `R_recency = exp(-Δt/μ)`(μ=1e7);热度超过阈值 τ 的 segment 升入 LPM,容量满时驱逐最低热度者。
- **Memory Retrieval**:STM 全量召回近期上下文;MTM 两阶段检索(先选 top-m segment,再选 top-k dialogue page);LPM 召回 top-10 最相关 User KB / Agent Traits。
- **Response Generation**:整合 STM/MTM/LPM 三路检索结果 + 用户 query 构造最终 prompt 交 LLM 生成回复。

## 结果

- **数据集与指标**:在 GVD(15 个虚拟用户、10 天多轮对话)与 [[benchmark|LoCoMo]](平均约 300 轮、约 9K token 的超长对话,问题分 Single-hop / Multi-hop / Temporal / Open-domain)上评测。GVD 用 Acc./Corr./Cohe.(DeepSeek-R1 自动评分),LoCoMo 用 F1 与 BLEU-1。
- **GVD(Table 1)**:在 [[gpt-4o-mini|GPT-4o-mini]] 上,MemoryOS 取得 Acc. 93.3 / Corr. 91.2 / Cohe. 92.3,较最强基线 A-Mem 分别提升 3.2% / 5.4% / 1.0%;在 Qwen2.5-7B 上为 91.8 / 82.3 / 90.5(提升 5.3% / 3.5% / 3.1%)。
- **LoCoMo(Table 2)**:在 GPT-4o-mini 上,F1 平均提升 49.11%、BLEU-1 平均提升 46.18%(Temporal 类提升最大,F1 +118.80%、BLEU-1 +111.52%),平均排名 F1/BLEU-1 均为第 1。
- **效率(Table 3)**:平均 4.9 次 LLM 调用、3,874 tokens、Avg.F1 36.23,优于 A-Mem*(13 次调用、F1 26.55)与 MemGPT(16,977 tokens、F1 29.13)。
- **消融**:去掉任一模块都掉点;其中 MTM 影响最大,其次 LPM,dialogue chain 影响最小。超参分析表明 MTM 检索 top-k 取 10 时性价比最佳。
- 代码开源:github.com/BAI-LAB/MemoryOS。

## 在本 wiki 中的位置

MemoryOS 属于 [[agent-memory|LLM agent 记忆]]与 [[llm-long-term-memory|长期记忆]]主题,与 [[2023-memgpt-llms-as-operating-systems|MemGPT]](OS 式分层 context 管理)、[[memorybank|MemoryBank]](基于 [[ebbinghaus-forgetting-curve|Ebbinghaus 遗忘曲线]]的检索式记忆)、[[2023-memorybank|MemoryBank 论文]]、A-Mem(Agentic Memory)等同属一脉,但强调"操作系统式"的统一 [[memory-module|记忆模块]]与 [[memory-stream|分层存储]] + heat 驱动的更新/驱逐。它服务于个性化对话型 [[ai-assistant-agent|AI 助手]]([[role-playing-agent|persona]] 持久化),与 [[generative-agents|Generative Agents]]、[[siliconfriend|SiliconFriend]] 等长期记忆工作相关。出自 [[beijing-university-of-posts-and-telecommunications|北京邮电大学]]与 [[tencent-ai-lab|Tencent AI Lab]]。
