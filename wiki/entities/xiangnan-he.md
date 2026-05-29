---
type: entity
subtype: person
tags: [researcher, recommender-systems, debiasing]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# Xiangnan He

Xiangnan He 是一位专注于推荐系统、信息检索与去偏(debiasing)等方向的研究者。

## 在本 wiki 中的出现

- [[2022-kuairand]]:作为该无偏序列推荐数据集相关工作的研究者参与其中。KuaiRand 由快手发布,通过在推荐流中随机插入视频收集百万级无偏交互(含 12 种反馈信号、完整用户/物品 ID 与特征),支持去偏与离线评估研究,与其在推荐去偏方向的研究关注点一致。
- [[2023-microlens-micro-video-recommendation-dataset]]:MicroLens:一个含 10 亿交互、3400 万用户、100 万微视频并提供原始视频/音频/图像/文本内容的内容驱动微视频推荐数据集与基准。
- [[2024-llm-learnable-planners-long-term-recommendation]]:提出 BiLLP 双层可学习 LLM 规划框架(Planner/Reflector 宏观 + Actor/Critic 微观),在稀疏推荐数据上以 LLM 规划能力做长期推荐,Len 与累积奖励超越从零训练的 RL 与现有 LLM agent 基线。
- [[2024-agentic-feedback-loop-recommendation]]:提出 AFL(Agentic Feedback Loop),让 recommendation agent 与 user agent 通过基于 memory 的多轮文本反馈回路相互协作,同时提升推荐(平均 +11.52%)与用户模拟(平均 +21.12%),且不放大流行度/位置偏差。
- [[2026-trirec-tri-party-agent-recommendation]]:TriRec 是首个用户—物品—平台 tri-party LLM-agent 推荐框架,让物品 agent 主动个性化自我推销,再由平台做曝光感知的多目标重排,在精度、公平与物品效用上同时提升。

## 相关

- [[kuaishou]]
- [[recommender-systems]]
- [[debiasing]]
- [[sequential-recommendation]]
- [[offline-evaluation]]
- [[micro-video-recommendation]]
- [[llm-for-recommendation]]
- [[recommendation-agent]]
- [[user-simulation]]
- [[trirec]]
