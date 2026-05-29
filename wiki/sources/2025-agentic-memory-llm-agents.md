---
type: source
subtype: paper
tags: [llm-agent, agent-memory, retrieval-augmented-generation, llm-long-term-memory, benchmark]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2502.12110
raw: raw/2502.12110.pdf
authors: [Wujiang Xu, Zujie Liang, Kai Mei, Hang Gao, Juntao Tan, Yongfeng Zhang]
year: 2025
---

# A-Mem: Agentic Memory for LLM Agents

A-Mem 提出一种受 Zettelkasten 笔记法启发的 agentic 记忆系统,让 [[llm-agents|llm-agent]] 通过动态生成结构化笔记、自主建立链接(link generation)与记忆演化(memory evolution),无需预定义的固定记忆操作即可组织长期记忆。

## 问题

现有 LLM agent 的记忆系统([[agent-memory]])只提供基础的存储与检索,缺乏精细的记忆组织能力。即便部分系统([[memorybank]]、[[memgpt]])引入 graph database 或缓存式架构,它们仍依赖预定义的 schema、固定的存储结构与工作流,导致跨任务适应性差。当 agent 学到新颖知识(如一种数学解法)时,系统只能在既有框架内归类,无法随知识演化自主形成新的连接或组织模式。论文要解决的核心问题是:如何设计一个灵活、通用、支持 LLM agent 长期交互的记忆系统。与 agentic [[retrieval-augmented-generation]] 在检索阶段体现 agency 不同,A-Mem 把 agency 下沉到记忆结构本身的自主演化。

## 方法

A-Mem 的存储分为三部分,外加检索:

- **Note Construction(笔记构建)**:每条记忆 note `m_i = {c_i, t_i, K_i, G_i, X_i, e_i, L_i}`,其中 `c_i` 为原始交互内容、`t_i` 时间戳,LLM 生成 keywords `K_i`、tags `G_i`、上下文描述 `X_i`,`e_i` 为对 `concat(c_i, K_i, G_i, X_i)` 的文本编码 embedding,`L_i` 为链接集合。遵循 Zettelkasten 的原子化原则,每条 note 自包含。文本编码器使用 all-minilm-l6-v2。
- **Link Generation(链接生成)**:新 note `m_n` 加入时,用 cosine 相似度检索 top-k 最相关历史记忆,再让 LLM 分析潜在共同属性以决定建立哪些链接,实现超越 embedding 相似度的概念/因果连接。
- **Memory Evolution(记忆演化)**:新记忆触发对其近邻记忆 `m_j` 的 context/keywords/tags 更新 `m_j* ← LLM(...)`,使旧记忆随新经验持续精炼,模拟人类学习过程,逐渐涌现高阶模式。
- **Retrieve Relative Memory(相关记忆检索)**:对当前 query 编码后用 cosine 相似度取 top-k 记忆构建提示;同一"box"(因相似上下文描述而互联的记忆簇)内的记忆会被一并访问。

## 结果

在长对话数据集 [[locomo]](平均 9K tokens、最多 35 个 session、7,512 个 QA 对,涵盖 single-hop、multi-hop、temporal、open-domain、adversarial 五类)与自建 DialSim 数据集上评测,baseline 为 LoCoMo、ReadAgent、[[memorybank]]、[[memgpt]],主指标为 F1 与 BLEU-1。

- 在六个 foundation model([[gpt-4o-mini]]、[[gpt-4o]]、Qwen2.5-1.5B/3B、Llama-3.2-1B/3B)上,A-Mem 在非 GPT 模型上全面超越所有 baseline;在 Multi-Hop 任务上至少达到 2 倍以上的提升。例如 GPT-4o-mini Multi-Hop F1 从 baseline 最高约 26.65 提升到 27.02。
- DialSim 上 A-Mem F1 = 3.45,较 LoCoMo 的 2.55 提升 35%、较 MemGPT 的 1.18 高 192%。
- **成本与效率**:每次记忆操作约需 1,200 tokens,相比 baseline(LoCoMo、MemGPT 约 16,900 tokens)token 用量降低 85–93%;单次记忆操作成本 < $0.0003。处理时延 GPT-4o-mini 约 5.4 秒,本地 Llama-3.2-1B(单 GPU)约 1.1 秒。
- **消融**:去掉 Link Generation 与 Memory Evolution 两模块后性能大幅下降;仅保留 LG(去掉 ME)居中,验证两模块互补。
- **扩展性**:空间复杂度 O(N),与 baseline 一致;检索时延从 1,000 条到 1,000,000 条仅由约 0.31μs 增至约 3.70μs,扩展性优异。

## 在本 wiki 中的位置

本文属于 [[llm-agents|llm-agent]] 长期记忆([[llm-long-term-memory]]、[[agent-memory]])方向,可与 [[memorybank]]、[[memgpt]]、[[generative-agents]] 的 [[memory-stream]] 等记忆机制对照。其检索基于 [[retrieval-augmented-generation]] 思路但强调记忆结构的自主演化,区别于 agentic RAG。评测使用 [[locomo]] 等 [[benchmark]],作者来自 [[rutgers-university]] / [[aios-foundation]],可关联 [[yongfeng-zhang]]。
