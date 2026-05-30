---
type: topic
tags: [llm-agents, recommender-system, user-simulation, multi-agent, conversational-recommendation]
created: 2026-05-30
updated: 2026-05-30
sources: 18
---

# 推荐系统中的 LLM 智能体 (LLM Agents for Recommendation)

> 一句话:把 [[llm-agents|LLM 智能体]]引入推荐,有两条主线——**模拟导向**(用 agent 模拟用户/物品,造可信仿真器做评估与数据生成)
> 与**推荐导向**(让 agent 直接做推荐:规划+记忆+工具,或多 agent 协作)。这是 wiki 两大半边(社会模拟 × 推荐系统)的**缝合点**。

综述见 [[2025-llm-agents-for-recommender-systems-survey]]。与 [[generative-social-simulation]]("可信度验证")、[[rl-for-recommendation]]("仿真器评估")
直接接壤。

---

## 一、模拟导向:用 agent 当"用户/物品"
动机:离线指标与线上表现存在鸿沟,需要忠实捕捉人类认知的**可配置仿真器**做数据收集、评估与算法迭代。
- [[2023-recagent-user-behavior-simulation]] —— 沙盒里 LLM agent 近零样本模拟用户行为,研究**信息茧房、从众**等社会现象(破解"造数据却需真数据训练"的鸡蛋困境)。
- [[2024-generative-agents-in-recommendation]](Agent4Rec)—— **1000 个**生成式 agent 的电影推荐用户模拟器,profile/memory/action 三模块;
  核心 RQ:LLM agent 到底能多忠实地模拟真实自主用户(直面可信度问题)。
- [[2023-agentcf-collaborative-learning-agents-recsys]](AgentCF)—— **把用户和物品都建模成 agent**,通过协同反思把协同过滤思想迁到 LLM(补上以往只建模用户侧的缺口)。
- 更多用户模拟器:[[2024-lusifer-llm-user-simulation]]、[[2025-simuser-llm-user-simulation-recsys]]、[[2025-g-ubs-group-aware-user-behavior-simulation]]、
  [[2025-recoworld-simulated-environments-agentic-recsys]]、[[2025-user-mirrorer-preference-aligned-user-simulator]]、[[2025-pub-personality-user-behaviour-simulator]]。

## 二、推荐导向:让 agent 直接做推荐

### 1) 单 agent + 规划/记忆/工具
- [[2023-recmind-llm-agent-for-recommendation]](RecMind)—— 自主推荐 agent,planning+memory+tools 做 zero-shot 推荐,提出
  **Self-Inspiring** 规划(保留所有已探索状态)。
- [[2023-recommender-ai-agent-interec]](InteRecAgent)—— LLM 当"大脑"、**传统推荐模型当工具**,把 ID-based 矩阵分解包装成对话式交互推荐。

### 2) 多 agent 协作
- [[2024-macrec-multi-agent-recommendation]](MACRec,SIGIR'24)—— Manager / User&Item Analyst / Reflector / Searcher / Task Interpreter 等
  **角色专门化** agent 协同求解(针对单 agent 在复杂推荐决策上不足)。
- [[2026-trirec-tri-party-agent-recommendation]] —— 用户—物品—平台**三方** agent;[[2026-entropy-guided-agentic-recommendation]]、[[2026-thinkrec-thinking-based-recommendation]]。

### 3) 把 LLM 知识注入传统推荐
- [[2025-grasp-world-knowledge-sequential-recommendation]](LLM 世界知识作辅助输入,抗幻觉)、[[2024-llm-learnable-planners-long-term-recommendation]]、
  [[2024-llm-tags-vs-classical-text-features]]、[[2026-lerl-llm-enhanced-rl-long-term-recommendation]]。

## 三、核心张力
1. **模拟的保真度**:agent 真能复刻真实用户吗?——Agent4Rec 的 RQ1、[[2025-can-llm-agents-simulate-human-behavior]] 的过程级证据(prompt-only ~11.86%)、
   验证综述 [[2026-generative-social-simulation-validation]] 都在敲警钟。这是模拟导向能否落地的命门。
2. **集成难度**:模拟导向的 agent 难以真正嵌入线上推荐系统(MACRec 即批评此点)。
3. **成本**:LLM agent 推理成本远高于传统模型,大规模在线服务受限。
4. **幻觉与 ID 鸿沟**:LLM 不懂 user-item 协同信号(AgentCF 的出发点),需与协同过滤/ID embedding 融合。

## 四、开放问题
- **可信仿真器的验证标准**:把"是否对齐真实用户"做成可操作基准([[2025-sim4ia-bench-user-simulation-benchmark]]、[[2026-ab-agent-recsys-evaluation]] 是尝试)。
- **agent × 传统模型的最优分工**:LLM 当大脑/工具调用 vs 当特征/知识注入。
- **多 agent 协作的收益归因**:协作真带来增益,还是只是集成投票?(呼应 [[llm-self-improvement]] 的归因问题)
- **成本-质量权衡**:何时值得上 agent,何时传统模型足矣。

## 相关概念页
[[llm-agents]]、[[user-simulation]]、[[recommender-systems]]、[[llm-for-recommendation]]、[[conversational-recommendation]]、
[[generative-social-simulation]]、[[offline-evaluation]]、[[multi-agent-systems]]
