---
type: source
subtype: paper
tags: [llm-agent, multi-agent-systems, game-theory, prisoners-dilemma, cooperation, ai-safety, evolutionary-game-theory]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2501.16173
raw: raw/2501.16173.pdf
authors: [Richard Willis, Yali Du, Joel Z Leibo, Michael Luck]
year: 2025
---

# Will Systems of LLM Agents Cooperate: An Investigation into a Social Dilemma

让前沿 [[large-language-models]] 为 iterated Prisoner's Dilemma 直接写出**完整策略**(而非逐步出招),再用 evolutionary game theory 模拟 [[llm-multi-agent]] 群体,考察其究竟倾向合作还是侵略。

## 问题

随着基于 LLM 的 [[autonomous-agents]] 越来越多地被部署,理解它们在策略性交互中的**集体行为**变得关键。社会困境(social dilemma)存在固有风险:理性行动的能干 agent 可能导致集体次优结果,若侵略性行为更成功,竞争压力可能把系统推向次优均衡。

以往工作通常让 LLM 在给定状态/轨迹下**输出单个动作**,但近期分析显示 LLM 在这种 action-level 粒度上表现挣扎(例如无法识别对手在镜像自己出招的基本模式),因为它们并非为数据科学任务或此类输入格式而训练。论文要回答:系统化的 LLM agent 群体在竞争压力下是否预先倾向于合作或冲突?不同模型是否存在不同的合作/侵略偏置?

## 方法

核心思路:不让 LLM 逐回合出招,而是**提示其用自然语言写出固定策略,再转成 Python 算法**。好处是抽象层级更高(许多策略会用模式识别),且可在部署前由人工检查、测试安全性。

- **博弈框架**:iterated Prisoner's Dilemma(IPD),收益矩阵 CC=3/3、CD=0/5、DC=5/0、DD=1/1。每场 match 含 1000 轮,全员对战(all-play-all)。部分实验加入 **noise**:每个玩家每回合有 10% 概率动作被替换为相反动作,模拟执行错误。实现基于 Axelrod Python library。
- **attitude(态度)**:提示 LLM 生成三类态度的策略 —— Aggressive / Cooperative / Neutral。用 [[chatgpt]](ChatGPT-4o)与 [[claude]](Claude 3.5 Sonnet)两个前沿模型,每个模型 × 每种 prompt × 每种态度生成 25 个策略,统一由 ChatGPT-4o 转成 Python(因为不评估编码能力)。
- **三种 prompt 风格**:Default(直接告知博弈并要求写策略)、Refine(在 Default 基础上用 [[self-refine]] 自我批判再改写)、Prose(把博弈伪装成贸易谈判等场景、回避博弈论术语)。作者观察到即便 Prose 也会让模型应用其知识库里的博弈论策略;Claude 3.5 Sonnet 会比较自己与对手的累计收益,而 ChatGPT-4o 不会;Claude 在"学术合作"侵略场景下常拒绝写侵略策略,改成商业工程场景才解决。
- **attitude-agent**:每类态度对应一个 agent,每场 match 从该态度的策略集中**均匀随机抽样**一个策略,模拟玩家为每次交互定制策略。
- **[[evolutionary-search]] / Moran process**:用 [[evolutionary-game-theory]] 的 Moran process 演化群体——每轮全员对战算 fitness(总收益),按 fitness 正比克隆某玩家替换随机玩家,直到群体全为同一态度(genome),该态度即收敛均衡。

## 结果

- **Validation(归一化合作倾向,Table 3,Default 无 noise)**:Cooperative 与 Neutral 行为相近,自对战时几乎全程合作(propensity ≈ 0.99–1.00),首轮合作后大致走 Tit-For-Tat;Aggressive 通常首轮 defect。ChatGPT-4o aggressive 自对战合作率仅 0.30,对 neutral 时比对手少合作约 **12%**(最显著的剥削)。Claude 3.5 Sonnet aggressive 对 cooperative/neutral 时合作最少(0.15/0.18),但对其他 aggressive 时合作率反而最高。
- **对人类手写算法(Beaufils tournament,11 个标准策略如 Tit-For-Tat、Random,重复 200 次)**:两个模型的 Neutral/Cooperative 表现好,Aggressive 表现差,说明 LLM 更擅长写合作型策略。ChatGPT-4o + Refine 时 aggressive 显著改善(Figure 3)。
- **Head-to-head 收益(归一化均值,范围 [1,5],Table 4–5)**:ChatGPT-4o 各 prompt 下 Cooperative/Neutral 达到接近互相合作的收益(约 2.97–3.00),引入 aggressive 会降低双方收益;在 Refine/Prose 下 aggressive 被另两态度严格 dominate(用户没有理由选 aggressive),但 aggressive 总能赢过对手(损人更甚于损己)。Default 下 aggressive 是对 aggressive 的最佳应对。Claude 3.5 Sonnet 整体侵略策略导致双方收益更低,作者判断 Claude 更不擅长产出有效的侵略策略、有更强的 defect 偏置。加 noise 后两模型 aggressive 均被 dominate;Claude 在 Default/Refine 下 cooperative 自对战收益从近 3 跌到约 2(约一半回合互相 defect),但 Prose 显著改善 Claude 的抗噪表现。
- **均衡(Moran process,n=12,各 100 次,Table 6)**:用平衡初始(1:1:1)与偏侵略初始(4:1:1=8 aggressive + 2 + 2)。无 noise 时最易收敛到侵略均衡的是 ChatGPT-4o + Default 与两模型的 Refine。ChatGPT-4o + Default 时 aggressive 是 evolutionarily stable(自对战表现最好),约 **2/3** 的 Moran process 收敛到侵略均衡(4:1:1 下 66% aggressive)。**加入 noise 普遍大幅提高收敛到侵略均衡的概率**(作者解释:noise 掩盖了侵略意图,使报复理由变模糊,便于"克制的侵略")。
- **结论性观察**:多数场景下侵略策略处于劣势、系统倾向合作;但用含博弈论术语的 prompt 时 ChatGPT-4o 能造出更有效的侵略策略,提高侵略均衡风险。两模型对 Neutral 与 Cooperative 表现相近,作者推测是 [[rlhf]] / [[alignment]] fine-tuning 注入了合作偏置。**Refine(self-refine)在不损害合作策略的同时提升侵略策略**,缩小合作与侵略能力差距,可能危险(增强 MAS 中侵略策略可行性)。作者开源 benchmark(github.com/willis-richard/evollm)供模型开发者评估 emergent behaviour。

## 在本 wiki 中的位置

本文属于 [[llm-multi-agent]] 与 [[ai-safety]] 交叉处的评测类工作:它把经典博弈论的 IPD 与 [[evolutionary-game-theory]] 引入对 LLM agent **集体涌现行为**的考察,关注 [[cooperation]] 与冲突的平衡。与"让 agent 逐步行动"的主流不同,它强调"先生成可检查的策略"以利部署前安全审计,这一思路呼应 [[scalable-oversight]] 与 differential capabilities 的讨论。在方法上用到 [[self-refine]] 提示;在被试模型上覆盖 [[chatgpt]] 与 [[claude]]。其关于对齐 fine-tuning 可能带来合作偏置的假设,可与 [[rlhf]] / [[alignment]] 相关条目互参。作者之一 [[joon-sung-park]] 的 Generative Agents 等社会模拟工作是其相关背景(本文亦引用 [[generative-agents]])。
