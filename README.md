# LLM Wiki — 一个由 LLM 维护的 AI 研究知识库

这是一个关于**大语言模型与 AI 研究**的个人知识库,采用 Andrej Karpathy 提出的 **"LLM Wiki"** 思路构建:
**人类策展、LLM 维护**。

## 核心思路:Karpathy 的 "LLM Wiki" 模式

> 心智模型:**Obsidian 是 IDE,LLM 是程序员,wiki 是代码库。**

分工很清晰:

- **人类**负责策展——把感兴趣的论文/博客/报告丢进 `raw/`,提出问题,指定要分析的方向。
- **LLM(本库的 Claude)**充当**图书管理员与维护者**——读原文、写摘要、建立交叉引用、归档、维护目录与日志。人类**读** wiki,但**不写** wiki;写的事交给 LLM。

知识就这样**复利式累积**:每 ingest 一篇,就更新它触及的 10–15 个实体/概念页;每次有价值的查询,就沉淀成一篇综述。

## 三层架构

| 层 | 内容 | 谁来动 |
|---|---|---|
| **`raw/`** | 原始资料(PDF、文章、数据),**不可变的真相来源** | 只读;绝不修改/删除。体积大+版权,已 `.gitignore`,**不入库**(溯源见 `log.md`) |
| **`wiki/`** | LLM 生成的一切,知识库本体 | LLM 完全拥有 |
| **`CLAUDE.md`** | schema 与操作手册(页面规范、ingest/query/lint 流程) | 人机共同演进 |

`wiki/` 内部分四类:

- **`wiki/topics/`** — 跨多源的**综述与演化中的论点**(知识的最高层凝结)
- **`wiki/entities/`** — 具体命名实体:模型、机构、人物、数据集、benchmark、产品
- **`wiki/concepts/`** — 方法与思想:attention、RLHF、MoE、scaling law、强化学习、因果推断……
- **`wiki/sources/`** — 每篇已 ingest 资料的一页摘要(年份前缀)
- **`wiki/index.md`** — 总目录(按类别分组,始终保持最新)

根目录 `log.md` 是**追加式**操作日志(`## [日期] <op> | <标题>`)。

## 从哪里开始读

👉 **入口是 [`wiki/index.md`](wiki/index.md)** —— 全部页面的目录。

或直接读 9 篇 **topic 综述**(本库知识的骨架,均读原文核实、交叉成网):

**智能体方向**
- [[generative-social-simulation]] — 生成式社会模拟("斯坦福小镇"线)
- [[solving-agents-search]] — 求解类智能体:推理时搜索与成本-质量权衡
- [[llm-self-improvement]] — LLM 自我改进/自我纠错
- [[llm-agent-memory]] — LLM 智能体的记忆机制

**推荐系统方向**
- [[rl-for-recommendation]] — 推荐中的强化学习
- [[debiasing-causal-recommendation]] — 推荐去偏与因果推断
- [[recsys-architectures]] — 推荐架构演进(Transformer × GNN × 生成式)
- [[fairness-multistakeholder-welfare]] — 公平性与多边福利

**两者的缝合点**
- [[llm-agents-for-recommendation]] — 推荐中的 LLM 智能体

> 九篇共享一条贯穿全库的**"验证 / 可信度"元主线**(涌现是否数据泄漏、自我纠错是否真有效、记忆基准是否测到点子上、去偏评估是否可靠、模拟是否对齐真人……)。

## 约定速览

- **语言**:wiki 正文用**简体中文**;专有名词(模型名、benchmark、方法缩写)保留原文;frontmatter 字段用英文(机器字段)。
- **wiki-links**:用 Obsidian 风格 `[[page-name]]` 互链;指向尚未创建的页是合法的"待写标记"(Karpathy 模式:长尾按需补)。
- **frontmatter**:每页带 YAML(`type` / `tags` / `created` / `updated` / `sources` …)以便 Dataview 查询。
- **可溯源**:每个论断尽量链回 source 页,保持可追溯到 `raw/`;矛盾与被推翻的旧结论显式标注,不静默覆盖。

## 三种操作(详见 `CLAUDE.md`)

1. **Ingest** — 把新资料读进来,写 source 页 + 更新相关实体/概念页 + index + log。
2. **Query** — 直接提问,LLM 带引用作答,好答案可归档成 topic/concept 页。
3. **Lint** — 全库体检:矛盾、过时结论、孤儿页、悬空链接、缺失枢纽概念、index 漂移等。

## 当前规模

- **topics**: 9 · **concepts**: 458 · **entities**: 478 · **sources**: 274

---

*领域横跨两大簇:生成式智能体 / 社会模拟,与 推荐系统 / offline RL。由 Claude(Anthropic)按上述模式持续维护。*
