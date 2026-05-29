---
type: concept
subtype: method
tags: [polarization, recommender-systems, dynamics, user-creator]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# polarization

极化(polarization)指在推荐系统等交互动态中,用户与内容(或创作者)的特征随时间相互强化,最终收敛到少数对立或集中的状态的现象。

## 在本 wiki 中的出现

- [[2024-user-creator-feature-polarization]]:提出 user-creator feature dynamics 模型刻画推荐系统对用户与创作者的双向影响,证明非零推荐概率下系统必然极化,并发现 top-k 截断等效率优化反而能抑制极化、而多样性提升方法在动态环境下失效。
- [[2025-bankfair-plus-regret-aware-reranking]]:BankFair+(BankFair 的扩展期刊版)把 regret theory 的非线性满意度函数与 fuzzy programming 引入推荐重排,在保证供给侧最低曝光公平与用户平均精度的同时,显著提升被忽视的用户个体公平(KuaiRand-1K 上 MMR 0.741 vs BankFair 0.493)。
- [[2026-policysim-proactive-policy-optimization]]:PolicySim 是一个基于 LLM 智能体的社会模拟沙盒,用 SFT+DPO 训练用户智能体、用带消息传递的 contextual bandit 自适应优化推荐与曝光控制等平台干预策略,实现部署前的主动评估与优化;极化是衡量这些干预策略社会效果的核心维度之一。

## 相关

- [[recommender-systems]]
- [[user-creator-feature-dynamics]]
- [[top-k-truncation]]
- [[diversity]]
