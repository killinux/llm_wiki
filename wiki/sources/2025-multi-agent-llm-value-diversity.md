---
type: source
subtype: paper
tags:
  - llm-multi-agent
  - social-simulation
  - ai-alignment
  - collective-intelligence
  - value-diversity
created: 2026-05-29
updated: 2026-05-29
arxiv: 2512.10665
raw: raw/2512.10665.pdf
authors:
  - Muhua Huang
  - Qinlin Zhao
  - Xiaoyuan Yi
  - Xing Xie
year: 2025
---

# On the Dynamics of Multi-Agent LLM Communities Driven by Value Diversity

通过 Schwartz 基本人类价值观理论给 LLM 智能体注入多样化价值,在多智能体社会模拟中考察"价值多样性如何塑造 AI 社群的集体行为",发现价值多样性能提升价值稳定性、催生涌现行为与更具创造性的自发规则,但极端异质会带来不稳定的边际递减。

## 问题

LLM 的能力提升主要靠扩大模型规模([[scaling-law]]),但单纯做大模型在性能上已出现边际递减。与此同时,人类研究表明群体可以表现出可测量的**集体智能**(collective intelligence,即 c-factor),且该能力更多取决于群体过程而非成员平均/最高个体智力,多样化的问题解决者团队甚至能胜过同质的高能力团队。

本文是一项 pilot study,聚焦一个更基础的问题:**价值多样性(value diversity)如何塑造 AI 智能体社群的集体行为?** 价值是人类多样性的核心维度,也与 [[ai-safety]]、[[ai-alignment]] 和用户偏好([[direct-preference-optimization]])紧密相关。论文同时连接三条研究脉络:把人类集体行为研究延伸到纯 AI 群体;基于 LLM 的多智能体[[social-simulation]];以及与 [[constitutional-ai]] 的对接——不再由开发者手工编写 constitution,而是探究**价值多样的 AI 智能体社群能否自组织出自己的规范与制衡**。

## 方法

采用 [[agent-based-modeling]] 的 LLM 驱动模拟,操纵三个自变量:(1) Group Size、(2) Value Composition、(3) Value Complexity。所有智能体用同一基座模型 [[llama-3]](LLaMA-3.1-70B)以固定语言能力,只通过 [[persona]] 区分。

- **价值初始化(naturalistic value elicitation)**:基于 [[schwartz-theory-of-basic-values]](十种普世价值排布成环状结构,相邻兼容、相对冲突,聚合为 Openness to Change / Self-Enhancement / Conservation / Self-Transcendence 四个高阶类别)。不直接贴抽象标签,而是生成 84 个伦理困境(ethical dilemmas),由人类标注其对应价值,让一个 LLM 写出体现该价值的 narrative,再用第二个 LLM 作 [[llm-as-judge]] 过滤逻辑/可信度差的叙事,最后让智能体从叙事中反思抽取出自己的价值画像。该流水线在概念上呼应作者团队的 IROTE([[iros]] 不适用,参见 arXiv:2508.08719)价值引出工作。
- **认知架构([[memory-module]])**:每个智能体维护 self-perception(自我概念与目标)、impression of others、action history、conversation history;为模拟人类记忆约束,会话记忆为 5 槽 rolling window,用 LRU 策略汇总归并旧记忆,防止智能体"全知"。
- **实验条件**:Group Size = 4 / 10 / 30;Group Composition = 同质组(四个高阶类别各一)/ 多样均衡组 / `no_value` 控制组(不经伦理困境引出、无价值先验);Value Complexity = single value vs multi value(多值仅限 Schwartz 环上相邻价值组合,如 Benevolence+Universalism 或 Achievement+Power)。
- **三阶段交互协议**:Stage 1 自由交互(25 轮"数字鸡尾酒会",智能体发出/接受/拒绝会话邀请,一次仅一段对话,记录全部对话);Stage 2 治理涌现(每个智能体独立提议两条社群规则,可简短互评,本研究未实现完整投票),把所产出的规则集视为社群自发起草的"宪章"。期间每 5 轮用轻量 Schwartz Value Survey 追踪价值漂移,并对会话图做网络分析与主题建模。

## 结果

- **网络结构**(同规模三种条件对比,Figure 2):`no_value` 条件网络弱连通、缺乏持久社群结构、连接随机且多在一两次交互后终止;single-value 条件出现高模块度的紧密同质聚类(经典 homophily,如 "hedonism & conservation" 抱团),但聚类内紧、缺乏桥接、易孤岛化;multi-value 条件最复杂——既有强模块度又有跨社群桥接,价值多元支撑了凝聚而不致碎裂,最利于集体智能涌现。
- **会话内容**(Figure 3,各 30 智能体):赋值组对话更聚焦、连贯、有深度,自发讨论治理结构、伦理困境、DAO、去中心化治理、参与式治理与基于区块链的透明问责等实质主题,并跨多轮维持叙事;`no_value` 基线对话更表层、礼貌但发散,常在不相关话题间跳跃或很快冷场。
- **多样性三轴上的涌现**:
  - Group Size:30 智能体组在讨论深度、规则发展、抗挑战韧性上持续优于 10 与 4 智能体组,呈正向但边际递减,约 30 智能体后趋于饱和(对应假设的"diversity scaling law")。
  - Value Complexity:multi-value 组在 constitution 任务中产出**多 20–30%** 的高质量规则,且规范收敛更稳定。
  - Value Composition:均衡多样组涌现得分最高,高于任何同质组与 `no_value` 控制组;涌现指标(会话深度、规则质量、安全韧性的复合分)从 no-value → 同质 → 多样均衡单调上升,从同质到完全多样的跃升大于从适度到完全多样。
- **宪章任务的意识形态分布**(Figure 4):`no_value` 基线近 **90%** 规则为 Rousseauian(趋向安全共识但缺乏程序深度);赋值组更多元——Rousseauian 仍主导(**80.3%**),Lockean 规则显著上升至 **15.7%**,引入个体权利与程序公平主题。价值-意识形态热图显示:benevolence/universalism/hedonism 价值的智能体更倾向 Rousseauian 规则,power/security 价值更关联 Hobbesian(强调层级与秩序)。
- **结论**:价值多样性是塑造集体表现的**结构性参数**(伴随协调成本),而非单纯社会属性;本工作为价值多样的 AI 社群的集体智能与对齐研究奠定方法论与概念基础(作者自评为探索性/early draft)。

## 在本 wiki 中的位置

本文位于 [[llm-multi-agent]]、[[social-simulation]] 与 [[ai-alignment]] 的交叉点。它把 [[generative-agents]] 一脉的开放式社会涌现研究推进到"价值多样性 × 集体智能"维度,实验上以 [[schwartz-theory-of-basic-values]] 系统化注入价值,方法上呼应 [[agent-based-modeling]] 与 [[human-behavior-simulation]]。在对齐方向上,它与 [[constitutional-ai]] 互补:不再外部硬编码 constitution,而观察价值多样的智能体社群能否**自组织出宪章**,与去中心化 AI 治理、[[scalable-oversight]] 的诉求相关。作者来自 [[stanford-university]] 与 [[microsoft-research-asia]],与 [[xing-xie]] 团队的 LLM 价值测量/引出工作([[adagin]] 不适用,见 ADAeam arXiv:2505.13531、Value Fulcra arXiv:2311.10766)一脉相承。
