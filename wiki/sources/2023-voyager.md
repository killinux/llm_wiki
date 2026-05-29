---
type: source
subtype: paper
tags: [llm-agent, embodied-agent, lifelong-learning, minecraft, gpt-4, code-generation, autonomous-agent]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2305.16291
raw: raw/2305.16291.pdf
authors: [Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, Anima Anandkumar]
year: 2023
---

VOYAGER 是首个由 LLM 驱动的、在 Minecraft 中持续探索并终身学习的具身智能体,通过黑盒调用 [[gpt-4]] 自动生成可执行代码技能,无需任何模型微调即可不断习得新技能并做出新发现。

## 问题

在开放世界中构建能够持续探索、规划并发展新技能的通用智能体是 AI 领域的重大挑战。经典方法依赖[[reinforcement-learning]](RL)和模仿学习,在原始动作空间上操作,难以做到系统化探索、可解释性与泛化。已有的 LLM 智能体虽能利用预训练知识生成动作计划,但缺乏一种机制让智能体在没有人类干预的情况下持续积累、复用并组合越来越复杂的技能,同时避免灾难性遗忘(catastrophic forgetting)。

## 方法

VOYAGER 通过黑盒查询 [[gpt-4]],由三个核心组件构成:

- **自动课程(Automatic Curriculum)**:由 GPT-4 根据智能体当前状态、技能水平、已完成与失败的任务,提出由易到难的任务,目标是"发现尽可能多样的事物",从而最大化探索。
- **技能库(Skill Library)**:把每个技能表示为一段可执行代码(从一个状态转移到另一个状态),由 GPT-4 生成;每个技能以其描述的 embedding 建立索引,便于在相似情境下检索复用。技能具有时序延展、可解释、可组合的特点,缓解灾难性遗忘。
- **迭代提示机制(Iterative Prompting)**:把代码当作动作空间(code as action space),结合三类反馈进行自我改进——环境反馈、执行错误、以及由独立 GPT-4 智能体执行的自我验证(self-verification),用以判断任务是否成功并驱动程序迭代。

实验环境基于 [[minedojo]] 框架与 Mineflayer JavaScript API 控制智能体;除技能检索使用 text-embedding-ada-002 外,所有组件均使用 gpt-4-0314。这是一种典型的 [[llm-agent]] 与 [[code-generation]] 结合的范式。

## 结果

- **探索能力**:在 160 次提示迭代内发现 63 种独特物品,是次优方法的 3.3×;[[autogpt]]、[[react]]、[[reflexion]] 分别只发现 19、9、11 种。
- **科技树掌握(Tech Tree)**:解锁木质工具快 15.3×、石质工具快 8.5×、铁质工具快 6.4×,且是唯一解锁钻石工具等级的方法;VOYAGER 平均分别在 6、11、21、102 次提示迭代解锁木、石、铁、钻石,而基线方法基本无法制作工具。
- **地图覆盖**:遍历的距离是基线的 2.3×,基线常困于局部区域。
- **零样本泛化**:清空物品栏并重置到新生成的世界后,VOYAGER 能持续解决所有未见任务,而基线在 50 次提示迭代内无法解决任何任务。
- **消融实验**:在自动课程、技能库、环境反馈、执行错误、自我验证、GPT-4 vs GPT-3.5 六个设计上做消融;自我验证是最关键组件(移除后性能下降最大),且 GPT-4 在代码生成上显著优于 GPT-3.5。

## 在本 wiki 中的位置

VOYAGER 是 [[llm-agent]] 方向的代表性工作,展示了"代码即动作 + 技能库 + 自我验证"的[[lifelong-learning]]范式。它与 [[react]]、[[reflexion]]、[[autogpt]] 等智能体框架同属一个谱系,但强调无需微调、依靠 in-context 持续学习与技能复用。可与 [[gpt-4]] 作为基座模型、[[code-generation]] 作为动作表示、[[minedojo]] 作为评测环境等条目互相参照。
