---
type: source
subtype: paper
tags:
  - recommender-system
  - multi-scenario-recommendation
  - ctr-prediction
  - dynamic-weight
  - multi-task-learning
created: 2026-05-29
updated: 2026-05-29
arxiv: "2309.02061"
raw: raw/2309.02061.pdf
authors:
  - Jingtong Gao
  - Bo Chen
  - Menghui Zhu
  - Xiangyu Zhao
  - Xiaopeng Li
  - Yuhao Wang
  - Yichao Wang
  - Huifeng Guo
  - Ruiming Tang
year: 2023
---

HierRec 是一个面向多场景推荐(multi-scenario recommendation)的 Scenario-Aware Hierarchical Dynamic Network,通过分层结构同时建模显式(explicit)与隐式(implicit)场景,在 CTR 预测任务上显著超越现有基线。

## 问题

CTR 预测是推荐与广告系统的基础技术。多场景推荐(也称 multi-domain recommendation)通过聚合相似场景的样本来缓解数据稀疏、提升预测精度。现有多场景模型可分为两类:Tower-based 模型(如 [[star]])和 Dynamic Weight(DW)模型(如 AdaSparse)。

但现有模型只考虑基于人工先验规则(如广告位、频道)的**粗粒度显式场景**识别,这是有偏且次优的,并且忽略了场景内部的数据差异。作者以 [[kuairand]] 数据集为例指出:同一显式场景内,样本数量与 CTR 在不同特征(尤其是特征组合)下差异显著。这些基于特征的隐式模式(称为 implicit scenarios)若能被利用,可更细粒度地刻画相关性。因此需要解决两大挑战:1) 如何在多场景推荐中结合显式建模与隐式建模;2) 如何自适应感知隐式模式并进行细粒度建模。

## 方法

HierRec 是一个分层结构,包含一个显式场景导向层与多个并行的隐式场景导向层,基于 dynamic weight(重参数化)技术自适应生成参数。

- **Scenario-Oriented Module**:基本模块由若干线性层组成,其权重 W_l 与偏置 b_l 由给定的 scenario condition SC 通过 Reshape 自适应生成(公式 1-2)。参照 bottleneck 结构,层数 L 设为 2(瓶颈层神经元少,第二层多)。
- **Explicit Scenario-Aware Module**:先用 embedding layer 把所有特征(scenario feature + common features)嵌入为稠密向量;common feature embeddings 拼接后过共享 FC 层得到全局表示 O^global;场景 embedding e_s 经 FC 得到显式场景条件 SC_explicit,用于实例化显式场景导向层,输出 O^explicit。
- **Implicit Scenario-Aware Module**:为自适应识别有益的隐式模式,设计了 scenario-aware multi-head attention。场景 embedding e_s 经 FC、Reshape、Softmax 归一化得到多组权重 weight_norm(公式 6),其每个元素反映对应 common feature 在该隐式场景下的重要性;weight_norm 与 common feature embeddings 逐元素相乘得到隐式场景表示 IE(公式 7),再经共享 FC 得到 G 个隐式场景条件 SC_implicit,实例化 G 个并行的隐式场景导向层。
- **Output Layer**:G 个隐式场景导向层的输出拼接后过 FC + Sigmoid 输出 CTR(公式 9),用 Binary Cross Entropy 损失训练(公式 10)。

## 结果

在两个公开数据集 [[ali-ccp]](3 场景,23 特征)与 [[kuairand]](5 场景,37 特征)上评测,指标为 AUC 与 Logloss,并用 RelaImpr 衡量相对提升。基线包括 Shared Bottom、[[mmoe]]、[[ple]]、[[star]]、AdaSparse。

- 整体性能(Table 2):HierRec 在所有场景级与整体指标上均显著超越基线(t-test p<0.05)。Ali-CCP 整体 AUC 0.6237、Logloss 0.1614,RelaImpr 6.18%;KuaiRand 整体 AUC 0.7847、Logloss 0.5376,RelaImpr 1.14%。单场景上 Ali-CCP sce_2 的 RelaImpr 达 7.84%,KuaiRand sce_5 达 8.10%。
- 消融实验(RQ2,Figure 4):w/o multi-head attention(-MI)、w/o implicit layers(-I)、w/o explicit layers(-E)均导致性能下降,说明显式与隐式建模都重要;显式建模更主导,但隐式建模的提升也不可忽略。
- 推理效率(RQ3,Table 3):在 NVIDIA GeForce RTX 3060 上,对 Ali-CCP 全测试集(43M 样本)推理 572.44 秒,KuaiRand(1.5M)10.29 秒,相比最耗时基线分别仅增加 2.43% 与 0.68%,适合工业部署。
- 工业应用:在主流在线广告平台的 Lead Ads Recommendation(以行业 industry 作为显式场景,80+ common features 作为隐式场景)中部署。离线超越 FiBiNet、DCN、DFFM、MMoE、PLE 等基线。两周在线 A/B 测试(Table 4):eCPM 提升 +10.33%,predicted bias 降低 -6.81%。

## 在本 wiki 中的位置

HierRec 属于 [[recommender-system]] 中的 multi-scenario / multi-domain CTR 建模方向,与多任务模型 [[mmoe]]、[[ple]] 以及多场景模型 [[star]] 同属一脉,但用 dynamic weight 思路同时建模显式与隐式场景。它在 [[ali-ccp]] 与 [[kuairand]] 上评测,后者是本 wiki 已收录的无偏序列推荐数据集。作者来自 [[huawei-noahs-ark-lab]]。本文与 wiki 中以 LLM 为主的 agent/reasoning 主线相对独立,代表传统深度推荐模型(deep CTR)的分支。
