---
type: source
subtype: paper
tags: [recommender-system, multi-scenario-recommendation, ctr, benchmark, mixture-of-experts]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2412.17374
raw: raw/2412.17374.pdf
authors: [Xiaopeng Li, Jingtong Gao, Pengyue Jia, Xiangyu Zhao, Yichao Wang, Wanyu Wang, Yejing Wang, Yuhao Wang, Huifeng Guo, Ruiming Tang]
year: 2024
---

# Scenario-Wise Rec: A Multi-Scenario Recommendation Benchmark

Scenario-Wise Rec 是首个专门面向 Multi-Scenario Recommendation(MSR,多场景推荐)的开源 [[benchmark]],它整合了 6 个公开数据集、12 个 MSR 基线模型,以及统一的数据处理、训练与评测流水线,并在工业广告数据集上验证其鲁棒性。

## 问题

多场景推荐(MSR)旨在用一个统一模型同时服务多个推荐场景(也称 "domain",如不同广告位、商品页或业务单元),通过场景间的知识迁移来缓解小场景数据稀疏并提升整体性能,核心挑战是平衡 shared(共享)与 scenario-specific(场景专属)信息。尽管 STAR、AdaSparse、CausalInt 等模型相继涌现,但该领域存在两大阻碍发展的问题:

1. **缺乏统一的数据处理流程**:不同研究对多场景数据集的处理方式不一致(场景切分策略、特征过滤、数据划分各异),导致难以做公平比较。
2. **大量模型闭源**:出于企业隐私保护,许多 MSR 模型不开源,难以复现,也难以与当前 SOTA 公平对比。

因此亟需一个为 MSR 量身定制、提供标准化数据处理/评测/模型接口的 benchmark。

## 方法

Scenario-Wise Rec 把任务定义为**多场景 CTR(Click-Through Rate)预测**:在标准 CTR 预测 ŷ = F_θ(x) 的基础上,引入场景专属特征 x_s 与场景指示符 s ∈ {1,...,S},模型 ŷ = F_θM(x_g, x_s, s) 需在参数 θM 中同时建模共享与场景专属特征(x_g 为场景无关的通用特征)。

benchmark 提供四个组件:
- **开放数据集接口**:统一的数据加载接口,标准化访问并便于扩展新数据集。
- **通用数据处理范式**:可复现的多场景处理流程(如场景特征声明、公共特征过滤),保证公平与可重复。
- **统一模型接口**:一致的模型搭建与超参数配置,确保复现性与公平对比。
- **可保存日志、配置与教程**:记录训练细节、便于复现,并提供环境搭建到评测的完整教程,支持自定义 MSR 模型与数据集。

数据集涵盖 [[movielens]]、[[kuairand]]、[[ali-ccp]]、Amazon([[amazon-reviews]])、Douban、Mind 共 6 个公开集,以及一个工业广告数据集;场景切分策略分为 context feature(如 Tab/位置)、item feature(如商品类目/平台)、user feature(如用户年龄)三类。复现的 12 个模型包括 Shared Bottom、[[mmoe]]、[[ple]]、STAR、SAR-Net、M2M、AdaSparse、ADL、EPNet & PPNet、HAMUR、M³oE 等,大量模型采用 [[mixture-of-experts]] 结构。框架基于 PyTorch,embedding 维度 d=16,采用 AUC 与 Logloss 两个评测指标,数据按 8:1:1 划分(工业集按天 7:1:1),每个实验跑 10 个随机种子。

## 结果

- 在 6 个公开数据集的统一对比(Table 3)中,**带 expert 结构的模型(如 MMoE、PLE、SAR-Net、M³oE)整体优于直接建模不同场景的模型(如 Shared Bottom、ADL)**,说明 expert 结构更能在深层网络捕捉跨场景动态;能根据场景动态调整关键结构/参数的模型(M2M、AdaSparse、HAMUR)也优于静态 expert 结构。
- 代表性最优数值(AUC↑ / Logloss↓):MovieLens 上 HAMUR 取得 AUC 0.8133;KuaiRand 上 M2M 取得 AUC 0.7821、SAR-Net 取得 Logloss 0.5393;Ali-CCP 上 M2M 取得 AUC 0.6257、Logloss 0.1611;Amazon 上 EPNet 取得 AUC 0.7101、SAR-Net 取得 Logloss 0.4595;Douban 上 SAR-Net 取得 AUC 0.8033、M³oE 取得 AUC 0.8036;Mind 上 STAR 取得 AUC 0.7512、SAR-Net 取得 AUC 0.7593("*" 表示 p<0.05 显著)。
- **效率分析**(Table 4):各模型参数量基本处于同一数量级(主要来自 embedding 层),模型大小与性能差距并不直接相关;数据规模(如 Ali-CCP)显著影响训练时间。
- **场景数量分析**:在 KuaiRand 上把场景数从 3 增到 7,稠密(Scenario-0#)与稀疏(Scenario-2#)场景性能总体均提升;稀疏场景出现先降后升的 "seesaw"(跷跷板)效应,SAR-Net 在稠密/稀疏间平衡能力突出。
- **工业实验**(Table 6,10 个场景、108 个特征、9 天数据):M2M(AUC 0.8392)与 M³oE(AUC 0.8384)表现最佳,印证 meta cell 与多层融合机制在真实大场景数下的优势,与 KuaiRand 上的结论一致。

## 在本 wiki 中的位置

本文是 [[recommender-systems|recommender-system]] 方向下多场景/多域推荐子领域的 [[benchmark]] 工作,核心任务为 [[ctr]] 预测。它系统地整合并复现了 [[mmoe]]、[[ple]] 等基于 [[mixture-of-experts]] 与 [[multi-task-learning]] 的代表性模型,使用 [[movielens]]、[[kuairand]]、[[ali-ccp]]、[[amazon-reviews]] 等本 wiki 中已有的推荐数据集进行 [[evaluation]]。作者通讯作者 [[xiangyu-zhao]] 与合作机构 [[huawei-noahs-ark-lab]] 在本 wiki 推荐系统脉络中多次出现。论文在结论处展望了将 [[large-language-models]] 引入 MSR 的方向,与本 wiki 中 [[llm-for-recommendation]] 等条目形成衔接。在评测基础设施层面,它可与 [[easyrl4rec]] 等推荐评测/工具类条目互为补充。
