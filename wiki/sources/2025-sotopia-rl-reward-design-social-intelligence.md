---
type: source
subtype: paper
tags:
  - reinforcement-learning
  - reward-design
  - social-intelligence
  - reward-model
  - process-reward-model
  - llm-agent
created: 2026-05-29
updated: 2026-05-29
arxiv: 2508.03905
raw: raw/2508.03905.pdf
authors:
  - Haofei Yu
  - Zhengyang Qi
  - Yining Zhao
  - Kolby Nottingham
  - Keyang Xuan
  - Bodhisattwa Prasad Majumder
  - Hao Zhu
  - Paul Pu Liang
  - Jiaxuan You
year: 2025
---

# SOTOPIA-RL: Reward Design for Social Intelligence

SOTOPIA-RL 把粗粒度的 episode 级反馈细化为 utterance 级、多维度的 reward,用单轮在线 RL 训练社交 agent,在 [[sotopia-eval|SOTOPIA]] 上取得 SOTA 的 social goal completion 分数。

## 问题

[[social-intelligence]](社交智能)正成为 [[large-language-models]] 的关键能力(协作、谈判、说服、迁就等)。[[reinforcement-learning]] 天然适合训练社交 agent——可直接从交互中学策略而无需人工标注。但社交任务与 math/coding 这类有 verifiable reward 的任务有两点本质不同:

1. **单条 utterance 的质量与最终成功只是弱相关**:谈判中一句误导性发言可能反而促成更好的结果,不像数学题"正确的中间步骤"才能得到正确答案。
2. **社交交互是内在多维度的**:有些 utterance 直接推进目标,有些则通过建立 rapport、维持参与度、维护对话流来起间接但关键的作用。

直接用 episode 级单一 reward 训练 sample-inefficient,且容易 [[reward-hacking|reward hacking]]、难以捕捉细粒度对话行为。作者主张:需要为社交任务专门设计 utterance 级、多维度的 [[reward-model|reward model]]。

## 方法

SOTOPIA-RL 是一套两阶段的 RL training recipe,基于 [[sotopia-eval|SOTOPIA]] 社交学习环境(社交交互建模为 POMDP,action 为 utterance,LLM-as-judge 给出多维度反馈)。

**Stage 1 —— 离线社交 reward 设计(用 LLM)。** 从已有社交 episode 出发,通过两步把 episode 级 reward 扩展成 utterance 级多维度 reward:
- **Reward attribution(episode 级 → utterance 级)**:用强 LLM(如 [[gpt-4o-mini|GPT-4o]])在**完整 episode 上下文**中为每条 utterance 打 attribution 分 A(a_t, τ)∈[0,1],再与 episode 结果 G 结合,r_t = G · A(a_t, τ)。这是一种"全局上下文"的离线信用分配。论文比较了四种 attribution 基线:UNIFORM、SINGULAR、SCALED、DIRECT,其中 DIRECT(独立归一化、放松约束)效果最好。
- **Reward aggregation(单维 → 多维)**:采用 SOTOPIA 全部 7 个评测维度作为 rubric,对每条 utterance 在各维度归一化后做加权平均聚合。实证发现 relationship maintenance(REL)和 knowledge seeking(KNO)对提升 goal 尤其关键。最终 SOTOPIA-RL 用 REL+KNO+GOAL 三者简单平均。

**Stage 2 —— 在线社交 agent 训练(RL)。** (2.1)用 SFT 初始化策略并从离线标签蒸馏出一个**只依赖当前对话历史**的 utterance 级 RM(MSE loss 回归 r_t);(2.2)先用 behavior cloning 在 GPT self-play rollout 上热身,再用 [[ppo|GRPO]] 做单轮在线 RL,每个 self-play rollout 拆成多个 (s_t, a_t) 对,策略根据在线 RM 的 reward 更新。刻意不加显式 reasoning trace,只优化 utterance 生成。

base LLM 为 Qwen2.5-7B-Instruct(策略与 RM),GPT-4o 作 LLM-as-judge。

## 结果

评测在 SOTOPIA-hard(14 个困难场景 × 10 个 agent 配对)和 SOTOPIA-all(90 场景 × 2 配对),指标含 BEL/REL/KNO/GOAL/AVG(GOAL 为主指标)。

- **SOTA goal completion**:Qwen2.5-7B + SOTOPIA-RL 在 SOTOPIA-hard 上 GOAL = **7.17**、SOTOPIA-all 上 GOAL = **8.31**(以 GPT-4o 为 partner),显著超过 GPT-4o(6.97 / 8.19)、Claude-Sonnet-3.5、Deepseek-v3,以及 PPDPP / EPO / DAT / DSI 等训练基线(GOAL 维度 paired t-test p<0.05)。
- **超越 GPT 蒸馏**:训练数据来自 GPT self-play 与 GPT 离线标注,但 SOTOPIA-RL(7.17)反超 GPT-4o 本身(6.97)——说明不只是蒸馏。
- **reward attribution 有效**:DIRECT 把 GOAL 从 SCALED 的 6.74 提到 7.21;远高于 UNIFORM。
- **reward aggregation 有效**:REL+KNO+GOAL 组合(以 BC 为 partner)在 SOTOPIA-hard 上 GOAL = **7.81**、AVG = 3.80,比单维 GOAL-RL(7.21)有约 7.9% 提升。
- **离线 attribution 是关键**:RL w/ 离线 reward 标签 GOAL = 7.81,远高于 online 标签(6.69)和 BC(6.76)。
- **不依赖最强 LLM**:用 GPT-4o / Qwen2.5-72B / Qwen2.5-7B 做 utterance reward 标注,标签两两相关性 >0.7。
- **无 reward hacking**:在 5 个不同 partner、5 个不同 evaluator 上提升一致;人工评测也确认提升(SOTOPIA-RL 7.81/GPT-4o、5.89/human,相关性 0.866)。AMPO 在 SOTOPIA-hard 达 7.50,但其需显式 reasoning、每条 utterance 平均 >640 推理 token,论文认为不可比。

## 在本 wiki 中的位置

本文是 [[sotopia-eval|SOTOPIA]] 系列([[2023-sotopia-social-intelligence-evaluation]] 提出环境与评测、[[2024-sotopia-pi-social-agents|SOTOPIA-π]] 用 self-reinforcement)的 RL 训练续作,核心贡献在 [[reward-design]] 而非新环境。它把 math/coding 领域的 [[process-reward-model|Process Reward Model]] 思想(如 PRIME、Math-Shepherd 的 step-level reward)迁移到社交对话:用 utterance 级信用分配 + 多维度 rubric 解决社交 reward 的弱相关与多维性问题,并以 [[reward-hacking]] 的多重检验作为可靠性证据。可与 [[reward-model]]、[[multi-task-learning]](多目标 RL)、[[reinforcement-learning]] 训练 [[role-playing-agent|社交 agent]] 等概念页对照。
