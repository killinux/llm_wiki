---
type: entity
subtype: model
tags: [llm, qwen, alibaba, open-weight]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# Qwen2.5

Qwen2.5 是阿里巴巴推出的开放权重大语言模型系列,常被用作智能体与人类行为模拟等研究中的基座模型。

## 在本 wiki 中的出现

- [[2025-can-llm-agents-simulate-human-behavior]]:首个用真实在线购物数据做过程级、动作级定量评测的工作,发现 prompt-only LLM 模拟人类逐步行为的准确率仅约 11.86%,而在真人点击数据加合成 reasoning trace 上微调可显著提升。
- [[2026-tooltree-tool-planning]]:免训练的 MCTS 工具规划框架,用执行前/执行后双反馈引导搜索并双向剪枝,在固定预算下提升 LLM 智能体多工具规划的准确率与效率(GTA 66.95 AVG,ToolBench 69.04 AVG)。
- [[2026-self-evolving-multi-agent-rts]]:SEMA 用结构熵驱动观测剪枝 + 闭环自演化的 LLM 多智能体框架,在 StarCraft II 上实现高胜率与低延迟的实时策略决策。
- [[2026-tencent-advertising-algorithm-challenge-2025]]:腾讯广告算法大赛 2025 发布两个真实工业广告日志构建的大规模全模态生成式推荐数据集(TencentGR-1M/10M)、基线模型与含转化加权的评测协议。

## 相关

- [[llm-agents]]
- [[human-behavior-simulation]]
- [[tool-planning]]
- [[multi-agent-systems|multi-agent-system]]
- [[generative-recommendation]]
