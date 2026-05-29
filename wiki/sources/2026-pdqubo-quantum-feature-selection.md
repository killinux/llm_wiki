---
type: source
subtype: paper
tags:
  - quantum-annealing
  - qubo
  - feature-selection
  - recommender-system
  - counterfactual-analysis
created: 2026-05-29
updated: 2026-05-29
arxiv: "2410.15272"
raw: raw/2410.15272.pdf
authors:
  - Jiayang Niu
  - Jie Li
  - Ke Deng
  - Mark Sanderson
  - Nicola Ferro
  - Yongli Ren
year: 2026
---

# Performance-Driven QUBO for Recommender Systems on Quantum Annealers

PDQUBO 是一种面向[[recommender-systems|推荐系统]]特征选择的「性能驱动」QUBO 构造方法,它用[[counterfactual-reasoning|反事实分析]]来量化单个特征与特征对对推荐性能的影响,从而让量子退火器(quantum annealer)的优化方向直接对齐推荐质量。

## 问题

特征选择是现代推荐系统的关键工程问题:冗余或低信息量的特征会损害检索效率、增加存储并降低性能。把特征选择形式化为 QUBO(Quadratic Unconstrained Binary Optimization,二次无约束二值优化)问题 $\min_{x\in\{0,1\}^n} x^\top Q x$,可以借助量子退火器(如 D-Wave)利用量子隧穿逃离局部最优来求解。

但现有 QUBO 特征选择方法构造系数矩阵 $Q$ 的方式都不直接面向推荐性能:

- MIQUBO / CoQUBO(Nembrini 等)用特征与标签之间的互信息 / 相关性填充 $Q$,类似 filter 方法,依赖 ground truth。
- QUBO-Boosting 用模型(如 SVC)的预测输出填充 $Q$,只用 model outcome。
- CQFS 用协同过滤模型与内容模型之间的相似性一致性填充 $Q$,偏 wrapper 思路,但评估的是相似性一致而非排序性能。

这些方法都没有显式优化下游推荐指标。论文围绕三个问题展开:Q1 量子退火器的不稳定性如何影响推荐性能;Q2 量子退火器在推荐特征选择上效果如何;Q3 它能否追平甚至超越成熟的经典特征选择方法。

## 方法

**PDQUBO(Performance-Driven QUBO)** 的核心是用反事实实例(counterfactual instances)构造 $Q$:

1. 先用全量特征集 $\mathcal{F}$ 训练一个 base model $G_\Theta$(模型无关:Item-KNN、MLP-DP、MLP-CON、NCF、[[deepfm|DeepFM]]、FiBiNET 等均可)。
2. 通过特征掩码 $\mathcal{F}_{\text{mask}} = \mathcal{F} \odot M_c$ 在 item 层面把某些特征置零,计算性能变化:$E_i = G(\mathcal{F}) - G(\mathcal{F}_{\text{mask}}^i)$(去掉特征 $f_i$ 的性能下降),以及 $E_{ij}$(同时去掉 $f_i,f_j$)。性能指标 Mtc 任意(如 [[ndcg|nDCG]]、[[recall|Recall]]、AUC),因此该方法对 base model 与评估指标都不敏感。
3. 由于 QUBO 是最小化问题,令对角元 $Q_{ii} = -E_i$、非对角元 $Q_{ij} = -E_{ij}$,使优化方向朝向最大化所选特征集对推荐性能的贡献。
4. 用软基数约束 $\lambda(\sum_i x_i - k)^2$ 控制选中特征数 $k$,$\lambda = \max_i \sum_j |Q_{ij}|$。
5. 构造好 $Q$ 后与训练完全解耦,直接提交给求解器:经典的 Simulated Annealing(SA)、SGD、Tabu Search(TS),或量子的 Quantum Annealing(QA)/ Hybrid(D-Wave Advantage 6.1,>5000 物理 qubit)。

