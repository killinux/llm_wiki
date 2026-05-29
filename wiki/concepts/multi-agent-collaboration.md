---
type: concept
subtype: method
tags: [multi-agent, collaboration, agent, LLM, software-engineering]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# 多智能体协作

多智能体协作(multi-agent collaboration)是指由多个 LLM 驱动的智能体(agent)分别承担不同角色,通过相互通信与分工来共同完成单个智能体难以独立处理的复杂任务的方法。

## 在本 wiki 中的出现

- [[2023-chatdev]]:ChatDev 把多智能体协作作为其核心机制。它用多个 LLM 驱动的角色化软件智能体(software agents),让它们通过对话链(chat chain)沿瀑布式(waterfall model)流程依次协作,覆盖设计、编码、测试、文档等阶段,从而完成端到端的软件开发。在这里,多智能体协作体现为"角色分工 + 对话驱动"的协同范式。
- [[2023-concordia-generative-agent-based-modeling]]:Google DeepMind 提出的库 Concordia,用 LLM 驱动的生成式 agent 在物理/社会/数字空间中扎根交互,通过 Game Master 控制环境,支持 Generative Agent-Based Modeling 的社会仿真与数字服务评估。
- [[2024-macrec-multi-agent-recommendation]]:清华提出的多 agent 协作推荐框架(SIGIR'24 demo),用 Manager、Analyst、Reflector、Searcher、Task Interpreter 等角色各异的 LLM agent 直接协作完成评分预测、序列推荐、解释生成与对话推荐。
- [[2024-megaagent-large-scale-mas-without-sop]]:借鉴操作系统进程/线程模型、无需预定义 SOP、可自动生成数百 agent 并行协作的大规模 LLM 多智能体系统,800 秒内开发五子棋、2991 秒协调 590 个 agent 生成国家政策。

## 相关

- [[multi-agent-systems]]:多智能体协作所依托的系统范式。
- [[role-playing-agent]]:为不同智能体分配角色(如 CEO、程序员、测试员)是多智能体协作的常见实现方式。
- [[chat-chain]]:ChatDev 中组织多智能体对话顺序的结构。
- [[llm-agent]]:多智能体协作的基本组成单元。
- [[communicative-dehallucination]]:ChatDev 在多智能体协作中用于缓解编码幻觉的沟通机制。
- [[role-playing]]:角色扮演式提示,是驱动多智能体分工的常用手段。
- [[generative-agent-based-modeling]]:用生成式 agent 群体进行社会仿真的建模范式。
- [[game-master]]:Concordia 中控制环境与协调 agent 交互的角色。
- [[standard-operating-procedure]]:多数 MAS 依赖的预定义流程,MegaAgent 则尝试摆脱它。
