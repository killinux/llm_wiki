---
type: concept
subtype: method
tags: [llm-agents, embodied-ai, robotics, planning, grounding]
created: 2026-05-30
updated: 2026-05-30
sources: 7
---

# 具身智能体 (Embodied Agent)

具身智能体指在**物理或仿真的具身环境**(机器人、游戏世界、自动驾驶)中**感知-行动**的智能体,需把语言/推理**扎根 (grounding)**
到可执行动作与真实反馈上,区别于纯文本的"无身"对话 agent。LLM 为其提供高层规划与常识,但需解决感知接口与动作可行性。

## 关键问题
- **接地 (grounding)**:把 LLM 的语言计划映射到环境可执行的低层动作,并接收真实反馈闭环——[[2022-inner-monologue]] 用环境反馈做闭环规划。
- **长程规划与技能学习**:[[voyager]] 在 Minecraft 中自主探索、积累技能库;[[2024-project-sid-minecraft-civilization]] 把具身多 agent 推到文明尺度。
- **多模态感知**:视觉/传感融合,如自动驾驶 [[2023-drivemlm-autonomous-driving]] 把多模态 LLM 决策对齐行为规划。
- **城市/真实空间**:[[2024-opencity-urban-llm-agents]]、[[2025-agentsociety-large-scale-social-simulation]] 让 agent 在真实城市空间移动与交互。

## 与相邻概念
是 [[llm-agents]] "任务求解"与"社会模拟"两分支在**物理世界**的交集;依赖 [[llm-planning|规划]]、[[tool-use|工具使用]]、[[world-model|世界模型]];
评测见 [[webshop]]、具身基准与 [[agent-evaluation]]。

## 相关页
[[llm-agents]]、[[voyager]]、[[2022-inner-monologue]]、[[world-model]]、[[grounding]]、[[robotics]]
