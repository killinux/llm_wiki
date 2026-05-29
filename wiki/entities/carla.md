---
type: entity
subtype: benchmark
tags: [autonomous-driving, simulator, closed-loop, benchmark]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# CARLA

CARLA 是一个开源的自动驾驶仿真平台,提供城市道路、车辆、传感器等环境,常用于自动驾驶模型的闭环(closed-loop)驾驶评测。

## 在本 wiki 中的出现

- [[2025-drivemlm-autonomous-driving]]:DriveMLM 将 multi-modal LLM 对齐到自动驾驶行为规划模块的离散决策状态,使语言输出可转为车辆控制,在 CARLA Town05 Long 上实现闭环驾驶并取得 DS 76.1、MPI 0.96。
- [[2025-llm-multi-agent-autonomous-driving-survey]]:系统综述 LLM 驱动的多智能体自动驾驶系统,按智能体交互模式与结构分类已有方法,并梳理 agent-human 交互、应用、数据集与未来方向。

## 相关

- [[carla-town05-long]]
- [[2025-drivemlm-autonomous-driving]]
- [[multimodal-llm|multi-modal-llm]]
