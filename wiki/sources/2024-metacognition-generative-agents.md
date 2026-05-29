---
type: source
subtype: paper
tags:
  - llm-agent
  - generative-agents
  - metacognition
  - self-reflection
  - simulation
created: 2026-05-29
updated: 2026-05-29
arxiv: "2401.10910"
raw: raw/2401.10910.pdf
authors:
  - Jason Toy
  - Phil Tabor
  - Josh MacAdam
year: 2024
---

# Metacognition is all you need? Using Introspection in Generative Agents to Improve Goal-directed Behavior

为 [[generative-agents]] 引入一个 metacognition(元认知)模块,让 agent 能够观察自身的思考过程与行动,并据此动态调整策略,从而在目标导向任务中表现更好。

## 问题

[[large-language-models]] 驱动的 [[generative-agents]](如 [[joon-sung-park]] 等人 Park et al. 的工作)已经通过 reflection、observation、planning、memory 等认知模块模拟出可信的人类行为。但 LLM 存在上下文窗口有限、泛化困难等问题,且已有 agent 往往需要被赋予明确的策略才能完成任务。本文提出问题:能否让 agent 具备"对自身思考进行思考"(thinking about thinking)的元认知能力,从而在没有预设策略的情况下自主评估进展、调整策略,并提升目标导向行为的有效性与可信度。

## 方法

作者借鉴 Daniel Kahneman 的 System 1 / System 2 双系统理论,把 metacognition 视为一种较慢、消耗大、适合内省与战略思考的 System 2 过程。核心是在 Park et al. 架构基础上新增一组名为 `meta_cognize` 的模块:

- **周期性自评**:agent 在仿真推进过程中积累 observation、memory、thought,定期回顾这些记忆与过往行动,给自己打一个数值分(score)并附上文字理由,作为 meta-thought 存入 memory。
- **触发元认知**:当 agent 发现进展不足时调用 `meta_cognize` 模块,反思如何改进表现,并周期性地自生成新的内省式问题(如"我对这个话题了解什么?""如何调整策略克服当前挑战?")来从不同视角审视目标。这一机制把更战术性的 reflect 与 plan 包含进来。
- **记忆系统**:agent 拥有短期记忆(最多 7 条、约 30 秒后遗忘,模拟人类工作记忆)与近乎无限的长期记忆。每条记忆含内容、时间戳、位置、重要性分数与类型;通过问题与记忆 embedding 的 cosine similarity 做相关性检索,本质是一种 [[retrieval-augmented-generation]] 式的记忆召回。meta-memory 会与普通记忆一起被召回,在后续对话与行动中"激发"agent 思考。
- **ReplicantLife 仿真框架**:作者自建可插拔框架 ReplicantLife,可接入任意带 HTTP 接口的 LLM(包括通过 ollama 本地托管的模型),用 world + scenario 两个 JSON 文件定义地图与 agent。支持线程并发,并通过 interview questions 在仿真结束时评估 agent。

## 结果

实验在三个场景测试:Christmas party、zombie apocalypse、murder mystery。

- **整体性能(Figure 5,1000 步、各跑 3 次)**:Full Architecture 得分 **39.20 ± 2.11**;去掉 meta 模块的 Full Architecture Without Meta 仅 **29.97 ± 8.72**;只用 meta 的 Architecture With Meta Only 为 **38.58 ± 2.72**。论文称 metacognition 模块比其它所有模块高出约 **33%**。
- **僵尸末日场景**:在 **73%** 的场景中 agent 最终无法存活;但带元认知的 agent 能自主发现"躲到无僵尸区域"的策略,并随时间适应改进。
- **评估方法**:采用 [[llm-as-judge]](参考 [[wanjun-zhong]] 之外的 Zheng et al. 工作),据称 LLM 判断与人类判断有 **80%** 一致性;评分由 believability、learning、individual goal performance、higher level cognitive performance、overall scenario performance 五项构成。评测主用 Mistral 7B,也测试了 Phi1/Phi2/Llama2/[[gpt-3-5-turbo]]/[[gpt-4]] 等,最终因速度、小模型尺寸与性能折中标准化到 Mistral。
- **实时性**:单 agent 在 RTX 4090 上每次完整请求可压到 1–2 秒;25 个 agent 时单步游戏时间约需 50 秒(随 agent 数线性增长)。
- 闭源模型(gpt-3.5-turbo、GPT-4)在 murder mystery 等涉及模拟谋杀的场景会触发安全机制,改用 Mistral 7B 等开源模型则无 prompt 拦截问题。

未来方向包括改进记忆检索(指出 cosine similarity 在高维空间会召回不相关记忆,可借鉴 KNN/重排序方案)、推理加速(Phi2、TinyLlama、PowerInfer、vLLM 的 PagedAttention 提速约 35%)、把元认知扩展到情绪、长期目标平衡等更广领域,以及将 metacognition 能力直接内建进 LLM 而非用 Python 外挂。

## 在本 wiki 中的位置

本文属于 [[llm-agents|llm-agent]] / [[generative-agents]] 方向,把 [[self-reflection]]、[[self-improvement]] 的思想抽象为更高阶的 metacognition(元认知)能力,与 [[reflexion]]、[[self-refine]] 等自我改进方法相关,并直接建立在 [[joon-sung-park]] 的 generative agents 工作之上。其记忆机制依赖 [[retrieval-augmented-generation]] 与 [[memory-stream]],评估采用 [[llm-as-judge]]。文中也引用了 [[chen-qian]] 等人的 [[chatdev]] 式多 agent 软件开发作为应用案例。
