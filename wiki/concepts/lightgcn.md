---
type: concept
subtype: method
tags: [recommendation, graph-neural-network, collaborative-filtering]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# LightGCN

LightGCN 是一种用于推荐系统的轻量级图卷积网络:它去掉了传统 GCN 中的特征变换和非线性激活,仅保留邻域聚合,通过在用户-物品二部图上传播嵌入来学习协同过滤信号。

## 在本 wiki 中的出现

- [[2024-bankfair-fluctuating-traffic-reranking]]:BankFair 借鉴破产问题的 Talmud rule,把两侧推荐的曝光分配建模为序列化破产问题并用在线学习求解,在波动用户流量下同时保证短期用户准确性与长期提供方公平性。
- [[2024-robust-recommendation-decision-boundary-gcl]]:提出 RGCL:用决策边界感知的对抗扰动约束 graph contrastive learning 增强视图,平衡语义不变性与对比难度并最大化间隔,在 5 个数据集上一致超越 12 个 baseline(Kuaishou Recall@10 +14.14%)。
- [[2025-fine-grained-skip-micro-video-recommendation]]:将 micro-video 中的 skip 行为细分为 highly positive、less positive、negative 三类,用双层图与分层 BPR ranking loss 建模,在 MVA 与 KuaiRand-Pure 的八项指标上超越 FRAME/LightGT/BM3。
- [[2025-causality-constraint-debiasing-recommender]]:LCDR 用 identifiable VAE (iVAE) 作为因果约束去对齐标准 VAE 的潜在表征,即使 proxy variable 低质/有噪声也能恢复 latent confounder,从而缓解推荐系统中的潜在混杂偏差。

## 相关

- [[contrastive-learning]]
- [[graph-contrastive-learning]]
- [[collaborative-filtering]]
