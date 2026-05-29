---
type: entity
subtype: lab
tags: [university, china, llm-agents, nlp, recommendation, autonomous-driving]
created: 2026-05-29
updated: 2026-05-29
sources: 10
---

# Tsinghua University

Tsinghua University 是位于中国北京的研究型大学,在本 wiki 中作为多项 LLM Agent、推荐系统与自动驾驶研究的研究机构出现。

## 在本 wiki 中的出现

- [[2023-multi-agent-debate]]:作为研究机构,参与提出 Multi-Agent Debate(MAD)框架,用多个 LLM 智能体"针锋相对"辩论并由裁判仲裁,缓解自我反思的 Degeneration-of-Thought 问题、激发发散性思维。
- [[2023-agentbench]]:作为研究机构,参与构建 AgentBench——首个系统评估 LLM-as-Agent 能力的多维基准,横跨 8 个交互环境测评 29 个模型,揭示商业与开源模型的巨大差距。
- [[2023-expel]]:作为研究机构,参与提出 ExpeL——让 LLM Agent 不更新参数,从跨任务经验中自主抽取自然语言洞见并召回相似成功轨迹来提升决策表现。
- [[2025-drivemlm-autonomous-driving]]:DriveMLM 将 multi-modal LLM 对齐到自动驾驶行为规划模块的离散决策状态,使语言输出可转为车辆控制,在 CARLA Town05 Long 上实现闭环驾驶并取得 DS 76.1、MPI 0.96。
- [[2023-agenttuning]]:通过构建跨任务 agent 交互轨迹数据集 AgentInstruct 并与通用指令混合微调,使开源 Llama 2 获得可泛化的 agent 能力且不损害通用能力。
- [[2023-drivemlm-autonomous-driving]]:DriveMLM 通过将多模态 LLM 的语言决策与模块化 AD 系统的行为规划状态对齐,在 CARLA 仿真器实现闭环自动驾驶,Town05 Long 上 DS 达 76.1,优于 Apollo 4.7 点。
- [[2024-macrec-multi-agent-recommendation]]:清华提出的多 agent 协作推荐框架(SIGIR'24 demo),用 Manager、Analyst、Reflector、Searcher、Task Interpreter 等角色各异的 LLM agent 直接协作完成评分预测、序列推荐、解释生成与对话推荐。
- [[2024-situation-aware-recommender-enhancer]]:提出 SARE，一个把情境视为交互前置条件的可插拔模块，以个性化方式建模情境对用户-物品偏好的动态影响，可嵌入各类推荐系统 backbone 并显著提升性能。
- [[2024-eeg-svrec-eeg-affective-engagement-dataset]]:首个在真实短视频观看场景下采集 EEG 脑电信号并配以六维情感参与度标注(MAES)与行为日志的推荐数据集,benchmark 显示加入 EEG 特征可提升推荐 AUC。
- [[2024-crocodile-cross-experts-covariance]]:Crocodile 用多嵌入架构 + cross-experts covariance loss(CovLoss)解耦各 expert 表示,并以 Prior Informed Element-wise Gating(PEG)路由,平衡多域推荐中"保持域差异性"与"充分学习参数"的两难,公开数据集与 Tencent 线上 A/B 均取得提升。

## 相关

- [[llm-agent]]
- [[multi-agent-debate]]
- [[agentbench]]
- [[expel]]
- [[self-reflection]]
- [[benchmark]]
- [[agenttuning]]
- [[drivemlm]]
- [[macrec]]
- [[multi-agent-recommendation]]
- [[autonomous-driving]]
- [[recommendation-systems]]
