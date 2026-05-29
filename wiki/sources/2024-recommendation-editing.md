---
type: source
subtype: paper
tags: [recommender-system, model-editing, collaborative-filtering, benchmark, negative-feedback]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2406.04553
raw: raw/2406.04553.pdf
authors: [Chengyu Lai, Sheng Zhou, Zhimeng Jiang, Qiaoyu Tan, Yuanchen Bei, Jiawei Chen, Ningyu Zhang, Jiajun Bu]
year: 2024
---

# Better Late Than Never: Formulating and Benchmarking Recommendation Editing

提出"recommendation editing"(推荐编辑)这一新任务:在**不重训练、不访问训练数据**的前提下,直接修正已部署 [[recommender-system]] 给出的已知且不当(unsuitable)的推荐行为,并给出形式化定义、评估指标、E-BPR 损失与综合 benchmark。

## 问题

在线推荐系统因模型容量有限、数据质量差或用户兴趣漂移,不可避免地会产生不当推荐(如向匿名未成年用户推荐成人内容、违法/违规内容)。这类错误虽占比很小但负面影响严重,需要被快速修正。现实约束有三:(1) 需要快速修正以减轻负面影响;(2) 计算高效,可应对频繁错误;(3) 最好无需访问训练数据(隐私考虑)。

现有方法都不能直接满足这些需求:[[fine-tuning]] / 增量推荐(online/incremental recommendation)关注的是对全体用户适配新反馈而非严格修正个别错误;[[recommendation-with-negative-feedback]](负反馈推荐)依赖从头训练、需要全部历史数据;recommendation unlearning(推荐遗忘)目标是消除特定训练数据影响,与修正错误推荐目标不同;NLP/CV 中的 [[model-editing]] 面向 instance-wise 分类任务,忽略了推荐数据的 non-iid 特性与排序(ranking)本质。

## 方法

作者把推荐编辑形式化。给定已训练模型 f 与推荐结果,定义需编辑的 user-item 对集合 E,并区分三类 pair:
- **Explicit Editing Pairs** E^B:少量可被显式获取(内测、用户投诉、监管反馈)且需严格编辑的对。
- **Implicit Editing Pairs** E^I:与显式对相似、应被编辑但未被访问到的对。
- **Unnecessary Editing Pair** E~:与编辑无关、应保持不变的对。满足 E^B+E^I=E,E^B+E^I+E~=R。

对应三个目标:**Strict Rectification**(严格修正显式错误)、**Collaborative Rectification**(协同修正相似但未观测到的错误)、**Concentrated Rectification**(仅在必要时编辑,保留大多数正确推荐)。

**三个评估指标**:
- **Editing Accuracy (EA)**:显式编辑对被成功编辑的比例(rank 超出 top-k)。
- **Editing Collaboration (EC)**:隐式编辑对被成功编辑的比例。
- **Editing Prudence (EP)**:不必要编辑对未被误编辑的比例。
- 并提出 **Editing Score (ES)**:EC 与 EP 的调和平均,综合衡量"错误编辑"表现。

**E-BPR (Editing BPR) 损失**:针对编辑对 (u_e, i_e),把 i_e 当作负样本、其他 top-k 候选 R_{u_e} 当作正样本,通过提升其他物品的排序来把 i_e 压下去,从而 model-agnostic 地直接作用于 user/item embedding(MF、graph 模型皆可)。还提出 **EFT (Editing Fine-Tuning)**:通过一个生成 embedding 的模型修改最终 user/item embedding,无需了解模型架构和训练细节;以及 **BiEGNN**(为 user/item 训练不同编辑模块的 [[graph-neural-network]] 编辑器)。

## 结果

在三个数据集上评测:**Epinions**(评分 1-5,>3 为正反馈)、**KuaiRand**([[kuaishou]] 视频,dislike 按钮为负反馈)、**QB-video**(QQ 浏览器,曝光未点击为负反馈),均用 10-core 预处理。三个 backbone:**MF**([[matrix-factorization]])、**LightGCN**、**XSimGCL**。对比方法涵盖 finetuning(FT、EFT)、正则化(LWF、L2、SRIU)、replay(RSR、SPMF)、optimization(SML)、负反馈 CF(SiReN、SiGRec)、model editing(EGNN、BiEGNN)。所有方法训练/测试 8:2 划分,微调最多 20 轮,重复 10 次取平均。

主要发现(Table 2,数值为百分比):
- **EFT 在 graph backbone 上 ES 最优**:如 Epinions+XSimGCL,EFT ES=70.35;KuaiRand+LightGCN,EFT ES=68.90。EFT 在所有设置下 EA 基本保持 1.00(100%)。
- **图结构对 model editing 非必需**:EFT(不用图可见性)在 LightGCN/XSimGCL 上优于依赖图的 Fine-Tune。
- **正则化方法提升 EP**(更谨慎),但牺牲 EC 与 EA(L2 在 QB-video+XSimGCL 仅 EA=0.91);**replay 方法提升 EC** 但牺牲 EP(SPMF 在 MF 上 ES 突出,如 Epinions+MF ES=84.21、QB-video+MF SPMF ES=80.73)。
- **现有推荐方法(SML、SiReN、SiGRec)与 model editing 方法均不适配**,显著落后于基础 fine-tuning。
- **效率(Fig 2)**:EFT 在 graph 模型上编辑时间最低;正则化与 replay 方法更慢。
- **负反馈强度影响效果**:KuaiRand(dislike,信号更强烈/有针对性)上各方法整体弱于另外两个数据集。
- **编辑目标(RQ4)**:BCE 损失给 MF 带来强 EP 但 EC 接近零;BPR 损失大幅提升 EC、略降 EP;图模型中 BPR 因引入(有时不准的)协同信息使 EP 更差。

代码开源:https://github.com/cycl2018/Recommendation-Editing

## 在本 wiki 中的位置

本文把 NLP/CV 中的 [[model-editing]] 思想迁移到 [[recommender-system]],与 [[recommendation-with-negative-feedback]] 关系密切但目标不同(快速无重训地修正已知错误,而非建模负偏好)。它提出的 E-BPR 是对经典 BPR 排序损失在编辑场景下的改造,backbone 涵盖 [[matrix-factorization]] 与图协同过滤([[collaborative-filtering]])。作者来自 [[zhejiang-university]] 等机构,[[jiawei-chen]]、[[ningyu-zhang]] 参与。
