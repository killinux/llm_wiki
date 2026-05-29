---
type: source
subtype: paper
tags: [multi-scenario-recommendation, multi-scenario-matching, mixture-of-experts, mmoe, two-tower, knowledge-distillation, recommender-system, matching]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2601.02368
raw: raw/2601.02368.pdf
authors: [Ruibing Wang, Shuhan Guo, Haotong Du, Quanming Yao]
year: 2026
---

# DSMOE:面向多场景推荐召回阶段的蒸馏式场景自适应 MoE

一句话:DSMOE 把擅长排序的 [[mmoe]] 迁移到多场景推荐的**召回(matching)阶段**,用 Scenario-Adaptive Projection(SAP)动态参数模块缓解头部场景对专家的统治,并用一个吃 user-item 联合特征的 teacher 通过 [[knowledge-distillation]] 指导 [[two-tower]] student,从而在保持检索效率的同时获得交互建模能力,尤其改善长尾、数据稀疏场景的召回质量。

## 问题

[[multi-scenario-recommendation]] 中,单个 app 常包含多个模块/类目(场景),用户跨场景有稳定偏好,但每个场景又有独特的布局与交互风格。[[mmoe]] 及其变体(如 [[ple]]、M3OE)在多场景**排序**上表现优异,但迁移到**召回**阶段面临两难:

- **结构瓶颈**:十亿级检索要求低延迟,工业系统普遍采用 [[two-tower]] 架构 + [[approximate-nearest-neighbor-search]](ANN)索引,user/item 独立编码,导致 MMOE 专家在没有 user-item 早期交互的情况下"盲目"优化,无法捕捉复杂高阶特征关系。
- **分布瓶颈**:共享专家容易被数据丰富的头部场景的梯度统治(gradient domination),压制长尾场景建模;而给每个场景配专属专家又会导致参数爆炸。

核心挑战是:如何在召回框架里调和"排序架构的复杂交互建模"与"召回的检索效率"。

## 方法

DSMOE 在模型和优化两个层面改进 MMOE(见原文 Fig.1):

- **Scenario-Adaptive Projection Modulation(SAP)**:轻量动态参数模块。基础线性层 y=Wx 被改写为 `Layer_SAP = W_shared · x + (ΔW(e_s)) · x`,其中场景相关的低秩修正 `ΔW(e_s) = Σ_{r=1..R} (b_s)_r · (A_{:,r} B_{r,:})`,A、B 为可训练低秩分解矩阵(秩 R ≪ d_in,d_out),b_s 由场景特征经线性层生成。每个场景因此分到一小组动态参数,缓解场景数据不均衡。论文指出动态参数技术此前主要用于排序阶段,因效率原因少见于召回。
- **SAP-based MMOE**:每个 expert 实现为 `DSBN(PReLU(SAP(x|e_s)))`,其中 DSBN 是场景专属的 batch normalization(参数 γ_d,β_d),门控网络按场景特征 softmax 得到专家权重 α_k,加权聚合得到 z_mix,再经一个 SAP_forward 前向网络做最终维度变换。
- **跨架构 [[knowledge-distillation]]**:把多场景召回建模为带随机负采样的二分类。teacher 吃**拼接的 user-item 联合特征**显式建模高阶交互,student 是高效的 two-tower MMOE,匹配分用内积 `ŷ=σ(⟨ê_u, ê_v⟩)`。总损失 `L_total = L_task + λ·L_KD(p_t, p_s)`,其中 `L_task` 为 BCE,`L_KD` 为 teacher 与 student 概率间的 KL 散度。关键是 **teacher 离线训练后即丢弃,线上只部署轻量 student**,保持 two-tower 范式的高效率。

## 结果

- **数据集**:[[kuairand]](KuaiRand-Pure,来自快手短视频,4 个场景按属性 tab 划分,K1 占 84%)与 Alimama(阿里妈妈广告,按 city level 划分 4 个场景,A1 占 45%);划分沿用 PERSCEN 设置。
- **指标**:Recall@K(K 取约候选集 1%):KuaiRand-Pure 用 K∈{50,100},Alimama 用 K∈{500,1000}。
- **baseline**:ICAN、ADIN、SASS、M5、PERSCEN。**DSMOE 在两个数据集所有场景均最优**,数据稀疏场景提升尤其显著。例:KuaiRand-Pure 最稀疏的 K4(3%)场景,DSMOE R@50=21.87% / R@100=32.60%,优于次优的 PERSCEN(R@50=21.39% / R@100=31.68%)和 ADIN(R@50=19.12%);Alimama 最稀疏 A4(10%)DSMOE R@500=12.73% / R@1000=17.62%。
- **效率(Table 3)**:DSMOE 参数量与 GFLOPs 最低。KuaiRand-Pure 上参数 2.11 MB、GFLOPs 6.21,训练 7174s;相比 PERSCEN(4.30 MB / 8.52 GFLOPs / 13431s)显著更轻量,且性能更好。
- **消融(Table 4)**:去掉 SAP、去掉蒸馏、去掉 DSBN 均带来明显下降,三者缺一不可;w/o SAP 在数据稀疏场景退化最大。
- **超参**:专家数 K=3、SAP 秩 R=4 为最优(过大 K 因过拟合/冗余而饱和或下降)。结果在 NVIDIA RTX 3090Ti 上 5 次独立运行平均。
- **case study**:SAP 生成的场景向量在头部与最稀疏场景间余弦相似度低(0.046),说明能为长尾生成专门投影;专家权重显示明确分工——一个专家专注主流量场景,一个专注小场景,第三个相对均衡。

## 在本 wiki 中的位置

本文是 [[recommender-systems|recommender-system]] 召回方向的工作,把 [[mixture-of-experts]] / [[mmoe]] 从排序迁移到 [[two-tower]] 召回,与 [[multi-scenario-recommendation]]、[[multi-scenario-matching]]、[[multi-scenario-matching]] 主题直接相关;可与多场景排序工作 [[ple]]、[[mmoe]] 及召回基础设施 [[dssm]]、[[approximate-nearest-neighbor-search]]、[[embedding-based-retrieval]] 对照。其用 teacher→student 的 [[knowledge-distillation]] 把交互信息注入双塔,与同样在召回阶段引入新机制的 [[t2diff]]、数据集 [[recflow]] 形成方法对照。低秩动态参数思路与 [[lora]] 相通。
