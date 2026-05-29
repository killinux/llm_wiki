---
title: "User Simulator"
type: concept
subtype: method
tags: [user-simulator, llm, recommender-system, simulation, reinforcement-learning, evaluation]
created: 2026-05-29
updated: 2026-05-29
sources: 7
---

# 用户模拟器 (User Simulator)

用户模拟器是一种用程序化或 LLM 驱动的代理来模仿真实用户对系统(尤其是推荐系统)输出做出反应的方法,从而生成可复现、低成本、无风险的交互反馈(点击、评分、跳过、评论等),用于推荐策略的离线评估与强化学习训练。

## 概述

用户模拟器把"真实用户"替换为一个可控的反馈生成器:给定推荐结果,它产出与真实用户分布尽量接近的行为信号,构成一个可闭环交互的环境。早期工作多以 RL 为导向、用显式模型刻画用户行为;近年的工作转向 LLM 驱动,利用大模型的世界知识生成更细粒度、更拟真的反馈,并维护可随交互演化的动态用户画像。该方向的核心张力在于"拟真度(fidelity)"与"效率/可控性"之间的权衡,以及如何缩小模拟行为与真实行为之间的分布差距。

## 在本 wiki 中的出现

- 在 source 页 [[2024-llm-powered-user-simulator-for-recommender-system]] 中,作者把 LLM 限定在离线阶段做关键词蒸馏(显式、可解释的偏好逻辑),在线推断则用 逻辑+统计 集成模型,从而以低延迟、低幻觉为 RL-based 推荐系统提供训练奖励信号。
- 在 source 页 [[2024-lusifer-llm-user-simulation]] 中,Lusifer 构建 LLM 驱动的用户反馈环境,逐 batch 更新用户画像并给出可解释说明,生成动态评分反馈,支持 RL-based 推荐策略训练与 cold-start 评估。
- 在 source 页 [[2025-user-mirrorer-preference-aligned-user-simulator]] 中,User-Mirrorer 作为"偏好对齐(preference-aligned)"的用户模拟器,力图忠实复现真实用户面对推荐时的决策,缩小模拟与真实行为的分布差距,以支撑更可靠的离线评估。
- 在 source 页 [[2025-simuser-llm-user-simulation-recsys]] 中,SimUser 作为 LLM-based 用户模拟框架,生成点击/评分/跳过等细粒度交互信号,用于推荐策略的离线评估与训练,捕捉超越二元反馈的细微用户反应。
- 在 source 页 [[2026-ab-agent-recsys-evaluation]] 中,A/B Agent 是一个多模态 LLM 用户智能体,在仿真沙盒 UI 中模拟多页感知、疲劳驱动退出等行为,以替代代价高昂的在线 A/B testing 来评估推荐模型。
- 在 source 页 [[2025-recoworld-simulated-environments-agentic-recsys]] 中,RecoWorld 用"用户模拟器 + agentic 推荐器"的双视角架构,让 LLM 模拟用户在多轮交互中更新 mindset 并生成反思式指令,作为面向 agentic 推荐器的强化学习训练环境。
- 在 source 页 [[2023-kuaisim-recommender-simulator]] 中,KuaiSim 是较早的、非 LLM、面向 RL 的综合性推荐系统模拟器,提供 multi-behavior、cross-session 反馈与 retention 优化,代表了从显式行为建模向 LLM 驱动演进之前的范式。

## 相关

- [[user-simulation]] —— 与本概念紧密关联的上位/同义概念。
- [[lusifer]]、[[kuaisim]] —— 本 wiki 中具体的用户模拟器实体。
- [[interactive-evaluation]] —— 用户模拟器是实现交互式评估的关键手段。
- [[benchmark]] —— 模拟器常作为可复现评测基准的基础。
- [[counterfactual-augmentation]]、[[system-exposure]] —— 与离线模拟评估中纠偏、曝光建模相关的概念。
