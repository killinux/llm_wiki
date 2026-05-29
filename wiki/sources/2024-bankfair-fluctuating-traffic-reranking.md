---
type: source
subtype: paper
tags: [recommender-system, fairness, two-sided-platform, re-ranking, bankruptcy-problem, talmud-rule, online-learning]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2405.16120
raw: raw/2405.16120.pdf
authors: [Xiaopeng Ye, Chen Xu, Jun Xu, Xuyang Xie, Gang Wang, Zhenhua Dong]
year: 2024
---

# Guaranteeing Accuracy and Fairness under Fluctuating User Traffic: A Bankruptcy-Inspired Re-ranking Approach

BankFair 是一个面向两侧平台(two-sided platform)的公平性感知 re-ranking 方法,借鉴破产问题(bankruptcy problem)中的 Talmud rule,在用户流量波动的场景下同时保证短期用户准确性与长期提供方公平性。

## 问题

在两侧 [[recommender-systems|recommender-system]] 中,提供方(provider)与用户(user)的需求紧迫性不同:提供方需要相对长期的曝光(exposure)需求,可以在较长周期内被满足;而用户的需求是短期、即时的,一旦遭遇差的推荐就会长期受损(损失厌恶效应,loss aversion)。已有的公平-准确性权衡方法在真实的波动用户流量(fluctuating user traffic)下往往失效:作者基于 KuaiRand 数据的实证研究(Figure 1)显示,用户流量越低,准确性损失越大,用户体验下降得越多。

作者还从约束优化(constrained optimization)角度给出理论分析,回答两个问题:
- 为什么提供方公平性会损害准确性?(Theorem 1:当准确性最优解不满足公平约束时,被迫移动到可行域内的提供方公平解,必然带来准确性损失。)
- 为什么低流量会导致更大的准确性损失?(Theorem 2:准确性损失 L 的期望与该时段用户流量 r_n 成反比,E[L] ∝ 1/r_n。低流量收紧了公平可行域,从而放大准确性损失。)

核心问题:如何在波动流量下同时保证准确性与公平性。

## 方法

BankFair 将曝光分配过程建模为一个**序列化的破产问题**(sequential bankruptcy problem),并用 Talmud rule 求解。它把破产问题的元素与两侧 re-ranking 对应(Table 1):时间区间 N ↔ 智能体集合,所需最小曝光 m_p ↔ 遗产(estate),需求最小曝光向量 D_p ↔ 索赔向量(claim),预测最小曝光向量 M_p ↔ 结果向量。

BankFair 包含两个模块(Algorithm 1):

- **Module 1:分配所需曝光(Talmud rule)。** 在每个区间 n,先用时间序列预测(实验中用 GRU)预测未来用户流量,据此得到需求向量 D_p(n) = αK·r̂(n);流量低时给提供方更低需求以减少准确性损失,流量高时给更高需求来补偿,从而摊平公平要求。再用历史分配更新剩余未满足的最小曝光 m̃_p(n),最后用 Talmud rule TAL(·) 计算输出向量 M_n,作为该区间的预测最小曝光。Talmud rule 直观上:在流量充裕期补偿流量稀缺期的曝光缺口,以保证长期公平的同时在低流量期降低公平度。

- **Module 2:在线推荐。** 把两侧 re-ranking 写成资源分配 / 整数规划(IP)问题,约束为每个提供方曝光不低于 Module 1 给出的 M_n,目标是最大化准确性。由于用户是顺序到达的,作者用 Lagrangian relaxation 把问题转化为正则化对偶问题(Theorem 3),用加权投影次梯度法在线更新对偶变量 μ_t,为每个到达用户即时生成 top-K 推荐列表。

## 结果

在两个真实数据集上评测(基座模型为 LightGCN,更新区间设为 24 小时):
- **KuaiRand-1K**:302870 条交互,933 用户,6825 视频,174 提供方;m_p=1000。
- **Huawei-Video**(华为浏览器短视频,2024.1.2–2024.1.8):19355 用户,5364 物品,200 提供方,118765 条交互;m_p=100。

指标:NDCG@K(准确性,越高越好)、Vio@K(准确性违反率,低于最小准确性 φ 的用户比例,越低越好)、ESP@K(enough satisfaction group,满足最小曝光的提供方比例,越高越好)。φ=0.95。

基线:P-MMF、FairRec、TFROM、PCT,以及简单分配规则的 Naive、Prop。

主要结论:
- BankFair 的 Pareto frontier 支配所有基线(位于右上角),在相同公平水平(ESP@K)下取得更高 NDCG@K 与更低 Vio@K。
- BankFair 对几乎所有提供方满足所需最小曝光(ESP=100%),并对几乎所有用户保证最小准确性(Vio@K≈0%)。当 top-K 较小(如 K=5)时,多数基线无法满足短期准确性需求,而 BankFair 仍能兼顾。
- 在更严格的最小曝光 m_p 和更高的所需准确性 φ 下,BankFair 仍保持稳定、低 Vio;在流量波动越剧烈(温度 τ∈[0,0.2])时优势越明显,验证了"低流量加剧准确性损失"的理论分析。
- 换基座模型的消融(Table 2,BPR / NCF):BankFair 取得 100% ESP,准确性更高、违反率更低。以 BPR 为基座,相对最佳基线 NDCG +1.6%、Vio −36.3%;以 NCF 为基座,NDCG +2.0%、Vio −95.9%(改进具统计显著性,p<0.05)。

## 在本 wiki 中的位置

本文属于 [[recommender-systems|recommender-system]] 公平性方向,聚焦两侧平台(two-sided platform)的提供方公平 re-ranking,与曝光公平基线 P-MMF、FairRec、TFROM 同一谱系。其特色在于用经济学的破产问题 / Talmud rule 处理流量波动下的曝光分配,并结合 Lagrangian relaxation 的在线学习。作者来自 [[renmin-university-of-china]] 与 [[huawei-noahs-ark-lab]],通讯作者 [[jun-xu]];数据集使用了 [[kuairand]] 与 Huawei-Video。
