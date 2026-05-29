---
type: concept
subtype: method
tags: [human-behavior-simulation, llm-agents, behavioral-modeling, evaluation]
created: 2026-05-29
updated: 2026-05-29
sources: 6
---

# 人类行为模拟

人类行为模拟指利用模型(尤其是大语言模型及智能体)在给定情境下复现真实人类的决策、动作与推理过程,以逼近人类逐步行为的方法。

## 在本 wiki 中的出现

- [[2025-can-llm-agents-simulate-human-behavior]]:首个用真实在线购物数据做过程级、动作级定量评测的工作,发现 prompt-only LLM 模拟人类逐步行为的准确率仅约 11.86%,而在真人点击数据加合成 reasoning trace 上微调可显著提升。
- [[2025-generative-mmo-simulation]]:用 LLM 驱动的生成式多智能体 MMO 游戏仿真系统:在真实玩家数据上 SFT+GRPO 微调 agent,高保真模拟玩家决策,低成本评估数值系统与机制设计的干预效果。
- [[2025-multi-agent-llm-value-diversity]]:通过 Schwartz 价值观给 LLM 智能体注入价值多样性的多智能体社会模拟,发现价值多样性提升集体行为的价值稳定性、涌现与自发规则创造,但极端异质带来边际递减与不稳定。
- [[2026-yerkes-dodson-curve-ai-agents]]:在网格世界生存竞技场中系统改变环境压力,首次实证发现 LLM 多智能体系统的合作行为遵循 Yerkes-Dodson 倒 U 形曲线——中等压力(upkeep=5)合作交易峰值达 29 次,过低或过高压力都抑制社会行为,且性选择压力可在不致死的前提下消除攻击。
- [[2026-policysim-proactive-policy-optimization]]:PolicySim 是一个基于 LLM 智能体的社会模拟沙盒,用 SFT+DPO 训练用户智能体、用带消息传递的 contextual bandit 自适应优化推荐与曝光控制等平台干预策略,实现部署前的主动评估与优化。
- [[2026-omnibehavior]]:OmniBehavior 是首个完全基于真实工业日志(快手)构建的用户模拟基准,刻画长时程、跨场景、异质行为轨迹,并揭示当前 LLM 模拟器存在"积极且趋均值"的结构性偏差。

## 相关

- [[llm-agents]]
- [[behavioral-evaluation]]
- [[reasoning-trace]]
- [[fine-tuning]]
