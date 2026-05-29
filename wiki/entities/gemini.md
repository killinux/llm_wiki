---
type: entity
subtype: model
tags: [llm, model, google, gemini]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Gemini

Gemini 是 Google 推出的多模态大语言模型系列,广泛用作各类研究与应用中的基座或对比模型。

## 在本 wiki 中的出现

- [[2024-score-self-correct-via-rl]]:SCoRe 用完全自生成数据的多轮在线强化学习(两阶段 + 奖励塑形)训练单个 LLM,在 MATH 上把内在自我纠错 Δ(t1,t2) 从 -11.2% 提到 +4.4%(整体提升 15.6%),HumanEval 上达 12.2%。
- [[2026-self-organizing-llm-agents]]:一项 25,000 任务的大规模实验发现"内生性悖论":固定智能体顺序但角色自主的混合协议(Sequential)在质量上同时超越中心化(+14%)与完全自主(+44%)协调,但仅当底层模型足够强(存在能力门槛)。
- [[2026-llm-agents-competition-cooperation-games]]:研究 LLM agent 在资源分配博弈与 Cournot 竞争中的策略行为:多轮非零和提示下 agent 倾向合作而非收敛到 Nash 均衡,fairness 推理是核心驱动,并提出 θ/γ 合成收益函数框架刻画其信任建立、报复与 endgame 衰减动态。

## 相关

- [[score-self-correction]]
- [[reinforcement-learning]]
- [[google-deepmind]]
- [[self-organizing-llm-agents]]
- [[llm-agents-competition-cooperation-games]]
