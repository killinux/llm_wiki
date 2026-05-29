---
type: source
subtype: paper
tags: [llm-agent, evaluation, benchmark, agent-evaluation, survey, ai-safety, enterprise-ai]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2507.21504
raw: raw/2507.21504.pdf
authors: [Mahmoud Mohammadi, Yipeng Li, Jane Lo, Wendy Yip]
year: 2025
---

# Evaluation and Benchmarking of LLM Agents: A Survey

这是一篇 SAP Labs 在 KDD '25 发表的综述,提出一个**二维分类法**(评测目标 × 评测过程)来组织 [[llm-agent]] 评测领域的工作,并特别强调了企业落地场景中常被忽视的挑战。

## 问题

[[large-language-models]] 驱动的 agent 能 reason、plan、调用 tool、利用 memory,并与人或其他 agent 协作,正从研究原型走向真实部署。但评测这类 agent 比评测孤立的 LLM 复杂得多:LLM 评测像"测引擎",而 agent 评测像"在各种驾驶条件下综合评估一辆车"。agent 是概率性的、在动态交互环境中行动,传统软件测试(确定性、静态)和标准 LLM 评测都不够用。现有综述要么只聚焦 LLM 评测,要么只覆盖单一能力,缺乏全局视角;企业应用带来的 role-based 数据访问、可靠性保证、合规等要求更是鲜被讨论。本文旨在为这一碎片化领域提供一个系统评估框架。

## 方法

作者提出沿两个轴组织的分类法(论文 Figure 1):

- **Evaluation Objectives(评测什么)**:
  - Agent Behavior(结果导向,把 agent 当黑箱):task completion、output quality、latency & cost。
  - Agent Capabilities(过程导向):[[tool-use]]、planning & reasoning、memory & context retention、[[multi-agent-collaboration]]。
  - Reliability:一致性(consistency)与 [[adversarial-robustness]] / robustness。
  - Safety and Alignment:fairness、harm/toxicity/bias、compliance & privacy。
- **Evaluation Process(怎么评测)**:Interaction Mode([[evaluation]] 分 static/offline 与 dynamic/online)、Evaluation Data(合成 / 真实 / 交互生成的 [[dataset]] 与 [[benchmark]])、Metrics Computation Methods(code-based、[[llm-as-judge]]、[[human-in-the-loop]])、Evaluation Tooling(OpenAI Evals、DeepEval、LangSmith 等)、Evaluation Contexts(从受控仿真到开放 web/API)。

此外用一节专门讨论企业特定挑战:Role-Based Access Control(RBAC)、可靠性保证、动态长程交互、领域合规。

## 结果

这是综述,核心产出是分类法与文献映射,而非新数字。关键要点与代表性 benchmark/指标:

- Table 1 把各评测目标对应到指标与论文:task completion 用 Success Rate、Pass@k、Progress Rate 等([[agentbench]]、[[webshop]]、SWE-bench、[[webarena]]、AppWorld、TheAgentCompany);planning/reasoning 用 T-Eval 的 reasoning metric、AgentBoard 的 Progress Rate、Step Success Rate;memory 用 LongEval、SocialBench、LoCoMo(测试 40+ 乃至 600+ 轮对话的 Factual Recall / Consistency)。
- Reliability 强调 τ-bench 的 pass^k 指标(k 次试验全部成功),作者指出当前 agent 在 retail / airline 等场景下一致性仍差。
- Robustness 引 HELM(扰动下性能下降)、WebLinX(页面结构变化时的适应)、ToolEmu(tool 失败时的恢复)。
- Safety 列举 [[realtoxicityprompts]]、CoSafe、AgentHarm、AgentDojo(prompt injection)、R-Judge 等;tool use 评测引 Gorilla 的 execution-based evaluation、Berkeley Function-Calling Leaderboard(BFCL)。
- 评测方法对比:code-based 最确定可复现但难评开放式输出;LLM-as-a-Judge(及其扩展 Agent-as-a-Judge)可扩展、适合主观任务;human-in-the-loop 是主观/安全判断的 gold standard 但昂贵难扩展。

未来方向:holistic、更真实、可扩展、且 time-/cost-bounded 的评测协议,以及 Evaluation-driven Development(EDD)与 AgentOps 式的持续在线监控。

## 在本 wiki 中的位置

本文是 [[llm-agent]] / [[autonomous-agents]] 评测方向的总览性 source,可作为理解 agent [[evaluation]] 与 [[benchmark]] 全景的入口。它把分散在 [[agentbench]]、[[webarena]]、[[webshop]] 等具体 benchmark 与 [[llm-as-judge]]、[[human-in-the-loop]]、[[tool-use]]、[[multi-agent-collaboration]] 等概念串联起来,并补充了企业 / [[ai-safety]] 视角(RBAC、合规、可靠性)。出自 [[sap-labs]],面向 [[llm-based-agents]] 的真实部署评估。
