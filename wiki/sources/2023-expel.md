---
type: source
subtype: paper
tags: [llm-agent, in-context-learning, experiential-learning, memory, transfer-learning, prompt-based]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2308.10144
raw: raw/2308.10144.pdf
authors: [Andrew Zhao, Daniel Huang, Quentin Xu, Matthieu Lin, Yong-Jin Liu, Gao Huang]
year: 2023
---

ExpeL(Experiential Learning)是一种让 LLM Agent 在**不更新参数**的前提下,从一组训练任务的成功/失败经验中自主积累经验、用自然语言抽取跨任务洞见(insights),并在推理时召回相似成功轨迹作为 few-shot 示例的方法。

## 问题

把 LLM 用于决策任务有两条主流路径,各有缺陷:

- **微调**(finetuning)需要大量环境交互或人工标注数据,计算成本高,且会损害模型原有的泛化能力;
- **prompt-based 规划**(如 [[react-reasoning-and-acting]])只用少量 in-context 示例,但受限于上下文窗口,Agent 对已经历过的任务"没有记忆",无法在 demonstration 之外做任何学习。

此外,GPT-4、Claude 等最强模型的参数是闭源的、无法微调。因此需要一种新范式:让 Agent 从**经验**中学习,而不依赖参数更新。论文还指出,像 [[reflexion]] 这类自我改进方法只能在**同一任务内**反复重试改进(intra-task),缺乏**跨任务**(inter-task)的记忆与迁移能力。

## 方法

ExpeL 分三个阶段(对应类比:学生反复做练习题、考前总结心得、考试时调用记忆):

1. **经验收集(Experience Gathering)**:以 [[reflexion]] 为基础,Agent 用 [[react-reasoning-and-acting]] 作为底层规划算法,对每个训练任务最多重试 Z 次;失败时做 self-reflect 再重试。所有成功与失败轨迹存入 experience pool。

2. **洞见抽取(Insight Extraction)**:把经验池分两种方式利用——对比"同一任务"的失败 vs 成功轨迹找出错误模式;在一组成功轨迹中识别共性"最佳实践"。让 instruction-following LLM 对一个洞见列表执行 `ADD` / `EDIT` / `UPVOTE` / `DOWNVOTE` 四种操作并维护 importance count(计数归零则删除),从而提炼出泛化的、高层级的自然语言规则。默认用 `gpt-4-0613` 做抽取(实验证明优于 `gpt-3.5-turbo`)。

3. **任务推理(Task Inference)**:评估时用 Faiss 向量库 + kNN + `all-mpnet-base-v2` embedder,按任务相似度召回 top-k 成功轨迹作为 few-shot 示例,并把全部抽取出的洞见拼接进任务描述。

此外提出**迁移学习**:把源任务抽取的洞见用少量目标任务 few-shot 示例"finetune"(prompt 层面改写),迁移到新任务分布。

## 结果

在四个文本 benchmark 上评估(底层动作用 `gpt-3.5-turbo-0613`,temperature 0):[[hotpotqa]](知识密集问答)、[[alfworld]](家居环境)、[[webshop]](网购环境)、[[fever]](事实核查,用于迁移)。

- **主结果(成功率)**:ExpeL 全面超越 ReAct 与 Act 基线。HotpotQA 39%(ReAct 28%、Act 29%);ALFWorld 59%(ReAct 40%、Act 37%);WebShop 41%(ReAct 35%、Act 34%)。消融显示 insights-only 与 retrieve-only 都低于完整 ExpeL(HotpotQA 36%/31%,ALFWorld 50%/55%),说明洞见抽取与相似度召回是**互补且协同**的。
- **跨任务学习 vs Reflexion**:ExpeL **不重试**即可匹配 Reflexion 在 HotpotQA R3 的成绩(40% vs 39%),并在 ALFWorld 超过它(54% vs 59%)。
- **迁移学习(HotpotQA→FEVER)**:ExpeL Transfer 达 70%,优于 ReAct 63%、Act 58%,且带 few-shot demos 的迁移(70%)优于不带 demos 的版本(65%)。
- **任务重试**:ExpeL+Reflexion 在 ALFWorld R0→R3 从 59.0% 提升到 64.2%,与 Reflexion 协同。
- **消融**:学到的洞见优于人工手写洞见(HotpotQA 39% vs 32%);在 success/fail 抽取中额外加入 reflections 反而有害(可能引入 hallucination,降到 29%);更强的 LLM 做抽取效果更好;in-context 示例用任务相似度召回(59%)优于 reason similarity(48.5%)和随机采样(42.5%)。

论文还观察到若干 emergent 行为:假设构建与约束自适应、world model 信念更新、self-correction(如 ALFWorld 中拿错物体后能纠正)。

## 在本 wiki 中的位置

ExpeL 把 [[reflexion]] 的单任务自反思扩展为**跨任务经验积累 + 洞见抽取 + 相似度召回**,核心机制是 [[agent-memory]] 与 [[in-context-learning]],无需 [[fine-tuning]]。它建立在 [[react-reasoning-and-acting]] 之上,召回机制本质上是一种 [[rag]]。与同期的 [[voyager]](Minecraft 技能库)、[[generative-agents]](记忆流)同属"带记忆/经验的 LLM Agent"路线;与 [[self-refine]]、[[critic]] 等 [[self-improvement]] 方法相比,ExpeL 强调的是 inter-task 的经验迁移而非单次输出精炼。
