---
type: source
subtype: paper
tags:
  - autonomous-driving
  - llm-multi-agent
  - survey
  - agent-human-interaction
  - cooperative-driving
created: 2026-05-29
updated: 2026-05-29
arxiv: 2502.16804
raw: raw/2502.16804.pdf
authors:
  - Yaozu Wu
  - Dongyuan Li
  - Yankai Chen
  - Renhe Jiang
  - Henry Peng Zou
  - Wei-Chieh Huang
  - Yangning Li
  - Liancheng Fang
  - Zhen Wang
  - Philip S. Yu
year: 2025
---

# Multi-Agent Autonomous Driving Systems with Large Language Models: A Survey of Recent Advances, Resources, and Future Directions

一篇综述,系统梳理 [[large-language-models]] 驱动的多智能体自动驾驶系统(multi-agent ADS),按智能体交互模式分类已有方法,并讨论 agent-human 交互、应用、数据集与挑战。

## 问题

自动驾驶系统(Autonomous Driving Systems, ADS)正在变革交通。传统 ADS 多依赖数据驱动方法(如强化学习、[[active-learning]]),但在"长尾"(long-tail)场景(罕见但关键的突发障碍等)上表现不佳,且"黑盒"特性限制了可解释性与信任。

[[large-language-models]] 被引入 ADS 以支持高层决策(凭借推理、指令遵循与沟通能力,并通过零样本设置缓解长尾问题)。但 LLM-based 单智能体 ADS 面临三大局限:

- **感知受限(Limited Perception)**:LLM 只能响应传感器输入,缺乏预测与泛化能力,无法补全不完整的传感器信息;
- **协作不足(Insufficient Collaboration)**:单个 LLM agent 无法与其他车辆或基础设施协调,在变道合流、环岛通行等场景表现欠佳;
- **高计算需求(High Computational Demands)**:数十亿参数使实时车载部署困难,尤其在车载资源受限时。

LLM-based 多智能体 ADS 通过让不同 agent 用自然语言通信与协调来缓解上述问题。本文是首篇系统审视该 NLP 与多智能体 ADS 交叉领域的综述。

## 方法

综述构建了如下分类框架(Figure 4 taxonomy):

- **核心概念(Section 2)**:介绍 agent 的环境(物理环境 vs 仿真环境,如 [[carla]])与 profile。Profile 生成有三类方法(Table 1):Pre-defined(预定义,可嵌入安全规则但耗人力)、Model-generated(LLM 生成,适应新场景但可能违反交规)、Data-derived(从大规模数据集派生,受数据可得性与隐私限制)。
- **Multi-Agent Interaction(Section 2.2.2 / Section 3)**:交互**模式**分为 cooperative、competitive、debate([[multi-agent-debate]]);交互**结构**分为 centralized、decentralized、hierarchical、shared message pool(共享消息池)。
- **三类交互场景(Section 3)**:① multi-vehicle interaction(多车交互,如 LanguageMPC 用中心 agent 作"大脑",AgentsCoDriver、CoDrivingLLM、KoMA 等);② vehicle-infrastructure interaction(车路交互,如 EC-Drive 的边云协同分层结构);③ vehicle-assistant interaction(车辆-助手交互,如 ChatSim、ALGPT 用 PM/manager agent 分解指令)。
- **Agent-Human Interaction(Section 4)**:分为 instructor paradigm(人类作"导师",给定量/定性反馈)与 partnership paradigm(人机平等协作,如 Talk2Drive、Receive 用 memory module 个性化驾驶偏好)。
- **应用(Section 5)**:collaborative perception(协同感知,扩展视野 FOV)、collaborative decision-making(协同决策)、collaborative cloud-edge deployment(云边部署)、collaborative assistance-tools(协同辅助工具)。

## 结果

作为综述,本文主要贡献是分类体系、资源汇编与未来方向,而非单一数字指标:

- **数据集汇编(Table 2)**:单智能体数据集如 KITTI、nuScenes、Waymo、BDD100K、BDD-X、nuScenes-QA、DriveLM;多智能体数据集如 DAIR-V2X、TUMTraf-V2X、V2V4Real、V2XSet(含多车/车路传感器,支持 cooperative perception/detection/tracking)。
- **Benchmark**:INTERACTION(环岛、变道等真实交互场景)、Waymo Open Motion Dataset(交互式多智能体运动预测)、SMARTS(匝道合流、无信号交叉口)。
- **代表性系统**:LanguageMPC(中心 LLM 协调多车)、AgentsCoDriver(含 lifelong learning 的五模块协作决策框架)、KoMA(分布式共享内存池 + 意图推理 + ranking-based reflection)、V-HOI MLCR(融合 collaboration 与 debate 的混合交互)、AD-H(分层:多模态 planner + 轻量 controller)、LDPD(teacher agent 蒸馏给 student agents)。
- 论文指出未来方向围绕鲁棒性、可解释性、实时部署、人车协同(human-vehicle co-driving)等。

## 在本 wiki 中的位置

本文是 [[llm-multi-agent]] 在自动驾驶([[autonomous-agents]])领域的应用综述,与具体系统页 [[2023-drivemlm-autonomous-driving]] 互补。涉及的核心概念包括 [[multi-agent-collaboration]]、[[multi-agent-debate]]、[[agent-orchestration]]、[[agent-memory]]、[[reflection]];仿真环境涉及 [[carla]];作者机构包括 [[stanford-university]] 之外的 University of Tokyo、Cornell University、UIC,通讯/资深作者为 [[philip-s-yu]]。
