---
type: entity
subtype: dataset
tags: [recommendation, music, dataset, offline-rl]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# LFM-1b

LFM-1b 是一个大规模音乐收听记录数据集,包含来自 Last.fm 用户的约十亿条收听事件,常用于推荐系统等研究。

## 在本 wiki 中的出现

- 在 [[2023-dorl-matthew-effect-offline-rl-recommendation]] 中,LFM-1b 作为评估推荐场景的数据集之一被使用。该论文提出 DORL,在 model-based offline RL 的悲观惩罚之上加入熵惩罚,以缓解推荐中的马太效应(Matthew effect),提升交互式推荐的用户长期满意度。
- [[2024-recmamba-lifelong-sequential-recommendation]]:提出 RecMamba,用带选择机制的状态空间模型 Mamba 替换 Transformer 层来建模长度 >=2k 的终身用户行为序列;在 KuaiRand 与 LFM-1b 上达到与 SASRec 相当的推荐效果,同时训练时长降低约 73%、推理时间约 61%、显存约 80%,并在 5k 长度下避免 SASRec 的 OOM。

## 相关

- [[matthew-effect]]
- [[offline-reinforcement-learning]]
- [[model-based-offline-rl]]
- [[interactive-recommendation]]
- [[dorl]]
- [[recmamba]]
- [[mamba]]
- [[sasrec]]
- [[kuairand]]
- [[sequential-recommendation|lifelong-sequential-recommendation]]
