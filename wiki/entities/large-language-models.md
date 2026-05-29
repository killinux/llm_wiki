---
type: entity
subtype: model
tags: [llm, language-model, reasoning, search]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Large Language Models

大语言模型(Large Language Models, LLMs)是在海量文本上训练、具备强大语言理解与生成能力的神经网络模型,可通过 prompting 执行推理、规划与搜索等复杂任务。

## 在本 wiki 中的出现

- [[2024-reflection-on-search-trees]]:RoT 让 strong LLM 反思 weak LLM 的历史树搜索经验、对关键状态总结出任务级 guideline 注入后续 prompt,显著提升 BFS/MCTS 等树搜索 prompting 在 Blocksworld、GSM8k、议价任务上的准确率与搜索效率,且任务越难收益越大。
- [[2024-scenario-wise-rec]]:首个面向多场景推荐(MSR)的开源 benchmark,整合 6 个公开数据集、12 个基线模型与统一的数据处理/训练/评测流水线,并在工业广告数据集上验证。
- [[2024-generative-regression-watch-time-prediction]]:提出 Generative Regression (GR),把短视频 watch time 预测从 ordinal regression 重构为 token 序列生成任务,配合 dynamic quantile 词表与 CLEM(curriculum learning + embedding mixup),在 KuaiRec/CIKM16/工业数据集及 Kuaishou 线上 A/B 上超过 SOTA,并可迁移到 LTV 预测。

## 相关

- [[tree-search]]
- [[prompting]]
- [[reasoning]]
- [[mcts]]
