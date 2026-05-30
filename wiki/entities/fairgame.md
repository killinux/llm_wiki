---
type: entity
subtype: framework
tags: [llm-agents, game-theory, evaluation, social-dilemma, auditing]
created: 2026-05-30
updated: 2026-05-30
---

# FairGame

FairGame 是一个用**博弈论**框架**审计 LLM 智能体**策略行为的评测框架。本页内容据本 wiki 已收录的引用工作
[[2025-llm-agent-game-theory-strategy-recognition]] 整理(该文在 FairGame 基础上扩展),**FairGame 原文尚未单独 ingest**(细节待补)。

## 据引用工作所述的特征
- **博弈设定**:聚焦**对称的两人矩阵博弈 (2×2 static matrix games)**、**同质玩家 (homogeneous players)**;
- **结果度量**:用简单的聚合指标(如**平均合作率**)刻画 LLM agent 的行为倾向;
- **用途**:系统化地审计不同 LLM 在经典社会困境([[game-theory|博弈论]])下的策略与合作偏差。

## 被扩展的方向
[[2025-llm-agent-game-theory-strategy-recognition]] 指出 FairGame 的两点局限并加以扩展:(i) 即使博弈结构固定,LLM agent 对**收益绝对量级 (stakes)**
的敏感性;(ii) 多玩家共享公共物品、可能出现**联盟与协调**的群体环境——把 FairGame 的 2×2 静态矩阵替换为**动态公共物品**收益模块,
并叠加机器学习**意图识别**流水线。

## 在本 wiki 中的位置
属于 [[generative-social-simulation]] 的**博弈/社会困境评测**子线,与 [[2025-llm-agents-cooperate-social-dilemma]]、
[[2025-emergent-coordination-multi-agent-language-models]]、[[game-theory]]、[[agent-evaluation]] 相关。
> 待办:获取 FairGame 原文后补 ingest 为正式 source 页并校正细节。
