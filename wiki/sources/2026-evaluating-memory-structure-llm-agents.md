---
type: source
subtype: paper
tags: [llm-agent, agent-memory, llm-long-term-memory, benchmark, memory-module, retrieval-augmented-generation]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2602.11243
raw: raw/2602.11243.pdf
authors: [Alina Shutova, Alexandra Olenina, Ivan Vinogradov, Anton Sinitsin]
year: 2026
---

# Evaluating Memory Structure in LLM Agents

提出 **StructMemEval** 基准,专门测试 [[llm-agent]] 能否为给定任务**组织(structure)**其长期记忆,而不仅仅是事实回忆,发现纯检索系统在任务规模超过检索窗口后崩溃,而 memory agents 在被提示如何组织记忆时能可靠求解,但常常不会主动识别出应使用的记忆结构。

## 问题

主流长期记忆基准(如 [[locomo]]、[[longmemeval]])聚焦于简单的事实保持、multi-hop 回忆和时间变化查询。但近期工作表明,这些任务用简单的 [[retrieval-augmented-generation]] LLM 就能解决,并不真正考验复杂的记忆层级——例如 Zhou & Han (2025) 的简单检索基线 EMem 在 LOCOMO 和 LongMemEval 上反而超过了更复杂的记忆架构。这引出核心问题:到底什么样的问题**需要**复杂的记忆层级,这些层级带来了什么能力?

作者给出的回答是:记忆让 LLM agent 能够**组织知识**——把消息提取并装配成最适合任务的结构(图、待办列表、按类别排序的事件、运行统计等),而非原样检索消息。

## 方法

**StructMemEval 设计原则**:实现无关(implementation-agnostic),只评估最终答案而非内部记忆结构(因为 [[mem0]]、Zep 用图数据库,A-Mem、Mem-agent 用互链笔记);并刻意挑选"在记忆组织正确时简单、但在没有正确组织时几乎不可能"的任务,以将记忆组织能力与编程/推理等其他能力解耦。

围绕人类已使用的记忆组织模式构建四类任务:
- **Tree-structured(树结构)**:维护家族树/公司层级等层级知识,从消息("A 是 B 的继女")构建完整图,含需要双向链接的隐含关系。
- **State tracking(状态追踪)**:实体状态随时间变化(如用户搬家后不再与旧邻居为邻),"neighbor"等词具上下文相关性,纯检索易错误纳入旧状态。
- **Counting-based(计数/记账)**:维护并对账总额,观察多方交易历史("A 为 B 垫付 $X"),计算 netting(抵消循环债务)后的最终结算,含无关干扰消息。
- **Recommendation(推荐)**:从事件历史组织并推理用户偏好,回答需聚合与运行统计的问题(如更喜欢哪种音乐类型、看了更多哪类电影),而非单条回忆。

**数据与评估**:用人工标注 + LLM 增强(人工核验)生成合成场景,规避隐私风险;每个场景含对话历史与不同对话深度的评估问题;用 [[llm-as-judge]](gpt-4o-mini)按对参考答案的事实正确性评分。

**Memory organization hints(记忆组织提示)**:为每个场景提供一段可选的"人类如何组织该任务知识"的非正式文本提示;主设置**不带提示**评估,提示仅用于错误诊断——若 agent 无提示失败、带提示成功,则原错误源于记忆组织不当;若带提示仍失败,则错误在执行(未能维护或正确利用所选结构)。

## 结果

数据集规模:共 **207 个评估场景**(90 tree、45 count、42 state tracking、30 recommendation),含 **2000+ 评估问题**,每个场景 10–500 条消息;其中 **main set 含 51 个最难问题**(10 tree、15 count、14 state、12 rec,均 ≥250 条消息),扩展集 207 个用于规模分析。代码与数据见 github.com/yandex-research/StructMemEval。

