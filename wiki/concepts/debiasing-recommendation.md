---
type: concept
subtype: method
tags: [recommendation, debiasing, causal-inference, selection-bias, confounding, evaluation]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# 推荐去偏 (Debiasing Recommendation)

推荐去偏(debiasing recommendation)指在推荐系统中,通过因果推断、倾向得分、潜在混杂建模等手段,纠正观测交互数据中固有的偏差(如 selection bias、exposure bias、popularity bias、潜在混杂偏差),从而更准确地估计用户对未曝光物品的反事实反馈。

## 概述

推荐系统的训练数据是观察性而非实验性的:用户只对被曝光的少量物品产生反馈,且曝光与反馈往往同时受未观测变量(如消费水平、社会经济地位)影响,造成系统性偏差与虚假关联。推荐去偏把"曝光看作 treatment、反馈看作 potential outcome",借助 [[inverse-propensity-scoring|IPS]]、[[doubly-robust|Doubly Robust]]、[[deconfounder|Deconfounder]]、[[proximal-causal-inference|近端因果推断]] 等方法估计去偏后的反馈。这一方向通常以 [[coat]]、[[yahoo-r3]]、[[kuairand]] 等同时含有偏训练集与无偏(随机曝光)测试集的数据集为基准评测;近期工作还质疑了这类评估范式本身的可靠性。

## 在本 wiki 中的出现

- [[2023-idcf-debiasing-recommendation]]:提出 iDCF(identifiable deconfounder),把推荐去偏建模为多 treatment 因果问题,引入代理变量(用户特征)与 [[proximal-causal-inference|近端因果推断]],用 [[ivae|iVAE]] 学习可识别的潜在混杂,解决经典 [[deconfounder|Deconfounder]] 的非可识别问题,为反事实反馈提供 [[identifiability|可识别性]] 理论保证;在 [[coat]]、[[yahoo-r3]]、[[kuairand]] 上优于现有去混杂方法。
- [[2025-causality-constraint-debiasing-recommender]]:提出 LCDR,用 [[ivae|iVAE]] 的可识别表征作为因果约束去对齐标准 VAE 的潜在表征,即使 proxy variable 低质/有噪声也能恢复 latent confounder;直接对标并改进 [[idcf|iDCF]],在三个去偏基准上全面取得 SOTA。
- [[2024-mitigating-dual-latent-confounding-biases]]:提出 IViDR,联合工具变量(IV,2SLS 重构 treatment)与 [[ivae|iVAE]],同时缓解推荐中 item-feedback 与 exposure-feedback 两类潜在混杂偏差(dual latent confounding biases),弥补 iDCF 与 IV4Rec 各自只处理单一混杂的不足。
- [[2023-conservative-doubly-robust]]:提出 CDR,针对 [[doubly-robust|Doubly Robust]] 去偏中插补模型外推产生的"毒性插补",用 Monte Carlo Dropout 估计插补值均值与方差并据此过滤不可靠插补,降低偏差方差;是 model-agnostic 的去偏增强,可即插即用到现有 DR 方法,缓解 [[selection-bias|选择偏差]]。
- [[2025-debias-can-be-unreliable]]:从评估方法学角度指出,用随机曝光数据集以传统方式评估去偏推荐模型并不可靠(小 K 处与全曝光真值相关性弱),提出 URE 方案仅凭随机曝光数据即可无偏估计全曝光数据上的 Recall@K,并据此重评估 IPS、DR、AutoDebias 等去偏基线。

## 相关

- [[debiasing]]
- [[causal-inference]]
- [[recommender-systems|recommender-system]]
- [[inverse-propensity-scoring]]
- [[doubly-robust]]
- [[selection-bias]]
- [[deconfounder]]
- [[proximal-causal-inference]]
- [[identifiability]]
- [[ivae]]
- [[idcf]]
- [[coat]]
- [[yahoo-r3]]
- [[kuairand]]
- [[kuairec]]
