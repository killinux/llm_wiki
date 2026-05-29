---
type: entity
subtype: product
tags: [multi-agent, software-engineering, llm-agents, code-generation]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# ChatDev

ChatDev 是一个由多个 LLM 驱动的角色化软件智能体组成的虚拟软件公司,它们通过对话协作,沿瀑布式流程完成从设计、编码、测试到文档的完整软件开发。

## 在本 wiki 中的出现

- [[2023-chatdev]]:本资料即 ChatDev 的提出工作。ChatDev 用多个 LLM 驱动的角色化软件智能体,通过对话链(chat chain)沿瀑布式流程(design、coding、testing、documenting)协作,完成完整的软件开发流程。
- [[2023-metagpt]]:MetaGPT 作为同类 LLM 多智能体软件开发框架,常与 ChatDev 并列对比。它把人类 SOP 编码进 prompt,用专业化角色与结构化输出构建框架,在 HumanEval/MBPP 上达到 SoTA。

## 相关

- [[2023-metagpt]] / [[metagpt]]:同为基于 LLM 多智能体的软件开发框架,定位与方法可对比。
- [[multi-agent-system]]:ChatDev 是 LLM 多智能体系统的代表性应用。
- [[llm-agent]]:ChatDev 中每个角色都是一个 LLM 智能体。
- [[waterfall-model]]:ChatDev 的开发流程组织方式。
- [[code-generation]]:ChatDev 的核心任务场景之一。
