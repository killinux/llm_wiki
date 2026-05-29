---
type: concept
subtype: method
tags: [recommendation, feature-interaction, factorization, ctr-prediction]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# Factorization Machines

Factorization Machines (FM) 是一类通用的监督学习模型,通过将特征两两交互的权重分解为隐向量(latent vector)的内积来高效建模高维稀疏特征之间的二阶交互,从而在稀疏数据下也能稳定估计交互参数。

## 在本 wiki 中的出现

- [[2023-data-heterogeneity-recommendation]]:该工作以 NFM(Neural Factorization Machine,FM 的神经网络扩展)作为推荐模型的骨干(backbone)。其提出的双层聚类方法 BHE 显式挖掘推荐数据中的预测机制异质性与协变量分布异质性,用于多子模型预测与去偏。在 Yelp 与 MovieLens-1M 上,基于 NFM 骨干的 NDCG@20 从 14.01 提升到 22.57。在此 FM/NFM 作为被增强与去偏的基础预测器。
- [[2024-feature-level-bias-ctr]]:自上而下分析揭示 CTR 模型的 feature-level bias 主要源自线性部分,并提出移除/重建线性权重的极简非侵入式去偏策略。
- [[2024-situation-aware-recommender-enhancer]]:提出 SARE,一个把情境视为交互前置条件的可插拔模块,以个性化方式建模情境对用户-物品偏好的动态影响,可嵌入各类推荐系统 backbone 并显著提升性能。
- [[2024-eeg-svrec-eeg-affective-engagement-dataset]]:首个在真实短视频观看场景下采集 EEG 脑电信号并配以六维情感参与度标注(MAES)与行为日志的推荐数据集,benchmark 显示加入 EEG 特征可提升推荐 AUC。

## 相关

- [[neural-factorization-machine]]:FM 的神经网络扩展,本 wiki 中作为 NFM 骨干被使用。
- [[recommender-system]]:FM 的主要应用领域。
- [[collaborative-filtering]]:FM 可视为对协同过滤的特征化推广。
- [[ctr-prediction]]:FM 常用于点击率预测等稀疏特征交互场景。
- [[feature-interaction]]:FM 的核心建模对象。
- [[matrix-factorization]]:FM 在思想上对矩阵分解的泛化。
