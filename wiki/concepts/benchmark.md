---
type: concept
subtype: method
tags: [evaluation, benchmark, agent, LLM]
created: 2026-05-29
updated: 2026-05-29
sources: 15
---

# Benchmark

Benchmark 指用于系统、可复现地评估模型在特定能力维度上表现的标准化任务集合与评测协议。

## 在本 wiki 中的出现

- [[2023-agentbench]]:提出 AgentBench,这是首个系统评估 LLM-as-Agent 能力的多维 Benchmark。它横跨 8 个交互环境对 29 个模型进行测评,以此揭示了商业模型与开源模型在 Agent 能力上的巨大差距。在该工作中,Benchmark 既是衡量模型交互式决策能力的统一标尺,也是暴露不同模型能力鸿沟的诊断工具。
- [[2023-microlens-micro-video-recommendation-dataset]]:MicroLens:一个含 10 亿交互、3400 万用户、100 万微视频并提供原始视频/音频/图像/文本内容的内容驱动微视频推荐数据集与基准。
- [[2024-sage-self-evolving-agents]]:由 User/Assistant/Checker 三 agent 组成、结合迭代反馈、反思与基于 Ebbinghaus 遗忘曲线的记忆优化的自进化 LLM agent 框架,对小模型提升尤为显著。
- [[2024-recflow-full-flow-recommendation-dataset]]:首个包含工业推荐系统多级漏斗各阶段未曝光样本的大规模全流程数据集,用于研究分布偏移、选择偏差与多阶段联合优化。
- [[2024-opencity-urban-llm-agents]]:通过 LLM 请求调度器与 group-and-distill 提示优化,把万级城市 LLM agent 模拟加速约 600 倍,使 10000 agent 的一天活动可在 1 小时内于普通硬件完成。
- [[2024-scenario-wise-rec]]:首个面向多场景推荐(MSR)的开源 benchmark,整合 6 个公开数据集、12 个基线模型与统一的数据处理/训练/评测流水线,并在工业广告数据集上验证。
- [[2025-agentic-memory-llm-agents]]:受 Zettelkasten 启发的 agentic 记忆系统,通过结构化笔记、自主链接生成与记忆演化为 LLM agent 提供可持续演化的长期记忆。
- [[2025-multiagentbench]]:MultiAgentBench 与 MARBLE 框架:在六个交互式场景中评测 LLM 多智能体的协作与竞争,衡量任务完成度与协调质量,gpt-4o-mini 平均任务分最高、graph 协议在研究场景最优、认知规划使里程碑达成率提升约 3%。
- [[2025-mem0-scalable-long-term-memory]]:Mem0 是一个以记忆为中心的架构,从持续对话中动态抽取、整合与检索关键信息,并提出图记忆变体 Mem0^g,在 LOCOMO 基准上以约 91% 更低延迟和逾 90% token 节省超越多种基线。
- [[2025-memory-os-of-ai-agent]]:借鉴操作系统内存管理,为 AI agent 设计分层(STM/MTM/LPM)、heat 驱动更新的 MemoryOS,统一 Storage/Updating/Retrieval/Generation 四模块,在 LoCoMo 上 F1 平均提升 49.11%、BLEU-1 提升 46.18%。
- [[2025-agentsnet-multi-agent-reasoning]]:AGENTSNET 是一个可任意扩展的多 agent LLM 基准,借鉴分布式计算的五个经典问题(coloring、vertex cover、matching、leader election、consensus)来衡量 agent 网络在给定通信拓扑下的自组织、去中心化通信与协作推理能力,实验最多探测 100 个 agent。
- [[2025-llm-agent-evaluation-survey]]:SAP Labs 的 LLM agent 评测综述,提出"评测目标 × 评测过程"二维分类法,并强调企业落地中的可靠性、合规与 RBAC 等挑战。
- [[2026-evaluating-memory-structure-llm-agents]]:提出 StructMemEval 基准,测试 LLM agent 组织(而非仅回忆)其长期记忆的能力:纯检索系统在任务规模超出检索窗口后崩溃,memory agents 在被提示如何组织记忆时可靠求解,但常不会主动识别所需的记忆结构。
- [[2026-convapparel-user-simulator-validation]]:Google 提出 ConvApparel(4,146 段人-AI 服装购物对话、双 agent good/bad 协议、逐轮第一人称标注)及 PLSA+HLS+counterfactual validation 三支柱框架,系统量化 LLM user simulator 的 realism gap,发现所有 simulator 平均 HLS 仅 0.004,但 ICL/SFT 在反事实泛化上优于纯 prompting。
- [[2026-tencent-advertising-algorithm-challenge-2025]]:腾讯广告算法大赛 2025 发布两个真实工业广告日志构建的大规模全模态生成式推荐数据集(TencentGR-1M/10M)、基线模型与含转化加权的评测协议。

## 相关

- [[agent]]
- [[evaluation]]
- [[llm-as-agent]]
- [[2023-agentbench]]
- [[user-simulator]]
- [[generative-recommendation]]
