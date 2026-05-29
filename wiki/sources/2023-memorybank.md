---
type: source
subtype: paper
tags: [llm, long-term-memory, memory, ai-companion, forgetting-curve, retrieval, chatbot]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2305.10250
raw: raw/2305.10250.pdf
authors: [Wanjun Zhong, Lianghong Guo, Qiqi Gao, He Ye, Yanlin Wang]
year: 2023
---

MemoryBank 为 LLM 设计了一套类人长期记忆机制:存储历史对话、按 Ebbinghaus 遗忘曲线动态更新记忆、检索相关记忆并构建用户画像,并据此实现了情感陪伴聊天机器人 SiliconFriend。

## 问题

尽管 ChatGPT、[[gpt-4]] 等 LLM 能力强大,但它们普遍缺乏鲁棒的长期记忆机制。在需要持续交互的场景(个人陪伴、心理咨询、秘书助理)中,这一缺陷尤为明显:AI 无法回忆过去的对话来建立关系,无法基于用户历史与情绪状态提供更有针对性的支持,也难以随时间理解并适应用户的个性。因此需要为 LLM 增加能够长期保留、更新记忆并刻画用户画像的能力。

## 方法

[[memorybank]] 是一套统一记忆机制,围绕三大支柱构建:

1. 记忆存储(Memory Storage):按时间顺序记录多轮对话(带时间戳);并通过提示 LLM 把对话蒸馏为分层的事件摘要(daily event summary 汇聚为 global summary);同时持续推断并更新用户画像(personality understanding),形成动态的多层记忆。
2. 记忆检索(Memory Retrieval):采用类似 [[dense-passage-retrieval]] 的双塔稠密检索。每条记忆 m 用编码器 E(·) 预编码为向量 h_m,整个记忆库用 FAISS 索引;当前对话上下文编码为查询向量 h_c,检索最相关记忆。编码器可灵活替换。
3. 记忆更新(Memory Updating):受 [[ebbinghaus-forgetting-curve]] 启发,用指数衰减模型 R = e^(-t/S) 建模记忆保留率(R 为保留率,t 为距上次学习的时间,S 为记忆强度)。S 初始化为 1,当某记忆被对话再次召回时,S 加 1 并把 t 重置为 0,从而以更低概率被遗忘,模拟"遗忘速率、时间衰减、间隔效应(spacing effect)"。

基于 MemoryBank,作者构建了 AI 陪伴聊天机器人 [[siliconfriend]],其开发分两阶段:第一阶段对开源 LLM 用 38k 条心理咨询对话数据做参数高效微调(采用 [[lora]],rank r=16,A100 GPU 上训练 3 epoch),使其更具同理心;第二阶段集成 MemoryBank。SiliconFriend 支持中英双语,落地在三个 LLM 上:闭源 [[chatgpt]],以及开源的 [[chatglm]](6.2B)与 [[belle]](基于 7B LLaMA)。开源版英文用 MiniLM、中文用 Text2vec 作为嵌入模型,并用 LangChain + FAISS 做检索。

## 结果

定性分析在心理陪伴、记忆召回、个性化交互三方面展示了 SiliconFriend 相比基线(如 ChatGLM)能提供更有同理心的回应、准确召回此前讨论过的内容(如此前推荐的书与算法),并能正确识别"未曾讨论过"的事件。

定量分析构建了模拟记忆库:由 ChatGPT 扮演 15 个不同个性的虚拟用户,生成跨 10 天、覆盖多话题的对话;人工编写 194 个探查问题(英文 97 + 中文 97)。评测四个指标:记忆检索准确率(Retrieval Acc.)、回答正确性(Correctness)、上下文连贯性(Coherence)、模型排序得分(Ranking)。Table 2 主要结果:

- 英文:SiliconFriend(ChatGLM)检索 0.809 / 正确性 0.438 / 连贯 0.68 / 排序 0.498;SiliconFriend(BELLE)0.814 / 0.479 / 0.582 / 0.517;SiliconFriend(ChatGPT)0.763 / 0.716 / 0.912 / 0.818。
- 中文:SiliconFriend(ChatGLM)0.84 / 0.418 / 0.428 / 0.51;SiliconFriend(BELLE)0.856 / 0.603 / 0.562 / 0.565;SiliconFriend(ChatGPT)0.711 / 0.655 / 0.675 / 0.758。

结论:(1) 综合最佳为 SiliconFriend(ChatGPT),各指标全面领先;(2) 开源的 BELLE 与 ChatGLM 版本在检索准确率上同样很高,说明 MemoryBank 对开源/闭源 LLM 都通用有效,但其余指标受基座模型能力限制不及 ChatGPT;(3) 语言差异明显:ChatGLM/ChatGPT 版英文表现更好,BELLE 版中文更强。

## 在本 wiki 中的位置

MemoryBank 是 LLM 长期记忆方向的代表工作,与 [[generative-agents]] 的 [[memory-stream]] 同属"为 LLM/agent 引入持久记忆"的研究线,但其特色在于把心理学的 Ebbinghaus 遗忘曲线引入记忆更新。它依赖 [[dense-passage-retrieval]] 式检索,与 [[rag]] 的检索增强思路相通;微调阶段使用 [[lora]]。相关方法概念见 [[llm-long-term-memory]] 与 [[llm-agents]]。
