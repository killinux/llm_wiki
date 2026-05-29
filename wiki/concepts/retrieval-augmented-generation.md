---
type: concept
subtype: method
tags: [retrieval, generation, knowledge-intensive, seq2seq, dense-retrieval]
created: 2026-05-29
updated: 2026-05-29
sources: 14
---

# Retrieval-Augmented Generation

Retrieval-Augmented Generation (RAG) 是一种将参数化的生成模型与可检索的非参数化外部知识(如稠密向量索引)结合的方法,在生成时检索相关文档以增强输出。

## 在本 wiki 中的出现

- [[2020-rag]]:提出 RAG,将预训练 seq2seq 生成器与可检索的 Wikipedia 稠密索引结合,统一进行端到端微调,用于知识密集型 NLP 任务并取得多项 SOTA。
- [[2023-chain-of-verification]]:Chain-of-Verification (CoVe) 让 LLM 先生成草稿,再独立回答自我规划的验证问题来核查事实,显著降低幻觉。
- [[2023-memgpt-llms-as-operating-systems]]:MemGPT 借鉴操作系统的分层内存与虚拟内存分页,用函数调用让 LLM 自主管理上下文内外的多级存储,在固定上下文模型上制造"无限上下文"的假象。
- [[2023-self-rag]]:Self-RAG 训练单个 LLM 用 reflection token 实现按需检索与自我反思批判,在推理时可控解码以提升生成质量、事实性与引用准确率。
- [[2024-metacognition-generative-agents]]:为 generative agents 引入元认知(metacognition)模块,让 agent 观察并反思自身思考与行动以动态调整策略,在僵尸末日等目标导向场景中显著提升表现。
- [[2024-self-reflection-llm-agents]]:在 9 个 LLM、1000 道多选题上对比 8 种自我反思类型,证明所有 self-reflection 都能显著提升 LLM agent 的解题准确率(p<0.001)。
- [[2024-aipatient-simulated-patient-llm-agents]]:AIPatient,一个由六个任务专用 LLM 智能体 + Reasoning RAG + 基于 MIMIC-III 真实病历构建的知识图谱驱动的模拟病人系统,EHR-QA 准确率达 94.15%、NER 知识库 F1=0.89,用户研究中匹配或优于真人模拟病人。
- [[2024-stateact-self-prompting-state-tracking]]:StateAct 通过 self-prompting 与 chain-of-states 状态跟踪增强 LLM base agent,纯 in-context learning 即在 Alfworld/Webshop/Textcraft 上比 ReAct 提升 7%-30%。
- [[2025-agentic-memory-llm-agents]]:受 Zettelkasten 启发的 agentic 记忆系统,通过结构化笔记、自主链接生成与记忆演化为 LLM agent 提供可持续演化的长期记忆。
- [[2025-multiagentbench]]:MultiAgentBench 与 MARBLE 框架:在六个交互式场景中评测 LLM 多智能体的协作与竞争,衡量任务完成度与协调质量,gpt-4o-mini 平均任务分最高、graph 协议在研究场景最优、认知规划使里程碑达成率提升约 3%。
- [[2025-reflective-memory-management]]:提出 RMM(Reflective Memory Management):用主题粒度的前瞻反思组织对话记忆,并用 LLM 引用信号在线 RL 精炼检索 reranker,在 LongMemEval 上比无记忆基线提升 10%+ 准确率。
- [[2025-llm-driven-cross-platform-npc]]:一个原型系统,让 LLM 驱动的游戏 NPC 通过云数据库在 Unity 游戏内与 Discord 社交平台间跨平台对话并同步记忆。
- [[2025-mem0-scalable-long-term-memory]]:Mem0 是一个以记忆为中心的架构,从持续对话中动态抽取、整合与检索关键信息,并提出图记忆变体 Mem0^g,在 LOCOMO 基准上以约 91% 更低延迟和逾 90% token 节省超越多种基线。
- [[2025-multi-actor-genai-as-game-engine]]:Google DeepMind 的立场/架构论文,主张用游戏引擎式的 Entity-Component 架构统一支撑 Evaluationist/Dramatist/Simulationist 三类多智能体生成式 AI 用户动机,以 Concordia v2 为实例。

## 相关

- [[dense-retrieval]]
- [[seq2seq]]
- [[knowledge-intensive-nlp]]
