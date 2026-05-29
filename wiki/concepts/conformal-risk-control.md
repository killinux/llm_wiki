---
type: concept
subtype: method
tags: [conformal-prediction, risk-control, distribution-free, uncertainty-quantification, statistical-guarantees]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Conformal Risk Control

一种 distribution-free 的统计框架,通过校准在分布无关假设下为某个可监控的风险(损失)期望提供可证明的上界,是 conformal prediction 在一般化风险控制场景下的推广。

## 在本 wiki 中的出现

- [[2025-mitigating-unwanted-recommendations-conformal-risk-control]]:一个 post-hoc、模型无关、distribution-free 的方法,用 conformal risk control 给推荐中"不想要内容"的比例提供可证明上界,并以用户曾看过的安全重复内容替换有害项以保住推荐质量。
- [[2026-collective-manipulation-risk-controlling-recsys]]:审计基于 conformal risk control 与二元 Not Interested 负反馈的推荐系统,证明仅 1% 协同对抗用户即可让非对抗用户 nDCG 最多降 20%,并提出个体级阈值校准作为缓解。

## 相关

- [[conformal-prediction]]
- [[distribution-free-uncertainty-quantification]]
- [[recommender-systems]]
