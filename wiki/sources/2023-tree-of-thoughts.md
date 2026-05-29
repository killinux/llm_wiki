---
type: source
subtype: paper
tags: [reasoning, prompting, search, llm, planning]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2305.10601
raw: raw/2305.10601.pdf
authors: [Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan]
year: 2023
---

Tree of Thoughts (ToT) 把 LLM 推理建模为在「思考(thought)」树上的搜索,让模型能探索多条推理路径、自评估、前瞻与回溯,从而在需要规划与搜索的任务上大幅超越 [[chain-of-thought]]。

## 问题

主流 LLM(如 [[gpt-4]]、[[palm]])在推理时仍依赖 token 级、从左到右的自回归生成,本质上类似认知科学里快速、无意识的「System 1」。这种机制在需要探索、战略性前瞻、或初始决策起决定性作用的任务上会失败:一旦早期某步走错,既无法尝试其它分支,也无法回溯纠正。作者借鉴 Newell、Shaw、Simon 1950 年代提出的「问题求解=在组合问题空间(树)中搜索」的经典 AI 思想,试图为 LLM 补上一个更审慎的「System 2」规划过程。

## 方法

[[tree-of-thoughts]] 把任意问题表述为对一棵树的搜索,每个节点是一个状态 s = [x, z_{1...i}],即输入加上目前为止的思考序列。一个具体实例由四个设计问题构成:

- **思考分解(Thought decomposition)**:利用问题结构把中间过程拆成思考步;一个思考可以是几个词(填字)、一行等式(24 点)或一整段写作计划(创意写作)。
- **思考生成(Thought generator)**:每个状态生成 k 个候选,两种策略——(a) 从 CoT prompt 独立采样(适合思考空间丰富),(b) 用「propose prompt」顺序提议(适合受限空间)。
- **状态评估(State evaluator)**:让 LM 对各状态评估求解进展,作为搜索启发式,两种策略——(a) 对每个状态独立打分/估值,(b) 跨状态投票;均可借助前瞻模拟与常识。
- **搜索算法(Search algorithm)**:可插拔,论文用了 BFS(每步保留最有希望的 b 个状态)与 DFS(深入最有希望状态,直到出解或被评估器判为不可解时回溯)。

ToT 无需额外训练,直接用预训练 LM 即可;[[input-output-prompting]]、CoT、[[self-consistency]] 与 self-refinement 都可视为 ToT 的特例。

## 结果

实验全部基于 [[gpt-4]],跨三个新任务:

- **[[game-of-24]]**:100 个较难题(索引 901-1000)。IO 7.3%、CoT 4.0%、CoT-SC(k=100)9.0%;ToT(b=1)已达 45%,ToT(b=5)达 **74%**。IO/CoT 即使 best-of-100 也只有 33%/49%。CoT 错误分析显示约 60% 的样本在生成第一步(前三个词)后就已注定失败。
- **创意写作(Creative Writing)**:输入 4 个随机句子,要求输出 4 段、每段以对应句子结尾的连贯文章。GPT-4 连贯性打分(1-10):IO 6.19、CoT 6.93、ToT **7.56**;人工成对评比中 100 对里 41 对偏好 ToT、仅 21 对偏好 CoT。迭代精修把 IO 从 6.19 提到 7.67、ToT 从 7.56 提到 7.91。
- **[[mini-crosswords]]**(5x5,20 个测试游戏,用 DFS):IO 字母/单词/整局 = 38.7%/14%/0%,CoT = 40.6%/15.6%/1%,ToT = **78%/60%/20%**(解出 4/20 局)。去掉剪枝或回溯的消融均会损害性能。

局限:ToT 比采样类方法消耗更多资源(如 GPT-4 API 成本),但模块化设计允许用户自定义性能-成本权衡;对 GPT-4 本已擅长的任务未必需要。

## 在本 wiki 中的位置

ToT 是 [[chain-of-thought]] 的直接泛化,与 [[self-consistency]] 同属「推理时计算(inference-time compute)」与提示工程脉络,但首次系统性地把经典 [[tree-search]](BFS/DFS)与 LLM 推理结合,为后续 agent / 规划 / 推理时搜索类工作(如以搜索增强推理、过程奖励)提供了框架性参照。
