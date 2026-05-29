---
type: entity
subtype: product
tags: [framework, llm, orchestration, agent]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# LangChain

LangChain 是一个用于构建基于大语言模型(LLM)应用的开源开发框架,提供链式调用、prompt 管理、工具集成与 agent 编排等组件。

## 在本 wiki 中的出现
- [[2024-generative-agents-in-recommendation]]:Agent4Rec 用 1000 个 LLM 驱动的生成式 agent(含 profile/memory/action 模块)构建电影推荐用户模拟器,探究其能否忠实模拟真实用户行为并复现 filter bubble 与 popularity bias。
- [[2025-agentsnet-multi-agent-reasoning]]:AGENTSNET 是一个可任意扩展的多 agent LLM 基准,借鉴分布式计算的五个经典问题(coloring、vertex cover、matching、leader election、consensus)来衡量 agent 网络在给定通信拓扑下的自组织、去中心化通信与协作推理能力,实验最多探测 100 个 agent。
- [[large-language-model]]
- [[generative-agent]]
- [[retrieval-augmented-generation]]
- [[user-simulation]]
- [[multi-agent-system]]

- [[2023-metagpt]]:MetaGPT 把人类 SOP 编码进 prompt,用专业化角色与结构化输出构建 LLM 多智能体软件开发框架,在 HumanEval/MBPP 上达到 SoTA。作为同类 LLM 应用/多智能体框架,LangChain 在该工作的相关方法与生态中被提及。
- [[2023-autogen]]:微软提出的开源多 agent 框架,通过可定制、可对话 agent 之间的会话编程来构建复杂 LLM 应用。作为 LLM 应用与 agent 编排框架的代表,LangChain 与之同属相关技术脉络。
- [[2024-opencity-urban-llm-agents]]:通过 LLM 请求调度器与 group-and-distill 提示优化,把万级城市 LLM agent 模拟加速约 600 倍,使 10000 agent 的一天活动可在 1 小时内于普通硬件完成。
- [[2024-lmagent-multimodal-agents-society]]:基于多模态 LLM 的万级规模 agents 社会,在电商场景模拟多用户的购物、社交、直播行为,复现真实 co-purchase 模式与从众等 emergent behavior。
- [[2026-orchestration-multi-agent-systems]]:Skan AI 提出的编排式多 agent 系统统一架构(专门化 agent + 四单元编排层 + MCP/A2A 双通信协议 + 治理与可观测性),作为面向企业落地的工程蓝图综述,涉及 LangChain 类框架在 agent 编排中的角色。

## 相关

- [[2023-metagpt]]
- [[2023-autogen]]
- [[llm-agents|llm-agent]]
- [[multi-agent-framework]]
- [[prompt-engineering]]
- [[llm-application-framework]]
