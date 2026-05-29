---
type: source
subtype: paper
tags:
  - collaborative-filtering
  - recommender-system
  - multi-task-learning
  - ordinal-logistic-regression
  - implicit-feedback
  - embedding-based-retrieval
  - ctr
created: 2026-05-29
updated: 2026-05-29
arxiv: "2505.20900"
raw: raw/2505.20900.pdf
authors:
  - Zhongjin Zhang
  - Yu Liang
  - Cong Fu
  - Yuxuan Zhu
  - Kun Wang
  - Yabo Ni
  - Anxiang Zeng
  - Jiazhi Xia
year: 2025
---

# GNOLR: Embed Progressive Implicit Preference in Unified Space for Deep Collaborative Filtering

提出 Generalized Neural Ordinal Logistic Regression(GNOLR),用有序映射 + 嵌套优化把点击/加购/购买等多种隐式反馈编码进**统一的 embedding 空间**,既建模用户参与度的递进关系,又把多路检索简化为单次最近邻搜索。

## 问题

基于 embedding 的 [[collaborative-filtering]](CF)通常配合最近邻搜索(NNS / [[approximate-nearest-neighbor-search]])部署在大规模 [[recommender-system]] 中。现代系统会利用多种隐式反馈信号(点击、加购、购买等)来刻画用户偏好,但主流做法采用 **feedback-wise(逐反馈)建模范式**,存在三个根本缺陷:

1. **忽略参与度递进**:把每种反馈当成独立的二分类/排序任务,例如在购买预测中,"点击但未购买"的物品与"完全未点击"的物品被同等视为负样本,丢失了前者偏好高于后者的语义。
2. **embedding 空间割裂**:不同任务产生互不可比(incommensurable)的 disjoint 空间,一个空间的相似度分数无法与另一个比较,导致大规模 RS 需要冗余索引/排序,且加性、乘性等融合启发式会引入精度损失。
3. **梯度冲突**:不同反馈用独立预测头,当标签相互矛盾(点击但未购买)时共享参数出现梯度冲突,影响训练稳定性。

[[ordinal-logistic-regression]](OLR,序数逻辑回归)能显式建模有序关系,但既有 OLR 推荐模型主要面向**显式反馈**(如电影评分),难以处理顺序模糊、非线性、相关的隐式反馈;且标准 OLR 对所有反馈共享同一组回归系数,无法处理 feedback-dependent 协变量。作者据此提出新问题 **Multi-Feedback Collaborative Filtering(MFCF)**:联合建模多种隐式反馈,为候选物品生成统一的全局排序。

## 方法

GNOLR 包含两大组件:**映射机制**(把无结构隐式反馈转成有序类别标签)与**广义 OLR 模型**(增强表达力)。

- **隐式反馈 -> 有序标签映射**。Step 1:依据"反馈越稀疏代表参与度/偏好越高"的先验(购买比点击罕见),按出现频率升序排列反馈类型。Step 2:对每个样本,取其正反馈在重排序列中的**最大索引**作为序数标签 k;无任何正反馈(impression)记为 k=1。例:点击 y1、加购 y2、购买 y3 自然按稀疏度排序为 [y1,y2,y3];三者皆无则 k=1;点击并直接购买(y1=1,y3=1)则 k=4(购买代表最高参与度)。

- **Neural OLR for MFCF**。采用 [[two-tower]](Twin Tower)架构,用户/物品分别经神经编码器得到 ℓ2 归一化的 embedding,把 Proportional Odds Model 重写为 `log[P(k≤c)/P(k>c)] = a_c - K(e_u,e_i)`,K 为核(用 cosine)。

- **Nested Optimization Framework(核心创新)**,解决共享编码器限制反馈特定依赖、而完全独立编码器又割裂空间的两难:
  - **Nested Category-Specific Encoding**:为每个类别 c 用单独的 Twin Tower 编码器产出子 embedding,再把它们 Concat 成嵌套 embedding `E_u^c = Concat(e_u^1,...,e_u^c)`,使高阶类别的表示包含所有低阶信息,统一进同一空间。`P(k>T)` 解释为**统一偏好分**,`E_u^T, E_i^T` 即统一偏好 embedding。
  - **Nested OLR Optimization**:定义 T 个子任务,每个子任务 t 只关注部分类别 {0,...,t+1}(把 >t+1 的标签重映射到 t+1),联合优化所有子任务,使概率沿用户参与度递进合理分布。

