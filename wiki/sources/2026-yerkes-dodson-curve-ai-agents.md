---
type: source
subtype: paper
tags: [llm-multi-agent, multi-agent-systems, emergent-behavior, curriculum-learning, social-simulation, cooperation, claude-3-5-sonnet]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2603.07360
raw: raw/2603.07360.pdf
authors: [Ivan Pasichnyk]
year: 2026
---

# The Yerkes-Dodson Curve for AI Agents: Optimal Environmental Pressure for Emergent Complexity in LLM Multi-Agent Systems

本文在一个网格世界"生存竞技场"里系统性地改变环境压力,首次实证发现 [[llm-multi-agent]] 系统的合作行为遵循 Yerkes-Dodson(倒 U 形)曲线:中等压力下合作最旺盛,过低或过高压力都会抑制社会行为。

## 问题

设计能最大化 AI agent 涌现行为发展速率的环境仍是开放问题。认知心理学的 Yerkes-Dodson 定律描述了唤醒/压力与任务表现之间的倒 U 形关系(太低则懈怠,太高则崩溃,中间最优),但此前从未在 LLM agent 群体中被系统验证。已有工作表明不同 LLM 在博弈环境中有稳定的行为"表型"、在资源稀缺下会表现出生存本能,但没有人系统性地变化环境压力来刻画完整的"压力-表现"曲线。作者提出三个研究问题:RQ1 LLM agent 是否在环境压力与合作行为间表现出倒 U 关系;RQ2 在何种压力下行为库会崩溃、崩溃是什么样子;RQ3 繁殖竞争(而非生存威胁)能否在不致死的前提下驱动社会复杂性。

## 方法

作者构建 Survival Arena —— 一个离散网格世界(生存压力实验用 v6.1 引擎、9×9 网格;性选择实验用 v7.0 引擎、7×7 网格),含会逐回合再生的食物节点(nf=8)与代币节点(nt=5,作为交易与代价信号的次级货币)。

- Agent 架构:每个 agent 有 6 个属性(STR/SPD/INT/SOC/END/CHA,取值 [1,8]、总预算 30 点);动作空间含 GATHER、MOVE、ATTACK、TRADE、REST、TRAIN,以及 v7 专有的 COMMUNICATE、REPRODUCE。
- Agent 策略:每回合由一次 [[claude-3-5-sonnet]] 调用产生决策,prompt 只给局部状态与可见信息,**不提供任何行为提示、few-shot 示例或微调**——所有行为均来自 LLM 预训练策略,作者称之为"遗传记忆"。
- 压力轴 1(生存成本 upkeep):每回合扣食物,食物归零即死亡;P2b 阶段固定其它参数只改 upkeep。
- 压力轴 2(性选择 V7):基于 Trivers 亲代投资理论,把 agent 分为 Provider(8 个,可提出繁殖,代价 6 食物+3 代币)与 Chooser(8 个,经独立 LLM 调用评估提议,无论是否接受都付 12 食物+5 代币);后代属性取双亲均值加高斯噪声;upkeep 设低(u=2),压力来自繁殖而非致死。
- 实验规模:四个阶段共 22 次完整运行(P1 验证 2 次、P2 宽扫 13 次、P2b 受控扫 6 次、V7 性选择 1 次),全部使用 [[claude-3-5-sonnet]],总计约 25 小时墙钟时间、50-100 美元 API 成本。
- 评估指标:交易数(主合作指标)、攻击数、存活者、游戏时长、社会动作占比、动作分布的归一化 [[shannon-entropy]]。

## 结果

- **发现 1(倒 U 曲线)**:P2b 中交易合作随压力呈清晰倒 U。低压(upkeep=2)两次复现各完成 11、12 次交易;中压(upkeep=5)交易飙升到 **29** 次;高压(upkeep=6、7)降到 16、8 次。最优点 upkeep=5 处于"生存边缘"——agent 仅靠初始资源约能撑 12 回合(upkeep=2 时可撑 30+ 回合)。
- **发现 2(行为崩溃)**:高压(upkeep≥7)游戏迅速崩溃;P2 阶段 upkeep=8-15 时游戏时长缩到 5-12 回合,动作收敛为 MOVE 主导(56-68%)。upkeep=15("末日"压力)游戏只持续 5 回合、67.7% 是 MOVE、零交易。
- **发现 3(性选择消除攻击)**:V7 实验中攻击降为 **0**(而生存压力下攻击占 9-14%),出现 COMMUNICATE/REPRODUCE 动作;17 次繁殖尝试产出 3 个后代、8 次通信事件;19 个 agent 中 12 个存活到 40 回合结束,种群从 16 增长到峰值 18。
- **发现 4(熵具误导性)**:Shannon 熵随压力单调上升(0.764→0.892),看似与倒 U 矛盾,但实为小样本伪迹——高压下 agent 早死、总动作数少(upkeep=7 仅 201 个动作 vs upkeep=2 的 648 个),全局 Shannon 熵不是可靠的行为复杂度代理。
- 结论:LLM agent 合作的最优环境压力在"生存边缘";环境压力即便不更新权重也能充当训练课程(类似 [[curriculum-learning]]),为 AI agent 课程设计提供了新设计参数。局限包括多数配置仅单次运行、仅用单一模型 Claude 3.5 Sonnet、规模小(16 agent)、upkeep=3 缺失。未来工作含多模型竞技场(V8,把 Claude/GPT-4o/DeepSeek-R1/Gemini/Llama 当作不同"物种")与多种子统计验证。

## 在本 wiki 中的位置

本文属于 [[social-simulation]] 与 [[human-behavior-simulation]] 方向中"用 LLM 当 agent 策略研究涌现社会行为"的一支,与 [[generative-agents]] 同样把环境交给 LLM 预训练策略驱动,但聚焦于**环境压力**这一变量。它把认知心理学的 Yerkes-Dodson 定律迁移到 [[multi-agent-systems]],并将性选择/繁殖竞争作为"软压力"机制引入,可与 [[multi-agent-reinforcement-learning]]、[[curriculum-learning]] 等关于压力驱动能力涌现的工作对照阅读。实验全程使用 [[claude-3-5-sonnet]]。
