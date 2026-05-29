---
type: source
subtype: paper
tags: [multi-agent-rl, llm-collaboration, magrpo, grpo, dec-pomdp, cooperative-marl]
created: 2026-05-29
updated: 2026-05-29
arxiv: "2508.04652"
raw: raw/2508.04652.pdf
authors: [Shuo Liu, Tianle Chen, Zeyu Liang, Xueguang Lyu, Christopher Amato]
year: 2025
---

# LLM Collaboration with Multi-Agent Reinforcement Learning (MAGRPO)

本文把多个 LLM 的协作建模为合作式 Multi-Agent Reinforcement Learning(MARL)问题,并提出 Multi-Agent GRPO(MAGRPO)算法,在写作与编码协作任务上微调多个 LLM,使其高效生成高质量且互相配合的回复。

## 问题

已有大量工作在 Multi-Agent Systems(MAS)中对多智能体交互进行建模与求解,但绝大多数 LLM 是独立预训练的,并未针对协作优化。现有 LLM 协作方法分两类,各有缺陷:

- **推理阶段协调**(debate、discussion、verification 等,prompt 层面):模型固定、未面向协调目标训练,智能体可能给出冲突答案或传播错误信息,且有效 prompt 的设计困难、不明确。
- **微调智能体**(individual reward 或 role-conditioned reward):需要为每个智能体精心设计奖励;作为 independent learning,缺乏收敛保证(非平稳环境下各自更新策略)。

因此需要一种在共享、人类对齐奖励下训练多个 LLM 协作的方法。

## 方法

将 LLM 协作形式化为合作式 MARL,具体为 **Dec-POMDP**(Decentralized Partially Observable Markov Decision Process),用一个 joint reward 实现协作,同时保留 decentralized execution(去中心化执行)。形式化要素:

- n 个 LLM agent 各由一个语言模型实例化;
- 全局状态 s_t 含可被 reward model 访问的部分 s^acc 与不可维护的用户状态 s^usr;
- 每个 agent 的 local observation 是 prompt(对状态的部分、有噪声视图),local action 是对该 prompt 的自然语言回复;
- joint reward 由预定义规则或预训练 [[reward-model]] 给出,取决于当前可访问状态与所有 agent 的联合动作;
- 每个 episode 多轮进行,用户/外部模型/系统验证方案并把更新嵌入后续 prompt,直至任务完成或达到 turn 上限 H。

**MAGRPO(Multi-Agent GRPO)**:在多轮设置下联合训练 LLM agent。基于单智能体 [[ppo]] 家族的 GRPO 思路,每个 turn t 每个 agent 按策略 π_i 采样一组 G 个回复(group),组合成 joint action 并获得 joint reward。借鉴 [[rlhf]] 与 [[direct-preference-optimization]] 的做法,把每个 agent 的决策建模为从输入指令到完整回复的直接映射。关键设计:

- 用 group-based Monte Carlo 估计当前历史的期望回报,从而无需大 value model 即可得到 centralized 估计(MARL 中常见),平衡了 centralized training 与 decentralized execution(CTDE 思想,但用组估计替代 centralized critic);
- advantage 用组内回报减去组均值(Eq.1);策略梯度按 Eq.2 更新;
- MAGRPO **不做 importance sampling、不做 epsilon clipping**(为简化),并把 KL 散度系数设为 0,以鼓励相对 base model 更大的策略偏移。

属于 [[multi-agent-reinforcement-learning]] 与 [[llm-multi-agent]] 交叉,与 [[multi-agent-collaboration]]、[[multi-agent-debate]] 等推理期协调方法形成对比。建立在 GRPO、[[ppo]]、MAPPO 等之上。

## 结果

在写作与编码两类协作上评测,base 模型分别为 Qwen3-1.7B(写作)与 Qwen2.5-Coder-3B(编码),硬件为 GeForce RTX 5090,结果归一化到 return scale,10 次运行平均。基线含 single model、parallel/naive concatenation、sequential generation/pipeline、one-round discussion。

**写作协作**(Table 1):
- TLDR 摘要(Reddit 帖子,2 个 Qwen3-1.7B agent):MAGRPO Return 94.5%,Structure 98.7、Coherence 78.5,均为各项最佳;速度 202.3 tokens/s,response time 2.1s,比同参数量 single Qwen3-4B 快约 3 倍。
- arXiv 摘要扩展:MAGRPO Return 93.1%,显著优于 single model(44.9%)与各多智能体基线。

**编码协作**(Table 2,HE=HumanEval,CHE=自建 CoopHumanEval):
- HumanEval:Multi-Turn MAGRPO Return 86.7%(Single-Turn 83.7%);Tests 通过率 68.4%、Cooperation 84.9%,均优于所有基线(naive concatenation 仅 53.9%)。
- CoopHumanEval:Multi-Turn MAGRPO Return 88.5%,Tests 75.0%、Cooperation 86.3%。
- 在 CHE(具良好协作结构的数据集)上训练比在 HE 上 return 更高、方差更低;multi-turn 训练后期可利用外部 AST/执行反馈的 error message 改进回复并最终超越 single-turn。

**涌现的协作模式**:auxiliary function 处理核心逻辑而 main agent 加备份/装饰;或 main agent 作为 coordinator 分解任务并分派给 auxiliary;auxiliary 作为 strategy filter。表明在相对简单的 joint reward 下即可涌现多样协作方案。

结论:MAGRPO 能学到有效的协作方案,为把 MARL 方法用于可扩展、鲁棒的 LLM 协作打开了大门。代码开源于 OpenMLRL/CoMLRL。

## 在本 wiki 中的位置

本文连接 [[large-language-models]]、[[reinforcement-learning]] 与 [[multi-agent-systems]] 三大主题:它不在 prompt 层做 [[multi-agent-debate]]/[[multi-agent-collaboration]],而是用合作式 [[multi-agent-reinforcement-learning]] 直接微调多个 LLM。算法上扩展了 GRPO/[[ppo]] 到多智能体多轮设置,与 [[rlhf]]、[[reward-model]]、[[code-generation]] 相关。来自 Northeastern University 的 Christopher Amato 团队(合作式 MARL 方向)。
