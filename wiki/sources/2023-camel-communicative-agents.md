---
type: source
subtype: paper
tags: [multi-agent, role-playing, autonomous-agents, llm-agents, instruction-data, cooperation]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2303.17760
raw: raw/2303.17760.pdf
authors: [Guohao Li, Hasan Abed Al Kader Hammoud, Hani Itani, Dmitrii Khizbullin, Bernard Ghanem]
year: 2023
---

CAMEL 提出用"角色扮演(role-playing)"框架,让两个 LLM 智能体(AI User 与 AI Assistant)在一套 inception prompting 引导下自主对话、协作完成任务,从而研究大规模语言模型"社会"的协作行为,并自动生成大规模指令/对话数据。

## 问题

让 LLM 自主完成复杂任务通常仍高度依赖人工在每一步进行提示与纠偏(human-in-the-loop),这既费力又难以扩展。作者关注的核心问题是:能否让多个对话式智能体在**最少人工干预**下自主协作、保持目标对齐、并完成一个由人类给出的初始 idea?这其中存在若干挑战,例如角色翻转(智能体偏离自己被指派的角色)、对话偏离任务、过早终止、以及无限重复/卡死等。

## 方法

- **角色扮演框架(role-playing)**:把任务拆给两个智能体——[[ai-user-agent]](给出指令、扮演"用户/任务发起方")与 [[ai-assistant-agent]](执行指令、给出解决方案)。两者通过多轮对话推进,直到任务完成。
- **任务具体化(task specifier)**:人类只提供一个宽泛的 idea,由一个 task specifier 智能体把它细化成更具体、可执行的任务描述,降低人工设计提示的成本。
- **[[inception-prompting]]**:用于"植入"角色与协作规则的提示工程方法。通过 assistant 系统提示与 user 系统提示,约束双方各自扮演的角色、协作目标、输出格式与终止条件,从而抑制角色翻转、跑题和过早结束等失败模式。
- **critic-in-the-loop**:可选地引入一个 critic 智能体(可由 AI 或人类充当),从候选回复中筛选或提供反馈,实现类似树搜索的决策。
- 该框架是 [[multi-agent-systems]] / [[autonomous-agents]] 思路的代表性早期工作,核心目标之一是利用 [[role-playing]] 自动产出可用于研究与训练的 [[instruction-tuning]] 数据。

## 结果

- **数据生成**:用两个 [[gpt-3-5-turbo]] 智能体生成多个数据集。AI Society 用了 50 个 assistant 角色、50 个 user 角色、每种角色组合 10 个任务,共 **25,000 段对话**;另含 Code、Math、Science 以及一个用于演示风险的 Misalignment 数据集。终止条件包括 user 连续 3 轮不下指令、出现角色翻转、收到 `<CAMEL_TASK_DONE>` token、达到 token 上限,以及每段对话**最多 40 条消息**。
- **智能体评测(Table 1)**:把 CAMEL 多智能体协作产出的解(经 GPT4 汇总)与 [[gpt-3-5-turbo]] 单次(single-shot)解对比。
  - AI Society 人类评测:CAMEL 胜 **76.3%**,gpt-3.5-turbo 胜 10.4%,平局 13.3%(共 453 份回应)。
  - AI Society 的 [[gpt-4]] 评测:CAMEL 胜 **73.0%**,gpt-3.5-turbo 胜 23.0%,平局 4.0%。
  - Code 的 GPT4 评测:CAMEL 胜 **76.0%**,gpt-3.5-turbo 胜 24.0%,平局 0.0%。
- **知识涌现(Table 2)**:在 CAMEL 生成的数据上**渐进式微调** [[llama]](7B),按 AI Society → Code → Math → Science 顺序逐步加入数据集,模型在新加入的领域上表现持续提升,呈现能力涌现。
- **代码能力(Table 3)**:最终的 CAMEL-7B(LLaMA-7B 在全部数据上微调)在 [[humaneval]] / HumanEval+ 上 pass@1 分别为 **14.0% / 12.2%**,pass@100 为 **57.9% / 50.0%**,优于 LLaMA-7B(10.5% / -)与 Vicuna-7B(11.0% / 9.9%);作为参考,gpt-3.5-turbo 为 69.4% / 61.7%(pass@1)。

## 在本 wiki 中的位置

CAMEL 是 LLM [[autonomous-agents]] 与 [[multi-agent-systems]] 方向的奠基性工作之一,与同期的 AutoGPT、Generative Agents 等思路相呼应,把"两个 LLM 互相对话以自主完成任务"系统化为可复现的 [[role-playing]] 框架,并通过 [[inception-prompting]] 解决协作对齐问题。它也是用 LLM 自动合成 [[instruction-tuning]] 数据这一范式的重要案例,后续被大量 agent / 数据合成工作引用。
