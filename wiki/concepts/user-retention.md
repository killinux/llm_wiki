---
type: concept
subtype: method
tags: [user-retention, recommendation, reinforcement-learning, short-video, mdp]
created: 2026-05-29
updated: 2026-05-29
sources: 8
---

# User Retention

User Retention(用户留存)指用户在一段时间后持续回访并继续使用产品的程度,是衡量推荐系统长期价值的核心指标,常以累计回访时间(cumulative return time)或 DAU 等形式刻画。

## 在本 wiki 中的出现

- [[2023-rlur-user-retention-short-video]]:该工作把短视频用户留存建模为**无限时域请求级 MDP**(infinite-horizon request-level MDP),并提出 **RLUR**,用强化学习**直接最小化累计回访时间**来优化留存。在 KuaiRand 上其留存效果优于 TD3、CEM 等基线,并在 Kuaishou 全量上线,带来用户留存与 DAU 的提升。在此论文中,User Retention 既是建模目标,也是最终的线上评估指标。
- [[2023-kuaisim-recommender-simulator]]:面向推荐系统的综合性用户模拟器,提供 multi-behavior 与 cross-session 反馈,统一支持 request 级 list-wise、whole-session 级 sequential 与 cross-session 级 retention 三类 RL 推荐任务并配套 benchmark。其中 cross-session 级别的 retention 任务直接以用户留存作为长期优化目标。
- [[2024-future-impact-decomposition-request-level-recommendation]]:提出 ItemA2C 框架,在 request-level MDP 下将 list-wise reward 分解为 item-wise 信用并用 actor-critic 优化每个 item 的长期未来影响,提升推荐长期效果;其优化的长期未来影响与用户留存等长期价值目标紧密相关。
- [[2026-hesitation-and-tolerance-in-recommender-systems]]:提出并验证推荐系统中介于接受与拒绝之间的 hesitation(犹豫)与 tolerance(容忍)两种中间交互状态,通过问卷、离线日志与线上 A/B 实验论证容忍侵蚀用户留存,并主张将其作为弱正/负信号重新建模。
- [[2025-multi-objective-controllable-decision-transformer]]:提出 MocDT,一种基于 Decision Transformer 的离线 RL 推荐方法,把未来多目标作为控制信号,在推理阶段自回归生成对齐指定目标(累积评分与多样性)的物品序列,无需重训。
- [[2025-multiscale-contextual-bandits-long-term]]:提出 MultiScale Policy Learning 框架与 MSBL 算法,用分层 off-policy contextual bandit 在多个时间尺度上协调短期反馈与长期目标,让低尺度数据作为高尺度稀疏数据的 PAC-Bayes 先验。
- [[2025-xmtf-formula-free-multi-task-fusion]]:xMTF 用可学习的单调融合单元(MFC)替代多任务融合中的预定义公式,配合 RL 外层 + 监督内层的两阶段混合训练,离线 Total Watch Time 1279.7s 超越全部基线,线上 Daily Watch Time +0.833%,Kuaishou 全量部署服务超 1 亿用户。
- [[2025-tadt-csa-temporal-advantage-decision-transformer]]:面向工业生成式推荐的 Decision Transformer 改进框架,用 Temporal Advantage 信号和对比式状态抽象解决 DT 的轨迹拼接弱与状态空间过大问题。

## 相关

- [[reinforcement-learning]]
- [[recommender-systems]]
- [[sequential-recommendation]]
- [[markov-decision-process]]
- [[constrained-mdp]]
- [[rlur]]
- [[td3]]
- [[kuairand]]
- [[kuaishou]]
- [[decision-transformer]]
- [[multi-task-fusion]]
- [[contextual-bandits]]
