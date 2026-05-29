---
type: concept
subtype: method
tags: [llm, evaluation, feedback, self-improvement, reasoning]
created: 2026-05-29
updated: 2026-05-29
sources: 26
---

# LLM-as-judge

LLM-as-judge 指用一个 LLM 来评估、批评或打分另一个(或同一个)模型的输出,以此替代或补充人工评估与显式奖励信号。

## 在本 wiki 中的出现

- [[2023-self-refine]]:LLM 既是生成者也是 judge——同一个 LLM 在测试时对自己的输出生成反馈(self-feedback),再据此自我修正(self-refine),迭代进行。无需额外训练即在 7 个任务上平均提升约 20%,体现了"模型自身充当评判者"这一思路。
- [[2023-multi-agent-debate|2023-multiagent-debate]]:多个 LLM 实例在多轮辩论中互相批评、评估彼此的答案,相当于让模型群体充当彼此的 judge。该机制在推理(GSM8K 77%→85%)与事实性(MMLU 63.9%→71.1%)任务上带来显著提升。
- [[2026-generative-social-simulation-validation]]:系统性文献综述指出,LLM 驱动的生成式 ABM 因黑箱性、文化偏见与随机性而加剧了模型"验证"难题,这直接质疑了将 LLM 作为评判与验证工具的可靠性。
- [[2023-shepherd-critic-for-lm-generation]]:Meta AI 用约 8K 反馈数据微调 7B LLaMA critic 模型 Shepherd,精确批判 LLM 输出并给改进建议,GPT-4 评估 win-rate 53-87%,是 LLM-as-judge/critic 的典型实例。
- [[2023-sotopia-social-intelligence-evaluation]]:SOTOPIA-EVAL 提出多维评测框架,交互式评估 LLM 智能体的社会智能,体现了用 LLM 评判开放式社交互动表现的范式。
- [[2024-metacognition-generative-agents]]:为 generative agents 引入元认知模块,让 agent 观察并反思自身思考与行动,本质上是 agent 对自身输出的自我评判与动态调整。
- [[2024-sotopia-pi-social-agents]]:通过 behavior cloning 与 self-reinforcement 在 GPT-4 评分过滤的社交对话数据上训练 7B LLM,使用 GPT-4 作为评判者来筛选训练数据。
- [[2024-llm-critics-help-catch-llm-bugs]]:OpenAI 用 RLHF 训练 CriticGPT,让 LLM 写自然语言批评指出代码 bug,以可扩展监督方式帮助人类评估模型生成的代码。
- [[2024-megaagent-large-scale-mas-without-sop]]:大规模 LLM 多智能体系统中,agent 间相互监督与协调隐含了用 LLM 评判其它 agent 输出的机制。
- [[2024-unbounded-generative-infinite-game]]:提出"生成式无限游戏"概念并实现一个角色生活模拟系统:游戏机制、叙事与角色/环境图像全部由 LLM 与 text-to-image 模型实时生成,核心创新是带 Block Drop 的 regional IP-Adapter(保证角色与环境一致性)与将多 LLM 协作能力蒸馏进 Gemma-2B 的实时游戏引擎。
- [[2024-oasis-million-agent-social-simulation]]:通用、可扩展的 LLM-agent 社交媒体模拟器,在 X 与 Reddit 上模拟最多 100 万个 agent,复现信息传播、群体极化与从众效应,并发现规模越大群体动态越丰富、意见越多样有用。
- [[2025-coser-literary-roleplay-dataset]]:CoSER 从 771 部名著抽取 17,966 个角色的真实多角色对话构建数据集,提出 given-circumstance acting 训练与评测角色扮演 LLM,训练出的 CoSER 70B 在自有评测与多个 RPLA benchmark 上达到 SOTA。
- [[2025-reflective-memory-management]]:提出 RMM(Reflective Memory Management):用主题粒度的前瞻反思组织对话记忆,并用 LLM 引用信号在线 RL 精炼检索 reranker,在 LongMemEval 上比无记忆基线提升 10%+ 准确率。
- [[2025-sotopia-s4-social-simulation-system]]:面向非技术用户的快速、灵活、可扩展社会模拟系统,通过模拟引擎+RESTful API+Web UI,让研究者无需编程即可用自然语言设计、并行运行并自动评估多轮多方 LLM 社会交互。
- [[2025-mem0-scalable-long-term-memory]]:Mem0 是一个以记忆为中心的架构,从持续对话中动态抽取、整合与检索关键信息,并提出图记忆变体 Mem0^g,在 LOCOMO 基准上以约 91% 更低延迟和逾 90% token 节省超越多种基线。
- [[2025-extended-refusal-defense-against-abliteration]]:通过 extended-refusal 微调把安全信号从单一潜在方向分散到多 token 位置与多维度,使模型在 abliteration 攻击后仍保持 >90% 拒绝率,同时通用性能几乎不变。
- [[2025-emergent-llm-behaviors-data-leakage]]:批判性短文:LLM 多智能体模拟中"自发涌现的社会约定"在观测上等价于 data leakage——模型只是复述预训练中已知的协调博弈知识,而非真正自组织。
- [[2025-llm-agent-evaluation-survey]]:SAP Labs 的 LLM agent 评测综述,提出"评测目标 × 评测过程"二维分类法,并强调企业落地中的可靠性、合规与 RBAC 等挑战。
- [[2025-multi-agent-llm-value-diversity]]:通过 Schwartz 价值观给 LLM 智能体注入价值多样性的多智能体社会模拟,发现价值多样性提升集体行为的价值稳定性、涌现与自发规则创造,但极端异质带来边际递减与不稳定。
- [[2025-multi-agent-reflexion-mar]]:把 Reflexion 的单 Agent 自我批评换成多 persona 辩论加 judge 合成反思,在 HotPotQA(EM 44→47)与 HumanEval(pass@1 76.4→82.6)上超过单 Agent Reflexion。
- [[2026-evaluating-memory-structure-llm-agents]]:提出 StructMemEval 基准,测试 LLM agent 组织(而非仅回忆)其长期记忆的能力:纯检索系统在任务规模超出检索窗口后崩溃,memory agents 在被提示如何组织记忆时可靠求解,但常不会主动识别所需的记忆结构。
- [[2026-convapparel-user-simulator-validation]]:Google 提出 ConvApparel(4,146 段人-AI 服装购物对话、双 agent good/bad 协议、逐轮第一人称标注)及 PLSA+HLS+counterfactual validation 三支柱框架,系统量化 LLM user simulator 的 realism gap,发现所有 simulator 平均 HLS 仅 0.004,但 ICL/SFT 在反事实泛化上优于纯 prompting。
- [[2026-tooltree-tool-planning]]:免训练的 MCTS 工具规划框架,用执行前/执行后双反馈引导搜索并双向剪枝,在固定预算下提升 LLM 智能体多工具规划的准确率与效率(GTA 66.95 AVG,ToolBench 69.04 AVG)。
- [[2026-memori-persistent-memory-layer-llm-agents]]:Memori 是 LLM-agnostic 的持久化记忆层,用 Advanced Augmentation 把对话压缩成语义三元组+摘要,在 LoCoMo 上仅用约 5% 上下文 token(1,294/query)达到 81.95% 准确率,优于 Zep/LangMem/Mem0 且成本远低于 full-context。
- [[2026-self-organizing-llm-agents]]:一项 25,000 任务的大规模实验发现"内生性悖论":固定智能体顺序但角色自主的混合协议(Sequential)在质量上同时超越中心化(+14%)与完全自主(+44%)协调,但仅当底层模型足够强(存在能力门槛)。
- [[2026-omnibehavior]]:OmniBehavior 是首个完全基于真实工业日志(快手)构建的用户模拟基准,刻画长时程、跨场景、异质行为轨迹,并揭示当前 LLM 模拟器存在"积极且趋均值"的结构性偏差。

## 相关

- [[self-critique]]
- [[self-refine]]
- [[reflexion]]
- [[reward-model]]
- [[rlaif]]
- [[scalable-oversight]]
- [[self-consistency]]
- [[2023-critic]]
- [[constitutional-ai]]
