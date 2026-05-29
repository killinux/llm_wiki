---
type: concept
subtype: method
tags: [recommendation, negative-feedback, model-editing]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Recommendation with Negative Feedback

指在推荐系统中处理与修正"不当推荐"(负反馈)的方法,即在不重新训练、不访问原始训练数据的前提下,纠正已部署模型已知的错误推荐行为。

## 在本 wiki 中的出现

- [[2024-recommendation-editing]]:提出 recommendation editing 新任务:不重训练、不访问训练数据地修正已部署推荐系统的已知不当推荐,给出形式化定义、ES/EC/EP/EA 评估指标、E-BPR 损失与综合 benchmark。
- [[2025-fine-grained-skip-micro-video-recommendation]]:将 micro-video 中的 skip 行为细分为 highly positive、less positive、negative 三类,用双层图与分层 BPR ranking loss 建模,在 MVA 与 KuaiRand-Pure 的八项指标上超越 FRAME/LightGT/BM3。

## 相关

- [[model-editing]]
- [[recommender-systems|recommendation-system]]
- [[bpr-loss]]
