---
type: concept
subtype: method
tags: [transfer-learning, pretraining, fine-tuning, domain-adaptation]
created: 2026-05-30
updated: 2026-05-30
sources: 8
---

# 迁移学习 (Transfer Learning)

迁移学习指把在**源任务/源域**学到的知识迁移到**目标任务/目标域**,以减少目标侧对数据与算力的需求。它是现代深度学习的范式基础——
"**预训练 + 微调**"正是迁移学习的主流形态。

## 主要形态
- **预训练-微调**:大规模自监督([[self-supervised-learning]])预训练学通用 [[representation-learning|表示]],再在下游小数据上 [[fine-tuning|微调]]
  ([[bert]]、[[gpt-3]] 的范式);参数高效微调 [[lora]] 等降低迁移成本。
- **域适应 (domain adaptation)**:源域有标签、目标域分布不同(常无标签),对齐表示以迁移。
- **多任务 / 多域**:[[multi-task-learning]]、[[multi-domain-recommendation]] 在共享与特化间权衡,防**负迁移 (negative transfer)**。
- **跨模态 / 跨场景**:[[clip]] 迁移图文表示;推荐里跨场景迁移用户兴趣([[2024-diit-domain-invariant-information-transfer]]、[[2025-cross-scenario-unified-user-interest-modeling-red-rec]])。

## 在本 wiki 的体现
- **LLM**:预训练→指令微调→对齐是层层迁移;[[in-context-learning|上下文学习]]是无需更新权重的"隐式迁移"。
- **推荐**:用 LLM 世界知识迁移到推荐([[2025-grasp-world-knowledge-sequential-recommendation]]、[[llm-for-recommendation]]);冷启动迁移([[2024-prompt-tuning-item-cold-start]])。

## 相关页
[[pretraining]]、[[fine-tuning]]、[[self-supervised-learning]]、[[representation-learning]]、[[multi-domain-recommendation]]、[[domain-adaptation]]
