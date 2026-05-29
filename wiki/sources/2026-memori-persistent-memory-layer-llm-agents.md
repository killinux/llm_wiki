---
type: source
subtype: paper
tags: [agent-memory, llm-agent, retrieval-augmented-generation, semantic-triple, context-efficiency, locomo, llm-as-judge]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2603.19935
raw: raw/2603.19935.pdf
authors: [Luiz C. Borro, Luiz A. B. Macarini, Gordon Tindall, Michael Montero, Adam B. Struck]
year: 2026
---

# Memori: A Persistent Memory Layer for Efficient, Context-Aware LLM Agents

Memori 是一个与具体 LLM 无关(LLM-agnostic)的持久化记忆层,把记忆当作"数据结构化"问题:用 Advanced Augmentation 流水线把杂乱对话压缩成语义三元组(semantic triples)和对话摘要,从而在 LoCoMo 上以约 5% 的上下文 token 达到 81.95% 的准确率。

## 问题

随着 [[large-language-models]] 演化为自主 [[llm-agents|llm-agent]],跨会话、跨模型的持久化记忆成为实现 context-aware 行为的关键。现有做法有两大缺陷:

- 厂商锁定(vendor lock-in),记忆绑定在特定 LLM 平台;
- 把大量原始对话直接注入 prompt,导致 token 成本飙升、上下文膨胀,并出现 "context rot"(相关信息存在但模型用不上)和 "lost in the middle" [[hallucination]]。

作者的核心洞见:LLM 系统中的记忆不是存储问题,而是结构化问题——挑战在于把噪声大、非结构化的对话数据转换成既便于检索、又利于下游推理的表示。

## 方法

Memori 作为解耦的记忆层,位于应用逻辑与底层 LLM 之间,通过轻量 SDK 拦截 LLM 调用。核心是 **Advanced Augmentation** 记忆创建流水线,充当"认知过滤器",把原始对话蒸馏为可检索的记忆资产:

- **语义抽取与三元组生成**:把对话拆解为知识原子,扫描事实、用户偏好、约束与演变属性,结构化为 subject–predicate–object 语义三元组;每个三元组链接到其来源对话。既是低噪声高信号的索引,又起压缩层作用。
- **对话摘要(Conversation Summarization)**:三元组捕捉静态事实但丢失上下文叙事,因此同时生成简洁的对话级摘要,记录用户总体意图、对话时间进展与隐含任务上下文;每个三元组可直接链接到对应摘要,补回"为什么"和"如何演变"。

这种双层记忆资产中,三元组提供精确、省 token 的事实召回,摘要提供时序与上下文推理所需的连贯叙事。检索阶段用混合检索:embedding 余弦相似度 + BM25 关键词匹配。三元组用 Gemma-300 embedding 模型编码,用 [[faiss]] 本地索引做快速相似检索。这本质上是对传统 [[retrieval-augmented-generation]] 直接 chunk+embed 原始文本(导致向量空间杂乱)的改进。

## 结果

在 LoCoMo(Long Conversation Memory)benchmark 上评测,排除 adversarial 类别,用 [[gpt-4]]-1-mini(GPT-4.1-mini)做答案生成,并用 [[llm-as-judge]](同样是 GPT-4.1-mini)评分。对比基线为 Zep、LangMem、Mem0,以及 Full-Context 上限。

准确率(Overall,%):

- **Memori 81.95**,Zep 79.09,LangMem 78.05,Mem0 62.47,Full-Context(ceiling)87.52。
- 分类别:Single-hop 87.87(领先),Temporal 80.37(逊于 LangMem 86.92 / Zep 83.33),Multi-hop 72.70,Open-domain 63.54(最难,略逊 LangMem 67.71)。

Token / 成本效率(每次查询):

- Memori 平均仅 **1,294 tokens**,占完整上下文的 **4.97%**;Full-Context 26,031 tokens,Mem0 1,764,Zep 3,911。
- 相比 Zep 减少约 **67%** token,同时准确率更高(81.95% vs 79.09%);相比 Full-Context 节省 **20 倍以上**成本(按 GPT-4.1-mini $0.8/1M tokens 计,Memori 约 $0.001/query)。

结论:LLM 记忆系统的性能不取决于用了多少上下文,而取决于其结构质量;结构化记忆可在不牺牲准确率的前提下替代大而无过滤的上下文,实现可扩展、低成本的持久化 agent 部署。

## 在本 wiki 中的位置

Memori 属于 [[agent-memory]] / [[llm-long-term-memory]] 方向,与 [[memgpt]]、[[memorybank]]、Mem0 等"为 LLM agent 提供持久长期记忆"的系统同类,但强调 LLM-agnostic 的 API 层记忆与 token 成本效率。其用 [[semantic-id]] 之外的语义三元组 + 摘要双层表示、以及混合检索([[faiss]]、BM25)是对 [[retrieval-augmented-generation]] 的针对性改进。评测沿用 LoCoMo 与 [[llm-as-judge]] 范式,可与本 wiki 中 [[longmemeval]]、[[locomo]]、[[msc-multi-session-chat]] 等长期记忆 benchmark 与 [[meminsight]]、[[cognitive-weave-spatio-temporal-resonance-memory]] 等记忆工作对照阅读。
