---
type: source
subtype: paper
tags: [llm-agents, social-simulation, multi-agent-systems, emergent-behavior, minecraft, agent-civilization]
created: 2026-05-30
updated: 2026-05-30
arxiv: 2411.00114
raw: raw/2411.00114.pdf
authors: [Altera.AL]
affiliations: [Altera]
year: 2024
---

# Project Sid: Many-agent Simulations Toward AI Civilization

把 **10 – 1000+** 个 [[llm-agents|LLM 智能体]]放进 **Minecraft**,首次尝试在开放世界里观察是否能自下而上涌现出
**文明级**结构(专业分工、治理、文化、宗教、法律)。提出 **PIANO** 认知架构以解决"多 agent 长时程下连贯性崩溃"问题。
Altera 出品(arXiv 2411.00114v1,2024-10)。

## 问题
此前 AI agent 多在**孤立或小群体**中评测,缺乏真正大规模、覆盖完整"文明进程"的多 agent 仿真。论文指出三大障碍:
- **Reason 1:单 agent 不进步** —— LLM agent 即便有规划/反思模块,也常陷入重复动作或被**幻觉**误导(例如谎称"在吃 bagel",
  该幻觉输出回灌后续 prompt,污染下游行为);极小的幻觉率在持续交互中会被放大。
- **Reason 2:agent 群体不进步** —— agent 间**误传**意图会传播幻觉并循环(如聊天模块说"给你镐子"但函数调用却去"探索",
  对方便拿着不存在的镐子挖矿)。论文把"多路输出流需双向影响"这一性质定义为 **coherence(连贯性)**。
- **Reason 3:缺乏文明进步的 benchmark**。

## 方法:PIANO 架构
**PIANO (Parallel Information Aggregation via Neural Orchestration)**:让单个 agent 能**并发处理多路输出流**(说话、动作、注视、
表情等),并在与人类/其他 agent 的**实时低延迟**交互中保持 coherence——避免"用单次 LLM 调用同时产出所有输出"的不可扩展做法。
规模上:单一社会 50–100 agent,文明级 500–1,000 agent 分居多个相互交互的社会。并提出对齐"人类文明进步"的新评测指标。

## 结果:涌现的文明要素
- **单 agent 进度**:用 Minecraft **独特物品获取数**做 benchmark;PIANO 的 **action awareness** 模块显著提升进度,49 个 agent 测上限;
  关键是**仅 GPT-4o 基座**才解锁显著个体进度(更弱基座不行)。
- **角色专业化**(50 agent,数小时 ≈ 12 游戏日):agent 自主分化出 **Trader 等不同职业角色**;**依赖 social awareness 模块**——消融掉它后
  agent 无法形成对他者的画像,角色便**不再持久**。
- **集体规则 / 法律**:在含初级税法与**民主投票**系统的世界里,25 个 agent 为被税选民、3 个为支持/反对税收的影响者、1 个为选举管理者;
  agent 对税法提反馈、**民主投票修订"宪法"**(中途第 10 分钟更新),并测量修宪前后的**纳税合规度**变化。
- **文化传播**:观察到 **meme 的自发生成**与**单一宗教的结构化传播**(cultural & religious transmission)。
作者视"能否在人类文明中共存并推动文明进步"为 AI agent 能力的**终极 benchmark**。

## 在本 wiki 中的位置
属于 [[generative-social-simulation]] 的**大规模 / 游戏世界模拟**子分支,与 [[2024-oasis-million-agent-social-simulation]]
(社媒百万级)、[[2025-generative-mmo-simulation]]、[[2025-mmoagent-economic-simulation-mmo]] 相关;其规模介于
[[2023-generative-agents]] 的"25 人小镇"与 OASIS 之间,被 [[2024-limits-of-agency-in-agent-based-models]] 列为"Minecraft 1000 agent"
小规模对照。它把 [[voyager]](单 agent Minecraft 探索)推向**多 agent 文明**。其"涌现文明"主张同样需面对
[[2025-emergent-llm-behaviors-data-leakage]] 的可信度审视。连接 [[multi-agent-systems]]、[[emergent-abilities]]、[[hallucination]]。
