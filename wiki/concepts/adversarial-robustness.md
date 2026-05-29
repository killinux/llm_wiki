---
type: concept
subtype: method
tags: [adversarial-robustness, contrastive-learning, recommendation, perturbation, machine-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# Adversarial Robustness

Adversarial Robustness 指模型在面对刻意构造的对抗扰动输入时仍能保持稳定、正确表现的能力。

## 在本 wiki 中的出现

- [[2024-robust-recommendation-decision-boundary-gcl]]:提出 RGCL,用决策边界感知的对抗扰动约束 graph contrastive learning 增强视图,平衡语义不变性与对比难度并最大化间隔,在 5 个数据集上一致超越 12 个 baseline(Kuaishou Recall@10 +14.14%)。
- [[2024-diit-domain-invariant-information-transfer]]:DIIT 通过 gating 域级聚合 + 对抗表示对齐双抽取器和 multi-spot 知识蒸馏迁移器,把多个 source domain 模型的 domain-invariant 信息注入 target domain 模型,实现推理只需 target 模型的高效工业跨域推荐。其中对抗表示对齐用于学习对域偏移鲁棒的表示。
- [[2025-llm-agent-evaluation-survey]]:SAP Labs 的 LLM agent 评测综述,提出"评测目标 × 评测过程"二维分类法,并强调企业落地中的可靠性、合规与 RBAC 等挑战,可靠性与对抗鲁棒性密切相关。
- [[2026-collective-manipulation-risk-controlling-recsys]]:审计基于 conformal risk control 与二元 Not Interested 负反馈的推荐系统,证明仅 1% 协同对抗用户即可让非对抗用户 nDCG 最多降 20%,并提出个体级阈值校准作为缓解。

## 相关

- [[graph-contrastive-learning]]
- [[recommender-systems|recommendation-systems]]
- [[adversarial-perturbation]]
- [[decision-boundary]]
- [[domain-invariant-representation]]
- [[representation-alignment]]
- [[llm-agent-evaluation]]
- [[conformal-risk-control]]
- [[collective-manipulation]]
