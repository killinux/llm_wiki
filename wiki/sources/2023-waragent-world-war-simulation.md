---
type: source
subtype: paper
tags: [llm-agents, social-simulation, multi-agent-systems, international-relations, history]
created: 2026-05-30
updated: 2026-05-30
arxiv: 2311.17227
raw: raw/2311.17227.pdf
authors: [Wenyue Hua, Lizhou Fan, Lingyao Li, Kai Mei, Jianchao Ji, Yingqiang Ge, Libby Hemphill, Yongfeng Zhang]
affiliations: [Rutgers University, University of Michigan]
year: 2023
---

# War and Peace (WarAgent): LLM-based Multi-Agent Simulation of World Wars

号称**首个**用 [[large-language-models]] 多智能体系统模拟**历史国际冲突**的工作:每个 agent 扮演一个参战**国家**
(含其特征与决策过程),在外交 / 冲突 / 合作中重演历史,借涌现的 agent 互动审视战争的触发与"历史必然性"。
Rutgers([[yongfeng-zhang]] 的 AGI research 组)+ University of Michigan(arXiv 2311.17227v2,2024-01)。

## 问题
传统通过史学分析研究冲突,受限于其**静态性**与**事后偏见 (hindsight bias)**。LLM 能建模复杂行为与互动(如虚拟小镇、
狼人杀、拍卖竞技场、复杂任务求解等模拟已有先例),但尚无人用它模拟国际外交与战争这一**多面而微妙**的领域。

## 方法
LLM 驱动的多智能体系统(MAS),以国家为 agent。围绕三个研究问题:
- **RQ1 Simulation Effectiveness(仿真有效性)**:MAS 能多大程度复现历史上战略规划与决策过程的演化?——以与史实的吻合度衡量可信度。
- **RQ2 Casus Belli(开战理由 / 触发)**:某些战争触发因素是否比其他更关键?能否经仿真识别?
- **RQ3 War Inevitability(战争必然性)**:历史的必然是否真不可避免?寻找导向战争(或和平)的条件。

三个历史场景:**一战 (WWI)**、**二战 (WWII)**、中国**战国时期 (Warring States Period)**。代码与数据开源(agiresearch/WarAgent)。

**架构**:四基石——国家 agent、**秘书 agent**(每轮校验动作的格式/内容/逻辑一致性并直接修正)、Board、Stick。国家 agent 档案含**六维**:
Leadership、Military Capability、Resources、Historical Background、Key Policy、Public Morale。backbone 用 **GPT-4** 与 **Claude-2**。

## 结果
- **RQ1 有效性**:复现与史实一致的国际格局——**100%** 的仿真都形成与历史一致的军事同盟(如 Serbia–Russia),叙事与史实吻合。
- **RQ2 开战触发 (Casus Belli)**:识别出结构性敌对(WWI 中 France 主敌为 German Empire,源于历史宿怨)。关键的**匿名化测试**:把真实
  国名替换后仍生成历史准确的叙事 → 说明结论**不只是靠记忆国名**(部分回应了 [[2025-emergent-llm-behaviors-data-leakage]] 式的数据泄漏质疑)。
- **RQ3 战争必然性**:用**反事实触发事件**(不同冲突强度)做实验(WWI / GPT-4,每事件 3 次重复),发现战争爆发更多由**结构性底层因素**驱动,
  仅改变触发事件**难以避免**战争。
- **意义**:把 [[llm-multi-agent]] 社会模拟从"个体 / 小群体"推到 **国家级宏观主体**,呼应 [[2023-concordia-generative-agent-based-modeling]]
  的跨尺度建模;作者定位为"用 AI 理解人类历史、或可预防未来冲突"的蓝图。

## 在本 wiki 中的位置
属于 [[generative-social-simulation]] 的**博弈 / 战略 / 多主体冲突**子分支,与 [[2025-llm-agent-game-theory-strategy-recognition]]、
[[2026-llm-agents-competition-cooperation-games]]、[[2025-emergent-coordination-multi-agent-language-models]] 相邻。其"复现历史结局"
的设定使它**直接暴露在** [[2025-emergent-llm-behaviors-data-leakage]] 式的**数据泄漏**质疑下(史实极可能在预训练语料里),
是讨论该范式可信度的典型案例。连接 [[multi-agent-systems]]、[[social-simulation]]、[[computational-social-science]]。