**main set 上不同 agent 类型对比(均用 gemini-3.1-pro 作 backbone,Table 1,准确率,Total 为四子集等权平均)**:
- Retrieval:State 0.00 / Tree 0.00 / Count 0.00 / Recsys 0.22 / **Total 0.06**
- EMem:0.50 / 0.00 / 0.00 / 0.20 / **0.175**
- EMem-G:0.57 / 0.00 / 0.00 / 0.19 / **0.19**
- Mem-agent:1.00 / 1.00 / 0.13 / 0.52 / **0.66**
- Mem0:0.36 / 0.90 / 0.01 / 0.24 / **0.39**

纯检索几乎完全无法解决记忆组织问题(唯一例外是推荐任务的多选题略好于随机);两个 agentic memory 框架(Mem0、Mem-agent)表现明显更好且相当。

**不同 backbone LLM(均用 Mem-agent 框架,main set,Table 2,Total)**:gemini-3.1-pro **0.66**、gemini-3.0-flash 0.53、deepseek-v4-pro 0.47、deepseek-v4-flash 0.46、gpt-5.5 0.35。所有 backbone 都能一定程度组织记忆并超过检索基线,但子集差异大:两个 "flash" 模型在记账任务上接近 0。

**规模实验(§4.1)**:跨所有任务类型,纯检索能可靠解决小任务,但一旦复杂度超出检索窗口便迅速崩溃;memory agents 起点更低但扩展性更好。count-based 任务因 gemini-2.5-pro 幻觉过多而改用更强的 gemini-3-pro。

**hints 效果(§4.3)**:加 hint 显著提升准确率但未达完美。例如 deepseek-v4-flash 上 tree 任务从 78.6%→90.0%、state 从 80.0%→85.7%,但 count-based 即使带 hint 仍为 0%。memory agent 带/不带 hint 的差距甚至大于 Mem0 与 Mem-agent 之间的差距,说明存在 hint 未覆盖的其他失败模式。

**失败模式分析(§4.4,用 claude-sonnet-4.6 辅助探查 + 人工核验)**:
- Tree:最常见错误是未记录**双向链接**(记了 A→B 却漏 B→A,导致找不到反向路径);其次是写入记忆时**幻觉出不存在的链接/人名/职位**。
- State tracking:把关联条目存成独立记录,用户搬家时只更新自身条目却未更新他人条目;有时口头承认状态变化却未真正写入。
- Count-based:即使 gemini-3.1-pro 这类高能力模型也表现差,主因不是结构或计算错误,而是**漏记记录与幻觉**(跳过交易、同笔重复计入、凭空生成交易);在长消息序列上几乎必有至少一次跳过或幻觉,而记账对单笔遗漏极敏感。

**结论**:两大主要失败模式——(i)LLM 不组织其记忆(尤其无提示时),(ii)LLM 幻觉出虚假记忆(正常场景罕见,但执行数百次连续记忆更新时频繁)。指向两个未来方向:训练/提示 backbone LLM 更好地结构化知识,以及设计能促进该能力的记忆系统。局限:主评估未用多随机种子(API 成本高),且评估包含多个专有 LLM(可用窗口有限),为此也纳入了开源的 deepseek-v4-pro/flash。

## 在本 wiki 中的位置

本文属于 [[agent-memory]] / [[llm-long-term-memory]] 的评测脉络,是继 [[memgpt]]([[memory-module]] 工具化)、[[mem0]] 等 agentic memory 框架之后的诊断性 [[benchmark]]。它与 [[locomo]]、[[longmemeval]] 形成对照:后两者考验事实回忆与 multi-hop,而 StructMemEval 专门考验记忆的**组织/结构化**能力,弥补了简单 [[retrieval-augmented-generation]] 基线即可刷高分的评测空白。方法上用 [[llm-as-judge]] 评分、用 [[hallucination]] 与结构错误作为失败模式分类,可与 [[llm-agent]] 的记忆设计与训练改进相互参照。
