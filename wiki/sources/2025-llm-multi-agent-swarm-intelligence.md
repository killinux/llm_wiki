---
type: source
subtype: paper
tags:
  - llm-multi-agent
  - multi-agent-systems
  - agent-based-modeling
  - swarm-intelligence
  - prompt-engineering
  - emergent-abilities
  - gpt-4
created: 2026-05-29
updated: 2026-05-29
arxiv: null
doi: 10.3389/frai.2025.1593017
raw: raw/10.3389_frai.2025.1593017.pdf
authors:
  - Cristian Jimenez-Romero
  - Alper Yegenoglu
  - Christian Blum
year: 2025
---

# Multi-agent systems powered by large language models: applications in swarm intelligence

把 agent-based modeling 中 agent 的硬编码程序替换为 LLM(GPT-4o)驱动的 prompt,在蚁群觅食和鸟群 flocking 两个经典 swarm intelligence 场景中复现并诱导出涌现集体行为。

## 问题

传统 [[multi-agent-systems]] 与 swarm intelligence 仿真依赖显式编程的、领域特定的 rule-based 行为,缺乏灵活性。近期虽有工作把 [[large-language-models]] 用于 [[role-playing-agent]] 或虚拟社会(偏重拟人推理),但很少把 LLM 作为非人类、非语言的 swarm-like agent 的去中心化"行为引擎"。本文研究:能否用 LLM 替换 agent-based modeling and simulation(ABMS)中 agent 的硬编码逻辑,让 LLM 通过 [[prompt-engineering]] 处理实时环境输入并生成动作,从而模拟并诱导 swarm 中的 self-organizing 涌现行为。

## 方法

构建一条 toolchain,把 NetLogo 仿真平台(经其 Python extension)与 [[gpt-4]](GPT-4o,经 OpenAI API,temperature=0.0 保证确定性)对接,形成 closed-loop:NetLogo 把实时环境状态(位置、信息素浓度、nest scent、邻居 heading 等)编码为 structured prompt → GPT-4o 处理并以 Python dict / JSON 形式返回 structured actions → 解码为可执行命令 → agent 执行并更新环境,迭代进行。prompt 均为 zero-shot、stateless(不保留对话上下文,用 chat.completions)。

文章对比两类 prompt 设计(Table 1):

- Structured rule-based prompts:显式、确定性规则,用于蚁群觅食(实验 1)。指定如沿信息素 trail 走、捡食物、释放信息素等精确动作。
- Knowledge-driven / principle-based prompts:依赖 LLM 对概念(如 alignment、cohesion、separation)的内在理解,用于鸟群 flocking(实验 2)。

每个实验展示了多轮 trial-and-error 的 prompt tuning 过程(蚁群 9 个 iteration,鸟群 5 个 iteration),LLM 自身的反馈被用于改进 prompt,例如蚁群需加入"携带食物时优先 nest scent 而非信息素"、"无信息素时远离巢穴随机旋转探索"、把数值环境信息改为方向性描述("Higher Pheromone Concentration: Front");鸟群需显式声明 NetLogo 的 compass convention(0=北、90=东)并加入 "rationale" 键促使 [[chain-of-thought]] 推理、选择最短旋转路径。

每个场景测试三种(或两种)变体:原始 NetLogo(纯 rule-based)、LLM(全部 agent 由 LLM 驱动)、Hybrid(一半 rule-based 一半 LLM)。

## 结果

蚁群觅食实验(10 只蚂蚁、3 个食物 patch、1000 步、5 次重复):

- 1000 步累积收集食物:NetLogo 与 LLM 表现相近,均约 85 单位;NetLogo 标准差约 20,而 LLM 仅约 7(更稳定)。
- Hybrid 表现最佳,平均约 95 单位(std 约 12),且约第 20 步即开始往巢运食物,而 LLM 与 NetLogo 约第 40 步才开始。
- 统计检验:LLM vs NetLogo 的 Kruskal-Wallis p≈0.99、Cohen's d≈0.006(无显著差异,均值几乎相同);Levene/Brown-Forsythe p≈0.0045(方差不同)。LLM vs Hybrid 与 NetLogo vs Hybrid 的 p 值接近 0、Cohen's d≈0.2–0.23(Hybrid 显著不同)。
- 单蚂蚁返巢步数(Table 2):food patch 1(最近)LLM 均值 23.04、NetLogo 21.0、Hybrid 21.98;patch 3(最远)三者约 38–39;rule-based 蚂蚁通常步数略少,LLM 蚂蚁更一致。

鸟群 flocking 实验(30 只鸟、800 步、5 次重复;Hybrid = 25 rule-based + 5 LLM):

- 加入 compass convention 与 "rationale" 键后,LLM 驱动的鸟形成更大、更稳定的 flock cluster,表现可与原始 rule-based NetLogo 相当。
- LLM 鸟倾向停在 flock 边缘、与 flock 中心保持更远距离;heading difference 上 Hybrid 与 NetLogo 的 Cohen's d≈0.16(效应小),但 Levene/Brown-Forsythe/Kruskal p 值极低(方差与分布显著不同)。
- LLM 鸟碰撞数(d≤1)远低于 rule-based 鸟(Figure 11);平均邻居数(Table 4):Hybrid(LLM)6.27、Hybrid(NetLogo)9.23、NetLogo 11.42,体现 LLM 鸟更"保守"。

讨论指出两大局限:计算时间与成本(每步 LLM 交互需秒级,远慢于 rule-based 的毫秒级,但对小规模探索性仿真仍可行);以及对外部模型/API 的依赖。作者强调框架不绑定 GPT-4o,可换用开源或本地部署 LLM;且在 2024 年 6 月前评估过多个 LLM,GPT-4o 最可靠,其他模型常出现随机丢食物等不稳定行为。代码与数据开源(github.com/crjimene/swarm_gpt)。

## 在本 wiki 中的位置

本文把 [[llm-multi-agent]] 与 [[multi-agent-systems]] 的研究从拟人化的 [[generative-agents]] / [[role-playing-agent]] 推向非语言的 swarm intelligence 领域,把 LLM 当作去中心化的 [[emergent-abilities]] 行为引擎。与强调显式编程规则的传统 [[agent-based-modeling]] 不同,它通过 [[prompt-engineering]](structured rule-based vs knowledge-driven 两类 prompt)与迭代 prompt tuning 驱动 [[gpt-4]] 生成 agent 动作,并借助 [[chain-of-thought]]("rationale" 键)提升数值推理质量。可与本 wiki 中关于 LLM-agent 协作、grounding 与 [[world-model]] 的条目互参。
