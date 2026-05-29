---
type: concept
subtype: method
tags: [multi-agent, collaboration, agent, LLM, software-engineering]
created: 2026-05-29
updated: 2026-05-29
sources: 11
---

# 多智能体协作

多智能体协作(multi-agent collaboration)是指由多个 LLM 驱动的智能体(agent)分别承担不同角色,通过相互通信与分工来共同完成单个智能体难以独立处理的复杂任务的方法。

## 在本 wiki 中的出现

- [[2023-chatdev]]:ChatDev 把多智能体协作作为其核心机制。它用多个 LLM 驱动的角色化软件智能体(software agents),让它们通过对话链(chat chain)沿瀑布式(waterfall model)流程依次协作,覆盖设计、编码、测试、文档等阶段,从而完成端到端的软件开发。在这里,多智能体协作体现为"角色分工 + 对话驱动"的协同范式。
- [[2023-concordia-generative-agent-based-modeling]]:Google DeepMind 提出的库 Concordia,用 LLM 驱动的生成式 agent 在物理/社会/数字空间中扎根交互,通过 Game Master 控制环境,支持 Generative Agent-Based Modeling 的社会仿真与数字服务评估。
- [[2024-macrec-multi-agent-recommendation]]:清华提出的多 agent 协作推荐框架(SIGIR'24 demo),用 Manager、Analyst、Reflector、Searcher、Task Interpreter 等角色各异的 LLM agent 直接协作完成评分预测、序列推荐、解释生成与对话推荐。
- [[2024-megaagent-large-scale-mas-without-sop]]:借鉴操作系统进程/线程模型、无需预定义 SOP、可自动生成数百 agent 并行协作的大规模 LLM 多智能体系统,800 秒内开发五子棋、2991 秒协调 590 个 agent 生成国家政策。
- [[2024-agentic-feedback-loop-recommendation]]:提出 AFL,让 recommendation agent 与 user agent 通过基于 memory 的多轮文本反馈回路相互协作,同时提升推荐(平均 +11.52%)与用户模拟(平均 +21.12%),且不放大流行度/位置偏差。
- [[2025-multi-agent-collaboration-mechanisms-survey]]:一篇系统综述,沿 actors、types、structures、strategies、coordination protocols 五个维度刻画基于 LLM 的多 agent 系统协作机制,并梳理其跨领域应用与挑战。
- [[2025-llm-multi-agent-autonomous-driving-survey]]:系统综述 LLM 驱动的多智能体自动驾驶系统,按智能体交互模式与结构分类已有方法,并梳理 agent-human 交互、应用、数据集与未来方向。
- [[2025-multiagentbench]]:MultiAgentBench 与 MARBLE 框架:在六个交互式场景中评测 LLM 多智能体的协作与竞争,衡量任务完成度与协调质量,gpt-4o-mini 平均任务分最高、graph 协议在研究场景最优、认知规划使里程碑达成率提升约 3%。
- [[2025-agentsnet-multi-agent-reasoning]]:AGENTSNET 是一个可任意扩展的多 agent LLM 基准,借鉴分布式计算的五个经典问题(coloring、vertex cover、matching、leader election、consensus)来衡量 agent 网络在给定通信拓扑下的自组织、去中心化通信与协作推理能力,实验最多探测 100 个 agent。
- [[2025-llm-agent-evaluation-survey]]:SAP Labs 的 LLM agent 评测综述,提出"评测目标 × 评测过程"二维分类法,并强调企业落地中的可靠性、合规与 RBAC 等挑战。
- [[2025-llm-collaboration-marl-magrpo]]:把多 LLM 协作建模为合作式 MARL(Dec-POMDP)并提出 Multi-Agent GRPO(MAGRPO),在写作与编码协作上微调多个 LLM;TLDR/arXiv return 达 94.5%/93.1%,HumanEval/CoopHumanEval return 达 86.7%/88.5%。

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
- [[coordination-protocol]]:多 agent 协作中约束通信与协调的协议(如 graph/star/chain)。
- [[multi-agent-reinforcement-learning]]:把多 LLM 协作建模为合作式 MARL 的视角。
- [[agent-evaluation]]:衡量多智能体协作质量的评测方法与基准。
