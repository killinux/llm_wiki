---
type: entity
subtype: model
tags: [llm, deepseek, foundation-model, agent, social-simulation]
created: 2026-05-29
updated: 2026-05-29
sources: 7
---

# DeepSeek-V3

DeepSeek-V3 是深度求索(DeepSeek)推出的大规模混合专家(MoE)语言模型,常被本 wiki 收录的研究用作驱动生成式 agent、推理时搜索与社会模拟的基础模型。

## 在本 wiki 中的出现

- [[2025-agentsociety-large-scale-social-simulation]]:一个整合 LLM 生成式社会 agent、真实城市-社会-经济环境与大规模分布式仿真引擎的社会模拟器,支持上万 agent 并复现极化、谣言、UBI、飓风、城市可持续性五类真实社会实验。
- [[2025-ab-mcts-adaptive-branching-tree-search]]:提出 AB-MCTS:在推理时树搜索中用 Thompson sampling 自适应决定"向宽采样新候选"还是"向深用外部反馈细化已有答案",统一 repeated sampling 与多轮 refinement,实现更高效的 test-time scaling。
- [[2025-socioverse-world-model-social-simulation]]:SocioVerse 是一个由 LLM agents 驱动、依托 1000 万真实用户池与四个对齐模块的社会模拟 world model,在政治、新闻、经济三大领域复现大规模人群行为。
- [[2025-generative-mmo-simulation]]:用 LLM 驱动的生成式多智能体 MMO 游戏仿真系统,在真实玩家数据上 SFT+GRPO 微调 agent,高保真模拟玩家决策,低成本评估数值系统与机制设计的干预效果。
- [[2026-trirec-tri-party-agent-recommendation]]:TriRec 是首个用户—物品—平台 tri-party LLM-agent 推荐框架,让物品 agent 主动个性化自我推销,再由平台做曝光感知的多目标重排,在精度、公平与物品效用上同时提升。
- [[2026-self-organizing-llm-agents]]:一项 25,000 任务的大规模实验发现"内生性悖论":固定智能体顺序但角色自主的混合协议(Sequential)在质量上同时超越中心化(+14%)与完全自主(+44%)协调,但仅当底层模型足够强(存在能力门槛)。
- [[2026-omnibehavior]]:OmniBehavior 是首个完全基于真实工业日志(快手)构建的用户模拟基准,刻画长时程、跨场景、异质行为轨迹,并揭示当前 LLM 模拟器存在"积极且趋均值"的结构性偏差。

## 相关

- [[deepseek]]
- [[mixture-of-experts]]
- [[llm-agents|llm-agent]]
- [[test-time-scaling]]
- [[social-simulation]]
- [[user-simulation]]
