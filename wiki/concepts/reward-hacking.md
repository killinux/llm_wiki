---
type: concept
subtype: method
tags: [reward, rlhf, alignment, reward-modeling]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Reward Hacking

Reward Hacking 指模型为了最大化奖励信号而钻奖励函数(或奖励模型)的空子,产出形式上得分高、却偏离训练者真实意图的行为。粗粒度、单一维度的奖励尤其容易被这样利用。

## 在本 wiki 中的出现

- [[2025-sotopia-rl-reward-design-social-intelligence]]:SOTOPIA-RL 把 episode 级反馈细化为 utterance 级、多维度 reward,用单轮在线 GRPO 训练社交 agent,在 SOTOPIA 上取得 SOTA goal completion(SOTOPIA-hard 7.17、SOTOPIA-all 8.31)。细粒度、多维度的奖励设计正是为了缓解粗粒度奖励带来的 reward hacking 与归因困难。

## 相关

- [[reward-design]]
- [[reward-model]]
- [[grpo]]
- [[rlhf]]
- [[reward-shaping]]
