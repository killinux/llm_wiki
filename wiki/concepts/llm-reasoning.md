---
type: concept
subtype: method
tags: [llm-reasoning, reasoning, chain-of-thought, planning, search, self-correction, llm]
created: 2026-05-29
updated: 2026-05-29
sources: 6
---

# 大语言模型推理 (LLM Reasoning)

LLM Reasoning 指让大语言模型在给出最终答案之前,显式或隐式地生成一系列中间推理步骤,以解决数学、逻辑、常识、规划与代码等需要多步思考的问题的一类方法与研究方向。

## 概述

LLM Reasoning 是围绕"如何让 LLM 更好地多步思考"的统称,而非单一算法。它涵盖从最基础的 [[chain-of-thought|思维链]] 逐步生成,到把推理建模为状态空间搜索/规划([[tree-of-thoughts]]、[[2023-reasoning-via-planning-rap]]),再到推理与外部行动交错([[react]])以及推理过程中的自我纠错([[self-correction]])等多条技术脉络。这些方法的共同点是把"答案"展开为"推理轨迹(reasoning trace)",从而可以对中间步骤进行搜索、验证、聚合或修正。本 wiki 把它作为连接搜索、规划、智能体与强化学习等方向的枢纽概念。

## 在本 wiki 中的出现

- [[2023-reasoning-via-planning-rap]]:RAP 把 LLM 同时当作"推理智能体"和"世界模型",用 [[monte-carlo-tree-search|MCTS]] 在推理树上做带奖励的规划,把 LLM 推理重新表述为"带 [[world-model|世界模型]] 的规划"问题,是搜索/规划一脉的代表性推理增强方法。
- [[react]] / [[2022-react-reasoning-and-acting]]:ReAct 让 LLM 交替生成推理痕迹("思考")与任务相关行动,使推理用于归纳、跟踪和更新计划并处理异常,行动用于与外部源交互获取信息,从而缓解纯推理(CoT)的幻觉与错误传播——把 LLM 推理扩展到 [[llm-agents|智能体]] 场景。
- [[2023-llms-cannot-self-correct-reasoning-yet]]:从批判视角考察 LLM 在推理任务上的"内在自我纠错"能力,指出在缺乏外部反馈时模型往往难以可靠地修正自己的推理,提醒该方向不要高估自纠错。
- [[2024-when-can-llms-correct-mistakes]]:进一步分析 LLM 在何种条件下能纠正推理中的错误,刻画自我纠错对 LLM 推理质量的影响边界。
- [[2024-rethinkmcts]]:在 LLM 推理/代码场景中结合 MCTS 式树搜索与对推理步骤的"再思考"机制,属于把搜索与反思引入推理过程的工作。
- [[2025-multi-agent-evolve]]:在多智能体协作/演化框架下使用并提升 LLM 的推理能力,把推理置于多智能体交互的语境中。

此外,概念页 [[reinforcement-learning]]、[[self-refine]]、[[reflection-on-search-trees]] 也将本概念作为相关方向引用,体现 LLM 推理与强化学习、自我精炼、搜索树反思之间的交叉。

## 相关

- [[chain-of-thought]]
- [[tree-of-thoughts]]
- [[monte-carlo-tree-search]]
- [[tree-search]]
- [[world-model]]
- [[react]]
- [[llm-agents]]
- [[self-correction]]
- [[self-refine]]
- [[reflection-on-search-trees]]
- [[reinforcement-learning]]