- 引入两个超参:阈值 `a_c`(横向平移 sigmoid,可由标签分布近似闭式计算 `a_c ≈ log[(1-E[P(k>c)])/E[P(k>c)]]`,无需调参)与 reshaping factor `γ`(控制 sigmoid 陡度,实现 hard sample mining)。理论上证明单反馈时 GNOLR 退化等价于 [[cross-entropy]] 损失,但通过 a_1、γ 改变 cosine 核输出分布,带来更强适应性;多反馈时避免了 feedback-wise CE 对"点击未购买"样本的矛盾监督。

## 结果

在 9 个大规模公开数据集上评估,涵盖电商与视频/电影场景:[[ali-ccp]]、AE(AliExpress 四个国家市场 AE-ES/FR/NL/US)、[[kuairand]](KR-Pure、KR-1K)、[[retailrocket]]、[[movielens-1m]] 与 ML-20M。指标用 AUC、GAUC、Recall@K。

- **单任务排序(AUC,Table 2)**:GNOLR 全面领先。AliCCP 0.6232(BCE 仅 0.5005);AE-ES 0.7366、AE-FR 0.7335、AE-US 0.7062、AE-NL 0.7298;KR-Pure 0.8506、KR-1K 0.9024;ML-1M 0.8139、ML-20M 0.8094;RetailR 0.7537。在极度不平衡的电商数据上,BCE 等基线常退化到 AUC≈0.5。
- **多任务排序(AUC,Table 4)**:对比 NSB、[[esmm]]、ESCM²-IPS/DR、DCMT、NISE、TAFE 等。CTCVR 上提升尤为明显,如 AliCCP CTCVR 0.5997、AE-ES CTCVR 0.8827、AE-FR CTCVR 0.8793;Like(KR-Pure 0.8456)、Follow、ATC(RetailR 0.7764)、Pay(RetailR 0.8242)多数为最优。
- **GAUC(Table 3)**:与 RankNet、LambdaRank、ListNet、S2SRank、SetRank、JRC 比较,结合 listwise 损失的 GNOLR_L 在多数数据集上最优(如 AliCCP 0.5602、KR-1K 0.5380)。
- **检索 Recall(Table 5/6)**:ML-1M 单任务 Recall@5 0.4086、@20 0.7865,均优于 BCE/RankNet/ListNet/SetRank/JRC;KR-1K 多目标检索 Like Recall@500 0.3841、Follow 0.2966,显著超过 NSB* 重加权基线。
- **可视化(Figure 4)**:标准 CE 训练的 embedding 拓扑差,正样本与用户向量夹角常 >90°;GNOLR 通过 a_c 调整角度分布,使正样本聚集在用户向量更小夹角内,提升 NNS 检索效果。
- **消融(Table 7)**:GNOLR-V0(共享编码器)、GNOLR-V1(仅嵌套类别编码)逐步验证,Nested Category-Specific Encoding 对稀疏目标增益明显,配合 Nested OLR Optimization 取得最佳。参数敏感性(Figure 5)显示对 a、γ 较鲁棒,且最优 a 与 §3.4 闭式计算吻合。

代码开源:https://github.com/FuCongResearchSquad/GNOLR

## 在本 wiki 中的位置

本文属于 **embedding-based 推荐 / 多任务建模**方向,核心贡献是用序数回归思想统一多种隐式反馈的 embedding 空间。与 [[esmm]] 等 [[multi-task-learning]] 的 [[ctr]]/CVR 建模形成对照——后者用独立预测头建模 feedback-wise,GNOLR 则强调反馈间的递进结构与统一空间,从而把多路 [[embedding-based-retrieval]] 简化为单次最近邻搜索。它把 [[ordinal-logistic-regression]] 从显式评分推进到隐式反馈,可与 [[collaborative-filtering]]、[[recommender-system]]、[[listwise-recommendation]]、[[approximate-nearest-neighbor-search]] 等条目互相参照。注:本文非 LLM 论文,属于推荐系统/CF 邻接主题。
