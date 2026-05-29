---
type: entity
subtype: model
tags: [llm, reasoning-model, deepseek, open-weights]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# DeepSeek-R1

DeepSeek-R1 是 DeepSeek 推出的开放权重推理大语言模型,通过强化学习强化链式推理(reasoning)能力,常被用作 agent 与行为模拟研究中的基线或推理后端。

## 在本 wiki 中的出现

- [[2025-can-llm-agents-simulate-human-behavior]]:首个用真实在线购物数据做过程级、动作级定量评测的工作,发现 prompt-only LLM 模拟人类逐步行为的准确率仅约 11.86%,而在真人点击数据加合成 reasoning trace 上微调可显著提升。
- [[2025-llm-driven-cross-platform-npc]]:一个原型系统,让 LLM 驱动的游戏 NPC 通过云数据库在 Unity 游戏内与 Discord 社交平台间跨平台对话并同步记忆。
- [[2025-agent-safety-alignment-via-reinforcement-learning]]:首个面向 tool-using agent 的统一安全对齐框架,通过 structured reasoning + sandbox 强化学习,用 benign/malicious/sensitive 三模态分类与 execute-refuse-verify 策略同时抵御用户侧与工具侧威胁。

## 相关

- [[deepseek]]
- [[reasoning-model]]
- [[reinforcement-learning]]
- [[tool-using-agent]]
- [[human-behavior-simulation]]
