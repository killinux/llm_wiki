---
type: source
subtype: paper
tags: [recommender-system, polarization, filter-bubble, diversity, dynamics, performative-prediction, content-creator]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2407.14094
raw: raw/2407.14094.pdf
authors: [Tao Lin, Kun Jin, Andrew Estornell, Xiaoying Zhang, Yiling Chen, Yang Liu]
year: 2024
---

# User-Creator Feature Polarization in Recommender Systems with Dual Influence

一句话:本文提出"user-creator feature dynamics"模型刻画推荐系统对用户与创作者的双向影响(dual influence),从理论上证明任意推荐概率非零的系统都将不可避免地走向极化(polarization),并意外发现常见的多样性提升方法在动态环境下失效、反而是 top-k 截断这类效率优化手段能抑制极化。

## 问题

[[recommender-system]] 同时服务两端:把相关内容推给用户,也帮助创作者(creator)触达目标受众。这种双向性意味着用户与创作者都不是静态实体——推荐既会改变用户偏好(exposure 影响兴趣),也会激励创作者调整内容风格以吸引更多用户。以往关于 filter bubble 与 polarization 的研究、以及多样性提升(diversity-boosting)方法,大多假设平台内容固定、只考虑单侧影响。作者提出核心疑问:在用户与创作者偏好共同演化的双向影响下,这些多样性提升设计是否仍然有效?系统的长期多样性会走向何方?

## 方法

- **User-creator feature dynamics 模型**:用单位球面 S^{d-1} 上的 embedding 向量表示 m 个用户偏好 u_j 与 n 个创作者风格 v_i,用 cosine similarity(内积)刻画相关性。每个时间步分三步演化:
  1. **Recommendation**:用户 j 以概率 p_ij 被推荐创作者 i,典型形式为 softmax(β⟨u_j, v_i⟩);β 越大越偏向相关性。
  2. **User update**:被推荐后用户向量朝(若喜欢)或远离(若不喜欢)创作者向量移动,再投影回单位球面,体现 "biased assimilation"。
  3. **Creator update**:创作者朝给出正反馈的用户偏好的加权平均移动,以使内容更易被推荐。
- 模型对 impact functions f、g 仅作温和假设(符号与内积一致、有上下界),泛化了 Dean & Morgenstern 的偏好动力学。
- **理论分析**:用 absorbing Markov chain 论证(区别于以往用 ODE 稳定性的 opinion dynamics 工作),证明 bi-polarization 状态是吸收态;给出收敛到极化的充分条件。
- **真实系统设计分析**:讨论 4 类实际设计——top-k truncation、threshold truncation、diversity boosting、uniform traffic——对极化的影响。
- **实验**:在合成数据(d=10, n=50, m=100, T=1000)与真实 [[movielens]] 20M 数据(用 16 维 two-tower 模型初始化 embedding)上仿真,提出 Creator Diversity (CD)、Recommendation Diversity (RD)、Recommendation Relevance (RR) 与新指标 Tendency to Polarization (TP) 来量化系统状态。

## 结果

- **不可避免的极化(Theorem 3.3)**:若每个创作者都能以非零概率(p_ij ≥ p0 > 0)被推荐给每个用户,且更新率满足 η_c ≤ η_u·L_f/2、η_u < 1/2,则从几乎所有初始状态出发,系统必将收敛到 R-consensus 或 R-bi-polarization——用户与创作者最终聚成至多两个对立簇,多样性丧失。这意味着天真地强加 p_ij ≥ p0 > 0(如 uniform traffic、softmax 探索)无法提升长期多样性。
- **diversity boosting 失效**:短视地优化推荐多样性(Eq.5 的 diversity-aware 目标)单独使用并不能阻止 bi-polarization,因为更新规则未变,定理条件仍满足;MovieLens 实验显示更大 ρ 虽提高短期 RD 与 CD 却同时升高 TP(更易极化)。
- **uniform traffic 反而有害**:作为定理的推论,加入均匀流量会保证所有推荐概率非零,从而导致极化——"为静态多样性优化反而长期摧毁系统多样性"。
- **top-k truncation 抑制极化(Prop 4.2)**:只推荐 k 个最相关创作者会让部分 p_ij = 0,可形成 ⌊n/k⌋ 个稳定簇而避免双极化。合成数据(Table 1):β=1 时 k=1 的 TP=0.27、CD=1.40;k=50 的 TP≈1.00、CD=1.00——k 越小创作者多样性越高、极化越低,但推荐多样性 RD 下降(存在 CD/TP 与 RD 的权衡)。MovieLens(Table 4)趋势一致:小 k 改善 CD/RR、降低 TP、但恶化 RD。
- **threshold truncation**:在 τ=0(90°)截断对多样性最差(TP 最高);较大阈值如 τ=cos(45°)=0.707 反而最利于多样性(合成数据 TP 降至约 0.28-0.33,CD 升至约 1.37-1.39)。
- **参数效应**:更大 β(更相关/更硬的推荐)、更小的更新率 η_c/η_u、更多 fixed dimensions(如年龄性别等不更新的特征)都能缓解极化——固定特征的存在可能解释了现实推荐系统不像理论预测那样极端极化。

## 在本 wiki 中的位置

本文属于 [[recommender-system]] 的长期动力学与社会影响研究,与 [[matthew-effect]]、[[selection-bias]] 等"系统自身造成的偏差"主题相关,也与 [[user-simulation]]、[[recsim]]、[[kuaisim-recommender-simulator]] 等用仿真研究推荐生态的工作呼应。其"双向影响"视角与 performative prediction 一脉相承,理论工具(absorbing Markov chain、单位球面上的 opinion dynamics)区别于本 wiki 中常见的 [[offline-rl]]/[[reinforcement-learning]] 推荐方法。结论上,它对 [[active-learning]] 式的探索流量与多样性目标提出告诫:在 creator 也会响应推荐的生态中,静态多样性优化可能损害长期 [[recommender-systems]] 健康度。数据集层面使用了 [[movielens]]。
