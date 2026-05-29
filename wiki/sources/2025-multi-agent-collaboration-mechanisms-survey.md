---
type: source
subtype: paper
tags: [llm-multi-agent, multi-agent-collaboration, multi-agent-systems, llm-agents, survey, agent-orchestration]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2501.06322
raw: raw/2501.06322.pdf
authors: [Khanh-Tung Tran, Dung Dao, Minh-Duong Nguyen, Quoc-Viet Pham, Barry O'Sullivan, Hoang D. Nguyen]
year: 2025
---

# Multi-Agent Collaboration Mechanisms: A Survey of LLMs

一篇系统综述,提出一个可扩展框架,沿 actors、types、structures、strategies、coordination protocols 五个维度刻画基于 [[large-language-models]] 的 [[multi-agent-systems]] 协作机制,并梳理其在 5G/6G、Industry 5.0、问答与社会文化场景中的应用。

## 问题

随着 [[large-language-models]] 的进展,Agentic AI 日益重要,[[llm-based-agents]] 借助 LLM 的推理与生成能力,并辅以 memory、planning、tool use 等模块实现自主决策与行动。然而许多现实任务过于复杂,单个 agent 无法独立完成——它们需要多样化的专业知识、并行处理与多视角整合。这推动了 [[multi-agent-systems]] 的兴起,即让多个 agent 协作完成超出任一单体能力的共同目标。本文指出,既有的 LLM agent 综述多关注 agent 本身,鲜有专门聚焦于 **协作机制(collaboration mechanisms)** 的系统性梳理,因而存在空白。

## 方法

论文提出一个可扩展框架,将 [[multi-agent-collaboration]] 沿以下关键维度进行刻画:

- **Actors**:参与协作的 agent 及其属性(profile、memory、planning、action 模块)。
- **Types(协作类型)**:cooperation(合作)、competition(竞争)、coopetition(竞合,即合作与竞争的混合)。
- **Structures(结构)**:peer-to-peer(去中心化)、centralized(由控制器/[[agent-orchestration]] 协调)、distributed/hierarchical(分布式/层级)。
- **Strategies(策略)**:rule-based(规则驱动)、[[role-playing|role-based]](角色驱动)、model-based(学习驱动)。
- **Coordination Protocols(协调协议)**:通信协议、消息传递、共享内存等。

论文进一步将协作建模为 actors、channels 与决策聚合的函数,讨论自然语言对话、[[multi-agent-debate]]、投票、协商等通信通道,并以 [[chatdev]]、[[metagpt]]、[[autogen]]、CAMEL 等具体系统为例说明编排模式。

## 结果

作为综述,本文不报告单一 benchmark 数字,而是给出结构化的领域全景与分析:

- 提出涵盖 **5 个维度**(actors / types / structures / strategies / coordination protocols)的协作刻画框架,并用其组织对现有方法的回顾。
- 系统梳理 [[multi-agent-collaboration]] 在 **5G/6G 网络**(资源分配、边缘智能)、**Industry 5.0**(人机协作制造、数字孪生)、**问答**(借 debate 提升事实性与推理)、**社会与文化领域**([[social-simulation]]、[[generative-agents]])等场景的应用。
- 总结经验教训:协作可在复杂任务上提升性能,而结构与协议设计至关重要。
- 指出开放挑战:agent 数量的可扩展性、通信开销、MAS 评估、[[hallucination]] 在 agent 间的传播、安全与信任。
- 给出未来方向:标准化 benchmark 与协议、更优的协调策略、走向集体智能(collective intelligence)。

## 在本 wiki 中的位置

本文是关于 [[llm-multi-agent]] 协作的综述性入口,可作为串联本 wiki 中各类多 agent 系统的总览。它将 [[chatdev]]、[[metagpt]]、[[autogen]] 等具体系统纳入 cooperation/competition/coopetition 与 peer-to-peer/centralized/distributed 的统一坐标系,与 [[multi-agent-debate]]、[[role-playing]]、[[agent-orchestration]]、[[multi-agent-collaboration]] 等概念页相互呼应;在应用侧又连接 [[social-simulation]] 与 [[generative-agents]]。对希望理解"为什么以及如何让多个 [[llm-based-agents]] 协作"的读者,本文提供框架级的参照。
