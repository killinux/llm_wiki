---
type: concept
subtype: method
tags: [causal-inference, recommendation, proxy-variable, proximal-causal-inference, latent-confounder]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# 可识别性

可识别性(identifiability)指在给定数据生成假设下,目标量(如因果效应、潜在结果分布或隐变量)能由可观测数据唯一确定的性质。

## 在本 wiki 中的出现

- [[2023-idcf-debiasing-recommendation]]:可识别性是 iDCF 方法的核心动机与理论保证。文中指出已有的 [[deconfounder|Deconfounder]] 存在固有的非可识别(non-identification)问题——即便替代混杂变量可唯一确定,反事实反馈分布 $p(r^a_{ui})$ 仍可能落在一个区间内取不同值,导致预测不一致。iDCF 借助代理变量(proxy variable,即用户特征)与 [[proximal-causal-inference|近端因果推断]],在存在未观测混杂变量(unobserved confounder)时为推荐场景的反事实反馈提供可识别性的理论保证(Theorem 4.3),并用 [[ivae|iVAE]] 实现潜在混杂变量的可识别学习。该方法在 Coat、Yahoo!R3、KuaiRand 上一致优于现有去混杂方法。
- [[2024-fairness-recommendation-missing-labels]]:证明大规模推荐系统在缺失标签下 REO 公平性指标不可识别,提出用小比例 random traffic 无偏估计公平性指标并给出误差上界,首次公开 TikTok 公平性数据集。

## 相关

- [[proximal-causal-inference]]
- [[deconfounder]]
- [[ivae]]
- [[causal-inference]]
- [[debiasing]]
- [[potential-outcome-framework]]
- [[multi-cause-confounders]]
