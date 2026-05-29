---
type: concept
subtype: method
tags: [recommendation, graph-neural-network, collaborative-filtering]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# LightGCN

LightGCN 是一种用于推荐系统的轻量级图卷积网络:它去掉了传统 GCN 中的特征变换和非线性激活,仅保留邻域聚合,通过在用户-物品二部图上传播嵌入来学习协同过滤信号。

## 在本 wiki 中的出现

- [[2024-bankfair-fluctuating-traffic-reranking]]:BankFair 借鉴破产问题的 Talmud rule,把两侧推荐的曝光分配建模为序列化破产问题并用在线学习求解,在波动用户流量下同时保证短期用户准确性与长期提供方公平性。
- [[2024-robust-recommendation-decision-boundary-gcl]]:提出 RGCL:用决策边界感知的对抗扰动约束 graph contrastive learning 增强视图,平衡语义不变性与对比难度并最大化间隔,在 5 个数据集上一致超越 12 个 baseline(Kuaishou Recall@10 +14.14%)。

## 相关

- [[contrastive-learning]]
- [[graph-contrastive-learning]]
- [[collaborative-filtering]]
