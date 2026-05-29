---
type: entity
subtype: product
tags: [multi-agent, llm-agent, software-development, code-generation, framework]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# MetaGPT

MetaGPT 是一个将人类标准作业程序(SOP)编码进 prompt 的 LLM 多智能体框架,通过专业化角色分工与结构化输出协作完成软件开发任务。

## 在本 wiki 中的出现

- [[2023-metagpt]]:本框架的提出来源。MetaGPT 把人类 SOP 编码进 prompt,用专业化角色与结构化输出构建 LLM 多智能体软件开发框架,在 HumanEval/MBPP 上达到 SoTA。
- [[2023-chatdev]]:同属 LLM 多智能体软件开发方向的相关工作。ChatDev 用多个 LLM 驱动的角色化软件智能体,通过对话链沿瀑布式流程协作完成设计、编码、测试、文档的完整软件开发,与 MetaGPT 的角色化协作思路相近。
- [[2024-megaagent-large-scale-mas-without-sop]]:作为对比对象提及。该工作借鉴操作系统进程/线程模型、无需预定义 SOP,可自动生成数百 agent 并行协作的大规模 LLM 多智能体系统,800 秒内开发五子棋、2991 秒协调 590 个 agent 生成国家政策。
- [[2026-self-organizing-llm-agents]]:一项 25,000 任务的大规模实验发现"内生性悖论":固定智能体顺序但角色自主的混合协议(Sequential)在质量上同时超越中心化(+14%)与完全自主(+44%)协调,但仅当底层模型足够强(存在能力门槛)。
- [[2026-orgagent-company-style-mas]]:提出公司式层级多智能体框架 OrgAgent(治理/执行/合规三层),实证表明层级组织在多数推理任务上同时提升效果并大幅降低 token 成本。

## 相关

- [[chatdev]]
- [[megaagent]]
- [[multi-agent-systems|multi-agent-system]]
- [[llm-agents|llm-agent]]
- [[standard-operating-procedure]]
- [[code-generation]]
- [[humaneval]]
- [[mbpp]]
- [[orgagent]]
