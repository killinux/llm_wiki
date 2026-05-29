---
type: entity
subtype: lab
tags: [university, china, llm-agents, nlp, recommendation, autonomous-driving]
created: 2026-05-29
updated: 2026-05-29
sources: 17
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
- [[2024-optima-optimizing-llm-multi-agent]]:OPTIMA 通过生成-排序-选择-训练的迭代范式同时优化 LLM 多智能体系统的通信效率与任务有效性,在重信息交换任务上达成 2.8x 性能提升且 token 用量不到 10%。
- [[2024-recflow-full-flow-recommendation-dataset]]:首个包含工业推荐系统多级漏斗各阶段未曝光样本的大规模全流程数据集,用于研究分布偏移、选择偏差与多阶段联合优化。
- [[2024-opencity-urban-llm-agents]]:通过 LLM 请求调度器与 group-and-distill 提示优化,把万级城市 LLM agent 模拟加速约 600 倍,使 10000 agent 的一天活动可在 1 小时内于普通硬件完成。
- [[2025-agentsociety-large-scale-social-simulation]]:一个整合 LLM 生成式社会 agent、真实城市-社会-经济环境与大规模分布式仿真引擎的社会模拟器,支持上万 agent 并复现极化、谣言、UBI、飓风、城市可持续性五类真实社会实验。
- [[2025-segment-level-user-interest-modeling]]:把短视频拆成时间片段,用混合表示+多模态用户-视频编码器+片段兴趣解码器建模用户沿时间线动态演变的片段级兴趣,用于 video-skip 预测与推荐。
- [[2025-ai-agent-behavioral-science]]:立场/综述论文,提出 AI Agent Behavioral Science 范式:把 LLM agent 当作行为实体,通过系统观察、干预与理论解释来研究其在个体、多 agent、人-agent 交互三类场景下的行为、适应与 responsible AI。
- [[2025-perscen-multi-scenario-matching]]:首个将用户个性化建模引入多场景匹配(召回)的两塔方法,用 user-specific 特征图+轻量 GNN、向量量化的场景偏好与渐进式 GLU,在 KuaiRand-Pure 与 Alimama 上以高效率刷新召回性能。

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
- [[llm-multi-agent-systems]]
- [[social-simulation]]
- [[urban-llm-agents]]
- [[ai-agent-behavioral-science]]
