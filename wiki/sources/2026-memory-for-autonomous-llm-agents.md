---
type: source
subtype: paper
tags:
  - agent-memory
  - llm-agent
  - retrieval-augmented-generation
  - survey
  - agent-evaluation
created: 2026-05-29
updated: 2026-05-29
arxiv: "2603.07670"
raw: raw/2603.07670.pdf
authors:
  - Pengfei Du
year: 2026
---

# Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers

一篇关于 [[llm-agent]] 记忆(memory)的综述,把 agent memory 形式化为"写入–管理–读取(write–manage–read)"循环,提出三维分类法,深入剖析五类记忆机制,梳理评测基准与工程实践,覆盖 2022 至 2026 年初的工作。

## 问题

单个 context window 太小,无法承载 [[large-language-models]] agent 在长时间交互中"发生了什么、学到了什么、不该重复什么"。没有记忆,一个跨越一周会话的 debugging assistant 每个周一都要重新发现目录结构、重读 README,甚至重试上周五弄崩构建的同一个修复。记忆是把无状态文本生成器变成真正自适应、[[self-evolving-agents|自进化]] agent 的关键,使其能积累事实知识与用户偏好、形成基于经验的行为模式、避免重复犯错并持续改进。

此前已有泛 agent 综述,以及 2024 年一篇聚焦记忆的综述,但 2025–2026 年涌现的新工作(Agentic Memory、MemBench、MemoryAgentBench、MemoryArena)引入了学习式记忆控制、更丰富的评测维度,以及把记忆与决策紧耦合的 agentic 基准,因此需要更新。综述围绕三个问题:RQ1 记忆应如何分解与形式化;RQ2 存在哪些机制、各有何权衡;RQ3 当最终检验是下游 agent 表现时记忆该如何评测。

## 方法

- **形式化**:把 agent memory 置于 [[markov-decision-process|POMDP]] 式 agent 循环中。动作 `a_t = π_θ(x_t, R(M_t, x_t), g_t)`,记忆更新 `M_{t+1} = U(M_t, x_t, a_t, o_t, r_t)`,其中 R 为读取、U 为写入与管理(含摘要、去重、优先级评分、冲突消解、删除),记忆 M_t 充当 agent 的 belief state(history 的充分统计量)。提出五个设计目标及其张力:Utility、Efficiency、Adaptivity、Faithfulness、Governance。
- **三维分类法**:(1) 时间尺度——working / episodic / semantic / procedural memory(对应认知科学的人类记忆系统);(2) 表征底物——context-resident 文本、向量索引存储([[approximate-nearest-neighbor-search]] / [[faiss]] / [[dense-passage-retrieval]])、结构化存储(SQL、知识图谱)、可执行库、混合存储;(3) 控制策略——heuristic、prompted self-control、learned control。
- **五类核心机制**:context-resident 压缩(滑动窗口、滚动/分层摘要,易出现 summarization drift 与 attentional dilution / lost-in-the-middle);[[retrieval-augmented-generation|检索增强]]存储([[rag]]、[[memgpt]] 等,瓶颈从存储转向 relevance);反思自改进([[reflexion]]、[[generative-agents]]、[[expel]],风险是 self-reinforcing error,对策为 reflection grounding);分层虚拟上下文管理([[memgpt]] 借鉴操作系统虚拟内存,JARVIS-1 扩展到多模态);策略学习式管理(Agentic Memory / AgeMem 把 store/retrieve/update/summarize/discard 当作工具,经三阶段 RL + 步级 [[group-relative-policy-optimization|GRPO]] 训练);此外还有参数化/权重式记忆(MemLLM)。
- **评测与工程**:指出 Precision@k、[[ndcg]] 等经典 IR 指标不足,提出四层评测栈(任务有效性 / 记忆质量 / 效率 / 治理);并给出写路径过滤、读路径两阶段检索、staleness 与冲突处理、延迟成本、隐私与 [[machine-unlearning|machine unlearning]]、三种架构模式(Monolithic context / Context+retrieval / Tiered with learned control)等工程实践。

## 结果

综述以表格汇总代表性系统的实证表现(转述自原文):

- [[reflexion|Reflexion]]:HumanEval pass@1 达 91%,优于无反思的 [[gpt-4|GPT-4]] 基线 80%。
- [[voyager|Voyager]]:相较此前 Minecraft agent 多 3.3× 独特物品、tech-tree 里程碑进度快 15.3×;去掉 skill library 即损失该 15.3× 优势。
- [[react|ReAct]]:在 [[alfworld]] 上获得 34% 绝对提升。
- [[rag|RAG]] / [[retrieval-augmented-generation|RETRO]]:RETRO 从 2 万亿 token 语料检索,7.5B 模型在 16 项基准中 10 项媲美 175B Jurassic-1。
- 四个记忆基准:[[locomo|LoCoMo]](最多 35 个 session、300+ 轮、每段对话 9k–16k token);MemBench(区分 factual / reflective,participation / observation 模式;ACL 2025 Findings);MemoryAgentBench(四项认知能力,无系统能全部掌握);MemoryArena(多 session 互依任务,在 LoCoMo 上近满分的模型在此跌至 40–60%)。
- 消融:[[generative-agents|Generative Agents]] 去掉 reflection 后 48 模拟小时内退化为重复、无上下文的响应;MemoryArena 中把 active memory agent 换成纯 long-context 基线,任务完成率从 80%+ 跌到约 45%。结论:"有无记忆"的差距常大于不同 LLM backbone 间的差距。

## 在本 wiki 中的位置

这是一篇 [[llm-agent]] 记忆主题的综述,串联起本 wiki 中大量已有条目:机制层面涉及 [[rag]]、[[retrieval-augmented-generation]]、[[memgpt]]、[[reflexion]]、[[generative-agents]]、[[voyager]]、[[expel]]、[[react]];方法层面把记忆嵌入 [[markov-decision-process|POMDP]] 框架,并用 [[group-relative-policy-optimization|GRPO]] 学习记忆控制策略;评测层面引入 [[locomo]] 等基准,与 [[agentbench]] 等 agent 评测互补。它可作为 [[agent-memory]]、[[llm-long-term-memory]]、[[memory-module]]、[[memory-augmentation]] 等概念的纵览入口,并与 [[multi-agent-collaboration]]、[[tool-use]] 等应用方向相连。
