---
type: source
subtype: paper
tags:
  - multi-agent-systems
  - agent-orchestration
  - mcp
  - a2a
  - enterprise-ai
  - llm-agents
created: 2026-05-29
updated: 2026-05-29
arxiv: 2601.13671
raw: raw/2601.13671.pdf
authors:
  - Apoorva Adimulam
  - Rajesh Gupta
  - Sumit Kumar
year: 2026
---

# The Orchestration of Multi-Agent Systems: Architectures, Protocols, and Enterprise Adoption

一篇来自 Skan AI 的工程蓝图式综述,把编排式(orchestrated)[[multi-agent-systems]] 的技术构成统一为一套架构框架:专门化 agent + 编排层 + 两个互补通信协议(MCP 与 A2A)+ 治理/可观测性,面向企业级落地。

## 问题

LLM 驱动的 agent 正从孤立、任务专一的单体系统,转向相互协作的 agent 生态。作者列出推动这一转向的技术动因:LLM 的 scalability 限制(上下文长度与推理瓶颈)、专门化 vs. 泛化的取舍、通信协议的进步(message-passing 抽象与 inter-agent API 标准)、以及经济效率(分布式的小 agent 集体往往胜过昂贵的全能部署)。

但简单地把多个自治 agent 连在一起并不够:缺乏编排会导致重复劳动、逻辑不一致、以及偏离目标的失控自治。本文的目标是把这类系统的技术组成形式化,并把概念架构桥接到可实现的设计原则。这是一篇综述/架构论文(arXiv cs.MA, 2026 年 1 月),不含原创实验。

## 方法

提出一个统一的编排式 MAS 架构,分层组织:

- **专门化 agent(Section IV)**:每个 agent 以 [[large-language-models]] 为认知核心。分三类——Worker Agents(执行原子任务,如 [[rag]] 流水线,可有/无状态)、Service Agents(共享工具能力:质检、合规、诊断、自愈 healing、升级调度)、Support Agents(监督与分析层:监控、分析、数据刷新)。
- **编排层(Section V)** 作为控制平面,含四个单元:Planning & Policy(目标分解 + 治理约束)、Execution & Control(分布式控制系统,管并发/依赖/优先级/遥测)、State & Knowledge Management(状态总线 + 知识库,把运行态与知识态分离)、Quality & Operations(执行后的校验与优化,schema 校验、异常检测、sandbox 部署)。
- **通信协议(Section VI)**:两个互补标准。
  - **Model Context Protocol (MCP)**:client-server 设计,标准化 agent 访问外部工具/数据/上下文,统一 schema、access control、auditability;支持有/无状态会话。提到扩展 ScaleMCP(动态同步工具清单)与 AgentMaster(把 MCP 与 A2A 集成做多模态协作)。
  - **Agent-to-Agent (A2A)**:规范 agent 之间的协商、委派、协调;peer 通信(可直连或经 orchestrator 中介),消息带结构化元数据与标准 payload,含 cryptographic signing、role-based routing 等安全控制;仍受编排层监督。
- **安全/治理/可观测性(Section VII)**:校验、监控、恢复机制;MCP/A2A 内嵌 schema 校验、鉴权交换、access control;guardrail 缓解 [[hallucination]];内部审计、事件日志、least-privilege、隐私约束(仅共享任务相关信息)。

## 结果

本文为综述,无 benchmark,主要证据来自引用的企业 case study(Section VIII):

- **BFSI(银行/金融/保险)**:自治 agent 解析保险申请与佐证文档,准确率超 **95%**;某抵押贷款机构用 Document AI + Decision AI agent,审批流程提速 **20×**,处理成本下降 **80%**。
- **软件工程/IT 现代化**:某大型银行用 agentic "digital factory" 现代化数百个遗留应用,不同 agent 分别做文档化、生成、互审、集成测试,早期采用团队的开发时间与人力减少超 **50%**。
- **跨行业**:客服场景中多达 **80%** 的常见支持事件可由 agent 无需人工解决,全 agent 工作流把解决时间压缩 **60–90%**;医疗等领域也在探索多 agent 协作。

行业信号方面提到 PwC Agent OS、Accenture Trusted Agent Huddle,以及 [[langchain]]、[[autogen]]、IBM Watsonx Orchestrate、Google Agent Development Kit 等框架。挑战与未来方向(Section IX):协调开销/消息拥塞、编排成本、去中心化自治带来的治理难题,以及 hallucination/bias/data leakage 在 agent 交互下被放大;未来聚焦 hybrid/federated 设计、语义编排、联邦学习 + 跨域协作、标准化 benchmark 与开源编排框架。

## 在本 wiki 中的位置

本文是 [[agent-orchestration]] 与 [[multi-agent-systems]] 的一份企业落地视角的工程综述,与 [[llm-multi-agent]]、[[multi-agent-collaboration]] 等主题相邻。它的独特价值在于把编排层拆成 planning/policy、execution/control、state/knowledge、quality/operations 四单元,并系统对比了两个新兴通信协议——MCP(工具访问)与 A2A(peer 协作),可与 [[agent-orchestration]]、[[tool-use]]、[[function-calling]] 等条目互链。相对于偏研究的多 agent 工作(如 [[autogen]]、[[metagpt]]、[[chatdev]]),本文更强调治理、可观测性、合规与可审计性等企业关切。
