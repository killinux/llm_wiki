---
type: concept
subtype: method
tags: [LLM, planning, reasoning, embodied-AI, robotics, closed-loop]
created: 2026-05-29
updated: 2026-05-29
sources: 8
---

# LLM Planning

LLM Planning 指利用大语言模型(LLM)将高层目标分解为可执行的步骤序列,并据此规划与调整行动的方法。

## 在本 wiki 中的出现

- [[2022-inner-monologue]]:把 LLM Planning 置于闭环之中。该工作通过持续向 frozen LLM 注入自然语言形式的环境反馈,让模型形成"内心独白"(inner monologue),从而在执行过程中对具身(embodied)任务进行闭环、可重规划(replanning)的推理。LLM Planning 在此扮演"根据最新反馈不断重写后续步骤"的核心角色。
- [[2025-drivemlm-autonomous-driving]]:DriveMLM 将 multi-modal LLM 对齐到自动驾驶行为规划模块的离散决策状态,使语言输出可转为车辆控制,在 CARLA Town05 Long 上实现闭环驾驶并取得 DS 76.1、MPI 0.96。
- [[2023-recommender-ai-agent-interec]]:提出 InteRecAgent,以 LLM 为大脑、传统推荐模型为工具,通过候选总线记忆、plan-first 执行与 actor-critic 反思构建交互式对话推荐 agent,并蒸馏出 7B 的 RecLlama。
- [[2024-llm-learnable-planners-long-term-recommendation]]:提出 BiLLP 双层可学习 LLM 规划框架(Planner/Reflector 宏观 + Actor/Critic 微观),在稀疏推荐数据上以 LLM 规划能力做长期推荐,Len 与累积奖励超越从零训练的 RL 与现有 LLM agent 基线。
- [[2024-reflection-on-search-trees]]:RoT 让 strong LLM 反思 weak LLM 的历史树搜索经验、对关键状态总结出任务级 guideline 注入后续 prompt,显著提升 BFS/MCTS 等树搜索 prompting 在 Blocksworld、GSM8k、议价任务上的准确率与搜索效率,且任务越难收益越大。
- [[2024-hiagent-hierarchical-working-memory]]:HiAgent 用 subgoal 作为 memory chunk 分层管理 LLM agent 的 working memory(汇总过去 observation、按需检索明细轨迹),在五个长程任务上成功率约翻倍(21→42)、context 减少 35%。
- [[2024-megaagent-large-scale-mas-without-sop]]:借鉴操作系统进程/线程模型、无需预定义 SOP、可自动生成数百 agent 并行协作的大规模 LLM 多智能体系统,800 秒内开发五子棋、2991 秒协调 590 个 agent 生成国家政策。
- [[2026-tooltree-tool-planning]]:免训练的 MCTS 工具规划框架,用执行前/执行后双反馈引导搜索并双向剪枝,在固定预算下提升 LLM 智能体多工具规划的准确率与效率(GTA 66.95 AVG,ToolBench 69.04 AVG)。

## 相关

- [[inner-monologue]]
- [[embodied-reasoning]]
- [[closed-loop-control]]
- [[replanning]]
- [[task-decomposition]]
- [[grounding]]
- [[frozen-llm]]
- [[chain-of-thought]]
- [[llm-agents|llm-agent]]
- [[hierarchical-planning]]
- [[tree-search]]
- [[reflection]]
- [[working-memory]]
- [[multi-agent-systems]]
- [[tool-planning]]
- [[mcts]]
- [[tool-use]]
