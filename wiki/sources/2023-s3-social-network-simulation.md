---
type: source
subtype: paper
tags: [llm-agents, social-simulation, social-network, agent-based-modeling, computational-social-science]
created: 2026-05-30
updated: 2026-05-30
arxiv: 2307.14984
raw: raw/2307.14984.pdf
authors: [Chen Gao, Xiaochong Lan, Zhihong Lu, Jinzhu Mao, Jinghua Piao, Huandong Wang, Depeng Jin, Yong Li]
affiliations: [Tsinghua University]
year: 2023
---

# S³: Social-network Simulation System with LLM-Empowered Agents

用 [[large-language-models]] 驱动的 agent 在真实社交网络数据上模拟用户,刻画 **emotion(情绪)· attitude(态度)·
interaction behavior(交互行为)** 三个层面,并观察个体行为累积涌现出的**信息 / 态度 / 情绪传播**。清华电子系
[[yong-li]] 团队(arXiv 2307.14984,v3 2025-06)。

## 问题
社交网络是社会科学核心研究对象。社会模拟分宏观(系统级,用方程描述群体状态演化)与微观([[agent-based-modeling]],
用规则或参数化模型描述个体)。LLM 具备**感知 · 推理/记忆 · 类人文本生成**三项能力,适合按 agent-based 范式逐用户模拟,
但此前尚无用 LLM 做社交网络模拟的系统性工作。

## 方法
- **环境**:用真实社交网络数据构建;提出 **user-demographic inference 模块**(prompt engineering + prompt tuning)推断
  用户年龄、性别、职业等人口属性。
- **个体层**:用 prompt engineering + prompt tuning 模拟用户的态度、情绪、行为(转发 / 创作 / 不活跃),决策同时考虑
  **人口属性**与**历史发帖记忆**。
- **群体层**:个体行为(生成、转发)与内部状态(态度、情绪)的累积,涌现出**信息传播、态度传播、情绪传播**。
- 既用 **fine-tuning** 也用 prompt engineering 让 agent 行为贴近真人。

## 结果
场景:**性别歧视** 与 **核能(power policies)** 两个话题;base model 为 GPT-3.5 API 或 ChatGLM-6B(微调用 ChatGLM)。
- **传播仿真(Table 5,零样本)**:对比需训练数据的 Voter / DeGroot / FNN / SINN / NDCN。S³ 零样本在**意见传播**上 MSED **0.182** /
  Cor **0.858**(与需训练的强基线相当),在**情绪传播**上 MSED **0.051** / Cor **0.892**(**超过所有基线**)。
- **人口属性预测**:gender Acc **0.710** / F1 0.667 / AUC 0.708(ChatGLM + P-Tuning-v2);age MSE 128 / MAE **7.53**(约 21.5% 误差);
  从用户中识别出 1,016 种职业,再用 LLM 归并为 **10 类**。
- **机制**:情绪用 **Markov 链**(calm / moderate / intense)+ 衰减系数建模;态度同理;内容生成与转发/发帖行为均由 LLM 据 profile + 记忆池决定。
- 定位为 LLM-based 社交网络模拟的**开创性一步**,应用面向预测、推理解释、模式发现/理论构建、政策制定。

## 在本 wiki 中的位置
属于 [[generative-social-simulation]] 的**社会模拟平台**子分支(早期、聚焦社交网络传播)。是清华 [[yong-li]] 团队
[[2025-agentsociety-large-scale-social-simulation]] 的**直接前身**(AgentSociety source 页点名继承 S³),并与
[[2024-oasis-million-agent-social-simulation]]、[[2025-socioverse-world-model-social-simulation]] 等更大规模平台一脉相承。
连接 [[social-simulation]]、[[agent-based-modeling]]、[[computational-social-science]]。
