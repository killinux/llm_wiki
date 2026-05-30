---
type: topic
tags: [recommender-system, fairness, multi-stakeholder, welfare, polarization, safety]
created: 2026-05-30
updated: 2026-05-30
sources: 16
---

# 推荐系统的公平性与多边福利 (Fairness & Multi-Stakeholder Welfare)

> 一句话:推荐平台是**多边市场**——同时服务**用户、创作者/提供方、平台**。只优化用户侧准确性会系统性损害创作者生态、
> 放大极化、传播有害内容。这条线研究如何在多方之间分配**曝光、福利与风险**,并应对**反馈回路**带来的长期动态后果。

概念枢纽见 [[recommendation-fairness]]、[[item-side-fairness]];与 [[debiasing-causal-recommendation]](偏差是不公平之源)、
[[rl-for-recommendation]](马太效应)、[[generative-social-simulation]](极化的社会后果)交叉。

---

## 一、提供方 / 物品侧公平:曝光分配
用户需求**短期即时**(差推荐即受损,损失厌恶),提供方需求**长期曝光**——二者紧迫性不同,需在时间上调和。
- [[2024-bankfair-fluctuating-traffic-reranking]](BankFair)—— 借**破产问题的 Talmud rule** 做重排,在**用户流量波动**下同时保证短期准确性与长期提供方公平;
  实证(KuaiRand)显示流量越低、传统方法准确性损失越大。[[2025-bankfair-plus-regret-aware-reranking]] 加 regret-aware 改进。
- [[2025-lhrl-lifecycle-fairness-recommendation]] —— 把**物品生命周期**作为公平旋钮,用**分层 RL** 按阶段动态调和:破除"长尾假设恒成立"的误区(陈旧内容被过推、新内容错失早期窗口)。
- [[2026-proactive-guiding-item-side-fairness]] —— 主动引导式物品侧公平;三方建模 [[2026-trirec-tri-party-agent-recommendation]]。

## 二、用户侧 / 群体公平
- [[2024-fairness-recommendation-missing-labels]] —— 在**标签缺失**下度量并缓解按敏感群体的性能差异(公平评估本身受 MNAR 缺失干扰)。
- 与 [[implicit-feedback]] 的 MNAR、曝光偏差同源(详见 [[debiasing-causal-recommendation]])。

## 三、动态视角:反馈回路与极化
公平不能只看静态一轮——推荐**同时改变用户偏好与创作者行为**,长期后果反直觉:
- [[2024-user-creator-feature-polarization]] —— 提出 user-creator **dual influence** 模型,**理论证明**:任意推荐概率非零的系统都**不可避免地走向极化**;
  并意外发现常见的**多样性提升方法在动态下失效**,反而 **top-k 截断**这类效率手段能抑制极化。
- 流行度偏置 / 马太效应("富者愈富")是不公平的动力学根源,见 [[2023-dorl-matthew-effect-offline-rl-recommendation]];社会层面的极化后果见 [[generative-social-simulation]]。

## 四、福利、安全与可被操控性
公平延伸到"**不想要/有害内容**"的可控曝光与抗操控:
- [[2025-mitigating-unwanted-recommendations-conformal-risk-control]] —— 用 **conformal risk control** 给"不想要内容"比例**可证明上界**(distribution-free、model-free,post-hoc),
  把潜在有害项替换为"安全"重复内容以保住质量。
- [[2026-collective-manipulation-risk-controlling-recsys]] —— 对上述风险控制系统的**部署前审计**:仅 **1%** 协同对抗用户用 "Not Interested" 即可让普通用户 NDCG **降最多 20%**;
  提出把风险保证从**群体级改为个体级**缓解。揭示"把用户反馈直接接入安全保证"反而开了被操控的新杠杆。
- 风控/操控延伸:[[2026-collective-manipulation-risk-controlling-recsys]] 与 shilling/crowdturfing、[[adversarial-robustness]] 相关。

## 五、核心张力
1. **短期用户 vs 长期提供方**:即时准确性 vs 累积曝光公平(BankFair 的出发点)。
2. **个性化 vs 多样性/极化**:过度个性化加剧信息茧房,且动态下"多样性提升"可能无效([[2024-user-creator-feature-polarization]])。
3. **公平 vs 准确**:公平约束的准确性代价,需在 [[reranking|重排]]/[[multi-objective-optimization|多目标]]层平衡。
4. **安全保证 vs 可被操控**:把用户反馈接入形式化保证,反而创造对抗杠杆。

## 六、开放问题
- **动态公平**:把反馈回路与长期均衡纳入公平目标(多数方法仍是静态/单轮)。
- **个体级 vs 群体级保证**:群体级风险控制易被协同操控,个体级代价几何。
- **多边目标的统一框架**:用户/创作者/平台福利的可计算权衡(与 welfare economics 接轨)。
- **评估**:公平评估在 MNAR 与缺失标签下本身不可靠(呼应 [[debiasing-causal-recommendation]] 的"评估不可靠"主题)。

## 相关概念页
[[recommendation-fairness]]、[[item-side-fairness]]、[[reranking]]、[[multi-objective-optimization]]、[[personalization]]、
[[causal-inference]]、[[conformal-risk-control]]、[[debiasing-causal-recommendation]]
