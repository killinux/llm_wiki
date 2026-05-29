---
type: concept
subtype: method
tags: [recommendation, diversity, recommender-systems, polarization]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# recommendation diversity

推荐多样性指在推荐系统中提升所推荐内容的多样化程度,以减少同质化与过滤气泡、避免用户兴趣过度收窄的一类目标与方法。

## 在本 wiki 中的出现

- [[2024-user-creator-feature-polarization]]:提出 user-creator feature dynamics 模型刻画推荐系统对用户与创作者的双向影响,证明非零推荐概率下系统必然极化,并发现 top-k 截断等效率优化反而能抑制极化、而多样性提升方法在动态环境下失效。
- [[2025-multi-objective-controllable-decision-transformer]]:提出 MocDT,一种基于 Decision Transformer 的离线 RL 推荐方法,把未来多目标作为控制信号,在推理阶段自回归生成对齐指定目标(累积评分与多样性)的物品序列,无需重训。
- [[2025-mitigating-unwanted-recommendations-conformal-risk-control]]:一个 post-hoc、模型无关、distribution-free 的方法,用 conformal risk control 给推荐中"不想要内容"的比例提供可证明上界,并以用户曾看过的安全重复内容替换有害项以保住推荐质量。
- [[2025-hid-vae-interpretable-generative-recommendation]]:HiD-VAE 用层次化监督量化 + uniqueness loss 学习可解释、解耦的 semantic ID,消除 ID 碰撞并显著提升生成式推荐性能。
- [[2026-entropy-guided-agentic-recommendation]]:提出 IDSS,用 Shannon 熵作为统一信号贯穿对话式推荐的偏好询问、排序与多样化呈现三阶段,在用户意图模糊时兼顾追问效率与残余不确定性驱动的多样化推荐。

## 相关

- [[recommender-systems]]
- [[polarization]]
- [[filter-bubble]]
- [[top-k-truncation]]
