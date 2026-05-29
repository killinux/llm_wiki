---
type: source
subtype: paper
tags: [role-playing, persona-simulation, dataset, llm-agent, llm-as-judge, multi-agent, evaluation, given-circumstance-acting]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2502.09082
raw: raw/2502.09082.pdf
authors: Xintao Wang, Heng Wang, Yifei Zhang, Xinfeng Yuan, Rui Xu, Jen-tse Huang, Siyu Yuan, Haoran Guo, Jiangjie Chen, Shuchang Zhou, Wei Wang, Yanghua Xiao
year: 2025
---

CoSER 是一个面向"已知文学角色"的高质量角色扮演数据集与框架,从 771 部名著中抽取 17,966 个角色的真实多角色对话,并提出 given-circumstance acting(GCA)来训练与评测角色扮演 LLM,据此训练出 CoSER 8B/70B 开源模型。

## 问题

Role-playing language agents(RPLAs,角色扮演语言智能体)是 [[large-language-models]] 的重要应用,但模拟"已确立的角色"(established characters)面临两大瓶颈:

- **数据**:现有数据集大多局限于两个角色之间的对话,缺少对话上下文与多形态知识;且很多数据由 LLM 合成(如 RoleLLM、PersonaHub),牺牲了对原著的真实性(authenticity)与忠实度(fidelity)。
- **评测**:现有方法多聚焦单轮、预设问题的交互,要么用 [[llm-as-judge]](存在长度/位置偏置等),要么用多选题(只测特定方面),缺乏基于真实角色数据的合适评测协议。

## 方法

作者提出 CoSER,包含数据集、开源模型与评测协议三部分。

- **CoSER 数据集**:数据源自 Goodreads "Best Books Ever" 榜单的 771 部名著,经一条 [[claude]](Claude-3.5-Sonnet)驱动的 LLM 流水线(分块 chunking、抽取 plot/conversation、统一角色名、聚合并生成角色画像)处理。数据按 plot / conversation / character 三层组织,涵盖对话、场景设定、角色动机、剧情摘要、角色经历与角色画像。关键创新是把消息空间从单一"言语(speech)"扩展为 **speech / action / thought** 三个维度,使 RPLA 能表达内心想法与肢体动作(thought 对其他角色不可见,形成信息不对称);并把 environment 作为一个特殊角色 e 来建模环境反馈。
- **Given-Circumstance Acting(GCA)**:借鉴 Stanislavski 的表演方法论。训练时,让 LLM 在给定场景 S、角色画像与动机的指令下,逐个扮演对话中每个角色 c,只对该角色的真实台词 M_c 做优化(属于 [[instruction-tuning]] / [[fine-tuning]],基于 [[llama-3]](LLaMA-3.1 Instruct)训练出 CoSER 8B 与 70B,并混入 Tulu-3 数据保持通用能力)。
- **GCA 评测**:两阶段。1)**多智能体模拟(multi-agent simulation)**:为测试对话构建多智能体系统,actor LLM 在相同设定下扮演每个角色,配合 next speaker prediction(NSP)与环境模型生成完整模拟对话 M̄(最多 20 轮,可设 continue-from 参数 k);属于 [[llm-multi-agent]] / [[multi-agent-systems]] 框架,也与 [[user-simulation]] / [[social-simulation]] 思路相通。2)**惩罚式 LLM 评判(penalty-based LLM judging)**:LLM critic(默认 [[gpt-4o]])对照原始对话,按 rubric 找出 flaw 实例并按严重度 1–5 扣分,沿四个维度评估:Anthropomorphism、Character Fidelity、Storyline Quality、Storyline Consistency,并做长度校正(λ=1.5)。

## 结果

- **数据规模**:771 部书、30,069 个 plot、29,798 段对话、17,966 个角色、392,298 条 utterance;平均每段对话约 13.2 条 utterance。
- **CoSER Test**:200 段留出对话(100 in-domain + 100 out-of-domain)。CoSER 70B 在 LLM 评判与 N-gram 指标上达到 SOTA,平均分 59.06,超过所有开源模型,与 [[gpt-4o]](59.95)相当;BLEU 10.10 / ROUGE-L 14.78,N-gram 第二名领先 58%。CoSER 8B 平均分 56.45,优于同量级模型。
- **现有 benchmark**(多选题):CoSER 70B 取得 SOTA,InCharacter(BFI)75.80%、LifeChoice 93.47%(比 GPT-4o 高 23%)、CroSS-MR 64.49%。([[benchmark]] / [[evaluation]])
- **人评**:60 个样本、7 个模型,CoSER 70B 平均分 6.783、胜率 86.9%,均为最高;结果与 GCA 评测一致,验证了评测协议可靠性。
- **消融**:加入 inner thoughts 与 motivations 在测试期与训练期都稳定提升表现;去掉 inner thoughts 训练的变体一致变差。检索增强中,检索角色"经历(Expr.)"与"对话(Conv.)"有效提升表现(尤其 CoSER 70B),而检索原始 raw text 几乎无增益。判官对齐分析显示 DeepSeek-R1 与人评对齐最高(77.5%)。

## 在本 wiki 中的位置

CoSER 把"角色扮演/[[role-playing-agent]]"从 LLM 合成数据推进到基于名著的真实多角色数据,并用 [[llm-multi-agent]] 模拟 + [[llm-as-judge]] 构成评测闭环,与 [[generative-agents]] 等 [[social-simulation]] 工作、以及 [[user-simulation]] 方向相邻;其 GCA 训练范式属于 [[instruction-tuning]] / [[fine-tuning]] 在角色扮演上的落地,可与 [[retrieval-augmented-generation]] 检索增强、[[in-context-learning]](continue-from k 类似上下文示例)结合阅读。
