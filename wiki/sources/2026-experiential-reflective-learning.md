---
type: source
subtype: paper
tags: [llm-agent, self-improvement, agent-memory, experiential-learning, retrieval-augmented-generation, gaia, reflexion]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2603.24639
raw: raw/2603.24639.pdf
authors: [Marc-Antoine Allard, Arnaud Teinturier, Victor Xing, Gautier Viaud]
year: 2026
---

# Experiential Reflective Learning for Self-Improving LLM Agents

ERL 是一个无需更新参数的自我改进框架:agent 对单次任务轨迹与成败信号进行反思、提炼出可迁移的"启发式(heuristics)"存入持久池,新任务到来时按相关性检索 top-k 注入上下文以指导执行,在 Gaia2 上比 ReAct 基线提升 7.8% 成功率。

## 问题

基于 [[large-language-models]] 的 [[llm-agents|llm-agent]] 虽能完成多步规划、推理与工具调用,但难以适应不熟悉工具与领域约定的专门环境,且每遇新任务都"从零开始",不利用已积累经验。[[fine-tuning]] 可实现适应但成本高、对闭源模型不可行、且不支持持续学习。已有的经验型记忆方法各有短板:

- [[expel]](ExpeL)对比成功/失败轨迹抽取洞见,但把抽取结果不分相关性地拼进每个测试 prompt,随经验积累扩展性差;并需要对每个任务用 [[reflexion]] 反复 rollout 直到成功来构造对比轨迹对。
- AutoGuide 通过对比配对轨迹生成 context-aware 指南,但在每个 agent turn 都做检索、开销大,且当前状态匹配不到任何已存上下文时无指导。

两者都依赖每任务多次 rollout 来构造对比轨迹对,而真实部署中任务往往不可重试。

## 方法

ERL(Experiential Reflective Learning)由两部分组成:

- **启发式生成(heuristic generation)**:面向提供二元成功/失败反馈的环境。agent 执行任务后,对"任务描述 + 执行轨迹(推理步骤、工具调用、输出)+ 成败信号"进行 post-mortem 反思,生成结构化启发式,包含(1)分析成败原因,与(2)带显式触发条件与推荐动作的 learned guideline(例如"给日历参会者发邮件前,先用 Contacts 工具把名字解析成邮箱地址再调用邮件 API")。启发式存入持久池。无奖励信号时由 agent 自评推断结果(见消融)。
- **检索增强执行(retrieval-augmented execution)**:新任务到来,由一个 LLM 把任务分解为子任务/动作步骤,并对每条已存启发式按"任务描述相似度 + 经验多样性 + 指南信息量"打分,把 top-k 注入 agent 的 system prompt(默认 k=20、用 LLM-based 检索)。这避免被整池启发式淹没。论文还评估了 Iterative ERL 变体(边积累边检索,见结果)。

主干模型为 GPT-5-mini;ARE LLM Judge 与启发式生成用 gpt-5-mini-2025-08-07,启发式检索用 gpt-5.2-2025-12-11;embedding 检索用 Qwen3-Embedding-0.6B。

## 结果

主基准为 Gaia2(ARE 平台,12 个 application / 101 个 tool),聚焦 Search 与 Execution 两个 split。在 8 个 universe(112 execution / 132 search 任务)上积累启发式,在 2 个 held-out test universe(48 / 28 任务)上评测,3 次运行平均:

- **总体成功率**:ERL 56.1%,ReAct 基线 48.3%(+7.8%);Execution 51.4%(基线 43.1,+8.3%),Search 60.7%(基线 53.6,+7.1%)。优于 [[expel]] ExpeL(50.9%)与 AutoGuide(50.8%);Few-shot 原始轨迹仅 46.4%(低于基线)。
- **可靠性(pass^3,三次全成功)**:ERL 在 Execution +8.3%、Search +10.6%;pass@3 提升较小,说明主要是让原本不稳定的任务更稳。
- **启发式优于原始轨迹**:Few-shot 原始轨迹相对基线 -1.9%;在固定 token 预算下,启发式在 Execution(约 20 场景处 +5.5%)与 Search(40 场景处 +23.8%)均胜过等量原始轨迹。
- **检索质量重于数量**:随机选启发式呈非单调曲线,在 40-60 条左右峰值后随数量增多下降;LLM-based 检索 k=20 达 56.1%,优于 embedding 检索(53.3%)与最佳随机配置(53.8%)。检索数 k 在 k=20 时 LLM 检索取得 Search 60.7、Overall 56.1 的最佳。
- **失败 vs 成功来源**:失败派生启发式整体更强;且分 split——失败启发式利于 Search(+14.3% over baseline),成功启发式利于 Execution(+9.0%);only-failures 总体 58.9% 最高但偏科 Search。
- **奖励信号重要性**:无环境验证奖励、靠 agent 自评(自评准确率约 70%)时,ERL 降到 51.2%(-4.8%),但仍超基线 48.3%。
- **成本**:ERL 相对基线总 token +85% 输入(检索启发式约 20k token 每 turn 附加到约 12k 的 base system prompt),但借助 prompt caching,scenario rollout 成本仅 +15%,计入启发式生成与检索后总 API 成本约 +40%;平均 turn 数 16.6 → 17.6。
- **Iterative ERL**:边积累边检索使 source 任务表现更高(Execution 44.6/Search 59.9),但 test 泛化更低(50.7,较标准 ERL 的 56.1 低 5.4%)。
- **τ²-bench(附录)**:三个客服域(Airline/Retail/Telecom)上 ERL 总体成功率 38.0% vs 基线 36.7%,Airline/Retail 提升、Telecom(dual-control)略降。

## 在本 wiki 中的位置

本文属于 [[llm-agents|llm-agent]] 的 [[self-improvement]] / [[agent-memory]] 方向,与 [[expel]]、[[reflexion]] 同属"经验型 in-context 学习"路线,但用 [[retrieval-augmented-generation]] 式的选择性检索替代全量拼接,并强调单次轨迹反思(无需重试)。可与 [[in-context-learning]]、[[self-reflection]]、[[react]] 交叉链接;评测主依托 [[gaia]] 的 Gaia2 基准。属于 ICLR 2026 MemAgents Workshop 的会议论文。
