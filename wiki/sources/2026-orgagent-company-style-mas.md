---
type: source
subtype: paper
tags: [llm-multi-agent, multi-agent-systems, agent-orchestration, organizational-structure, hierarchical-coordination, reasoning, token-efficiency]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2604.01020
raw: raw/2604.01020.pdf
authors: [Yiru Wang, Xinyue Shen, Yaohui Han, Michael Backes, Pin-Yu Chen, Tsung-Yi Ho]
year: 2026
---

# OrgAgent: Organize Your Multi-Agent System like a Company

把 [[llm-multi-agent]] 系统按"公司式层级"组织——拆成治理(governance)、执行(execution)、合规(compliance)三层——并系统验证这种组织结构相比扁平协作能同时提升推理效果与降低 token 成本。

## 问题

LLM 驱动的 Multi-Agent Systems(MAS)在复杂推理上潜力很大,但"如何有效组织多个 agent"仍是开放问题。已有研究分两条线:一条研究 agent 间的交互机制(角色扮演、辩论、投票、共识,如 [[multi-agent-debate]]、CAMEL),另一条研究更高层的编排(角色分工、工作流设计,如 [[autogen]]、[[metagpt]]、[[chatdev]])。但这些工作几乎没有把"组织结构(organizational structure)本身"当作核心变量来研究:在一个任务内部,究竟谁来规划、谁来执行、谁来审核、决策权如何分配,缺乏系统化的对比。本文借鉴组织理论中"扁平结构 vs. 层级结构"的对比,聚焦经过数十年打磨的"公司式层级"作为 MAS 的组织范式。

## 方法

提出 **OrgAgent**,一个公司式层级 MAS 框架,把推理过程拆成三层:

- **Layer A — 治理层(Governance)**:由 CEO(战略方向/整体协调)、CTO(技术合理性/方案设计)、COO(资源使用/执行效率)组成。负责技术角色分配(选 Drafter、是否需要 Specialist、选 Specialist)、资源控制(任务风险、最大轮数)、以及决定执行模式。
- **Layer B — 执行层(Execution)**:由 Drafter(主写手,产出候选答案并修订)、Reviewer(质量与错误检测)、以及按需调用的 Specialist(对难点/易错部分提供专项支持)组成。
- **Layer C — 合规层(Compliance)**:由 CSO(在 benchmark 特定约束下产出最终答案、对齐格式)与 CCO(检查输出是否满足结构要求,只验证格式不做推理)组成。

框架还包含:**Skill-Based Worker Pool**(六类技能 worker:Technical、Quantitative、Reasoning、Domain、Communications、Data,可充当 Drafter 或 Specialist);三种**执行模式(Execution Mode)**——DIRECT(只用 Drafter,1 轮)、LIGHT MAS(Drafter+Reviewer,最多 3 轮)、FULL MAS(Drafter+Reviewer+Specialist,最多 5 轮);四种**执行策略(Execution Policy)**——STRICT(最严约束/最省 token)、BALANCE(折中)、NOCAP(最少约束/最灵活)、AUTO(按任务自适应选配置)。同时实现一个**扁平(Flat)框架**作为对照:所有 agent 同级、无显式指挥链,最多 3 轮。

## 结果

在三个推理 benchmark 上评测:[[musr]](多步软推理,754/756 例,报告 Accuracy)、[[musique]](组合式多跳 QA,24,814 例,报告 F1)、[[squad]] 2.0(含不可回答问题的阅读理解,151,054 例,报告 F1 与 abstention rate)。骨干模型为 [[gpt-oss-120b]]、GPT-5 mini、[[llama-3]].1-8B。

效果(层级 AUTO vs. 扁平,Table 1):

- 层级组织普遍优于扁平 MAS 与单 agent baseline,在 MuSiQue 与 SQuAD 2.0 上尤为明显。
- SQuAD 2.0 上,GPT-OSS-120B 层级设置相对扁平 **+102.73%** F1(同时 token 减少 **74.52%**);GPT-5 mini **+120.47%**,LLaMA-3.1-8B **+58.96%**。
- MuSiQue 上,GPT-5 mini F1 提升 +37.11%,LLaMA-3.1-8B +123.99%,GPT-OSS-120B +18.97%。
- MuSR 上结果更参差:GPT-5 mini 略优(+3.81%),但 GPT-OSS-120B(-13.77%)与 LLaMA-3.1-8B(-9.12%)反而落后,说明层级协作并非对所有推理任务都占优。

效率与行为:

- 层级组织在所有 benchmark、所有模型上 token 用量都不高于扁平 MAS,降幅 **46.38%–79.31%**,几乎砍掉一半以上的交互开销。
- 执行策略上 STRICT 最省 token(如 SQuAD 2.0 仅约 1,148–1,554 平均 token),NOCAP 最费;AUTO/BALANCE 居中。
- 协调行为分析:层级会诱导清晰但依模型而异的技能专化。SQuAD 2.0 上 GPT-5 mini 与 LLaMA-3.1-8B 高度偏向 domain specialist(选择率 87.50%、90.82%),GPT-OSS-120B 更偏 reasoning specialist(73.50%)。
- 弃答(abstention)行为:单 agent baseline 几乎从不弃答(0–3.02%),而层级策略在 SQuAD 2.0 不可回答子集上把弃答率显著抬高(最高 NOCAP 下 GPT-OSS-120B 达 39.78%),说明层级化的受控信息流与分层校验有助于"该拒答时拒答"。

局限:在 MMLU、MMLU-Pro 等多选 benchmark 上提升有限(答案空间受限,留给层级协作发挥的余地小);框架用固定最大轮数,未收敛时被强行终止;评测的模型/任务/组织设置有限,未考察延迟、跨次稳定性与人工评估。

## 在本 wiki 中的位置

本文是 [[llm-multi-agent]] / [[multi-agent-systems]] 组织结构方向的实证研究,把"组织结构本身"作为核心自变量,与 [[autogen]]、[[metagpt]]、[[chatdev]]、[[multi-agent-debate]] 等编排/交互框架互补。它给出的关键经验——公司式层级(治理/执行/合规分层)能在多数推理任务上同时提升效果并大幅降低 token 成本——可作为 [[agent-orchestration]]、[[multi-agent-collaboration]] 设计的参考。涉及的评测资源 [[musr]]、[[musique]]、[[squad]] 及模型 [[gpt-oss-120b]]、[[llama-3]] 在本 wiki 中均有相关条目。
