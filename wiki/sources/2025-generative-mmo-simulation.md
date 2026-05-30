---
type: source
subtype: paper
tags: [llm-agent, multi-agent-systems, human-behavior-simulation, game-simulation, agent-based-modeling, reinforcement-learning]
created: 2026-05-29
updated: 2026-05-29
arxiv: "2512.02358"
raw: raw/2512.02358.pdf
authors: [Ran Zhang, Kun Ouyang, Tiancheng Ma, Yida Yang, Dong Fang]
year: 2025
---

# Beyond Playtesting: A Generative Multi-Agent Simulation System for Massively Multiplayer Online Games

提出一个由 [[large-language-models]] 驱动的生成式多智能体 MMO(大型多人在线)游戏仿真系统,通过在真实玩家行为数据上做 SFT + RL 微调,让 agent 高保真地模拟玩家决策,从而在不上线真实 A/B 测试的情况下,低成本地评估数值系统与机制设计(mechanism design)的优化效果。

## 问题

MMO 游戏的数值系统(numerical system)与机制设计直接决定玩家体验、经济平衡与长期可持续性,但优化它们很难:

- **传统方法代价高**:依赖大规模线上实验或基于预设统计模型的参数调优,耗时、昂贵,且可能破坏真实玩家体验(高时间成本 High Time Costs、高机会成本 High Opportunity Costs)。某些重大机制改动(如引入交易系统、开放新玩法)根本无法靠小规模线上 A/B 测试验证。
- **离线仿真保真度低**:简化的离线仿真系统虽可替代,但保真度有限,agent 无法准确模仿真实玩家的推理与对干预的反应。
- **已有生成式 agent 工作局限于孤立场景**:此前用 [[generative-agents]] 做游戏仿真的研究(如玩家谈判、Pay-to-Win 机制)只聚焦单一隔离场景与机制,忽略了玩家行为之间相互关联的后果(如战斗结果会影响购买决策),且多以定性观察验证,而非用真实游戏数据做数值校验。

## 方法

系统包含五大组件:Simulation Server、Game Services、Data Services、Experiment Manager、Real Game Data。

- **Player Agent(玩家智能体)**:核心组件,采用三阶段微调流水线把通用 LLM 适配到 MMO 领域。
  1. **Vocabulary Expansion SFT**:针对游戏专有实体(如装备 "AWM")扩展 tokenizer 并训练新 token 嵌入,用 [[deepseek-v3]] 自动生成领域 QA 对,以 [[lora]] adapter + cross-entropy loss 优化。
  2. **Action Planning SFT**:学习根据历史动作、环境反馈与玩家画像(profile)预测下一步动作 ∈ {offline, battle, buying, selling},复刻真实玩家的人性化决策。
  3. **RL Enhancement(GRPO)**:用 GRPO([[reinforcement-learning]])强化推理与泛化能力,鼓励 agent 在行动前像人类一样审慎推理,提升决策的保真度与可解释性。
  - agent 还配有 ReAct([[react]])规划、推理与长短期记忆模块([[memory-module]])。基座模型为 Qwen2.5-1.5B([[qwen2-5-instruct]] 系列),LoRA rank=16、α=0.2。
- **Battle Server(环境模型)**:数据驱动的环境模型,用真实大规模连续对局数据训练分类与回归模型,预测每场战斗的胜负与赛内收益(income),并保证胜负/收益预测对后续行为转移的因果影响(如败北后购买更好装备、连败后下线)。
- **Game Services**:实现三个核心服务——Battle Server(货币来源 / currency source)、NPC Shop 与 Black Market(货币回收 / currency sink,黑市靠交易税抽走货币)。
- **Data / Simulation Services**:用轻量 [[mqtt]] 消息队列(point-to-point / group / broadcast)连接 agent、Experiment Manager 与 Simulation Server;基于 Python 异步框架 + 协程实现高并发、非阻塞的 agent 生命周期管理;Resource Manager 控制对外通信池以提升可扩展性。Experiment Manager 提供 GUI 控制面板用于配置、干预与实时监控。

## 结果

- **Player Agent 动作预测**:在单日采集的 10,000 条玩家轨迹上做四分类(offline/battle/buy/sell)next-step 预测。相比未微调的 SOTA 基线 [[deepseek-v3]](28.50% 准确率),在玩家轨迹上微调的 PlayerAgent-GRPO 达 36.84%(+8.34%);再加入玩家画像信息的 PlayerAgent-Profile-GRPO 达 38.69%(再 +1.85%,总计 +10.19%)。真实动作分布:battle 42.4%、buy 31.3%、sell 23.1%、offline 3.2%。
- **Battle Server 校验**:用 2025 S1 赛季对局数据训练,在 2025 S2 赛季上做无数据泄漏验证。基于游戏局数、声望、段位、时长、模式偏好、场均击杀等十余个特征,把玩家聚成五类典型画像(Stable Development、Novice、Wealth-Accumulating Elite、Casual、High-skill)。预测的胜率与场均收益对全部五类玩家都很准确,尤其对 Wealth-Accumulating Elite 与 Stable Development 玩家;Novice 与 Casual 玩家波动较大、误差相对更大。
- **干预案例研究(Black Market)**:复现真实游戏中"引入官方黑市交易平台"这一干预。仿真显示非正式赛内交易(in-game trading)占比从干预前 27.4% 降至干预后 1.5%(战斗 25.6%→31.4%、购买 43.2%→61.4%),与真实世界因果效应一致——说明系统能在部署前可靠预测设计决策的因果效果。

## 在本 wiki 中的位置

本文属于 [[human-behavior-simulation]] 与 [[social-simulation]] / [[agent-based-modeling]] 在游戏领域的应用,延续 [[generative-agents]] 与 [[2023-s3-social-network-simulation]] 等"用 LLM agent 模拟人类社会"的脉络,但更强调用真实行为数据做 SFT+RL 微调与数值校验,而非纯 prompt 驱动。与 [[recommendation-simulator]]、[[agent4rec]]、[[oasis]] 等用户/社会仿真器一样,其价值在于提供一个低成本、可解释的离线"沙盒"来评估干预效果;不同之处是聚焦 MMO 游戏的数值系统与机制设计。技术上结合了 [[supervised-fine-tuning]]、[[lora]]、GRPO([[reinforcement-learning]])、[[react]] 规划与 [[memory-module]],基座为 [[qwen2-5-instruct]] 系列,并用 [[deepseek-v3]] 作合成数据生成与基线对比。
