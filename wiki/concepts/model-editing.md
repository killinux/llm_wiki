---
type: concept
subtype: method
tags: [model-editing, knowledge-editing, post-deployment-correction]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Model Editing

Model Editing(模型编辑)指在不重新完整训练模型的前提下,对已部署/已训练模型的特定行为或知识进行精准、局部的修正,同时尽量不破坏其它无关能力。

## 在本 wiki 中的出现

- [[2024-recommendation-editing]]:提出 recommendation editing 新任务:不重训练、不访问训练数据地修正已部署推荐系统的已知不当推荐,给出形式化定义、ES/EC/EP/EA 评估指标、E-BPR 损失与综合 benchmark。
- [[2024-mitigating-false-refusal-single-vector-ablation]]:提出 training-free、零推理开销的方法,通过正交化并消融单个 false refusal vector 来缓解 LLM 的过度拒绝,同时保持安全性与通用能力。
- [[2026-memory-in-the-age-of-ai-agents-survey]]:一篇关于智能体记忆的综述,提出 forms-functions-dynamics 三维统一分类法,整合碎片化的 agent memory 研究并汇总相关 benchmark 与开源框架;其中参数化记忆的更新与模型编辑密切相关。

## 相关

- [[knowledge-editing]]
- [[recommender-systems|recommendation-system]]
- [[catastrophic-forgetting]]
- [[activation-steering]]
- [[false-refusal]]
