---
type: source
subtype: paper
tags: [llm-agent, agent-memory, memory-augmentation, retrieval, recommendation, question-answering, summarization]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2503.21760
raw: raw/2503.21760.pdf
authors: [Rana Salama, Jason Cai, Michelle Yuan, Anna Currey, Monica Sunkara, Yi Zhang, Yassine Benajiba]
year: 2025
---

# MemInsight:面向 LLM Agent 的自主记忆增强

一句话:本文提出 MemInsight,一种让 [[llm-agents|llm-agent]] 自主从历史交互中挖掘语义属性并据此增强记忆表示与检索的框架,在对话推荐、问答与事件摘要三类任务上显著提升效果(LLM-REDIAL 上推荐说服力提升最高 14%,LoCoMo 上召回率比 RAG 基线高 34%)。

## 问题

[[llm-agents|llm-agent]] 依赖长期 [[agent-memory]] 来保持上下文连贯、做出个性化响应并实现自我演化。但随着交互不断累积,记忆规模迅速增长,**原始历史数据会变得嘈杂且检索困难**,尤其在长期或复杂任务中。此外,**非结构化的记忆**限制了 agent 跨任务、跨上下文整合知识的能力。已有方法大多依赖非结构化记忆或人工定义的 schema(如 A-Mem 用人工任务笔记、Mem0 提供生产级流水线),缺乏自主发现语义属性、构建结构化记忆表示的能力。因此需要一种结构化的知识表示来支撑高效检索、上下文理解与可扩展的长期记忆。

## 方法

MemInsight 包含三个核心模块(见原文 Figure 1):

- **属性挖掘(Attribute Mining)**:用一个 backbone LLM 从输入对话中自主抽取结构化、语义化的属性。挖掘遵循三个维度:
  - **视角(Perspective)**:entity-centric(针对具体条目,如电影的导演/作者/年份)与 conversation-centric(针对用户意图、偏好、情感、动机等);
  - **粒度(Granularity)**:turn-level(单轮内容)与 session-level(整段对话的宏观模式与用户意图);
  - **标注(Annotation)**:用 LLM 抽取函数 F_LLM 产生属性-值对集合 A = {(a_j, v_j)},再据此标注对应记忆实例 m_i。
- **属性优先级(Attribute Prioritization)**:分为 Basic(无序聚合)与 Priority(按与记忆的相关度排序,最重要属性排首位)两种聚合方式。
- **记忆检索(Memory Retrieval)**:两种用法——
  - **Comprehensive retrieval**:检索全部相关记忆实例及其增强信息;
  - **Refined retrieval**:从当前上下文抽取任务相关属性来引导检索,又分为 attribute-based retrieval(用属性作过滤器匹配)与 embedding-based retrieval(用 Titan Text Embedding 编码增强记忆为稠密向量,经 [[faiss]] 做 top-k 相似度检索)。

实验中属性生成使用 [[claude]] Sonnet、[[llama]] 3、[[mistral-7b]] 等;主任务的 base model 在各实验内保持一致以保证公平,Claude Sonnet 作为所有基线评估的 backbone。

## 结果

在两个基准上评测:**LLM-REDIAL**(对话电影推荐,约 1 万对话、1.1 万电影提及)与 **LoCoMo**(问答 + 事件摘要,30 段多轮对话,含 single-hop/multi-hop/temporal/open-domain/adversarial 五类问题)。

**问答(LoCoMo,F1 %)**:MemInsight(Claude-3-Sonnet, Priority, embedding-based)整体 30.1,优于 base、ReadAgent(8.5)、MemoryBank(6.2)与 RAG/DPR 基线;attribute-based 设定下 single-hop 18.0、open-domain 27.0、adversarial 58.3 均为最佳。
**问答召回(RECALL@k=5)**:MemInsight(Claude-3-Sonnet, Priority)整体 60.5,而 DPR 基线仅 26.5——**比 RAG 基线高约 34%**;multi-hop 达 75.1。

**对话推荐(LLM-REDIAL)**:attribute-based 过滤检索优于 LLM-REDIAL 模型且与 baseline 可比,同时**少检索约 90% 的记忆**(15 条 vs 144 条)。主观指标上,记忆增强使 partial persuasiveness 提升 10-11%,attribute-based 检索使 highly persuasive 推荐增加约 4%;embedding-based 检索使 highly persuasive 提升约 12%。

**事件摘要(LoCoMo,G-Eval)**:turn-level 增强提供更精确细致的事件信息,优于 baseline 与 session-level;用 Claude-3-Sonnet 做增强(配合 Llama v3 摘要)在 Relevance/Coherence/Consistency 上全面优于纯 Llama v3 增强。

**质量分析**:用 DeepEval 幻觉指标检验 Claude-3-Sonnet 生成的标注,**99.14% 的标注有对话依据(grounded)**,剩余 0.86% 多为抽象/泛化属性而非明确错误,显示高事实一致性。

## 在本 wiki 中的位置

本文属于 [[llm-agents|llm-agent]] 的 [[agent-memory]] / [[llm-long-term-memory]] 方向,与 [[memorybank]]、[[memory-module]]、[[memory-stream]] 等记忆机制条目相关,并与 [[retrieval-augmented-generation]]([[rag]])、[[dense-passage-retrieval]]([[dpr]])、[[embedding-based-retrieval]]、[[faiss]] 等检索条目互为对照——MemInsight 强调用自主属性挖掘补充传统 RAG。其评测覆盖 [[interactive-recommendation]] 类的对话推荐、[[open-domain-qa]] 与摘要,可与 [[llm-for-recommendation]]、[[llm-as-judge]](G-Eval/LLM-based 指标)等条目参照。作者来自 AWS AI(Amazon)。
