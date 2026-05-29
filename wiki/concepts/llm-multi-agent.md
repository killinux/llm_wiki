---
type: concept
subtype: method
tags: [multi-agent, llm, collaboration, role-play, sop]
created: 2026-05-29
updated: 2026-05-29
sources: 23
---

# LLM 多智能体系统

LLM 多智能体系统(LLM Multi-Agent System)指由多个基于大语言模型的 agent 通过分工、协作与通信共同完成复杂任务的系统。

## 在本 wiki 中的出现

- [[2023-metagpt]]:MetaGPT 把人类工作流中的标准操作流程(SOP)编码进 prompt,通过为不同 agent 分配专业化角色并要求结构化输出,构建了一个 LLM 多智能体软件开发框架,在 HumanEval 与 MBPP 上达到 SoTA。
- [[2026-generative-social-simulation-validation]]:一篇系统性文献综述(AI Review 2026, 59:15),梳理 LLM 驱动的生成式 Agent-Based Models 在社会模拟中的应用,论证引入 LLM 因黑箱性、文化偏见与随机性而加剧而非缓解了 ABM 长期的"验证"难题。
- [[2025-llm-multi-agent-swarm-intelligence]]:把 agent-based modeling 中 agent 的硬编码程序替换为 GPT-4o 驱动的 prompt,在蚁群觅食与鸟群 flocking 两个经典 swarm intelligence 场景中复现并诱导涌现集体行为。
- [[2023-concordia-generative-agent-based-modeling]]:Google DeepMind 提出的库 Concordia,用 LLM 驱动的生成式 agent 在物理/社会/数字空间中扎根交互,通过 Game Master 控制环境,支持 Generative Agent-Based Modeling 的社会仿真与数字服务评估。
- [[2024-hiagent-hierarchical-working-memory]]:HiAgent 用 subgoal 作为 memory chunk 分层管理 LLM agent 的 working memory(汇总过去 observation、按需检索明细轨迹),在五个长程任务上成功率约翻倍(21→42)、context 减少 35%。
- [[2024-megaagent-large-scale-mas-without-sop]]:借鉴操作系统进程/线程模型、无需预定义 SOP、可自动生成数百 agent 并行协作的大规模 LLM 多智能体系统,800 秒内开发五子棋、2991 秒协调 590 个 agent 生成国家政策。
- [[2024-sage-self-evolving-agents]]:由 User/Assistant/Checker 三 agent 组成、结合迭代反馈、反思与基于 Ebbinghaus 遗忘曲线的记忆优化的自进化 LLM agent 框架,对小模型提升尤为显著。
- [[2024-multi-agent-tot-validator]]:将 Tree-of-Thoughts 与多智能体推理结合,新增 Thought Validator agent 过滤无效推理分支后再共识投票,在 GSM8K 上比标准 ToT 平均提升 5.6 个百分点。
- [[2024-aipatient-simulated-patient-llm-agents]]:AIPatient,一个由六个任务专用 LLM 智能体 + Reasoning RAG + 基于 MIMIC-III 真实病历构建的知识图谱驱动的模拟病人系统,EHR-QA 准确率达 94.15%、NER 知识库 F1=0.89,用户研究中匹配或优于真人模拟病人。
- [[2024-optima-optimizing-llm-multi-agent]]:OPTIMA 通过生成-排序-选择-训练的迭代范式同时优化 LLM 多智能体系统的通信效率与任务有效性,在重信息交换任务上达成 2.8x 性能提升且 token 用量不到 10%。
- [[2024-unbounded-generative-infinite-game]]:提出"生成式无限游戏"概念并实现一个角色生活模拟系统:游戏机制、叙事与角色/环境图像全部由 LLM 与 text-to-image 模型实时生成,核心创新是带 Block Drop 的 regional IP-Adapter(保证角色与环境一致性)与将多 LLM 协作能力蒸馏进 Gemma-2B 的实时游戏引擎。
- [[2024-lmagent-multimodal-agents-society]]:基于多模态 LLM 的万级规模 agents 社会,在电商场景模拟多用户的购物、社交、直播行为,复现真实 co-purchase 模式与从众等 emergent behavior。
- [[2025-multi-agent-collaboration-mechanisms-survey]]:一篇系统综述,沿 actors、types、structures、strategies、coordination protocols 五个维度刻画基于 LLM 的多 agent 系统协作机制,并梳理其跨领域应用与挑战。
- [[2025-llm-agents-cooperate-social-dilemma]]:让 ChatGPT-4o 与 Claude 3.5 Sonnet 为 iterated Prisoner's Dilemma 写出完整策略(而非逐步出招),用 evolutionary game theory / Moran process 模拟 LLM agent 群体演化,发现多数场景下侵略策略劣势、系统倾向合作,但博弈论 prompt 与 self-refine 会增强侵略策略并提高收敛到侵略均衡的风险。
- [[2025-agentsociety-large-scale-social-simulation]]:一个整合 LLM 生成式社会 agent、真实城市-社会-经济环境与大规模分布式仿真引擎的社会模拟器,支持上万 agent 并复现极化、谣言、UBI、飓风、城市可持续性五类真实社会实验。
- [[2025-coser-literary-roleplay-dataset]]:CoSER 从 771 部名著抽取 17,966 个角色的真实多角色对话构建数据集,提出 given-circumstance acting 训练与评测角色扮演 LLM,训练出的 CoSER 70B 在自有评测与多个 RPLA benchmark 上达到 SOTA。
- [[2025-llm-multi-agent-autonomous-driving-survey]]:系统综述 LLM 驱动的多智能体自动驾驶系统,按智能体交互模式与结构分类已有方法,并梳理 agent-human 交互、应用、数据集与未来方向。
- [[2025-multiagentbench]]:MultiAgentBench 与 MARBLE 框架:在六个交互式场景中评测 LLM 多智能体的协作与竞争,衡量任务完成度与协调质量,gpt-4o-mini 平均任务分最高、graph 协议在研究场景最优、认知规划使里程碑达成率提升约 3%。
- [[2025-sotopia-s4-social-simulation-system]]:面向非技术用户的快速、灵活、可扩展社会模拟系统,通过模拟引擎+RESTful API+Web UI,让研究者无需编程即可用自然语言设计、并行运行并自动评估多轮多方 LLM 社会交互。
- [[2026-agentorchestra-tea-protocol]]:提出 TEA 协议将工具/环境/智能体建模为带生命周期与版本的一等资源,并构建分层多智能体框架 AgentOrchestra,在 GAIA Test 上达到 89.04% 平均准确率。
- [[2025-agentsnet-multi-agent-reasoning]]:AGENTSNET 是一个可任意扩展的多 agent LLM 基准,借鉴分布式计算的五个经典问题(coloring、vertex cover、matching、leader election、consensus)来衡量 agent 网络在给定通信拓扑下的自组织、去中心化通信与协作推理能力,实验最多探测 100 个 agent。
- [[2025-multi-actor-genai-as-game-engine]]:Google DeepMind 的立场/架构论文,主张用游戏引擎式的 Entity-Component 架构统一支撑 Evaluationist/Dramatist/Simulationist 三类多智能体生成式 AI 用户动机,以 Concordia v2 为实例。
- [[2025-llm-collaboration-marl-magrpo]]:把多 LLM 协作建模为合作式 MARL(Dec-POMDP)并提出 Multi-Agent GRPO(MAGRPO),在写作与编码协作上微调多个 LLM;TLDR/arXiv return 达 94.5%/93.1%,HumanEval/CoopHumanEval return 达 86.7%/88.5%。

## 相关

- [[multi-agent-systems]]
- [[multi-agent-debate]]
- [[standard-operating-procedure]]
- [[role-playing]]
- [[llm-agents]]
- [[generative-agents]]
- [[code-generation]]
- [[chatdev]]
- [[agent-based-modeling]]
- [[generative-agent-based-modeling]]
- [[swarm-intelligence]]
- [[emergent-behavior]]
- [[social-simulation]]
- [[llm-agent-memory]]
