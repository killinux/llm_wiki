---
type: concept
subtype: method
tags: [missing-at-random, mar, debiasing, unbiased-evaluation, missing-data, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Missing-at-Random Data

Missing-at-Random (MAR) 指数据的缺失机制与"缺失值本身"无关:在控制已观测变量后,某个值是否被观测到与其未观测到的取值相互独立——在推荐系统中通常通过随机曝光(random exposure)收集,从而得到不受用户/系统选择偏差影响的交互数据。

## 在本 wiki 中的出现

- [[2022-kuairand]]:KuaiRand 在快手的常规推荐流中**随机插入视频**进行曝光,由此采集到的交互即为 Missing-at-Random 数据。这部分无偏交互(随机曝光下的真实反馈)是该数据集区别于一般日志数据的核心价值,使其能够支持去偏(debiasing)算法研究与无偏的离线评估(offline evaluation)。数据集还配套了 12 种反馈信号、完整的用户/物品 ID 与特征,便于在 MAR 设定下做基准对比。
- [[2024-fairness-recommendation-missing-labels]]:证明大规模推荐系统在缺失标签下 REO 公平性指标不可识别,提出用小比例 random traffic 无偏估计公平性指标并给出误差上界,首次公开 TikTok 公平性数据集。
- [[2025-where-to-explore-reach-cost-aware-unbiased-data]]:提出按用户 scroll-depth 触发、低成本高触达的专用 UI 行("Something Completely Different")来交付随机化探索内容,在不损害短期参与度的前提下大规模收集无偏交互数据,并回灌候选生成提升长期推荐质量(线上 +0.94% 参与度,无偏数据 Gini 0.203 vs 0.494)。

## 相关

- [[missing-not-at-random]]:与 MAR 相对的缺失机制(MNAR),即缺失与未观测取值相关——常规推荐日志因曝光由系统决定而属于 MNAR,这正是需要 MAR 数据来校正的来源。
- [[selection-bias]]:推荐日志中缺失非随机所导致的核心偏差,MAR 数据是评估与纠正它的手段。
- [[debiasing]]:利用 MAR 数据做训练/评估去偏的算法方向。
- [[unbiased-offline-evaluation]]:以 MAR 数据作为无偏测试集的离线评估方法。
- [[2022-kuairand]]:提供 MAR 数据的数据集来源。
