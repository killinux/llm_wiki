---
type: source
subtype: paper
tags: [llm-agent, multi-agent-systems, agent-orchestration, agent-protocol, hierarchical-agent, self-evolution, gaia, tool-use]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2506.12508
raw: raw/2506.12508.pdf
authors: [Wentao Zhang, Liang Zeng, Yuzhen Xiao, Yongcong Li, Ce Cui, Yilei Zhao, Rui Hu, Yang Liu, Yahui Zhou, Bo An]
year: 2026
---

# AgentOrchestra:用 Tool-Environment-Agent(TEA)协议编排多智能体系统

提出 **TEA(Tool-Environment-Agent)协议**,把工具、环境、智能体统一建模为带生命周期与版本管理的一等资源,并在其上构建分层多智能体框架 **AgentOrchestra**,在 GAIA Test 上达到 89.04% 平均准确率。

## 问题

现有 [[llm-agents|llm-agent]] 系统在复杂、长时程任务上表现强劲,但已有的 agent 协议(如 Google 的 A2A、[[anthropic]] 的 MCP)在协议层面存在三大缺口:

1. **生命周期与上下文管理割裂**:没有协议标准化跨 agent 组件的、一致且带版本的执行上下文(context 散落在 prompt 和 log 中)。
2. **协议层不支持 self-evolution**:prompt 与资源被当作外部维护的资产,而非可在执行反馈下被可追溯地版本化、持续改进的组件。
3. **环境不是一等公民**:环境被下放给应用特定的运行时,而非带显式边界与约束的受管组件,导致切换 agent、复用环境、隔离并行运行退化为脆弱的胶水代码编排。

## 方法

**TEA 协议**:围绕基于协程的异步执行设计,把环境、agent、工具显式建模为受管组件。架构分三层:

- **Basic Managers**(六个):model manager(抽象异构 LLM 后端)、prompt manager、memory manager(基于 session 的并发控制持久化)、dynamic manager(运行时代码执行与序列化)、version manager(维护所有组件演化历史)、tracer(记录执行轨迹与遥测,可用于审计、调试和合成训练数据)。
- **三大核心协议**:Tool Context Protocol(TCP,扩展 MCP,自动合成 function-calling schema / 自然语言描述 / 类型安全参数 schema,带版本系统与基于向量嵌入的语义检索)、Environment Context Protocol(ECP,把计算环境形式化为带 observation/action 空间的一等组件)、Agent Context Protocol(ACP,统一 agent 注册、表示与编排)。每个协议由 context manager + server 实现,并生成一份 contract document(类比 Agent Skills)。
- **Protocol Transformations**:六类双向转换实现动态角色重配置——A2T、T2A、E2T、T2E、A2E、E2A(如把 deep researcher 工作流封装成搜索工具,或把博弈环境提升为会自适应策略的对手 agent)。
- **Self-Evolution Module**:把 prompt、tool/agent/environment/memory 代码、成功的执行解都当作可演化变量,用 [[textgrad]] 做梯度式精炼、用 self-reflection 做策略分析,优化后的组件经 version manager 自动注册为新版本。

**AgentOrchestra**:TEA 的具体实例化,是分层多智能体框架。中央 **Planning Agent** 分解用户目标、把子任务委派给专门子 agent 或 TCP 工具,采用带局部上下文所有权的分层委派(每个子任务只暴露经过筛选的工具集与局部上下文),从而把全局协调转化为有界的局部路由决策,支持树状扩展。专门子 agent 包括:Deep Researcher Agent(多引擎并行 BFS 检索)、Browser Use Agent(DOM 级与像素级浏览器/计算机操作)、Deep Analyzer Agent(多模态多步推理)、Tool Generator Agent(自动创建/检索/复用 TCP 工具)、Reporter Agent(汇总证据并生成结构化 markdown)。

## 结果

四个 benchmark 评测:[[gaia]]、HLE、AIME、GPQA-Diamond。报告 pass@1。Planning agent m=50,默认用 gemini-3-flash-preview;browser-use 用 gpt-4.1 与 computer-use-preview(4o)。Vanilla 指无 self-evolution,Evolved 指带 self-reflection 演化的变体。

- **GAIA**:Evolved 变体在 GAIA Test 上 89.04% 平均准确率;Level 2 达 85.53%、Level 3 达 81.63%。GAIA Validation 上 Evolved 达 93.33% 平均(Level1 96.23 / Level2 93.02 / Level3 88.46),超过 agent-2030 与 Alita(87.27%)及 Vanilla(89.70%)。从 Vanilla 到 Evolved 在 Validation Level 2 提升最大(+5.26 分)。
- **HLE**:Evolved 达 59.6,较 Vanilla 提升 7.97%,超过 Kimi K2.6 Thinking(54.0)、GPT-5.5 Pro(57.2)、GPT-5.4 Pro(58.7);最强系统 Claude Mythos Preview 为 64.7。
- **GPQA / AIME**(仅用 Deep Analyzer Agent 的精简设置):Evolved 在五个 backbone 上一致提升 GPQA,在四个 backbone 提升 AIME25。gpt-4.1 在 AIME24 提升 71.38%、AIME25 提升 66.65%;gpt-4o 的 AIME25 翻倍(6.67→13.34,即 +100%)。
- **子 agent 消融**(GAIA Test,Table 5):仅 Planner 36.54 → +Researcher 57.14 → +Browser 72.76 → +Analyzer 79.07 → +Tool Generator 89.04(Level 3 从 61.22 升到 81.63)。Tool Generator 在评测中自动生成 50+ 专门工具,跨后续任务复用率达 30%。
- **效率**:简单任务约 30 秒、约 5k token;中等约 3 分钟、约 25k token;复杂多模态/长时程约 10 分钟、约 100k token。

## 在本 wiki 中的位置

本文属于 [[llm-multi-agent]] / [[agent-orchestration]] 主题。其 TEA 协议与 [[anthropic]] 的 MCP、Google 的 A2A 同属 agent 协议层,但把环境与 self-evolution 提升为一等概念;分层 planner-子 agent 设计与 [[metagpt]] 等多智能体框架可对比。评测覆盖 [[gaia]] 等 agent benchmark,self-evolution 模块复用 [[textgrad]] 与 [[self-reflection]] 思路,工具检索沿用 [[tool-use]] 与语义检索范式。

- 主要实体:[[skywork-ai]](提出机构)、[[nanyang-technological-university]]、[[bo-an]]、[[gaia]]
- 主要概念:[[agent-orchestration]]、[[llm-multi-agent]]、[[multi-agent-systems]]、[[self-improvement]]、[[tool-use]]
