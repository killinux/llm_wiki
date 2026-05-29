---
type: source
subtype: paper
tags: [llm-agents, base-agent, react, self-prompting, state-tracking, in-context-learning, chain-of-thought, alfworld, webshop]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2410.02810
raw: raw/2410.02810.pdf
authors: [Nikolai Rozanov, Marek Rei]
year: 2024
---

StateAct 是一种增强 LLM「base agent」的纯 in-context learning 方法,通过 self-prompting(每步自我提醒目标)与 chain-of-states(把状态跟踪引入推理)显著超越 ReAct,且不依赖任何额外训练数据或外部工具。

## 问题

基于 [[large-language-models]] 的智能体在交互式环境(家务机器人、在线购物、网页导航等)中越来越常用,其性能取决于底层的「base agent」(基础智能体)。当前最强的 base agent 是 [[react|react-reasoning-and-acting]](ReAct),它把 acting 与 [[chain-of-thought]] 结合;几乎所有 SOTA 方法(ActRe、AutoGuide、ADaPT 等)都构建在 ReAct 之上。

但现有改进路线大多资源密集:有的需要人工标注规则,有的需要 code-execution 环境与代码化 prompt,有的需要额外训练数据做 [[fine-tuning]] 或 [[retrieval-augmented-generation]](RAG),有的需要 test-time scaling。作者指出两个根本痛点:
1. LLM 智能体在较长交互中**无法持续遵循原始指令和目标**(goal adherence)。
2. 尽管上下文窗口变长,LLM 仍在长上下文下表现退化(long-context 退化、「haystack」问题)。

## 方法

StateAct 是工作在预训练 LLM 之上的 base agent:接收环境的文本 observation,单次 LLM 调用后输出 action,无需额外工具或资源。核心是两个机制:

- **Self-prompting(自我提示)**:让智能体在**每一轮**把目标(goal)作为指令传给自己,即每步「提醒」自己当前任务,以在长程交互中保持对主目标的追踪。
- **Chain-of-states(状态链)**:对 [[chain-of-thought]] 的扩展。不同于 ReAct 把 CoT 理解为口头「thoughts」,chain-of-states 让智能体输出可从环境推断的结构化中间预测,如 current location、current inventory、locations visited 等。

每步 LLM 被要求生成 `goal`、`state`、`thought`、`action` 四部分,action 被抽取并送回环境。这一结构与 ReAct 形态相似,因此 StateAct 可作为 ReAct 的「drop-in replacement」嵌入到 test-time scaling 等扩展方法中。方法完全基于 [[in-context-learning]],复用 ReAct 的 few-shot 交互轨迹(并修正了其中的小错误),仅额外标注 goal 与 state。

## 结果

评测环境:[[alfworld]](134 个测试样本,家务机器人,长时程、部分可观测、OOD 测试集,最长 50 步)、[[webshop]](100 样本,在线购物,最多 15 步)、Textcraft(100 样本,基于 Minecraft 的文本造物游戏,最多 40 步)。模型用 temperature 0、贪婪解码,vllm 推理。

- 整体提升:StateAct 在多 benchmark 上比 ReAct 提升 **7%–30%**(Alfworld >10%、Textcraft 30%、Webshop 7%);并在 ADaPT 的 test-time scaling 上额外带来 **12%** 提升(Textcraft)。
- Alfworld(gpt-3.5)base agent 对比(Table 1):StateAct **0.77** > ReAct 0.64 > AdaPlanner(code-prompt only)0.45 > Act 0.41;接近依赖额外数据/检索的 SOTA(AutoGuide=ReAct+RAG 0.79、ActRe=ReAct+FT 0.83、AdaPlanner code+exec 0.75、ADaPT+ReAct 0.72)。
- 多模型(Table 2,跨 Mistral-24B / Qwen2.5-7B,14B,32B / Gemma2-27B):15 个实验中 StateAct 在 13 个上胜过 ReAct。Alfworld 平均 StateAct 0.66 vs ReAct 0.58;Webshop 0.28 vs 0.26;Textcraft 0.31 vs 0.23。
- 更大/闭源模型(Table 3,Alfworld):gpt-3.5 77.04(ReAct 63.7,+13.3)、gpt-4o-mini 71.85(ReAct 68.15,+3.7)、Mixtral-8x22B 83.70(ReAct 72.59,+11.2)。
- 效率(Table 5,Alfworld,gpt-3.5):StateAct 平均 **19.11 步**完成,ReAct 31.49 步;消融去掉 goal 升至 20.09、去掉 state 22.50、去掉 thought 23.76。
- 状态跟踪准确率(Figure 6,Alfworld):完整 StateAct 达 **88%**;thoughts 与 goals 都有助于 state-tracking。
- 消融发现:在 Webshop 中加入 `thought`(CoT)反而有害(环境文本冗长易干扰),说明 CoT 并非总是有益。

## 在本 wiki 中的位置

- 直接对标与替换对象:[[react|react-reasoning-and-acting]](ReAct),StateAct 定位为新的更强 base agent。
- 所属范式:[[llm-agents]] / [[autonomous-agents]],纯 [[in-context-learning]],不依赖 [[fine-tuning]] 或 [[retrieval-augmented-generation]]。
- 关键技术:扩展自 [[chain-of-thought]](chain-of-states),与 self-prompting 协同应对长程推理与目标遵循。
- 评测基准:[[alfworld]]、[[webshop]]、Textcraft。
- 涉及模型:[[gpt-3-5]]、[[gpt-4o-mini]]、[[mistral-7b]] 系列(Mistral-Small-24B)、[[llama-2]] 之外的 Qwen2.5 / Gemma2 / Mixtral 等开源 LLM。
