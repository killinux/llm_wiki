---
type: source
subtype: paper
tags: [social-media-simulation, persona, dataset, llm-agent, privacy, next-action-prediction, computational-social-science]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2510.02343
raw: raw/2510.02343.pdf
authors: [Aurélien Bück-Kaeffer, Je Qin Chooi, Dan Zhao, Maximilian Puelma Touzel, Kellin Pelrine, Jean-François Godbout, Reihaneh Rabbany, Zachary Yang]
year: 2025
---

# BluePrint: A Social Media User Dataset for LLM Persona Evaluation and Training

提出隐私保护框架 SIMPACT 及其落地数据集 BluePrint(来自 Bluesky 2025 加拿大联邦大选讨论,683 万条 action、23.6 万用户),把社交媒体用户行为建模为"下一动作预测"任务,用行为 persona 聚类替代个体身份,用于训练和评估 LLM 社交媒体 agent。

## 问题

[[large-language-models]] 为大规模模拟社交媒体动态(信息扩散、社群形成、平台干预)提供了新机会,可以替代在人类受试者身上难以开展的实验。但 LLM-based 社交媒体 [[social-simulation|模拟]] 面临三个关键缺口:

- 缺乏标准化、行为基础扎实的数据资源用于微调和评估 LLM 作为真实社交媒体 [[llm-agents|agent]];现有数据集多聚焦对话生成、缺乏交互多样性。
- 缺乏一致的评估协议,使得进展难以衡量。
- 隐私问题限制了对真实用户数据的访问,削弱了模拟的真实性。

现有方法常依赖简化场景或合成/脚本化 persona,无法捕捉真实用户行为的复杂性(尤其是 like、follow、block 等非文本交互行为)。

## 方法

**SIMPACT(Simulation-oriented Persona and Action Capture Toolkit)** 是一个隐私保护的框架,把原始社交媒体数据转化为可用于 agent 训练的结构化资源:

- **用户聚类成行为 persona**:对每个用户的所有 post/quote/repost 用 `intfloat/multilingual-e5-large` 生成句向量并平均得到 user embedding,再用 constrained K-means(最小簇大小 10)聚成行为原型(如科学社群、体育粉丝、政治群体)。提供 K=2、25、100、1000 多粒度聚类。
- **隐私保护**:用 Presidio 做 [[pii|PII]] 移除与匿名化(邮箱、电话、IP 等替换为占位符);**时间戳混淆**(用簇内相对序号 1..N 替换精确 Unix 时间);**伪名化**(用 32-byte 密钥对每个会话线程的用户 ID 做哈希,同一线程内一致、跨线程不同,防止跨线程关联,符合 GDPR)。
- **next-action prediction 任务**:把用户行为建模为动作序列。定义 12 种 action,分 text-directed(post、reply、quote、post_update、post_delete、repost、unrepost、like、unlike)和 user-directed(follow、unfollow、block、unblock)两类。数据组织为 thread(以初始 post 开始,以一个用户 action 结束),建模目标是预测 thread 的最后一个动作。簇归属由该 thread 末尾动作的作者所属簇决定。

**BluePrint** 是 SIMPACT 的端到端落地:采集 2025 年 3 月加拿大联邦大选相关 Bluesky 公开数据(用官方 Jetstream 客户端,按 97 个政治关键词、43 个候选人/政党标识、11 个通用选举词过滤),仅保留英文、去除发帖≤1 的用户。

评估用两类指标:embedding 相似度(Maximum / Average Cosine Similarity、Jaccard Similarity on top-100 TF-IDF、JS Divergence)与动作预测的 F1,均在 cluster 级和 population 级计算;并辅以人类评估(给标注者看真实/生成 post 对,判断哪条是真人写的)。

## 结果

- 数据集规模:**683 万条 action(6.8M)、236,331 个不同用户**;25-原型版本统计见 Table 3。
- 评测模型:专有 [[gpt-4-1-mini|GPT-4.1-mini]]、[[o4-mini|o3-mini]];开源以 [[qwen2-5-instruct|Qwen2.5-7B-Instruct]] 为基座,并用 [[lora]] 微调两个版本(focal loss 与 cross-entropy loss),base 模型作为对照。
- 文本生成:微调模型在多数指标上大幅提升——population 级 **JS Divergence 降低约 2 倍、Jaccard Similarity 提升约 10 倍**,显示更好的词汇与分布对齐。
- 动作预测:微调模型的 F1 与未微调 baseline 相当,说明模型在生成真实内容上有进步,但**仍难以可靠预测用户在具体情境下会采取的动作**(开放挑战)。
- 人类评估(Fig 2,越低越好,0.5=无法区分):未训练模型被正确识别为 AI 的比例为 **71.9%**,而在 BluePrint 上微调后的最佳模型降到 **56.0%**(接近随机 50%),即更难与真人区分。

## 在本 wiki 中的位置

本文属于 [[social-simulation]] / [[human-behavior-simulation]] 与 [[computational-social-science]] 交叉方向,提供面向 [[llm-agents|llm-agent]] 的隐私保护 [[dataset]] 与评估 [[benchmark]]。与同类社交模拟平台 [[oasis]]、[[recagent]]、[[2023-s3-social-network-simulation]] 及 persona 建模工作 [[persona]]、[[persona-driven-data-synthesis]]、[[incharacter]] 相关,但独特之处在于结合真实 Bluesky 数据、文本与非文本动作、以及 [[pii]] 移除/时间戳混淆/伪名化等隐私保护机制。作者来自 [[mila]]、McGill University、Université de Montréal 等机构。
