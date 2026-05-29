---
type: source
subtype: paper
tags: [multi-agent, llm-agents, framework, orchestration, tool-use]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2308.08155
raw: raw/2308.08155.pdf
authors: [Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Beibin Li, Erkang Zhu, Li Jiang, Xiaoyun Zhang, Shaokun Zhang, Jiale Liu, Ahmed Awadallah, Ryan W. White, Doug Burger, Chi Wang]
year: 2023
---

AutoGen 是微软研究院等提出的开源框架,通过让多个可定制、可对话的 agent 相互对话来构建下一代 LLM 应用,把复杂任务编排表达为「多 agent 会话编程(conversation programming)」。

## 问题

基于大型语言模型(LLM)的应用越来越多地需要在解决任务的多个步骤中与 LLM 反复交互,并整合工具、人类反馈与其它能力。然而:

- 单一的、整体式(monolithic)的 LLM 调用难以处理需要多步推理、工具调用、代码执行与人在回路(human-in-the-loop)的复杂任务。
- 不同任务对 agent 的角色、能力组合与交互流程差异很大,缺少一个统一、可复用、可灵活定制的编程抽象来开发这类应用。
- 工作流既包含确定性的控制逻辑,又包含由 LLM 驱动的、不确定的自然语言决策,二者难以在同一框架内自然融合。

论文要回答的核心问题:能否用一个通用框架,把「多个 agent 之间的对话」作为构建 LLM 应用的基本范式,从而以最小代价实现多样化、高效的复杂任务求解?

## 方法

AutoGen 的核心是**可对话(conversable)且可定制(customizable)的 agent**,以及围绕 agent 间对话的编程范式。

- **统一的 agent 抽象(ConversableAgent)**:每个 agent 都能发送/接收消息并据此生成回复。一个 agent 的能力来自三类可组合后端:LLM(语言模型)、人类输入(human-in-the-loop)、以及工具/代码执行;可以任意组合与开关。
- **内置 agent 类型**:`AssistantAgent`(由 LLM 驱动,擅长写代码/推理)与 `UserProxyAgent`(代表用户,可自动执行代码、调用工具或征询人类输入),二者对话即可完成「LLM 出方案、proxy 执行并反馈」的闭环。
- **会话编程(conversation programming)**:开发者用两个维度来编排应用——(1)定义各 agent 的角色与能力;(2)用编程+自然语言混合的方式编写对话驱动的控制流(如何回复、何时终止、是否转交人类、是否调用工具)。
- **灵活的对话模式**:支持两 agent 对话、顺序对话、层级对话,以及由 `GroupChatManager` 协调的**动态群聊(dynamic group chat)**——由一个管理者根据上下文动态决定下一个发言的 agent。
- **统一接口与自动回复机制**:通过注册的自定义回复函数,把确定性逻辑与 LLM 决策融合进同一对话循环,实现自动化的工具使用与多轮协作。

## 结果

论文通过六类应用展示框架的通用性与有效性(均基于 GPT-3.5 / GPT-4 等 [[gpt-4]] 类模型):

- **数学问题求解**:在 [[math-dataset]] 上,用 AutoGen 的内置 agent(AssistantAgent + UserProxyAgent,带代码执行)相比多种基线(如纯模型、开源工具增强方案)取得更高的正确率,展示了「LLM 出解 + 自动执行验证」的优势。
- **检索增强对话(retrieval-augmented chat)**:基于 [[rag]] 的对话式问答,AutoGen 的 RetrieveChat 在文档问答中改善了回答质量,并能通过交互式检索处理上下文不足的情况。
- **决策制定 / ALFWorld**:在 [[alfworld]] 文本具身环境中,把 [[react]] 风格的 agent 与一个额外的「grounding agent」结合,显著提升任务成功率(相较单一 ReAct agent 减少了因常识缺失导致的失败)。
- **多 agent 编程(OptiGuide)**:用多 agent 协作回答供应链优化中的「what-if」问题,相比单一 agent 方案在正确率与代码量/可维护性上更优。
- **对话式国际象棋**:两个棋手 agent 加一个棋盘 agent 进行合法性校验,展示了带工具校验的对话能够保证动作合法、对话连贯。
- **动态群聊**:在需要多角色协作的任务上,动态群聊(由管理者选择下一发言者)优于固定顺序/预定义流程的编排。

整体结论:多 agent 会话作为统一范式,能用更少的代码实现多样化的复杂 LLM 应用,并在多个任务上优于单 agent 或固定流程的基线。

## 在本 wiki 中的位置

本文是 [[multi-agent-systems]] 与 [[llm-agent]] 方向的代表性框架工作,把 [[agent-orchestration]] 抽象为 agent 间对话,与 [[tool-use]]、[[human-in-the-loop]]、[[code-execution]] 等概念紧密相关。它建立在 [[react]] 等单 agent 推理-行动范式之上,并常与 [[rag]] 检索增强结合使用。作为产品/框架,可与 [[langchain]] 等 LLM 应用开发栈对照阅读;由 [[microsoft-research]] 主导。
