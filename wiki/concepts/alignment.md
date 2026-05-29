---
type: concept
subtype: method
tags: [alignment, rlhf, human-preference, safety]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# Alignment

Alignment 指通过训练手段让语言模型的行为符合人类意图与价值偏好,使其输出更有用(helpful)、更真实(truthful)、更无害(harmless)。

## 在本 wiki 中的出现

- [[2022-instructgpt]]:Alignment 是该工作的核心目标。InstructGPT 采用 RLHF(SFT → 奖励模型 → PPO)流程对齐 GPT-3,使得 1.3B 参数的模型在人类偏好评测中胜过 175B 的 GPT-3,同时在真实性上更好、毒性更低。这是 Alignment 作为一种训练方法落地的代表性案例。
- [[2025-drivemlm-autonomous-driving]]:DriveMLM 将 multi-modal LLM 对齐到自动驾驶行为规划模块的离散决策状态,使语言输出可转为车辆控制,在 CARLA Town05 Long 上实现闭环驾驶并取得 DS 76.1、MPI 0.96。
- [[2025-llm-agents-cooperate-social-dilemma]]:让 ChatGPT-4o 与 Claude 3.5 Sonnet 为 iterated Prisoner's Dilemma 写出完整策略(而非逐步出招),用 evolutionary game theory / Moran process 模拟 LLM agent 群体演化,发现多数场景下侵略策略劣势、系统倾向合作,但博弈论 prompt 与 self-refine 会增强侵略策略并提高收敛到侵略均衡的风险。
- [[2025-extended-refusal-defense-against-abliteration]]:通过 extended-refusal 微调把安全信号从单一潜在方向分散到多 token 位置与多维度,使模型在 abliteration 攻击后仍保持 >90% 拒绝率,同时通用性能几乎不变。

## 相关

- [[rlhf]]:本页中实现 Alignment 的主要技术手段。
- [[sft]]:RLHF 流程的第一步(监督微调)。
- [[reward-model]]:用于建模人类偏好。
- [[ppo]]:用于按奖励模型优化策略的强化学习算法。
- [[human-preference]]:Alignment 优化所依据的信号。
- [[2022-constitutional-ai]]:另一种 Alignment 路线,用 AI 反馈(RLAIF)替代部分人类反馈。
- [[2022-instructgpt]]:提及本概念的资料。
- [[refusal]]:拒绝有害请求是无害性对齐的核心行为。
- [[abliteration]]:针对拒绝方向的攻击,extended-refusal 是其防御手段。
- [[multi-agent-llm]]:多智能体场景下的合作与对齐问题。
