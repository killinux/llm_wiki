---
type: concept
subtype: method
tags: [recommender-system, personalization, user-modeling, llm]
created: 2026-05-30
updated: 2026-05-30
sources: 8
---

# 个性化 (Personalization)

个性化指系统根据**个体用户的历史、画像与情境**定制输出(推荐、排序、生成),而非千人一面。它是推荐系统的根本目标,
近年也扩展到 LLM 的个性化对齐与角色扮演。

## 推荐中的个性化
- **用户表示**:从 ID [[embedding]] 到行为序列建模([[gru4rec]]、[[bert4rec]]、[[din|DIN]] 兴趣建模),刻画动态兴趣。
- **多场景/多域**:同一用户在不同场景偏好不同,需跨场景统一建模([[2025-cross-scenario-unified-user-interest-modeling-red-rec]]、[[2025-perscen-multi-scenario-matching]])。
- **长期 vs 短期兴趣**:生命周期/时序建模([[2025-deep-interest-life-cycle-network]]、[[2024-recmamba-lifelong-sequential-recommendation]])。

## LLM 时代的个性化
- **个性化生成/对齐**:按用户偏好定制回答;persona 驱动([[persona]]、[[2025-opencharacter-role-playing-synthetic-personas]])。
- **个性化用户模拟**:用 LLM 模拟特定用户的逐步行为([[2025-user-mirrorer-preference-aligned-user-simulator]]、[[2025-pub-personality-user-behaviour-simulator]]),
  与 [[generative-social-simulation]] 的"个体高保真"目标相通([[2024-generative-agents-self-reports]])。

## 张力
个性化 vs 公平/多样性/信息茧房:过度个性化加剧极化与回声室,需与 [[item-side-fairness]]、探索([[exploration-exploitation]])平衡。

## 相关页
[[recommender-systems]]、[[user-modeling]]、[[embedding]]、[[user-simulation]]、[[llm-for-recommendation]]
