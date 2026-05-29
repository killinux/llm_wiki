---
type: source
subtype: paper
tags:
  - recommender-system
  - llm-agent
  - user-simulation
  - simulated-environment
  - reinforcement-learning
  - instruction-following
created: 2026-05-29
updated: 2026-05-29
arxiv: "2509.10397"
raw: raw/2509.10397.pdf
authors:
  - Fei Liu
  - Xinyu Lin
  - Hanchao Yu
  - Mingyuan Wu
  - Jianyu Wang
  - Qiang Zhang
  - Zhuokai Zhao
  - Yinglong Xia
  - Yao Zhang
  - Weiwei Li
  - Mingze Gao
  - Qifan Wang
  - Lizhu Zhang
  - Benyu Zhang
  - Xiangjun Fan
year: 2025
---

RecoWorld 是 Meta 提出的一套为 agentic recommender system 构建模拟环境(simulated environment)的蓝图,采用"模拟用户 + agentic 推荐器"的双视角架构,在以最大化用户留存为目标的多轮交互中训练 agent,让其在不影响真实用户的前提下从错误中学习。

## 问题

传统 [[recommender-system]] 依赖离线指标(如 [[recall]]、[[ndcg]])与在线 A/B 测试做评估。离线评估基于历史用户行为,会引入 [[exposure-bias]],使系统强化已知模式而非发现新兴兴趣;在线 A/B 测试虽有价值,但反馈回路慢、必须谨慎对待真实用户,无法激进试错。

随着 agentic recommender system 兴起——推荐器作为自主 agent,主动接受用户指令、习得新技能、根据经验调整行为——亟需可复现真实用户反馈的模拟环境,以便在不损害用户体验的前提下大胆测试新策略。RecoWorld 旨在为这类系统提供类似 OpenAI Gym 的训练空间。

## 方法

**双视角架构(dual-view architecture)**:

- **用户模拟器(user simulator)**:利用现代 LLM 的推理能力,逐项审阅推荐物品、更新自身"mindset(心态)",并在感知到可能脱离(disengagement)时生成反思式自然语言指令(reflective instruction),如"show me more interesting content"。用户动作空间包含 7 类:Click、Comment、Share、Like、Watch(指定时长)、Skip、Leave。每个物品决策走三步:Think it through(推理)→ Take action(动作)→ Update your mindset(更新心态),示例用 [[gpt-4-1-mini]](GPT-4.1)搭建用户画像生成。
- **agentic 推荐器(instruction-following recommender)**:作为自主 agent,具备四项核心能力——perception(感知用户状态)、reasoning and planning(将指令拆解为子任务并分派给检索/排序模块)、action/tool use(生成更新后的推荐列表)、memory(记录用户行为)。

**多轮交互(multi-turn interaction)**:模拟用户在一个 session 内跨多轮与 agentic RecSys 交互,产生 interaction trajectory;系统建模为 [[markov-decision-process]],状态 s_t 表示用户 mindset,奖励信号取自轨迹级交互统计(如总停留时间、点击数),用于 RL 训练。可用 [[ppo]](异步奖励)或 [[dpo]](off-policy)优化策略,并引入 LLM-based judge 对轨迹按预定义任务规则评分,仅保留满足成功标准的高质量轨迹用于训练。

**参与历史建模(engagement modeling)**:提出三种利用 LLM 推理能力的方案——text-based modeling(文本表示)、multimodal modeling(用 Qwen3-Omni 等 MLLM 或 Gemini-2.5-Pro 等 VLM)、[[semantic-id]] modeling(用语义 ID 表示物品内容)。并定义了 engagement memory(交互级 + session 级双层记忆)、evolving preference modeling(用 recurrent/attention/diffusion 风格函数建模偏好演化与 mindset update)。

**多智能体模拟(multi-agent simulator)**:支持 N 个模拟用户相互交互,模拟社交网络中的信息扩散、群体极化、内容创作者的发布策略试验等 collective impact。

## 结果

本文是定位论文/蓝图(blueprint),明确不提供实验结果,而是给出构建模拟环境的框架与评估设计。文中给出的相关数字均为对已有工作的引用,例如:Meta 的 HSTU 生成式推荐器相比基线最高带来 65% 的排序指标提升,其 1.5 万亿参数版本提升在线 A/B 指标 12.4%;Kuaishou 的 OneRec 用端到端生成模型替代检索-排序流水线、部署到百万级用户,watch-time 提升 +1.6%。

四个示例用例:评估 RecSys 的指令遵循能力、让创作者试验发布策略、支持边缘/新用户探索兴趣、为 agentic RecSys 建立排行榜(leaderboard)。论文于 2025 年 9 月内部发布,称已获得 Google 与 Kuaishou 推荐团队的关注。

## 在本 wiki 中的位置

RecoWorld 是用 [[llm-agent]] 构建 [[recommendation-simulator]] / [[user-simulation]] 的代表性工作,与 [[kuaisim]]、[[agent4rec]]、[[agentcf]]、[[recagent]]、[[interecagent]] 等 LLM 驱动的推荐模拟器一脉相承,但更强调"用户指令 + agentic 推荐器响应"的多轮交互范式与 [[rl-based-recsys]] 训练。它把 [[long-term-recommendation]] / [[user-retention]] 作为奖励信号,可与 [[reinforcement-learning]]、[[markov-decision-process]]、[[human-behavior-simulation]] 等概念对照,也是 [[meta]] 在 agentic recommender 方向上的方法论蓝图。
