---
type: source
subtype: paper
tags: [hallucination, rag, reasoning, agentic-system, survey, chain-of-thought, tool-use, symbolic-reasoning, benchmark]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2510.24476
raw: raw/2510.24476.pdf
authors: [Yihan Li, Xiyuan Fu, Ghanshyam Verma, Paul Buitelaar, Mingming Liu]
year: 2025
---

# Mitigating Hallucination in Large Language Models (LLMs): An Application-Oriented Survey on RAG, Reasoning, and Agentic Systems

一篇以"能力增强"为分析视角的综述,系统梳理 RAG、推理增强及二者整合的 Agentic System 如何分别缓解 knowledge-based 与 logic-based 两类 [[hallucination]]。

## 问题

[[hallucination]](幻觉)指模型生成看似合理但与事实不符、逻辑不一致或偏离用户意图的内容,是 [[large-language-models]] 在高风险场景(医疗、法律、科研、金融)可靠部署的核心障碍。现有综述多从成因、分类或生命周期阶段切入,或孤立分析单一缓解技术,缺乏从**能力增强**角度的系统性梳理:即如何通过提升模型的知识获取、推理与规划能力来减少幻觉。

作者提出一个面向缓解的二分 taxonomy:
- **Knowledge-based hallucination**(知识型):涉及客观事实错误(如虚构人名、错误年代、不存在的术语),可借助数据库、文献核实修正。
- **Logic-based hallucination**(逻辑型):前提正确但推理、推导或归纳过程有缺陷(如数学推导错误、循环论证、因果混淆、代码逻辑不一致)。

## 方法

综述围绕三条能力增强路径展开,核心原则是"不改架构、不加正则,而是通过外部知识 grounding 与逻辑一致性约束增强可靠性":

- **[[retrieval-augmented-generation]](RAG)缓解 knowledge-based 幻觉**:沿检索 pipeline(pre-retrieval / retrieval / post-retrieval)梳理关键技术。pre-retrieval 包括 query rewrite、辅助模型、多轮对话、检索反馈以增强意图理解;retrieval 涵盖 sparse / dense / hybrid 三类 retriever(BM25、[[dense-passage-retrieval]]、ColBERT)、检索粒度、[[learning-to-rank]] 与神经 reranking、文档预处理(如 [[longllmlingua]] 压缩);post-retrieval 涉及知识整合方式(input/intermediate/output-level integration)、知识冲突处理、post-hoc checking、traceability。进一步分为 **Precise Retrieval**([[graphrag]]、KG-RAG 如 [[gnn-rag]]、Hybrid RAG)与 **Broad Retrieval**(cross-domain 泛化、长上下文理解、AIGC 内容识别、[[web-search]]、multi-modal RAG 如 MuRAG/VisRAG)。
- **推理增强缓解 logic-based 幻觉**:对比三种 test-time 推理范式——[[chain-of-thought]](CoT,含 [[self-consistency]]、Natural Program、reasoning path supervision)、[[tool-use]]/Tool-augmented Reasoning(如 [[react-reasoning-and-acting]]、[[toolformer]]、[[program-of-thought]] PoT)、Symbolic Reasoning(神经符号,如 ChatLogic、Logic-LM、SymbCoT)。
- **Agentic System 整合**:将 agentic system 定义为"至少配备推理能力与检索模块的 LLM",通过 retrieval 做 factual grounding + 结构化推理做逻辑一致性,统一缓解 **composite hallucination**。代表系统包括 Agentic Reasoning(Mind-Map Agent + Web-Search Agent)、MA-RAG(多智能体)、HM-RAG(层次化多模态)、[[swe-bench]] 类的 SWE-agent、AI Scientist-v2(Agentic Tree Search)。

## 结果

本文为综述,不含原创实验数字,而是汇总技术脉络并整理 benchmark 评测维度(Table III):

- **Knowledge-based benchmarks**:[[truthfulqa]](817,问答,内在知识,Accuracy/人工)、MedHallu(10,000,医疗问答,RAG,F1)、RAGTruth(18,000,QA/数据到文本,RAG,人工)、[[freshqa]]、HalluLens(区分 intrinsic / extrinsic 幻觉)。
- **Logic-based benchmarks**:[[big-bench]](200,逻辑推理,F1/Accuracy)、[[prontoqa]](40,000,CoT,Accuracy)、ToolBench(16,464,API 调用,Accuracy)、LogicBench(rule-based,Accuracy)、ProofWriter、ReClor、LogiQA。
- **Composite benchmarks**:[[agentbench]](17,000,八类交互环境,Accuracy)、L-MARS(200,法律多轮问答)、InfoDeepSeek(245,Web 环境检索,F1/人工)、R-Judge(交互风险)。

核心结论与挑战:RAG 缓解知识幻觉但严重依赖检索质量,检索失败本身会成为新的幻觉源;CoT 缺乏可验证的逻辑 grounding,且面临 "overthinking" 风险;Agentic System 潜力大但多为 ad hoc 拼接,检索与推理常顺序而非协同执行,存在 error propagation 与计算开销问题。作者呼吁建立 RAG + 推理协同进化、带多维检测/验证/纠错机制的统一框架。

## 在本 wiki 中的位置

本文是 [[hallucination]] 缓解领域的综述类 source,横跨 [[retrieval-augmented-generation]]、[[chain-of-thought]]、[[tool-use]]、symbolic reasoning 与 [[llm-agent]]/agentic system 多个方向,可作为连接"事实性增强(RAG)"与"推理增强(CoT/工具/符号)"两条线索的总览节点。其提出的 knowledge-based vs logic-based vs composite 幻觉三分法,以及对应的 benchmark 清单([[truthfulqa]]、[[prontoqa]]、[[agentbench]] 等),为本 wiki 中 [[evaluation]] 与 [[ai-safety]] 相关条目提供分类与索引参考。
