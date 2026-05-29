---
type: entity
subtype: dataset
tags: [recommendation, debiasing, benchmark, dataset]
created: 2026-05-29
updated: 2026-05-29
sources: 9
---

# Coat

Coat 是推荐系统去偏研究中常用的基准数据集,记录用户对外套(coat)商品的评分,同时包含有偏的自选(self-selected)评分与无偏的随机曝光(random exposure)评分,因而被广泛用于评估反事实/去混杂推荐方法。

## 在本 wiki 中的出现

- [[2023-idcf-debiasing-recommendation]]:作为评测数据集之一。该论文提出 iDCF,借助代理变量(用户特征)与近端因果推断,在存在未观测混杂变量时为推荐反事实反馈提供可识别性保证;实验在 Coat、Yahoo!R3、KuaiRand 上进行,结果优于现有去混杂方法。
- [[2023-conservative-doubly-robust]]:作为去偏推荐方法的评测数据集之一。该论文提出 CDR,通过审查插补值的均值与方差过滤 Doubly Robust 去偏中的"毒性插补",降低偏差方差并提升性能。
- [[2024-easyrl4rec]]:面向 RL-based 推荐系统的易用代码库,基于五个公开数据集构建轻量 RL 环境,提供四个核心模块与面向长期收益的统一训练/评测流程,并给出经典与近期 RL 方法的对照实验。
- [[2024-roler-reward-shaping-offline-rl-recsys]]:ROLeR 用非参数(kNN/聚类)reward shaping 与解耦的不确定性惩罚修正 model-based offline RL 推荐中 world model 的 reward 估计误差,在 KuaiRand/KuaiRec/Coat/Yahoo 四个 benchmark 上达到 SOTA。
- [[2024-mitigating-dual-latent-confounding-biases]]:IViDR 联合工具变量(IV)与 identifiable VAE,同时缓解推荐系统中 item-feedback 与 exposure-feedback 两类潜在混淆偏差。
- [[2025-policy-guided-causal-state-representation]]:PGCR:面向离线 RL 推荐的两阶段因果状态表示框架,用策略引导的因果特征选择隔离因果相关分量,再用 encoder 学习紧凑状态表示。
- [[2025-causality-constraint-debiasing-recommender]]:LCDR 用 identifiable VAE (iVAE) 作为因果约束去对齐标准 VAE 的潜在表征,即使 proxy variable 低质/有噪声也能恢复 latent confounder,从而缓解推荐系统中的潜在混杂偏差。
- [[2025-reward-balancing-revisited]]:提出 R3S,用 diffusion world model 显式建模 reward 不确定性并配合带衰减的多样性惩罚,在 offline RL 推荐中同时平衡 world model 偏差与策略多样性,在 Coat/Yahoo/KuaiRand 上超越 DORL、ROLeR 等 11 个 baseline。

## 相关

- [[2022-kuairand]]
- [[yahoo-r3]]
- [[doubly-robust]]
- [[proximal-causal-inference]]
- [[debiasing-recommendation]]
- [[counterfactual-feedback]]
- [[offline-rl]]
- [[recommender-systems|recommender-system]]
