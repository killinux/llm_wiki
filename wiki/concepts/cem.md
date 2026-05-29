---
type: concept
subtype: method
tags: [optimization, sampling, reinforcement-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Cross-Entropy Method

交叉熵方法(Cross-Entropy Method, CEM)是一种基于重要性采样的迭代优化算法:通过反复采样、筛选精英样本、并最小化采样分布与精英分布之间的交叉熵来更新分布参数,从而逼近最优解,常用于稀有事件估计与黑盒/组合优化。

## 在本 wiki 中的出现

- [[2025-xmtf-formula-free-multi-task-fusion]]:xMTF 用可学习的单调融合单元(MFC)替代多任务融合中的预定义公式,配合 RL 外层 + 监督内层的两阶段混合训练,离线 Total Watch Time 1279.7s 超越全部基线,线上 Daily Watch Time +0.833%,Kuaishou 全量部署服务超 1 亿用户。

## 相关

- [[reinforcement-learning]]
- [[importance-sampling]]
- [[black-box-optimization]]
- [[multi-task-fusion]]
