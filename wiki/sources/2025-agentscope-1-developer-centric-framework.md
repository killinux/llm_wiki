---
type: source
subtype: paper
tags: [llm-agent, agent-framework, react, multi-agent-systems, tool-use, mcp, agent-orchestration]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2508.16279
raw: raw/2508.16279.pdf
authors: [Dawei Gao, Zitao Li, Yuexiang Xie, Weirui Kuang, Liuyi Yao, Bingchen Qian, Zhijian Ma, Yue Cui, Haohao Luo, Shen Li, Lu Yi, Yi Yu, Shiqi He, Zhiling Luo, Wenmeng Zhou, Zhicheng Zhang, Xuguang He, Ziqian Chen, Weikai Liao, Farruh Isakulovich Kushnazarov, Yaliang Li, Bolin Ding, Jingren Zhou]
year: 2025
---

# AgentScope 1.0: A Developer-Centric Framework for Building Agentic Applications

一句话:AgentScope 1.0 是 [[alibaba]] 推出的以开发者为中心的 [[llm-agent]] 框架,以 [[react-reasoning-and-acting]] 范式为核心,通过异步设计、细粒度工具/MCP 管理、内置 agent、评估与运行时沙箱,系统性支持灵活高效的工具化 agent-环境交互。

## 问题

随着 [[large-language-models]] 的 [[tool-use]](tool-calling)能力增强,LLM-based agent 的重心已从单纯依赖内在推理转向"感知环境 + 用一组工具与环境交互"。要把这种能力工程化落地,需要一个既灵活又高效的框架,但现有方案在以下方面存在不足:

- 缺乏对异构模型/协议(如各家 LLM API、[[function-calling]]、MCP)的统一抽象,开发者需为每个 provider 重复适配。
- 工具数量增多时出现 "paradox of choice",过多工具反而降低 agent 选对工具的成功率,并占用宝贵 context。
- 缺少对实时交互(人类中途打断/引导 agent)、并行工具调用、状态持久化、长轨迹可观测/可追踪的工程化支持。
- 长轨迹 agentic 应用的开发、评估、部署与安全执行缺乏配套工具链。

## 方法

AgentScope 1.0 围绕 [[react-reasoning-and-acting]] 范式构建,分四层:

- **Foundational Components(基础组件)**:抽象为 message、model、memory、tool 四个强解耦模块。message 用 `ContentBlock`(文本/图像/音频/视频/tool_use/tool_result/thinking)统一多模态;model 基于 `ChatModelBase` 统一 OpenAI、DeepSeek、vLLM、DashScope、[[anthropic]]、[[gemini]]、Ollama 等 provider,支持流式、异步调用、统一 `ChatResponse`、usage 追踪与 `@trace_llm` 分布式 tracing;memory 分短期(`InMemoryMemory`)与长期([[agent-memory]],`LongTermMemoryBase`,并给出基于 Mem0 的 `Mem0LongTermMemory` 实现);tool 以 `Toolkit` 统一注册/执行函数与 MCP,提供 stateful/stateless MCP client 与 **group-wise tool management**(按需激活工具组以缩小选择空间)。
- **Agent-level Infrastructure**:ReAct agent 提供 Reply / Observe / Handle Interrupt 三大功能;支持基于 asyncio cancellation 的 **real-time steering**(把中断当作可观测事件存入 memory)、**parallel tool calling**(单步多工具并发)、**dynamic tool provisioning**(`reset_equipped_tools` 动态激活工具组)、基于 `StateModule` 的状态持久化,以及非侵入式 hook 系统(reply/observe/reasoning/acting/print 的前后钩子)。内置三类 agent:Deep Research Agent([[deep-research-agent]],query 扩展/[[reflection]]/总结)、Browser-use Agent(基于 Playwright MCP 的网页自动化)、Meta Planner([[agent-orchestration]],分层任务分解 + 动态 worker agent 调度)。
- **Multi-Agent**:支持 "agent as a tool"、pipeline(顺序/条件/循环)与 `MsgHub`(广播式群聊)两种多智能体编排方式。
- **Developer-Friendly Experience**:Evaluation 模块(Task/Solution/Metric/Benchmark 抽象,`GeneralEvaluator` 顺序调试 + 基于 [[ray]] 的 `RayEvaluator` 分布式并行,支持断点续跑与 bootstrapping 置信区间);Studio 可视化平台(基于 OpenTelemetry 的 chatbot 式对话与 trace,以及内置 copilot "Friday");Runtime 运行时(Engine 一键 `deploy` 生成 FastAPI 服务并支持 Google A2A 协议;Sandbox 提供 Filesystem/Browser/Training 等隔离环境保障安全工具执行)。

整套框架强调强模块解耦、异步设计与可扩展性,均为纯工程框架(无新模型训练)。

## 结果

本文是框架/系统论文,不以 benchmark 数字为主,主要贡献与可量化特性包括:

- 统一集成 5 类 LLM provider(OpenAI/DeepSeek/vLLM、DashScope、Anthropic、Gemini、Ollama),全部支持 Streaming / Tools / Vision / Reasoning 四项能力(Table 1)。
- `Toolkit` 提供 register/execute/remove/get_json_schemas、MCP client 注册、以及 create/update/remove tool group 等接口(Table 2),实现细粒度工具与 MCP 管理。
- 提供并行工具调用、real-time steering(可中断/可恢复)、动态工具配置、状态持久化与 hook 等工业级特性,降低长轨迹 agentic 应用的延迟与开发成本。
- 给出 user-assistant 对话、多智能体对话(MsgHub + pipeline)、Deep Research、Browser-use(示例中成功用 Google 检索阿里巴巴股价)、Meta Planner(生成 roadmap 并调度 worker)等 signature applications 的可运行示例与开源实现。
- 代码开源:https://github.com/agentscope-ai/agentscope ,运行时为 agentscope-runtime。

## 在本 wiki 中的位置

AgentScope 1.0 属于 [[llm-agent]] / [[multi-agent-systems]] 的 agent 框架一脉,与 [[autogen]]、[[metagpt]]、[[langchain]]、[[aios-foundation]] 等 [[agent-orchestration]] 框架并列,核心采用 [[react-reasoning-and-acting]] 范式并深度整合 [[tool-use]]、[[function-calling]] 与 MCP。其 memory 设计关联 [[agent-memory]] / [[memory-module]] / [[llm-long-term-memory]],内置 [[deep-research-agent]] 与浏览器 agent 关联 [[webarena]]/[[mind2web]] 类网页智能体研究,Meta Planner 关联 [[llm-planning]]。出品方 [[alibaba]] 同系工作还包括 AgentScope 早期版本(very large-scale multi-agent simulation,Pan et al.)与 Kimas/[[concordia]] 等多智能体系统。
