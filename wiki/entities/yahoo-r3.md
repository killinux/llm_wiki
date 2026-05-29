---
type: entity
subtype: dataset
tags: [recommendation, debiasing, missing-not-at-random, benchmark]
created: 2026-05-29
updated: 2026-05-29
sources: 9
---

# Yahoo!R3

Yahoo!R3 是一个常用于推荐系统去偏研究的数据集,其特点是同时包含按用户自然交互收集的有偏(MNAR)训练数据与通过随机曝光收集的无偏(MCAR)测试数据,因而成为评估反事实/无偏推荐方法的标准基准之一。

## 在本 wiki 中的出现

- [[2023-idcf-debiasing-recommendation]]:作为评估 iDCF 的基准数据集之一。该工作借助代理变量(用户特征)与近端因果推断,在存在未观测混杂变量时为推荐反事实反馈提供可识别性保证,并在 Coat、Yahoo!R3、KuaiRand 上优于现有去混杂方法。
- [[2023-conservative-doubly-robust]]:CDR 在推荐去偏的常用基准设置中被评估,Yahoo!R3 属于此类 MNAR/MCAR 去偏基准。CDR 通过审查插补值的均值与方差过滤 Doubly Robust 去偏中的"毒性插补",降低偏差方差并提升性能。
- [[2024-easyrl4rec]]:面向 RL-based 推荐系统的易用代码库,基于五个公开数据集构建轻量 RL 环境,提供四个核心模块与面向长期收益的统一训练/评测流程,并给出经典与近期 RL 方法的对照实验。
- [[2024-roler-reward-shaping-offline-rl-recsys]]:ROLeR 用非参数(kNN/聚类)reward shaping 与解耦的不确定性惩罚修正 model-based offline RL 推荐中 world model 的 reward 估计误差,在 KuaiRand/KuaiRec/Coat/Yahoo 四个 benchmark 上达到 SOTA。
- [[2025-debias-can-be-unreliable]]:揭示用随机曝光数据集传统评估去偏推荐不可靠,提出 URE 方案无偏估计全曝光数据上的 Recall@K。
- [[2024-mitigating-dual-latent-confounding-biases]]:IViDR 联合工具变量(IV)与 identifiable VAE,同时缓解推荐系统中 item-feedback 与 exposure-feedback 两类潜在混淆偏差。
- [[2025-causality-constraint-debiasing-recommender]]:LCDR 用 identifiable VAE (iVAE) 作为因果约束去对齐标准 VAE 的潜在表征,即使 proxy variable 低质/有噪声也能恢复 latent confounder,从而缓解推荐系统中的潜在混杂偏差。
- [[2025-reward-balancing-revisited]]:提出 R3S,用 diffusion world model 显式建模 reward 不确定性并配合带衰减的多样性惩罚,在 offline RL 推荐中同时平衡 world model 偏差与策略多样性,在 Coat/Yahoo/KuaiRand 上超越 DORL、ROLeR 等 11 个 baseline。

## 相关

- [[coat]]
- [[2022-kuairand]]
- [[debiasing-recommendation]]
- [[doubly-robust]]
- [[missing-not-at-random]]
- [[proximal-causal-inference]]
- [[offline-rl]]
- [[rl-based-recommendation]]
