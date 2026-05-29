---
type: entity
subtype: dataset
tags: [recommendation, debiasing, benchmark, dataset]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# Coat

Coat 是推荐系统去偏研究中常用的基准数据集,记录用户对外套(coat)商品的评分,同时包含有偏的自选(self-selected)评分与无偏的随机曝光(random exposure)评分,因而被广泛用于评估反事实/去混杂推荐方法。

## 在本 wiki 中的出现

- [[2023-idcf-debiasing-recommendation]]:作为评测数据集之一。该论文提出 iDCF,借助代理变量(用户特征)与近端因果推断,在存在未观测混杂变量时为推荐反事实反馈提供可识别性保证;实验在 Coat、Yahoo!R3、KuaiRand 上进行,结果优于现有去混杂方法。
- [[2023-conservative-doubly-robust]]:作为去偏推荐方法的评测数据集之一。该论文提出 CDR,通过审查插补值的均值与方差过滤 Doubly Robust 去偏中的"毒性插补",降低偏差方差并提升性能。
- [[2024-easyrl4rec]]:面向 RL-based 推荐系统的易用代码库,基于五个公开数据集构建轻量 RL 环境,提供四个核心模块与面向长期收益的统一训练/评测流程,并给出经典与近期 RL 方法的对照实验。
- [[2024-roler-reward-shaping-offline-rl-recsys]]:ROLeR 用非参数(kNN/聚类)reward shaping 与解耦的不确定性惩罚修正 model-based offline RL 推荐中 world model 的 reward 估计误差,在 KuaiRand/KuaiRec/Coat/Yahoo 四个 benchmark 上达到 SOTA。

## 相关

- [[2022-kuairand]]
- [[yahoo-r3]]
- [[doubly-robust]]
- [[proximal-causal-inference]]
- [[debiasing-recommendation]]
- [[counterfactual-feedback]]
- [[offline-rl]]
- [[recommender-system]]
