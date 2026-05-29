---
type: source
subtype: paper
tags: [cvr, multi-task-learning, online-advertising, recommender-system, mmoe, ranking-loss]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2512.13300
raw: raw/2512.13300.pdf
authors: [Qinglin Jia, Zhaocheng Du, Chuhan Wu, Huifeng Guo, Ruiming Tang, Shuting Shi, Muyu Zhang]
year: 2025
---

KAML 是一个面向在线广告 CVR(conversion rate)预测的 [[multi-task-learning]] 框架,针对广告主只提交部分转化行为所导致的"不完整且偏斜的多标签数据(asymmetric multi-label data)",用归因驱动的掩码策略 ADM、层级知识抽取 HKE 与基于排序的标签利用 RLU 三件套挖掘未标注样本的信息,在工业数据集与线上 A/B 测试上显著超越现有 MTL 基线。

## 问题

在线广告中,广告主有多样化的获客目标(activation、re-engagement、registration、payment、retention 等),业界常用 [[multi-task-learning]] 训练统一模型来预测这些目标的 [[ctr]] / CVR(参见 [[recommender-systems|recommender-system]]、[[esmm]] 等转化建模工作)。

但实践中存在一个核心难题:出于隐私和商业机密考虑,**广告主只提交一部分用户转化行为**,导致多任务标签不完整,作者称之为 **asymmetric multi-label data(非对称多标签数据)**。具体表现:

- 对某个 post-click 样本,只有部分转化标签是准确的;label=1 表示观测到并确认了转化,而 label=0 既可能是真的没转化、也可能只是广告主没上传或归因数据不足。
- 若在所有可用数据上训练,部署时服务于只针对特定转化行为的广告主,会因训练/部署的数据分布不匹配(违反 i.i.d. 假设)而引入偏差;若只用与广告主目标严格相关的样本训练,又会丢弃大量有价值信号、加剧数据稀疏。

如何用一个统一模型在这种不完整、偏斜的多标签数据上有效训练,是长期挑战。

## 方法

KAML(Knowledge transfer framework for Asymmetric Multi-Label data)在一个 [[mmoe]] 基座模型(Shared Embedding Layer + Multi-Expert Bottom Layer + Target-specific Towers,可替换为 [[ple]] / HMOE / TAML)之上做三点改进:

- **ADM(Attribution Driven Masking,归因驱动掩码)**:不像 base mask 那样只用与广告主目标严格匹配的样本(`Mask=1[o_i=j]`),而是统计每个广告任务在时间窗 T 内的转化数 c_i,当 `c_i^j ≥ α_j`(阈值超参)时就把该样本纳入对应任务 j 的训练。这样能把"虽非目标但被可靠观测到"的转化信号(如 registration 广告主也上报了 activation)用起来,过滤掉不可靠的标签噪声。
- **HKE(Hierarchical Knowledge Extraction,层级知识抽取)**:ADM 扩大了样本范围,但原始样本与 ADM 扩展样本之间存在特征/标签分布差异。HKE 在 target tower 内部用两个 sub-tower 分别建模 original 与 extended 两类样本的表示,再用指示器 M 区分两类样本后融合 `ŷ_j=σ(MLP(M·h_j^original+(1-M)·h_j^extended))`,缓解分布差异、实现可靠的知识迁移。HKE 依赖 ADM,不能单独使用。
- **RLU(Ranking-based Label Utilization,基于排序的标签利用)**:把训练样本分为三类——Type A(y=1 确认转化)、Type B(y=0 且最终不会转化)、Type C(y=0 但实际可能转化,因上传缺失/延迟反馈/隐私)。Type C 的转化意图明显高于 Type A 之外的负样本,据此引入成对 ranking loss(见 [[learning-to-rank]]),用指示器过滤掉不确定的比较(如 B 与 C 的真假负样本无法区分),从而进一步利用未标注样本、增强排序能力。

最终联合优化 `L_all = γ·L_BCE + (1-γ)·L_Ranking`,其中 BCE 项用 ADM 掩码并对每个 batch 的有效样本做动态平均以稳定训练。

## 结果

**工业数据集**:来自某 app 推广业务的约 2×10^8 样本,5 个转化行为(Action A–E),四周训练 + 次日测试。指标为 AUC 与 LogLoss(AUC 越高越好、LogLoss 越低越好),以 RelaImpr 衡量相对提升。对比 SingleTask、Shared Bottom、[[star]]、[[mmoe]]、[[ple]]、TAML:

- KAML 在 All(整体)上 AUC=0.9133,优于 MMoE(0.9108)、PLE(0.9108)、TAML(0.9116)等所有基线。
- 各任务 RelaImpr(相对 best baseline):Action A +1.24%、Action B +0.41%、Action C +0.48%、Action D +9.62%、Action E +1.89%、All +0.41%。
- 作者也指出 KAML 的 LogLoss 存在一定不稳定性(Action A、E 上非最优),归因于 RLU 模块——排序损失可提升 AUC 但可能使 LogLoss 上升。

**模拟公开数据集**:把 [[kuairand-pure]] 改造成非对称多标签格式(取 is_like / is_follow / is_comment / is_forward 4 类反馈作为 Action A–D,约 9×10^5 样本)。对比 Oracle(全标签)、Vanilla(仅随机一类目标)、KAML(目标 + 随机两类相关反馈 + rank loss):KAML 在 4 个转化行为中的 3 个上超过 Vanilla;在 Action C、D 上甚至优于 Oracle(添加额外标签的 seesaw 效应可能损害 C、D 性能)。

**消融实验**(基于 MMoE):MMoE → +ADM → +ADM+HKE → KAML 逐步提升,All AUC 从 0.9108 提升到 0.9133,验证 ADM 过滤噪声标签、HKE 缓解分布差异、RLU 增强排序各自的有效性。

**线上实验**:在华为在线广告平台部署,8 天线上 A/B 测试(基线与实验各约 10% 流量,同样的曝光日志训练)。平均 RPM(Revenue Per Mille)提升 12.11%,CVR 提升 0.92%。

## 在本 wiki 中的位置

本文属于 [[recommender-systems|recommender-system]] / 在线广告中的 [[ctr]] / CVR 多任务建模主题,基座沿用 [[mmoe]] / [[ple]] 等 [[multi-task-learning]] 架构,与 [[esmm]] 等转化建模工作相关,但聚焦"广告主部分上报"导致的非对称多标签这一新问题,用归因掩码 + 层级知识抽取 + 排序损失利用未标注样本,可与 [[multi-scenario-recommendation]]、[[negative-transfer]]、[[learning-to-rank]] 等条目互相参照。作者来自 [[huawei-noahs-ark-lab]] 与 [[peking-university]]。
