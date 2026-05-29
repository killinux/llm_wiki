---
type: source
subtype: paper
tags: [multi-agent, llm-agent, code-generation, software-engineering, role-playing]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2307.07924
raw: raw/2307.07924.pdf
authors: [Chen Qian, Wei Liu, Hongzhan Lin, Nuo Chen, Yufan Dang, Jiahao Li, Cheng Yang, Weize Chen, Yusheng Su, Xin Cong, Juyuan Xu, Dahai Li, Zhiyuan Liu, Maosong Sun]
year: 2023
---

ChatDev 提出一个由多个 [[llm]] 驱动的“软件智能体”组成的虚拟软件公司框架,通过自然语言对话沿瀑布式流程协作完成设计、编码、测试、文档撰写的完整软件开发生命周期。

## 问题

软件开发是需要多种技能协作的复杂任务。以往工作多用深度学习改进瀑布模型(waterfall model)中的单个开发阶段(需求分析、设计、编码、测试等),但每个阶段的深度学习模型需要各自独立的设计,导致跨阶段的技术不一致、整个开发流程碎片化且低效。同时,直接用 LLM 一步把文本需求转成可用软件存在编码幻觉(coding hallucination)问题——生成的代码不完整、不可执行或与需求不符,需要大量人工干预。如何用 LLM 把整个开发流程统一在一个基于语言的协作框架中、并缓解编码幻觉,是本文要解决的问题。

## 方法

ChatDev 是一个 chat-powered 的软件开发框架,核心机制包括:

- **Chat Chain(对话链)**:把开发过程沿瀑布模型拆成顺序的三个阶段——设计(design)、编码(coding)、测试(testing,另含文档环节);编码阶段细分为代码编写与代码补全(code complete),测试阶段细分为代码评审(code review,静态测试)与系统测试(system testing,动态测试)。每个子任务由两个具不同社会角色的智能体进行多轮对话求解,前一子任务的输出作为后一子任务的输入。
- **双智能体角色专精(role specialization)**:每个子任务由一个指令者(instructor)与一个助手(assistant)组成,通过 inception prompting / 系统提示赋予角色,如 CEO、CTO、程序员(programmer)、评审员(reviewer)、测试员(tester)等。这种双智能体设计避免了复杂的多智能体拓扑,简化共识达成过程。
- **记忆(memory)**:区分短期记忆(short-term memory,维持单阶段内对话连续性)与长期记忆(long-term memory,仅传递各阶段的解决方案以跨阶段保持上下文,避免信息过载)。
- **沟通式去幻觉(communicative dehallucination)**:通过“角色反转”,让助手在给出正式回复前主动向指令者索取更具体的信息(如外部依赖的精确名称),再进行精确优化,以缓解编码幻觉。

底层模型(backbone)使用 ChatGPT-3.5(gpt-3.5-turbo),temperature 设为 0.2,集成 Python-3.11.4 提供反馈。子任务在连续两次代码无修改、或达到 10 轮沟通后终止。这一范式无需为每个阶段训练专门模型。相关概念见 [[multi-agent-collaboration]]、[[role-playing-agent]]、[[chat-chain]]、[[communicative-dehallucination]]、[[llm-agent]]。

## 结果

- 评测使用作者构建的 **SRDD(Software Requirement Description Dataset)**,涵盖 Ubuntu、Google Play、Microsoft Store、Apple Store 等平台的软件类别,共 1,200 条软件任务提示,分为 Education、Work、Life、Game、Creation 5 大类、40 个子类,每子类 30 条。
- **整体性能**(Table 1,均为全任务平均):ChatDev 完整性 Completeness 0.5600、可执行性 Executability 0.8800、一致性 Consistency 0.8021、综合 Quality 0.3953,在四项指标上均超过基线 GPT-Engineer(单智能体,Quality 0.1419)和 MetaGPT(Quality 0.1523);相比 MetaGPT,Quality 从 0.1523 提升到 0.3953。
- **配对评测**(Table 2):面对 MetaGPT,GPT-4 评判下 ChatDev 胜率 57.08%,人类评判下胜率 88.00%;面对 GPT-Engineer,人类评判下胜率 90.16%。
- **效率统计**(Table 3):ChatDev 平均耗时 148.2148 秒,消耗约 22,949.4450 tokens,生成 4.39 个代码文件、144.3450 行代码;多智能体范式虽比单智能体更慢、token 更多,但生成的代码库更大、功能更完整。
- **消融实验**(Table 4):去掉对话链各阶段、去掉沟通式去幻觉(CDH)或去掉角色设定都会降低软件质量;其中移除所有智能体角色对性能影响最大(Quality 降至 0.2212),验证了多智能体协作与角色分配的关键作用。
- **沟通分析**:自然语言沟通占 57.20%;评审阶段最常见的建议是 "Method Not Implemented"(34.85%),测试阶段最常见的报错是 "ModuleNotFoundError"(45.76%)。

## 在本 wiki 中的位置

本文是 LLM 多智能体协作(multi-agent)在软件工程领域的代表性工作,与 [[role-playing-agent]]、[[llm-agent]] 等 LLM 智能体方向密切相关,可与 [[chain-of-thought]] 等推理增强方法以及 MetaGPT、GPT-Engineer 等自动化代码生成研究对照阅读。由 [[tsinghua-nlp]] 等团队提出,开源于 [[openbmb]] 的 ChatDev 项目。
