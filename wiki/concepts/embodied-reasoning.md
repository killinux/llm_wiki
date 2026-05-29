---
type: concept
subtype: method
tags: [embodied-reasoning, robotics, llm, closed-loop, replanning, grounding]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Embodied Reasoning

Embodied Reasoning 指智能体(通常是机器人)在与真实物理环境的交互循环中进行推理:它把环境反馈纳入推理过程,据此规划、执行并在失败时重新规划,从而让语言模型的推理"落地"到具体的身体与场景之中。

## 在本 wiki 中的出现

- [[2022-inner-monologue]]:把持续注入的自然语言环境反馈(如成功检测、场景描述、人类指令)喂给一个 frozen LLM,使其形成"内心独白"(inner monologue)。借助这种闭环反馈,LLM 无需额外训练即可对机器人任务进行 grounded 的具身推理,实现失败后的可重规划与闭环控制,是 Embodied Reasoning 的一种具体实现方式。
- [[2025-drivemlm-autonomous-driving]]:DriveMLM 将 multi-modal LLM 对齐到自动驾驶行为规划模块的离散决策状态,使语言输出可转为车辆控制,在 CARLA Town05 Long 上实现闭环驾驶并取得 DS 76.1、MPI 0.96。
- [[2023-drivemlm-autonomous-driving]]:DriveMLM 通过将多模态 LLM 的语言决策与模块化 AD 系统的行为规划状态对齐,在 CARLA 仿真器实现闭环自动驾驶,Town05 Long 上 DS 达 76.1,优于 Apollo 4.7 点。

## 相关

- [[react]]:同样交错"推理"与"行动",在与环境交互中迭代决策,与 Embodied Reasoning 的闭环思路相通。
- [[chain-of-thought]]:为推理提供中间步骤的表达形式,内心独白可视为其在具身、闭环设定下的延伸。
- [[grounding]]:将语言与物理世界中的感知、状态对应起来,是 Embodied Reasoning 得以落地的前提。
- [[closed-loop-control]]:依据反馈不断调整行为的控制范式,是 Embodied Reasoning 的执行骨架。
- [[task-planning]]:把高层目标分解为可执行步骤,Embodied Reasoning 在其中加入反馈驱动的重规划。
