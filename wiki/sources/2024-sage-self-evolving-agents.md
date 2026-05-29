---
type: source
subtype: paper
tags: [llm-agents, agent-memory, self-reflection, multi-agent, ebbinghaus-forgetting-curve, memory-management]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2409.00872
raw: raw/2409.00872.pdf
authors: [Xuechen Liang, Yangfan He, Yinghui Xia, Xinyuan Song, Jianhui Wang, Meiling Tao, Li Sun, Xinhang Yuan, Jiayi Su, Keqin Li, Jiaqi Chen, Jinsong Yang, Siyuan Chen, Tianyu Shi]
year: 2024
---

# SAGE: Self-evolving Agents with Reflective and Memory-augmented Abilities

SAGE 是一个由 User、Assistant、Checker 三个 agent 组成、结合迭代反馈、反思机制与基于 Ebbinghaus 遗忘曲线的记忆优化(MemorySyntax)的自进化 [[llm-agents]] 框架,在闭源模型上带来 2.26 倍提升、在开源模型上带来 57.7% 到 100% 的提升,对小模型尤其显著。

## 问题

[[large-language-models]] 在 NLP 上取得显著进展,但作为 [[llm-agents|llm-agent]] 在动态环境中仍面临三类挑战:

- 需要在变化的环境中持续决策并适应新情况与任务;
- 缺乏长期记忆机制,在需要持续与环境交互时尤为明显;
- 有限的上下文窗口阻碍模型处理长时间跨度的信息。

现有针对记忆的方案多为任务特定:MemGPT 用 FIFO 队列管理遗忘,MemoryBank 用基于插入时间的遗忘曲线;而 [[autogpt]]、BabyAGI 等 [[llm-multi-agent]] 框架仍受通信开销大、过度依赖记忆维护上下文之苦,随交互历史增长而带来资源与延迟压力。

## 方法

SAGE 框架包含三个 agent:User(任务提出者)、Assistant(执行者)、Checker(评估者),核心是三个机制:

- 迭代反馈(Iterative Feedback):Assistant 根据 Checker 的反馈 f_t 迭代更新策略 π_θ,直至 Checker 验证输出正确或达到迭代上限 N。论文用 Debreu-Glicksberg-Fan 不动点定理证明该三方博弈存在 Nash 均衡,论证三 agent 系统相较 two-agent 系统的稳定性优势。
- 反思(Reflection):Assistant 基于稀疏奖励信号(二元成败)、轨迹 T_t 与长期记忆,生成自我反思 r_t = ref(o_{1:t}, R_{1:t}) 并存入长期记忆,反思比标量奖励更丰富,提升学习能力(借鉴 [[reflexion]] 思路)。
- MemorySyntax:结合 [[ebbinghaus-forgetting-curve]] 与语言学原则管理记忆衰减。保留率建模为 R(I_t, τ) = e^{-τ/S},S 为信息强度。通过语言学优化提升信息强度 S* > S,再用阈值 θ_1 > θ_2 动态更新短期记忆([[memory-module]] 中的 STM)与长期记忆(LTM):R ≥ θ_1 留在 STM;θ_2 ≤ R < θ_1 转入 LTM;R < θ_2 丢弃。

整体形成 STM/LTM 双记忆系统:STM 容量有限、快速更新最近轨迹;LTM 长期保留关键信息与自我反思。该框架无需额外训练即可应用到不同 LLM。

## 结果

- AgentBench(见 [[agentbench]]):在 CODE(Knowledge Graph、OS、DB)、GAME([[alfworld]])、WEB([[webshop]]、[[mind2web]])六个任务上评测。GPT-4 与 GPT-3.5 虽已强仍有提升,DB 任务上 GPT-3.5 提升达 2.26 倍(25.9 → 63.1)。小模型增益巨大:Llama2-7B Chat 在多数任务从 0.0 提升,Qwen-1.8B 应用后接近 GPT-3.5 水平。
- 复杂问题求解(Table 2):SAGE-GPT-3.5 在 [[hotpotqa]] 长问答上答案准确率从 54.1% 升至 74.9%(+20.8%);SAGE-Mistral-7b 在 [[alfworld]] 序列任务完成率提升 +17.3%(56.5% → 73.8%)。对话连贯度、步骤完成度均显著提升。
- 长上下文任务(Table 3):对比 [[reflexion]] 与 Beam Search。在 LCC 代码补全上 F1 为 79.29(略优);在推理任务 [[hotpotqa]] 与 [[triviaqa]] 上 F1 分别为 22.06 与 22.76,大幅超过 Reflexion(11.26 / 11.23)与 Beam Search(10.26 / 12.13)。RepoBench-P 上 F1 为 81.22。
- RAG agents(Table 4):对比 [[rag]] 配 BM25、配 [[dpr]]、OpenAI Retrieval、TART、FiD。ChatGPT-4(SAGE)带来 3.6% 到 4.7% 的稳定准确率提升,并在部分任务上几乎减半内存消耗,且不增加延迟。
- 自报总体效果:闭源模型 2.26 倍提升,开源模型 57.7% 到 100% 提升,对小模型尤为显著。

## 在本 wiki 中的位置

本文属于 [[llm-agents]] 的记忆与自我改进方向,将 [[reflection]]/[[self-reflection]] 与受 [[ebbinghaus-forgetting-curve]] 启发的记忆衰减机制(类似 [[memorybank]] 的遗忘曲线、[[siliconfriend]] 系工作)结合到一个多 agent 框架中。它与 [[reflexion]]、[[autogpt]] 等 [[autonomous-agents]] 一脉相承,通过 Checker 提供的迭代反馈实现无训练的策略改进,并在 [[agentbench]]、[[alfworld]]、[[webshop]]、[[mind2web]]、[[hotpotqa]]、[[triviaqa]] 等 [[benchmark]] 上验证,体现 [[agent-memory]] 与 [[llm-multi-agent]] 协作的最新进展。
