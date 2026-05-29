---
type: entity
subtype: model
tags: [llm, qwen, instruct, agent, alignment, recommendation, simulation]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# Qwen2.5-Instruct

Qwen2.5-Instruct 是阿里巴巴 Qwen 系列的指令微调大语言模型,常被用作 tool-using agent 与安全对齐研究的基座模型。

## 在本 wiki 中的出现

- [[2025-agent-safety-alignment-via-reinforcement-learning]]:首个面向 tool-using agent 的统一安全对齐框架,通过 structured reasoning + sandbox 强化学习,用 benign/malicious/sensitive 三模态分类与 execute-refuse-verify 策略同时抵御用户侧与工具侧威胁。
- [[2025-grasp-world-knowledge-sequential-recommendation]]:GRASP 用"生成增强检索 + Sigmoid 整体注意力增强"把 LLM 世界知识作为辅助输入(而非监督信号)注入序列推荐,抵抗 LLM 幻觉噪声,在 Beauty/Fashion/Industry-100K 上叠加多种 backbone 均达 SOTA,并通过线上 A/B 验证 GMV +1.71%。
- [[2025-generative-mmo-simulation]]:用 LLM 驱动的生成式多智能体 MMO 游戏仿真系统:在真实玩家数据上 SFT+GRPO 微调 agent,高保真模拟玩家决策,低成本评估数值系统与机制设计的干预效果。
- [[2026-policysim-proactive-policy-optimization]]:PolicySim 是一个基于 LLM 智能体的社会模拟沙盒,用 SFT+DPO 训练用户智能体、用带消息传递的 contextual bandit 自适应优化推荐与曝光控制等平台干预策略,实现部署前的主动评估与优化。

## 相关

- [[reinforcement-learning]]
- [[agent-safety-alignment]]
- [[tool-using-agent]]
- [[qwen]]
- [[sequential-recommendation]]
- [[social-simulation]]
