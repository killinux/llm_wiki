---
type: concept
subtype: method
tags: [rl, rlhf, policy-optimization, alignment]
created: 2026-05-29
updated: 2026-05-29
sources: 6
---

# PPO

PPO(Proximal Policy Optimization)是一种基于策略梯度的强化学习算法,通过裁剪(clipping)目标函数限制每次策略更新的幅度,从而在保证训练稳定的同时高效地优化策略。

## 在本 wiki 中的出现

- [[2022-instructgpt]]:作为 RLHF 三阶段流程(SFT → 奖励模型 → PPO)中的最后一环,PPO 被用来根据奖励模型给出的偏好信号微调策略模型,使 GPT-3 与人类偏好对齐。借助这一流程,1.3B 的 InstructGPT 模型在人类偏好评测上胜过 175B 的 GPT-3,同时更真实、毒性更低。
- [[2024-easyrl4rec]]:面向 RL-based 推荐系统的易用代码库,基于五个公开数据集构建轻量 RL 环境,提供四个核心模块与面向长期收益的统一训练/评测流程,PPO 作为经典 RL 方法之一被纳入对照实验。
- [[2024-llm-critics-help-catch-llm-bugs]]:OpenAI 用 RLHF(其中以 PPO 进行策略优化)训练 GPT-4 级别的 critic 模型 CriticGPT,让 LLM 写自然语言批评指出代码 bug,以可扩展监督方式帮助人类更准确评估模型生成的代码。
- [[2024-score-self-correct-via-rl]]:SCoRe 用完全自生成数据的多轮在线强化学习(两阶段+奖励塑形)训练单个 LLM,在 MATH 上把内在自我纠错 Δ(t1,t2) 从 -11.2% 提到 +4.4%(整体提升 15.6%)、HumanEval 上达 12.2%。
- [[2025-sotopia-rl-reward-design-social-intelligence]]:SOTOPIA-RL 把 episode 级反馈细化为 utterance 级、多维度 reward,用单轮在线 GRPO 训练社交 agent,在 SOTOPIA 上取得 SOTA goal completion(SOTOPIA-hard 7.17、SOTOPIA-all 8.31)。
- [[2025-llm-collaboration-marl-magrpo]]:把多 LLM 协作建模为合作式 MARL(Dec-POMDP)并提出 Multi-Agent GRPO(MAGRPO),在写作与编码协作上微调多个 LLM;TLDR/arXiv return 达 94.5%/93.1%,HumanEval/CoopHumanEval return 达 86.7%/88.5%。

## 相关

- [[rlhf]]
- [[reward-model]]
- [[sft]]
- [[gpt-3]]
- [[2022-instructgpt]]
- [[2024-easyrl4rec]]
- [[2024-llm-critics-help-catch-llm-bugs]]
- [[grpo]]
