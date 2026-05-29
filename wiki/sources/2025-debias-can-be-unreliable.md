---
type: source
subtype: paper
tags: [debiasing, evaluation, recommender-system, recall, off-policy-evaluation]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2409.04810
raw: raw/2409.04810.pdf
authors: [Chengbing Wang, Wentao Shi, Jizhi Zhang, Wenjie Wang, Hang Pan, Fuli Feng]
year: 2025
---

# Debias Can Be Unreliable: Mitigating Bias in Evaluating Debiasing Recommendation

本文揭示了用随机曝光数据集(randomly-exposed dataset)以传统方式评估去偏推荐模型并不可靠,并提出 Unbiased Recall Evaluation (URE) 方案来无偏估计 fully-exposed 数据上的 Recall@K。

## 问题

[[debiasing]] 推荐模型理论上应在 [[fully-exposed-dataset|全曝光数据集]] $D_{full}$ 上评估其真实 Recall 性能(此为 gold standard)。但全曝光数据集在实践中极难获得(目前唯一公开的研究用全曝光数据集是 [[kuairec|KuaiRec]]),因此现有工作普遍退而求其次,在 randomly-exposed 数据集 $D_{rand}$ 上用与全曝光相同的公式计算 Recall(称为 Recall@$\overline{K}$),作为代理来评估去偏模型。

作者指出:$D_{rand}$ 上的 Recall@$\overline{K}$ 与 $D_{full}$ 上的真实 Recall@$K$ 之间存在不一致(inconsistency)。这种传统评估方案("traditional evaluation scheme on $D_{rand}$")可能导致对此前去偏方法效果的错误结论。

## 方法

**理论分析(Theorem 1)**:假设 $D_{full}$ 有 $N^+$ 正样本、$N^-$ 负样本(共 $N$),$D_{rand}$ 从中采样 $\overline{N}$ 个。当 $\overline{K} = \frac{\overline{N}}{N}\cdot K$ 时,期望上有 $E[\text{Recall@}\overline{K}] - \text{Recall@}K = 0$。但由于 $D_{rand}$ 是 $D_{full}$ 的稀疏子集($\overline{N}\ll N$),只有在 $K$ 取较大值时,$D_{rand}$ 上的 Recall@$\overline{K}$ 才与 $D_{full}$ 上的 Recall@$K$ 强相关;而实际部署关心的是小 $K$(如 K=50)处的性能,此时相关性很弱。

**URE 方案**:仅依赖 $D_{rand}$ 即可无偏估计 $D_{full}$ 上的 Recall@$K$,步骤为:
1. 用待测模型 $M$ 对所有候选物品(全部 $N$ 个)产生预测分 $\hat{y}=M(uid, iid)$;
2. 按 $\hat{y}$ 降序排序候选物品;
3. 将 $D_{rand}$ 中的标签(正:1,负:0,缺失:\\)赋给排序后的物品;
4. 定位第 $(K+1)$ 个物品及其预测分;
5. 计算该用户的 $\widehat{\text{Recall@}K} = \frac{m}{n}$,其中 $n$ 为 $D_{rand}$ 中正标签物品数,$m$ 为其中预测分高于第 $(K+1)$ 物品的数量;
6. 对所有用户取平均作为模型整体 Recall@$K$ 的无偏估计。

核心思想是利用模型对**全部候选物品**的预测信息(传统方案忽略了这一点),将随机曝光数据上的"正样本比例"作为全曝光 Recall 的无偏估计。**Theorem 2(URE Unbiasedness)** 证明对任意 $K$,$E[\widehat{\text{Recall@}K}] = \text{Recall@}K$。

## 结果

在 [[kuairec|KuaiRec]](全曝光,1411 用户、3327 物品)和 [[yahoo-r3|Yahoo!R3]] 两个数据集上,以 [[matrix-factorization|MF]] 为骨干重评估多种经典去偏方法:[[inverse-propensity-scoring|IPS]]、[[doubly-robust|DR]]、[[autodebias|AutoDebias]]、[[hard-negative-mining|DNS]]。

- **相关性实验(Figure 1)**:当 $\overline{N}$、$\overline{K}$ 固定时,Recall@$\overline{K}$ 与 Recall@$K$ 的最高相关性出现在大 $K$ 处;Pearson 相关系数在 $K>100$ 时超过 0.9,但在 $K<10$ 时低于 0.6。$K_{max}$ 随采样量 $\overline{N}$ 增大而减小,随 $\overline{K}$ 减小而减小。
- **URE 无偏性(Figure 3)**:在 KuaiRec 上,小 $K$(如 K=30)时 Recall@$\overline{1}$、Recall@$\overline{5}$ 与 Recall@$K$ 相关性差;而 URE 的 $\widehat{\text{Recall@}K}$ 与 Recall@$K$ 相关系数高于 0.9。
- **重评估结果(Table 1,$p<0.01$)**:在 KuaiRec 上,URE 的 Recall@5 与全曝光数据上的真实 Recall@5 高度吻合(如 MF:URE 0.0267 vs 全曝光 0.0257;AutoDebias:URE 0.0323 vs 全曝光 0.0317),而传统方案与真值差距大且无法保持排序一致(如 MF 传统 0.4859)。值得注意的是,用 Recall@$\overline{5}$ 验证时,部分去偏方法表现反而**劣于**原始 MF,提示现有去偏技术仍有改进空间。Yahoo!R3 因缺乏全曝光数据集而无 Recall@5 真值列。

## 在本 wiki 中的位置

本文属于 [[recommender-systems|推荐系统]] 中 [[debiasing|去偏]] 方向的**评估方法学**工作,与 [[off-policy-evaluation|off-policy 评估]]、[[selection-bias|选择偏差]]、[[exposure-bias|曝光偏差]] 相关。它质疑了用 [[yahoo-r3|Yahoo!R3]] 等随机曝光数据评估去偏模型的传统范式,并依赖 [[kuairec|KuaiRec]] 这一全曝光数据集作为 gold standard。所评估的方法 [[inverse-propensity-scoring|IPS]]、[[doubly-robust|DR]]、[[autodebias|AutoDebias]] 是去偏推荐的代表性基线。作者团队来自 [[university-of-science-and-technology-of-china|USTC]] 与 [[national-university-of-singapore|NUS]]。
