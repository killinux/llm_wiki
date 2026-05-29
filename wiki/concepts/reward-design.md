---
type: concept
subtype: method
tags: [reward-design, reinforcement-learning, llm, reward-function]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# reward design

奖励设计(reward design)指为强化学习任务构造能正确引导智能体行为的奖励函数,是 RL 中既关键又依赖人类专家经验的环节。

## 在本 wiki 中的出现

- [[2024-eureka-reward-design-via-coding-llms]]:Eureka 用编码 LLM(GPT-4)零样本生成可执行奖励函数代码,结合进化搜索与奖励反思迭代改进,在 29 个 RL 环境上达到人类专家级奖励设计并首次让模拟 Shadow Hand 学会转笔。
- [[2025-multiscale-contextual-bandits-long-term]]:提出 MultiScale Policy Learning 框架与 MSBL 算法,用分层 off-policy contextual bandit 在多个时间尺度上协调短期反馈与长期目标,让低尺度数据作为高尺度稀疏数据的 PAC-Bayes 先验。
- [[2025-sotopia-rl-reward-design-social-intelligence]]:SOTOPIA-RL 把 episode 级反馈细化为 utterance 级、多维度 reward,用单轮在线 GRPO 训练社交 agent,在 SOTOPIA 上取得 SOTA goal completion(SOTOPIA-hard 7.17、SOTOPIA-all 8.31)。

## 相关

- [[reinforcement-learning]]
- [[reward-shaping]]
- [[code-generation]]
- [[evolutionary-search]]
