---
type: concept
subtype: method
tags: [social-simulation, agent-based-model, llm-agents, validation]
created: 2026-05-29
updated: 2026-05-29
sources: 18
---

# Social Simulation

社会模拟(Social Simulation)是借助计算模型(尤其是基于 Agent 的模型,Agent-Based Models / ABM)来再现和研究个体交互如何涌现出宏观社会现象的方法;近年趋势是用 LLM 驱动生成式 Agent,以期获得更贴近真实人类行为的模拟。

## 在本 wiki 中的出现

- [[2026-generative-social-simulation-validation]]:一篇系统性文献综述(AI Review 2026, 59:15),梳理 LLM 驱动的生成式 Agent-Based Models 在社会模拟中的应用,论证引入 LLM 因黑箱性、文化偏见与随机性而加剧而非缓解了 ABM 长期的"验证"难题。
- [[2024-limits-of-agency-in-agent-based-models]]:提出 LLM archetypes——为少数代表性 agent 类型查询 LLM 行为再概率采样到个体,从而在百万级 ABM 仿真(NYC 840 万人 COVID-19)中保持规模的同时引入 LLM 自适应行为。
- [[2024-opencity-urban-llm-agents]]:通过 LLM 请求调度器与 group-and-distill 提示优化,把万级城市 LLM agent 模拟加速约 600 倍,使 10000 agent 的一天活动可在 1 小时内于普通硬件完成。
- [[2024-generative-agents-self-reports]]:用基于真人深度访谈与问卷自述构建的 generative agents,可对单个个体在多种社会科学结果上做通用模拟,留出题目预测精度接近个体两周后的重测一致性。
- [[2024-oasis-million-agent-social-simulation]]:通用、可扩展的 LLM-agent 社交媒体模拟器,在 X 与 Reddit 上模拟最多 100 万个 agent,复现信息传播、群体极化与从众效应,并发现规模越大群体动态越丰富、意见越多样有用。
- [[2024-lmagent-multimodal-agents-society]]:基于多模态 LLM 的万级规模 agents 社会,在电商场景模拟多用户的购物、社交、直播行为,复现真实 co-purchase 模式与从众等 emergent behavior。
- [[2025-multi-agent-collaboration-mechanisms-survey]]:一篇系统综述,沿 actors、types、structures、strategies、coordination protocols 五个维度刻画基于 LLM 的多 agent 系统协作机制,并梳理其跨领域应用与挑战。
- [[2025-agentsociety-large-scale-social-simulation]]:一个整合 LLM 生成式社会 agent、真实城市-社会-经济环境与大规模分布式仿真引擎的社会模拟器,支持上万 agent 并复现极化、谣言、UBI、飓风、城市可持续性五类真实社会实验。
- [[2025-coser-literary-roleplay-dataset]]:CoSER 从 771 部名著抽取 17,966 个角色的真实多角色对话构建数据集,提出 given-circumstance acting 训练与评测角色扮演 LLM,训练出的 CoSER 70B 在自有评测与多个 RPLA benchmark 上达到 SOTA。
- [[2025-multiagentbench]]:MultiAgentBench 与 MARBLE 框架:在六个交互式场景中评测 LLM 多智能体的协作与竞争,衡量任务完成度与协调质量,gpt-4o-mini 平均任务分最高、graph 协议在研究场景最优、认知规划使里程碑达成率提升约 3%。
- [[2025-socioverse-world-model-social-simulation]]:SocioVerse 是一个由 LLM agents 驱动、依托 1000 万真实用户池与四个对齐模块的社会模拟 world model,在政治、新闻、经济三大领域复现大规模人群行为。
- [[2025-sotopia-s4-social-simulation-system]]:面向非技术用户的快速、灵活、可扩展社会模拟系统,通过模拟引擎+RESTful API+Web UI,让研究者无需编程即可用自然语言设计、并行运行并自动评估多轮多方 LLM 社会交互。
- [[2025-emergent-llm-behaviors-data-leakage]]:批判性短文:LLM 多智能体模拟中"自发涌现的社会约定"在观测上等价于 data leakage——模型只是复述预训练中已知的协调博弈知识,而非真正自组织。
- [[2025-mmoagent-economic-simulation-mmo]]:提出 MMOAgent，一个基于 LLM 的 Generative Agent-Based Modeling 框架，用具备 profile/感知/推理/记忆/行动的 LLM 智能体模拟 MMO 游戏经济，涌现出角色分化与符合供需规律的价格波动。
- [[2025-multi-actor-genai-as-game-engine]]:Google DeepMind 的立场/架构论文,主张用游戏引擎式的 Entity-Component 架构统一支撑 Evaluationist/Dramatist/Simulationist 三类多智能体生成式 AI 用户动机,以 Concordia v2 为实例。
- [[2025-multi-agent-llm-value-diversity]]:通过 Schwartz 价值观给 LLM 智能体注入价值多样性的多智能体社会模拟,发现价值多样性提升集体行为的价值稳定性、涌现与自发规则创造,但极端异质带来边际递减与不稳定。
- [[2026-yerkes-dodson-curve-ai-agents]]:在网格世界生存竞技场中系统改变环境压力,首次实证发现 LLM 多智能体系统的合作行为遵循 Yerkes-Dodson 倒 U 形曲线——中等压力(upkeep=5)合作交易峰值达 29 次,过低或过高压力都抑制社会行为,且性选择压力可在不致死的前提下消除攻击。
- [[2026-policysim-proactive-policy-optimization]]:PolicySim 是一个基于 LLM 智能体的社会模拟沙盒,用 SFT+DPO 训练用户智能体、用带消息传递的 contextual bandit 自适应优化推荐与曝光控制等平台干预策略,实现部署前的主动评估与优化。

## 相关

- [[agent-based-model]]
- [[llm-agents]]
- [[model-validation]]
- [[generative-agents]]
- [[s3-social-network-simulation]]
- [[multi-agent-systems]]
- [[role-playing-agents]]
- [[emergent-abilities|emergent-behavior]]
