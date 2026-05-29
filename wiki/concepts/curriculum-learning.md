---
type: concept
subtype: method
tags: [curriculum-learning, training-strategy, recommendation, generative-modeling]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Curriculum Learning

Curriculum Learning 是一种训练策略,通过让模型先学习"简单"样本、再逐步过渡到"困难"样本(模仿人类由易到难的学习过程),以提升训练稳定性与最终效果。

## 在本 wiki 中的出现

- [[2024-generative-regression-watch-time-prediction]]:提出 Generative Regression (GR),把短视频 watch time 预测从 ordinal regression 重构为 token 序列生成任务,配合 dynamic quantile 词表与 CLEM(curriculum learning + embedding mixup),在 KuaiRec/CIKM16/工业数据集及 Kuaishou 线上 A/B 上超过 SOTA,并可迁移到 LTV 预测。
- [[2026-yerkes-dodson-curve-ai-agents]]:在网格世界生存竞技场中系统改变环境压力,首次实证发现 LLM 多智能体系统的合作行为遵循 Yerkes-Dodson 倒 U 形曲线——中等压力(upkeep=5)合作交易峰值达 29 次,过低或过高压力都抑制社会行为,且性选择压力可在不致死的前提下消除攻击。

## 相关

- [[generative-regression]]
- [[watch-time-prediction]]
- [[embedding-mixup]]
- [[ordinal-regression]]
