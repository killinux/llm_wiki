---
type: entity
subtype: benchmark
tags: [benchmark, agent, tool-use, evaluation]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# GAIA

GAIA 是一个面向通用 AI 助手能力的基准测试,通过需要多步推理、工具使用与网页/环境交互的真实世界问题,评估智能体系统完成复杂任务的端到端能力。

## 在本 wiki 中的出现

- [[2026-agentorchestra-tea-protocol]]:提出 TEA 协议将工具/环境/智能体建模为带生命周期与版本的一等资源,并构建分层多智能体框架 AgentOrchestra,在 GAIA Test 上达到 89.04% 平均准确率。
- [[2026-memory-in-the-age-of-ai-agents-survey]]:一篇关于智能体记忆的综述,提出 forms-functions-dynamics 三维统一分类法,整合碎片化的 agent memory 研究并汇总相关 benchmark 与开源框架。
- [[2026-experiential-reflective-learning]]:ERL:agent 反思单次任务轨迹与成败信号、提炼可迁移启发式存入持久池,新任务时按相关性检索 top-k 注入上下文,无需更新参数即可自我改进,在 Gaia2 上比 ReAct 基线提升 7.8% 成功率。

## 相关

- [[agentorchestra]]
- [[tea-protocol]]
- [[multi-agent-framework]]
- [[tool-use]]
- [[agent-memory]]
- [[react]]
- [[experiential-reflective-learning]]
