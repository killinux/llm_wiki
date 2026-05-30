---
type: concept
subtype: method
tags: [self-supervised, pretraining, representation-learning, contrastive]
created: 2026-05-30
updated: 2026-05-30
sources: 8
---

# 自监督学习 (Self-Supervised Learning, SSL)

自监督学习从**无标注数据**中构造**代理任务 (pretext task)** 来学习表示——监督信号由数据自身生成,无需人工标注。
它是预训练大模型的引擎:用海量无标签语料/图像学到通用 [[representation-learning|表示]],再微调到下游任务。

## 主要范式
- **生成式 / 预测式**:掩码重建([[bert]] 掩词、MAE 掩图)、自回归下一 token 预测([[gpt-3]]);[[bart]] 去噪自编码。
- **对比式 (contrastive)**:拉近正样本对、推远负样本(SimCLR、MoCo);[[clip]] 用图文对做跨模态对比对齐。
- **自蒸馏 / 非对比**:BYOL、DINO/[[dinov3]](无需负样本的视觉自监督)。

## 与相邻概念
是 [[representation-learning|表示学习]]的主流实现路径,产出可迁移 [[embedding|嵌入]];在推荐中用于序列/图的自监督预训练(对比学习增强鲁棒性,如 [[2024-robust-recommendation-decision-boundary-gcl]]);
LLM 的"预训练-微调-对齐"范式中,**预训练**阶段即大规模自监督。

## 相关页
[[representation-learning]]、[[contrastive-learning]]、[[pretraining]]、[[clip]]、[[bert]]、[[embedding]]
