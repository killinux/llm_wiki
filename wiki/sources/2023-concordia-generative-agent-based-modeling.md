---
type: source
subtype: paper
tags: [generative-agents, agent-based-modeling, llm-agents, multi-agent-systems, social-simulation, foundation-models]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2312.03664
raw: raw/2312.03664.pdf
authors: [Alexander Sasha Vezhnevets, John P. Agapiou, Avia Aharon, Ron Ziv, Jayd Matyas, Edgar A. Duéñez-Guzmán, William A. Cunningham, Simon Osindero, Danny Karmon, Joel Z. Leibo]
year: 2023
---

# Concordia:基于 LLM 的生成式 agent-based modeling 库

Concordia 是 [[google-deepmind]] 提出的一个库,用于构建 **Generative Agent-Based Models (GABM)**——即用 [[large-language-models]] 驱动的生成式 [[generative-agents]] 在物理、社会或数字空间中扎根(grounded)地交互,从而进行社会科学仿真和数字服务评估。

## 问题

传统的 Agent-Based Modeling (ABM) 在社会与自然科学中已应用数十年,但通常停留在较为抽象的分析层面,难以把行为经济学等关于"人真正如何决策"的洞见与制度、资源经济学整合进同一个模型。LLM 的出现带来了新的可能:agent 不仅拥有更丰富的自适应决策能力,还能用自然语言彼此沟通、运用常识、调用数字工具(app、AI 助手如 Bard、ChatGPT)。

论文要解决的核心问题是:如何提供一个灵活、模块化的框架,把 LLM 驱动的 agent 行为**扎根(grounding)**到具体的物理、社会、数字环境中——既要让 agent 的行为符合常识与社会规范,又要让环境状态(金钱、选票、物品等"grounded variables")保持一致与可信,以支持科学研究和对真实数字服务的合成数据生成与评估。

## 方法

Concordia 由两部分组成:生成式 agent + 生成式环境(由 **Game Master, GM** 控制)。

- **Generative agents(生成式 agent)**:借鉴 [[joon-sung-park]] 等人的 [[generative-agents]] 工作,采用 associative memory(联想记忆)记录经验。每个 agent 由一组 **components(组件)** 构成,组件充当长期记忆与"行动上下文(context of action)"之间的中介(灵感来自 Minsky 的"society of mind")。组件状态都是自然语言字符串(如 identity、plan、observation)。agent 区分长期记忆 m 与工作记忆 z。形式上定义为两步采样:行动步 a_t ∼ p(·|f^a(z_t)) 用 LLM 采样要执行的动作;更新步 z_{t+1}^i ∼ p(·|f^i(z_t, m_t)) 更新组件状态。agent 通过用自然语言描述意图来产生行为(例如"Alex makes breakfast")。
- **Game Master(GM,游戏主持人)**:灵感来自桌面角色扮演游戏(Dungeons & Dragons)中的叙事者。GM 消费 agent 的 action attempt,判定发生的事件(event statement),决定其对世界和其他 agent 的影响,维护并更新 grounded variables、推进时钟。GM 同样用 components + associative memory 实现,但描述的是世界状态而非动作选择。它负责检查动作的物理可行性,解决多 agent 动作冲突,并向 agent 发送 observations。事件生成:e_t ∼ p(·|f^e(z_t, a_t));观测发送:o_{t+1}^i ∼ p(·|f^o(z_{t+1}))。
- **数字活动仿真**:通过嵌套的 PhoneGameMaster 与 PhoneUniverse,把自由文本动作翻译成手机 app(Calendar、Chat、Navigation 等)上的"definite functions"(明确输入输出的 API 调用),支持四种数字函数表示:纯自然语言、简易 app 行为模拟、LLM prompt 模拟、真实 app API 集成。

论文还讨论了对验证(validation)的方法论:提出 evidence hierarchy(证据等级)、algorithmic fidelity(算法保真度)等概念,并强调 train-test contamination、LLM 可能代表人群刻板印象等未解问题。

## 结果

这是一篇库/方法论与立场论文,不以定量 benchmark 为主,而是给出框架、形式化定义(eq.1–4)与一系列应用场景。论文随库一同发布了若干示例环境:模拟小镇选举(有人竞选市长、有人发起抹黑活动)、小生意、财产纠纷、社会心理实验、通过数字 app 中介的社会规划场景。Concordia 需要标准 LLM API,可选地与真实 app/服务集成,已在 GitHub 开源(google-deepmind/concordia)。

论文阐述的应用包括:
- **合成用户研究**:在数字动作空间(如智能手机)中仿真用户活动,生成合成用户日志,在沙盒中测试未发布产品。
- **数据生成与服务评估**:在单用户层面做服务的 A/B 测试,生成训练/评估数据。
- **In silico 序列社会困境实验**:研究多 agent 的资源管理、合作、协调,把 GABM 视为继 Homo economicus、Homo RLicus 之后的"model animal"。
- **实现经典与当代心理学模型**:用 components 建模 Ajzen 的 theory of planned behavior、心理建构主义情绪模型等。
- **可审计的 AI 助手与 credit assignment**:由于 agent 的 chain of thought 以自然语言/Python 程序形式存在,每个 episode 都留下 (z_t, a_t) 的完整 trace,人工审计者可判断动作是否合理,把责任归因到具体组件或 LLM 调用,数据可用于 [[fine-tuning]] 或 [[rlhf]],与 [[ai-safety]]/[[ai-alignment]] 相关。
- **涌现与多尺度建模**:agent 可代表个体、组织、机构乃至国家,跨尺度建模经济活动。

## 在本 wiki 中的位置

本文是 LLM-driven [[generative-agents]] / [[llm-multi-agent]] 仿真方向的重要框架性工作,直接继承并扩展了 [[joon-sung-park]] 的 [[generative-agents]] 路线([[memory-stream]]、[[agent-memory]] 思想),把单纯"agent 互相交谈"推进到"动作扎根于物理/社会/数字空间"。它与 [[autonomous-agents]]、[[llm-based-agents]]、[[multi-agent-collaboration]] 类工作互补:不同于 [[generative-agents]] 偏重涌现行为观察,Concordia 强调可控实验设计、grounded variables 与服务评估。其 GM 机制与 [[world-model]]、[[grounding]]、[[user-simulation]] 概念相关,数字 app 集成思路与 [[tool-use]]、[[toolformer]] 一脉相承。作为社会模拟工具,它也连接到 [[multi-agent-systems]] 与 [[foundation-models]] 在社会科学中的应用。
