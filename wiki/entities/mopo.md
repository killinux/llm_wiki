---
type: entity
subtype: model
tags: [model-based-offline-rl, offline-rl, pessimism, uncertainty-penalty]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# MOPO

MOPO(Model-based Offline Policy Optimization)是一种 model-based offline RL 方法,通过在学习到的环境模型奖励上施加基于模型不确定性的悲观惩罚来约束策略,避免在数据分布之外的区域过度乐观。

## 在本 wiki 中的出现

- 在 [[2023-dorl-matthew-effect-offline-rl-recommendation]] 中,MOPO 作为 model-based offline RL 中"悲观惩罚"思路的基础/参照:DORL 在这类悲观惩罚之上额外加入熵惩罚,以缓解交互式推荐中的马太效应并提升用户长期满意度。

## 相关

- [[2023-dorl-matthew-effect-offline-rl-recommendation]]
- [[model-based-offline-rl]]
- [[offline-rl]]
- [[pessimism]]
- [[matthew-effect]]
