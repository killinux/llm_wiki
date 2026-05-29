---
type: concept
subtype: method
tags: [lifelong-learning, continual-learning, agent, skill-library]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Lifelong Learning

Lifelong Learning(终身学习)指智能体在持续与环境交互的过程中不断获取、积累并复用新技能,而无需从头训练、且不遗忘已有能力的学习范式。

## 在本 wiki 中的出现

- [[2023-voyager]]:Voyager 是首个由 GPT-4 驱动、在 Minecraft 中实现 Lifelong Learning 的具身智能体。它通过三大组件支撑终身学习:自动课程(automatic curriculum)以最大化探索、可执行代码技能库(skill library)以存储和复用学到的行为、以及结合环境反馈与自我验证的迭代提示机制。技能以代码形式持续累积,使智能体能够在不更新模型参数的前提下不断习得越来越复杂的能力。
- [[2024-recmamba-lifelong-sequential-recommendation]]:提出 RecMamba,用带选择机制的状态空间模型 Mamba 替换 Transformer 层来建模长度 >= 2k 的终身用户行为序列,在 KuaiRand 与 LFM-1b 上达到与 SASRec 相当的推荐效果,同时训练时长降低约 73%、推理时间约 61%、显存约 80%,并在 5k 长度下避免 SASRec 的 OOM。
- [[2025-survey-self-evolving-agents]]:首个系统聚焦自进化智能体的综述,沿 what/when/how/where 四维建立统一框架并梳理评测体系与通往 ASI 的路线图。

## 相关

- [[2023-voyager]]
- [[continual-learning]]
- [[skill-library]]
- [[automatic-curriculum]]
- [[self-verification]]
- [[embodied-agent]]
- [[catastrophic-forgetting]]
- [[state-space-model]]
- [[mamba]]
- [[sequential-recommendation]]
