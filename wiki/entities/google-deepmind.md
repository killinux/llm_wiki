---
type: entity
subtype: lab
tags: [lab, ai-research, google, llm]
created: 2026-05-29
updated: 2026-05-29
sources: 10
---

# Google DeepMind

Google DeepMind 是 Google 旗下的人工智能研究实验室,专注于机器学习、深度学习与大语言模型等前沿 AI 技术的研究与开发。

## 在本 wiki 中的出现

- [[2023-self-debugging]]:该论文提出 SELF-DEBUGGING 方法,通过 few-shot prompting 让 LLM 执行并解释自己生成的代码,从而在没有人工反馈的情况下实现自我调试。Google DeepMind 在此工作中作为相关研究机构出现。
- [[2023-llms-cannot-self-correct-reasoning-yet]]:本文证明在无外部反馈的"内在自我纠正"设定下,LLM 无法纠正自身推理错误,性能反而往往下降。
- [[2023-timesfm-time-series-foundation-model]]:Google Research 的 TimesFM:一个在 O(100B) 时间点真实+合成时序上预训练的 decoder-only 时序预测基础模型,zero-shot 表现接近全监督 SOTA。
- [[2023-concordia-generative-agent-based-modeling]]:Google DeepMind 提出的库 Concordia,用 LLM 驱动的生成式 agent 在物理/社会/数字空间中扎根交互,通过 Game Master 控制环境,支持 Generative Agent-Based Modeling 的社会仿真与数字服务评估。
- [[2024-v-star-verifiers-for-self-taught-reasoners]]:V-STaR 在自我提升迭代中复用正确与错误的模型生成解,用 DPO 训练 verifier 在测试时对候选解排序,使 LLaMA2 在数学推理上绝对提升 6%~17%、代码生成 4%~12%。
- [[2024-score-self-correct-via-rl]]:SCoRe 用完全自生成数据的多轮在线强化学习(两阶段 + 奖励塑形)训练单个 LLM,在 MATH 上把内在自我纠错 Δ(t1,t2) 从 -11.2% 提到 +4.4%(整体提升 15.6%)、HumanEval 上达 12.2%。
- [[2024-generative-agents-self-reports]]:用基于真人深度访谈与问卷自述构建的 generative agents,可对单个个体在多种社会科学结果上做通用模拟,留出题目预测精度接近个体两周后的重测一致性。
- [[2025-reflective-memory-management]]:提出 RMM(Reflective Memory Management):用主题粒度的前瞻反思组织对话记忆,并用 LLM 引用信号在线 RL 精炼检索 reranker,在 LongMemEval 上比无记忆基线提升 10%+ 准确率。
- [[2025-multi-actor-genai-as-game-engine]]:Google DeepMind 的立场/架构论文,主张用游戏引擎式的 Entity-Component 架构统一支撑 Evaluationist/Dramatist/Simulationist 三类多智能体生成式 AI 用户动机,以 Concordia v2 为实例。
- [[2026-llm-agents-competition-cooperation-games]]:研究 LLM agent 在资源分配博弈与 Cournot 竞争中的策略行为:多轮非零和提示下 agent 倾向合作而非收敛到 Nash 均衡,fairness 推理是核心驱动,并提出 θ/γ 合成收益函数框架刻画其信任建立、报复与 endgame 衰减动态。

## 相关

- [[google-brain]]
- [[denny-zhou]]
- [[self-debugging]]
- [[code-generation]]
- [[few-shot-prompting]]
- [[llm-reasoning]]
- [[self-correction]]
- [[time-series-forecasting]]
- [[generative-agents]]
- [[reinforcement-learning]]
- [[memory-management]]
- [[multi-agent-systems]]
- [[concordia]]
- [[game-theory]]
- [[nash-equilibrium]]
