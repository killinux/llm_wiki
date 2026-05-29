---
type: source
subtype: paper
tags:
  - agent-memory
  - llm-agent
  - llm-long-term-memory
  - retrieval-augmented-generation
  - knowledge-graph
  - benchmark
created: 2026-05-29
updated: 2026-05-29
arxiv: "2504.19413"
raw: raw/2504.19413.pdf
authors:
  - Prateek Chhikara
  - Dev Khant
  - Saket Aryan
  - Taranjeet Singh
  - Deshraj Yadav
year: 2025
---

# Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory

Mem0 是一个以记忆为中心的架构,从持续对话中动态抽取、整合与检索关键信息,使 [[llm-agents|llm-agent]] 在跨会话的长程对话中保持一致性,并在 LOCOMO 基准上以远低于全上下文方案的延迟与 token 成本超越多种基线。

## 问题

[[large-language-models]] 受限于固定的上下文窗口,一旦信息超出窗口便会"重置",无法跨会话持久保留用户偏好与历史事实,导致 AI 助手重复提问、自相矛盾、丢失人物设定。即便 GPT-4(128K)、o1(200K context)、Claude 3.7 Sonnet(200K)、Gemini(至少 10M tokens)等扩展了上下文长度,也只是延缓而非解决根本问题:真实对话很少保持主题连续,关键信息(如饮食偏好)常被埋没在大量无关 token 中;且单纯加长上下文不保证有效检索利用,注意力机制在远距离 token 上会退化。因此需要超越静态上下文扩展的记忆系统,选择性地存储重要信息、整合相关概念、按需检索——模拟人类认知过程。

## 方法

论文提出两套记忆架构,所有 LLM 操作均使用 [[gpt-4o-mini]] 作为推理引擎。

**Mem0(基础版)** 采用增量处理范式,管线含两个阶段:
- **抽取阶段(extraction)**:对每个新消息对 (m_{t-1}, m_t),结合两种上下文——数据库中的对话摘要 S(由异步摘要生成模块周期性刷新)与最近 m 条消息序列——构造提示 P,由 LLM 抽取函数 φ 产生候选记忆集 Ω = {ω_1, ..., ω_n}。
- **更新阶段(update)**:对每个候选事实,先用向量嵌入检索数据库中 top-s 条语义相似的已有记忆,再通过函数调用("tool call")让 LLM 自行判定四种操作之一:ADD(新建)、UPDATE(补充扩展)、DELETE(删除被新信息矛盾的记忆)、NOOP(无需修改)。利用 LLM 推理能力直接决策而非单独训练分类器。

实验中设 m=10、s=10,向量数据库使用 dense embeddings。

**Mem0^g(图记忆版)** 将记忆表示为有向带标签图 G=(V,E,L):节点 V 为实体(如 ALICE、SAN_FRANCISCO),边 E 为关系(如 lives_in),标签 L 为节点语义类型(如 Person、City)。每个实体节点含类型分类、embedding 向量与含时间戳的元数据;关系存为三元组 (v_s, r, v_d)。抽取采用两阶段:**entity extractor** 识别实体及类型,**relationship generator** 推导实体间有意义的关系三元组。整合新信息时为三元组两端计算 embedding,与现有节点按阈值 t 做相似匹配;**conflict detection** 识别冲突关系,**update resolver** 将过时关系标记为无效(而非物理删除)以支持时序推理。检索采用双策略:实体中心法(定位查询实体对应节点并探索其入/出边构建子图)与语义三元组法(整条查询编码为 dense embedding 与所有关系三元组匹配)。图数据库使用 Neo4j。

## 结果

在 [[benchmark]] **LOCOMO** 数据集上评测(10 段长对话,平均约 600 轮对话、26000 tokens,每段约 200 个问题,问题类型:single-hop / multi-hop / temporal / open-domain;对抗类问题因缺真值被排除)。评测指标含 F1、BLEU-1,以及主指标 **LLM-as-a-Judge(J)**(为应对词面相似指标无法捕捉事实正确性的缺陷,每方法跑 10 次取均值 ±1 标准差)。部署指标含 token 消耗(cl100k_base 编码)与延迟(p50/p95)。基线分六类:已建立的 LOCOMO 方法(LoCoMo、ReadAgent、MemoryBank、MemGPT、A-Mem)、开源记忆方案(LangMem)、不同 chunk size 与 k 的 RAG、全上下文、专有模型(OpenAI ChatGPT memory)、记忆管理平台(Zep)。

关键数字:
- **Single-Hop**:Mem0 最强,F1=38.72、B1=27.13、J=67.13;加图记忆(Mem0^g)无增益。A-Mem 等旧基线在 J 上落后逾 25 分。
- **Multi-Hop**:Mem0 领先,F1=28.64、J=51.15;图记忆未带来提升。
- **Open-Domain**:Zep 最高(F1=49.56、J=76.60),Mem0^g(J=75.71)以 0.89 分微弱落后为强劲第二,Mem0(J=72.93)次之。
- **Temporal**:Mem0^g 最高,F1=51.55、J=58.13;Mem0 也达 J=55.51;OpenAI 因生成记忆缺时间戳,得分低于 15%。
- **总体**:Mem0 在 LLM-as-a-Judge 指标上相对 OpenAI 提升 26%;Mem0^g 总体得分比基础 Mem0 高约 2%。
- **效率**:Mem0 search p95 延迟 0.200s、total p95 1.440s、J=66.88%、记忆 token=1764;Mem0^g total p95 2.590s、J=68.44%。相较 Full-context(26031 tokens、total p50 9.870s、p95 17.117s、J=72.90%),Mem0 实现约 **91% 更低的 p95 延迟**并节省 **逾 90% token 成本**。

结论:dense 自然语言记忆(Mem0)对简单/多跳检索效率与准确兼优;显式关系图(Mem0^g)在时序与开放域等需细粒度关系建模的任务上更有优势,二者形成互补。

## 在本 wiki 中的位置

本文属于 [[agent-memory]] 与 [[llm-long-term-memory]] 方向,为生产级 [[llm-agents|llm-agent]] 提供可扩展的持久记忆基建。其核心机制可与 [[retrieval-augmented-generation]] 对比(把整段历史做 RAG 是其主要基线之一),并以 [[gpt-4o-mini]] 为推理引擎、Neo4j 为图存储。与同类记忆系统 MemGPT、MemoryBank([[memorybank]])、A-Mem、Zep、LangMem 形成横向比较;评测主指标采用 [[llm-as-judge]]。图记忆变体延续了知识图谱式的实体-关系建模思路,可与本 wiki 中 [[generative-agents]] 的 [[memory-stream]] 等记忆机制相互参照。
