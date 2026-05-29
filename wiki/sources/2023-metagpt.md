---
type: source
subtype: paper
tags: [multi-agent, llm-agents, code-generation, software-engineering, sop, meta-programming]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2308.00352
raw: raw/2308.00352.pdf
authors: [Sirui Hong, Mingchen Zhuge, Jiaqi Chen, Xiawu Zheng, Yuheng Cheng, Ceyao Zhang, Jinlin Wang, Zili Wang, Steven Ka Shing Yau, Zijuan Lin, Liyang Zhou, Chenyu Ran, Lingfeng Xiao, Chenglin Wu, Jürgen Schmidhuber]
year: 2023
---

MetaGPT 是一个将人类标准作业程序(SOP)编码进 prompt 序列的 LLM 多智能体协作框架,通过给智能体分配软件公司中的专业角色并使用结构化输出,在协作式软件工程任务上生成比此前基于聊天的多智能体系统更连贯的解决方案。

## 问题

现有 LLM 多智能体系统已能解决简单的对话任务,但面对复杂任务时,由于天真地链式调用 LLM,级联的[[hallucination]]会引入逻辑不一致,使解决方案变得混乱。智能体之间通过无约束自然语言(类似"传话游戏"/Chinese whispers)沟通,经过多轮交流后原始信息容易被严重扭曲,导致"助手重复指令"或"消息无限循环"等问题。此前如 [[chatdev]]、AutoGPT、[[langchain]]、AgentVerse 等框架未能充分利用带结构化输出格式的有效工作流,难以应对复杂软件工程问题。

## 方法

- **将 SOP 编码进 prompt**:借鉴人类软件公司的标准作业程序,把复杂任务按流水线(assembly line)范式拆解为子任务,分配给具有人类领域专长的不同智能体。
- **角色专业化**:定义五种角色——Product Manager、Architect、Project Manager、Engineer、QA Engineer。每个智能体有 name/profile/goal/constraints 的 profile,并配备特定工具(如 Product Manager 用 web search,Engineer 可执行代码)。所有智能体遵循 ReAct 风格行为。
- **工作流**:Product Manager 产出含 User Stories 与 Requirement Pool 的 PRD;Architect 将其转为系统设计(File Lists、Data Structures、Interface Definitions、流程图与时序图);Project Manager 做任务分配;Engineer 写代码;QA Engineer 编写测试用例。
- **结构化通信**:用文档与图表(结构化输出)而非对话进行交流,为每个角色规定 schema 与格式。
- **发布-订阅机制(Shared Message Pool)**:智能体把结构化消息发布到共享消息池,并基于角色 profile 订阅相关消息,避免一对一通信带来的拓扑复杂性和信息过载。
- **可执行反馈(Executable Feedback)**:Engineer 在生成初始代码后编写并执行单元测试,根据历史执行与调试记忆迭代改进代码,直到测试通过或达到最多 3 次重试;这是一种运行时自我纠错机制(对应 [[reflexion]] 类自反思思路但强调可执行性)。

## 结果

- **HumanEval 与 MBPP**:用 Pass@1(unbiased Pass@k)评测。MetaGPT 取得 SoTA:HumanEval 85.9%、MBPP 87.7%。优于 [[gpt-4]](HumanEval 67.0)、Codex+CodeT(65.8/87.7)、PaLM Coder 等。无可执行反馈的版本为 HumanEval 81.7 / MBPP 82.3。
- **可执行反馈增益**:加入可执行反馈在 HumanEval / MBPP 上分别带来 +4.2% / +5.4%(绝对值)的 Pass@1 提升。
- **SoftwareDev 基准**(作者自建,70 个软件开发任务,评测时随机选 7 个):相比 [[chatdev]],MetaGPT 在 Executability 上达 3.75(接近满分 4),运行时间 503s(更短),Human Revision Cost 0.83(ChatDev 为 2.5);代价是 token 用量更高(31,255 vs ChatDev 19,292),但每行代码 token(Productivity)更低(124.3 vs 248.9)。
- **能力对比(Table 2)**:在 PRD 生成、技术设计、API 接口生成、预编译执行、基于角色的任务管理等能力上覆盖最全。
- **角色消融(Table 3)**:从仅 Engineer(1 个智能体)逐步加到 4 个角色,Executability 从 1.0 升到 4.0,Human Revision 从 10 降到 2.5,验证了多角色 SOP 的有效性。
- 在实验评估中 MetaGPT 实现 100% 任务完成率。

## 在本 wiki 中的位置

MetaGPT 是 [[llm-multi-agent]] 与 [[llm-based-agents]] 方向的代表性工作,把 [[standard-operating-procedure]] 引入多智能体协作,与 [[chatdev]] 同属"LLM 模拟软件公司"路线,但强调结构化输出而非纯对话。其可执行反馈机制可与 [[reflexion]]、[[react]] 的自纠错/推理-行动思路对照。作者将 SOP 注入类比为给 LLM 注入 [[chain-of-thought]]。常用代码生成评测基准为 [[humaneval]] 与 [[mbpp]]。作者之一 [[jurgen-schmidhuber]] 将该工作与其"meta-programming / 元学习"思想脉络相联系。
