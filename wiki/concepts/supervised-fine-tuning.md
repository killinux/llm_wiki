---
type: concept
subtype: method
tags: [fine-tuning, sft, alignment, training]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Supervised Fine-Tuning

监督微调(SFT）是指在带标注的指令-响应对数据上对预训练大模型继续训练,使其学会按期望的格式与行为产生输出的对齐方法。

## 在本 wiki 中的出现

- [[2025-opencharacter-role-playing-synthetic-personas]]:用 Persona Hub 大规模合成 persona 造角色对齐 SFT 数据,微调 LLaMA-3 8B 获得 out-of-domain 角色泛化能力,在 PersonaGym 上比肩 GPT-4o。
- [[2026-convapparel-user-simulator-validation]]:Google 提出 ConvApparel(4,146 段人-AI 服装购物对话、双 agent good/bad 协议、逐轮第一人称标注)及 PLSA+HLS+counterfactual validation 三支柱框架,系统量化 LLM user simulator 的 realism gap,发现所有 simulator 平均 HLS 仅 0.004,但 ICL/SFT 在反事实泛化上优于纯 prompting。
- [[2026-policysim-proactive-policy-optimization]]:PolicySim 是一个基于 LLM 智能体的社会模拟沙盒,用 SFT+DPO 训练用户智能体、用带消息传递的 contextual bandit 自适应优化推荐与曝光控制等平台干预策略,实现部署前的主动评估与优化。

## 相关

- [[synthetic-data]]
- [[instruction-tuning]]
- [[role-playing]]
- [[llama-3]]
- [[direct-preference-optimization|dpo]]
- [[in-context-learning]]
- [[llm-user-simulator]]
