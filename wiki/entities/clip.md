---
type: entity
subtype: model
tags: [multi-modal, vision-language, representation-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# CLIP

CLIP(Contrastive Language-Image Pre-training)是一种通过对比学习在大规模图文对上联合训练图像编码器与文本编码器的视觉-语言模型,可将图像与文本映射到统一的表示空间。

## 在本 wiki 中的出现

- [[2025-drivemlm-autonomous-driving]]:DriveMLM 将 multi-modal LLM 对齐到自动驾驶行为规划模块的离散决策状态,使语言输出可转为车辆控制,在 CARLA Town05 Long 上实现闭环驾驶并取得 DS 76.1、MPI 0.96。
- [[2024-unbounded-generative-infinite-game]]:实现"生成式无限游戏"的角色生活模拟系统,游戏机制、叙事与图像由 LLM 与 text-to-image 模型实时生成,核心创新为带 Block Drop 的 regional IP-Adapter(保证角色与环境一致性)及将多 LLM 协作能力蒸馏进 Gemma-2B 的实时游戏引擎。
- [[2025-segment-level-user-interest-modeling]]:将短视频拆为时间片段,用混合表示+多模态用户-视频编码器+片段兴趣解码器建模随时间演变的片段级兴趣,用于 video-skip 预测与推荐。
- [[2026-ab-agent-recsys-evaluation]]:A/B Agent 是一个多模态 LLM 用户智能体,在带海报的推荐沙盒 UI 中模拟用户的多模态感知、多页交互与疲劳退出,用以替代昂贵的在线 A/B testing 来评估推荐模型并做数据增强;其多模态感知能力与 CLIP 类视觉-语言表征方法相关。

## 相关

- [[multi-modal-llm]]
- [[vision-language-model]]
- [[drivemlm]]
