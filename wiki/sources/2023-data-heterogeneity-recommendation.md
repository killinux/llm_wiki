---
type: source
subtype: paper
tags: [recommendation, data-heterogeneity, clustering, debiasing, robustness, sub-population]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2305.15431
raw: raw/2305.15431.pdf
authors: [Zimu Wang, Jiashuo Liu, Hao Zou, Xingxuan Zhang, Yue He, Dongxu Liang, Peng Cui]
year: 2023
---

提出 Bilevel Heterogeneity Exploration(BHE):一种通过双层聚类显式探索推荐数据中"预测机制异质性"与"协变量分布异质性"的方法,并将挖掘出的异质性用于多子模型预测与去偏(debias),从而提升推荐模型的泛化性与子群体鲁棒性。

## 问题

海量数据是数据驱动推荐模型的基础,而大数据天然存在**数据异质性(data heterogeneity)**:数据由多个子群体(sub-population)聚合而成,不同子群体具有不同特性。在推荐场景中,联合分布 P(Y, U, V) 可分解为**预测机制 P(Y|U,V)**(评分模式)与**协变量分布 P(U,V)**(交互模式)两部分,二者在不同子群体间均存在异质性。

忽略数据异质性会:限制推荐模型性能、损害子群体鲁棒性(少数子群体被多数群体主导)、并使模型被偏差(bias)误导。然而推荐社区此前对数据异质性缺乏显式建模——已有去偏工作只处理由系统本身引起的偏差(曝光偏差、位置偏差、流行度偏差),并未显式定义和探索异质性。一个关键挑战是:测试阶段没有真值评分 Y,无法直接判断样本属于哪个子群体。

## 方法

提出 **Bilevel Heterogeneity Exploration(BHE)** 双层聚类框架:

- **E 层聚类(预测机制异质性)**:用类 EM 算法挖掘潜在环境标签 E。M 步在每个环境上训练独立的因子分解推荐器 h_e(如 [[matrix-factorization]] / [[factorization-machines]]);E 步按各模型对样本的损失把样本重新分配到拟合最好的环境,迭代直至收敛,得到环境 G_e。
- **R 层聚类(协变量分布异质性)**:在每个 E 环境内,对原始特征映射到的 embedding 空间用 **k-means** 聚类,挖掘 R 环境,输出样本到各环境中心的距离 G_{e,r}。
- **耦合假设**:由于推荐系统的选择机制,预测机制异质性与协变量分布异质性是对齐(aligned)且耦合的;论文用 compactness 指标实证验证(按预测机制划分的子群体在协变量上更紧凑)。测试期通过联合训练分类器 f_c(用 embedding 预测环境),解决无 Y 时的子群体推断。

挖掘出的异质性有**两种利用方式**:
- **多子模型预测**:为每个环境构造按距离 softmax 加权的训练集,训练专属推荐器 f_e;预测时按分类器给出的环境概率 p_{u,v,e} 对各 f_e 输出加权求和,组合成 f_cm。
- **支持去偏**:为每个环境学习专属的倾向得分(propensity score),比传统在所有环境上共享的 Naive Bayes 估计更准确,再结合 IPS / SNIPS 训练去偏推荐器。

## 结果

在真实数据集上实验,回答 RQ1-RQ4。骨干模型:有充足原始特征的数据集(Yelp、MovieLens-1M)用 FM 与 NFM;去偏设置用 [[matrix-factorization]](MF)与 NCF。去偏数据集为 Yahoo 与 Coat(含随机曝光的无偏 uniform 集)。

- **更好泛化(Table 2,NDCG/Recall ×10^-2)**:BHE 在所有指标上均取得最佳。例如 Yelp 上 FM 骨干 NDCG@20 从基线 None 的 6.52 提升到 BHE 的 8.24;NFM 骨干 NDCG@20 从 14.01 提升到 22.57、Recall@30 从 30.90 提升到 41.22。MovieLens-1M 上 NFM 骨干 NDCG@20 从 11.11 提升到 14.61。BHE 显著优于 cluster-user/item、raw feature、embedding 等基线。
- **预测机制异质性显著(RQ1)**:在不同环境训练/评估时性能急剧下降甚至崩溃,而在同一环境训练/评估则优于其他设置,证明 BHE 挖掘的环境间预测机制确有巨大差异。
- **可解释性(RQ1)**:在 Yelp 上 BHE 挖掘出三个可解释子群体——新用户(29.51%,偏好热门餐厅、社交少)、普通用户(50%,有独特口味、社交多)、影响者(20.49%,偏好知名餐厅、粉丝多)。
- **子群体鲁棒性(RQ2)**:骨干模型偏向多数子群体而忽视少数子群体;BHE 在各子群体尤其少数子群体上均有提升。
- **更好去偏(RQ3)**:BHE 在所有情形下优于 IPS / SNIPS 基线;消融显示只用 E 或只用 R(BHE-E / BHE-R)在多数情形也优于 IPS/SNIPS,说明 E 与 R 两种异质性都对去偏有帮助。

## 在本 wiki 中的位置

本文属于**推荐系统**与**分布异质性 / 分布外泛化(OOD generalization)** 的交叉脉络,与 [[peng-cui]] 课题组在稳定学习 / 因果推断方向的工作一脉相承。它把"环境划分 + 不变性"的思想(类似 [[invariant-risk-minimization]] / [[distributionally-robust-optimization]] 的动机)迁移到推荐场景,并与推荐去偏中的 [[inverse-propensity-score]] 方法结合。可与传统 [[factorization-machines]] / [[matrix-factorization]] 推荐模型、以及 [[recommender-systems]] 中的去偏与子群体鲁棒性研究对照阅读。