构造 $Q$ 的主要开销是 $|\mathcal{F}| + \frac{|\mathcal{F}|(|\mathcal{F}|-1)}{2}$ 次掩码推理($O(|\mathcal{F}|^2)$),可并行化;论文还探讨了两阶段剪枝(two-stage pruning)加速,但发现它会破坏二次交互结构。

## 结果

数据集:QuantumCLEF 2024 的 **150_ICM**(每 item 150 稀疏特征)和 **500_ICM**(500 特征),以及工业级 [[kuairec|KuaiRec]](116 特征,1411 用户/3276 item)和 [[kuairand|KuaiRand]](224 特征,13077 用户/3359 item)。主指标 nDCG@10,结果取 5 次随机初始化平均。

- **超越 QUBO baseline**:在 150ICM/500ICM 上,PDQUBO 相对 CQFS、QUBO-Boosting、CoQUBO、MIQUBO 普遍更优。例如 Item-KNN + SA、$k=130$ 时 PDQUBO 达 0.1140,优于最佳 baseline QUBO-Boosting 的 0.1021(+11.7%);$k=140$ 时 0.1121 对 CQFS 0.1015(+10.4%)。
- **二次项的必要性**:用完整 $Q$(「all」,含 $E_{ij}$)对比只用对角项(「Indiv」),在 $k=*$ 时 all 全面胜出;KS 检验显示 all 的 nDCG@10 均值 0.1151 vs Indiv 0.1139,KS 统计量 0.2465,p 值 7.84e-5,差异显著。
- **量子退火不稳定性**:QA 的解质量随问题规模 $|\mathcal{F}|$ 增大而急剧恶化(Table 3 中带约束 $k=90\%|\mathcal{F}|$ 时,scale=150 的 $Y$ 从 SA 的 -7.970 暴增到 QA 的 164.041);增大采样数(50→10000)可降低能量方差并提升重训练 nDCG;问题越稀疏(难度越高)QA 改进越大但越不稳定。
- **速度**:QA/Hybrid 的求解时间几乎不随规模增长(scale=500 时 SA 391.03s、SGD 212.19s、TS 472.01s,而 Hybrid 仅 16.49s;QA 单次退火 <1e-4 秒)。
- **工业级 + 重训练**:在 150_ICM/500_ICM/KuaiRec/KuaiRand 上做完全重训练 + Bayesian 调参后,PDQUBO 在多数配置取得最佳或次佳;如 NCF + 500_ICM 从全特征 0.1388 提升到 0.1491。
- **对比经典方法(CTR 任务)**:在 Avazu、Criteo、ICM_150、ICM_500 上换用 DeepFM/FiBiNET、指标改 AUC,与 ERASE 基准下的 Lasso、GBDT、AutoField、LPFS、SFS、Permutation、SHARK 等比较。PDQUBO_hybrid 多数场景取得最佳或次佳(如 DeepFM+Criteo AUC 0.76857、Logloss 0.47770),并全面超过其他 QUBO baseline;PDQUBO_Indiv(只用对角项)性能明显退化,再次印证交互项的重要性。

## 在本 wiki 中的位置

这是一篇把 [[counterfactual-reasoning|反事实分析]] 用作 [[causal-inference|因果推断]] 工具来构造组合优化目标、并在量子退火硬件上做 [[recommender-systems|推荐系统]] 特征选择的工作,核心创新是让 QUBO 的优化方向显式对齐下游推荐性能(performance-driven),概念上属于 wrapper 式特征选择。它使用 [[ndcg|nDCG]] 与 [[recall|Recall]] 作为推荐评估指标,base model 覆盖 [[collaborative-filtering|协同过滤]]、[[deepfm|DeepFM]] 等,数据集包含 [[kuairec|KuaiRec]]、[[kuairand|KuaiRand]]。与本 wiki 中以 LLM/RL 为主的推荐研究不同,本文代表了「量子计算 + 推荐系统」这一相对小众但新颖的交叉方向。
