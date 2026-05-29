---
type: source
subtype: paper
tags: [llm-agent, recommender-system, planning, llm-for-recommendation, self-inspiring]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2308.14296
raw: raw/2308.14296.pdf
authors: [Yancheng Wang, Ziyan Jiang, Zheng Chen, Fan Yang, Yingxue Zhou, Eunah Cho, Xing Fan, Xiaojiang Huang, Yanbin Lu, Yingzhen Yang]
year: 2023
---

# RecMind: Large Language Model Powered Agent For Recommendation

RecMind 是一个由 LLM 驱动的自主推荐 agent,通过规划、记忆与外部工具实现 zero-shot 个性化推荐,并提出 Self-Inspiring (SI) 规划算法以保留所有已探索状态来增强规划能力。

## 问题

[[large-language-models]] 在多种任务上表现出色,但直接用于推荐任务面临挑战:LLM 训练于通用语料,缺乏推荐所需的领域知识;难以获取最新信息与外部知识;在个性化推荐所需的复杂推理与规划上能力不足。与此同时,传统基于 [[deep-neural-network]] 的 [[recommender-system]] 通常只针对特定任务训练,缺乏泛化到新的、未见过的推荐任务的能力。本文旨在构建一个能利用外部工具与知识、无需任务专门训练即可完成多种推荐任务的 [[llm-agent]]。

## 方法

RecMind 是一个用于推荐任务的 [[llm-based-agents]],由三个关键组件构成:

- **Planning(规划)**:将复杂推荐任务分解为可执行的中间步骤。本文提出 **Self-Inspiring (SI)** 规划算法:在每个中间步骤,LLM 会"自我启发"(self-inspire),综合考虑所有先前已探索的状态来规划下一步。与 [[chain-of-thought]](单一推理路径)以及 [[tree-of-thoughts]](可能丢弃部分已探索路径)不同,SI 保留全部已探索状态,从而更好地利用历史信息并探索多条推理路径。
- **Memory(记忆)**:[[memory-module]] 包含个性化记忆(用户历史交互、评论等用户特定信息)与世界知识(item 元数据与领域知识)。
- **Tools(工具)**:配备数据库工具(从结构化数据库检索)、搜索工具(从网页检索)与文本摘要工具,实现 [[tool-use]] 以访问外部知识与计算。

RecMind 借鉴了 [[react]]、[[reflexion]]、[[toolformer]] 等 LLM 自主 agent 工作的思路,但将其应用到推荐场景。backbone 使用 [[gpt-3-5-turbo]] 与 [[gpt-4]],整体以 zero-shot 方式工作。

## 结果

在三个不同领域数据集上评测:[[amazon-reviews]](Beauty)、[[yelp-dataset]]、[[movielens]],覆盖电商、商业、电影推荐场景。共评测五类推荐任务:rating prediction、sequential recommendation、direct recommendation、explanation generation、review summarization。baseline 包括全量训练模型(MF、MLP、[[p5]])与 LLM 方法([[chatgpt]] 的 zero-shot、few-shot、CoT、ReAct)。

在 Amazon Beauty 上的主要数字(RecMind-SI few-shot 为最佳配置):

- **Rating prediction**:RecMind-SI (few-shot) 取得 RMSE 1.0756、MAE 0.6892,优于 ChatGPT zero-shot(RMSE 1.4173),且优于全量训练的 P5(RMSE 1.2982),也优于 MF/MLP/AFM 等传统模型。
- **Direct recommendation**:RecMind-SI (few-shot) HR@5 0.0915、NDCG@5 0.0624,优于 ChatGPT 系列与多数 LLM baseline,但仍低于全量训练的 P5(HR@5 0.1478)与 ENMF。
- **Sequential recommendation**:RecMind-SI (few-shot) HR@5 0.0415、NDCG@5 0.0289,达到与全量训练 P5(HR@5 0.0459)、S^3-Rec 可比的水平。
- **Explanation generation**:RecMind-SI (few-shot) BLEU2 1.3459、ROUGE2 2.7479,优于其他 LLM 方法,与全量训练 P5 可比。

一致的现象:在 rating prediction 上 RecMind 多种规划机制甚至超过全量训练模型(因其可同时访问用户对不同 item 的评分历史与 item 收到的他人评分);而在 direct/sequential recommendation 等需处理长候选列表(100 个 item)的任务上,受限于 LLM 的长上下文与 position bias,RecMind 仍弱于 P5。

消融与扩展实验:

- **规划方法对比**:在通用推理任务上,SI 优于 CoT 与 ToT。Game of 24 上 accuracy 分别为 CoT 4%、ToT 74%、SI 80%;Mini Crosswords 上 SI 的 game-level accuracy 26%(ToT 20%、CoT 1%)。
- **运行时间**:Beauty 域上 SI 平均推理时间 29.7s,低于 ToT 的 53.2s(SI 仅在当前步不够好时才探索替代分支)。
- **foundation LLM 鲁棒性**:在 Llama2-70b、text-davinci-003、GPT-3.5、GPT-4 上 RecMind-SI 表现稳定,对 backbone 选择不敏感。
- **跨域迁移**:few-shot 示例取自 Beauty 域,迁移到 Toys/Sports 域时 RecMind 优于 P5 与 ChatGPT,表明 P5 等微调模型易过拟合训练域。

总体上 RecMind 超过现有 zero/few-shot LLM 推荐方法,并在多任务上达到与全量训练推荐模型可比甚至更优的性能。

## 在本 wiki 中的位置

本文处于 [[llm-agent]] 与 [[recommender-system]] 的交叉点,是将 [[llm-based-agents]] 范式(planning + [[memory-module]] + [[tool-use]])迁移到推荐任务的代表性工作。其 Self-Inspiring 规划可与 [[chain-of-thought]]、[[tree-of-thoughts]]、[[react]] 等推理/规划方法对照阅读;在 [[llm-for-recommendation]] 方向上,可与全量训练的 [[p5]] 范式形成对比。
