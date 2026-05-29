---
type: source
subtype: paper
tags:
  - agent-memory
  - llm-agent
  - survey
  - memory-module
  - rag
  - context-engineering
created: 2026-05-29
updated: 2026-05-29
arxiv: 2512.13564
raw: raw/2512.13564.pdf
authors:
  - Yuyang Hu
  - Shichun Liu
  - Yanwei Yue
  - Guibin Zhang
  - Tao Gui
  - Ji-Rong Wen
  - Xuanjing Huang
  - Philip Torr
  - Yu-Gang Jiang
  - Shuicheng Yan
year: 2026
---

# Memory in the Age of AI Agents: A Survey — Forms, Functions and Dynamics

一篇关于 [[agent-memory]] 的综述,提出 "forms-functions-dynamics"(形态-功能-动态)三维统一分类法,把碎片化的智能体记忆研究整合为一张系统化的研究图景。

## 问题

随着 [[llm-agent]] 的能力快速扩张,memory 已成为支撑长程推理、持续适应与复杂环境交互的核心能力。但该领域日益碎片化:不同工作对 "agent memory" 的动机、实现、假设和评测协议差异巨大,而 declarative / episodic / semantic / parametric memory 等术语的泛滥进一步模糊了概念边界。作者指出传统的 long/short-term memory 分类已不足以刻画当代智能体记忆系统的多样性与动态性,且既有综述(如 Zhang et al. 2025s、Wu et al. 2025g)未能覆盖 2025 年涌现的新方向(如从过往经验蒸馏可复用工具、记忆增强的 test-time scaling)。本文围绕五个关键问题展开:agent memory 的定义及其与 [[large-language-models]] memory、[[retrieval-augmented-generation]]、[[context-engineering]] 的关系;记忆的 forms、functions、dynamics;以及未来研究前沿。

## 方法

论文首先给出 [[llm-based-agents]] 与 agent memory system 的形式化定义,把记忆建模为随时间演化的状态 M_t,并通过三个生命周期算子刻画其动态:Memory Formation(形成算子 F)、Memory Evolution(演化算子 E,含 consolidation/updating/forgetting)、Memory Retrieval(检索算子 R)。这三个算子无需在每个时间步都触发,short-term 与 long-term 记忆现象由调用的时间模式而非架构模块区分。作者还用 Venn 图厘清 agent memory 与 LLM memory、RAG、context engineering 的重叠与区别:agent memory 聚焦持续演化的认知状态。

随后沿三条主线组织全文:

- Forms(形态,第 3 节):按记忆载体分为三类。Token-level Memory(显式离散单元,可外部访问/编辑,又细分为 Flat 1D / Planar 2D / Hierarchical 3D 拓扑)、Parametric Memory(存于模型参数,含内部与外部参数记忆,如 [[model-editing]]、Retroformer)、Latent Memory(存于隐状态/连续表示,如 MemoryLLM、MemGen、VisMem,兼顾隐私与压缩密度)。
- Functions(功能,第 4 节):提出超越粗粒度时序划分的细分法。Factual Memory(陈述性知识库,回答 "agent 知道什么",含 user / environment factual memory)、Experiential Memory(过程性/策略性知识,回答 "agent 如何提升",含 case-based / strategy-based / skill-based / hybrid)、Working Memory(单任务内的有限容量工作区,回答 "agent 当下在想什么",含 single-turn 与 multi-turn)。
- Dynamics(动态,第 5 节):分析记忆如何形成、演化、检索,涵盖 semantic summarization、knowledge distillation、structured construction、latent representation、parametric internalization,以及 consolidation/updating/forgetting 与检索时机、query 构造、检索策略、post-retrieval processing。

最后第 7 节讨论前沿:memory retrieval → memory generation、自动化记忆管理、[[reinforcement-learning]] 与记忆系统结合、multimodal memory、多智能体共享记忆、记忆可信性等。

## 结果

作为综述,主要贡献是分类法与资源整合而非数值结果:

- 形态层面识别出 3 大记忆形态(token-level / parametric / latent),其中 token-level 进一步按拓扑分为 1D/2D/3D。
- 功能层面提出 factual / experiential / working 三大功能支柱。
- 动态层面用 formation / evolution / retrieval 三算子统一刻画。
- 资源整合(第 6 节):Table 8 汇总了约 35 个相关 benchmark,分为 "memory/lifelong/self-evolving 导向" 与 "其他相关" 两类。记忆导向 benchmark 含 [[locomo]](300 样本,真实对话记忆)、[[longmemeval]](500 任务,交互记忆)、MemBench(53,000 样本)、PersonaMem(180 任务,动态用户画像)、MemoryBank、LongBench / LongBench v2、RULER、BABILong、HaluMem(3,467 样本,记忆幻觉)、MM-Needle(多模态长上下文检索)、StreamBench(9,702 样本,在线持续学习)、LifelongAgentBench、Evo-Memory 等;其他相关含 [[gaia]]、[[webshop]]、[[webarena]]、[[swe-bench]] Verified、[[toolbench]]、[[alfworld]]、[[scienceworld]]、xBench-DS、GenAI-Bench 等。
- Table 9 汇总约 24 个开源记忆框架,标注其支持的记忆类型(factual/experiential)、是否多模态、核心结构与评测:[[memgpt]](分层 S/LTM)、Mem0(graph+vector)、Memobase、MIRIX、MemoryOS、MemOS(tree memory + memcube)、Zep(temporal knowledge graph)、LangMem、SuperMemory、Cognee、Memary、Pinecone、Chroma、Weaviate 等,多数在 LoCoMo 上评测。

## 在本 wiki 中的位置

本文是 [[agent-memory]] / [[memory-module]] 主题的纲领性综述,可作为理解智能体记忆研究全貌的入口。它系统区分了 agent memory 与 [[large-language-models]] memory、[[retrieval-augmented-generation]]、[[context-engineering]] 三个相邻概念,并将 [[memgpt]]、[[memorybank]]、[[hipporag]]、[[a-mem]]、[[g-memory]] 等具体系统、以及 [[locomo]]、[[longmemeval]]、[[gaia]] 等评测纳入统一坐标。其 "forms-functions-dynamics" 框架与本 wiki 中 [[llm-long-term-memory]]、[[agent-memory]]、[[self-evolving-agents]]、[[memory-evolution]]、[[memory-augmentation]] 等条目互为补充,并指向 [[reinforcement-learning]] 内化记忆管理、multimodal memory、多智能体共享记忆等前沿方向。
