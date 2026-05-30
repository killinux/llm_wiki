---
type: source
subtype: paper
tags: [llm-agents, social-simulation, computational-social-science, survey-simulation, algorithmic-fidelity, foundational]
created: 2026-05-30
updated: 2026-05-30
arxiv: 2209.06899
raw: raw/2209.06899.pdf
authors: [Lisa P. Argyle, Ethan C. Busby, Nancy Fulda, Joshua Gubler, Christopher Rytting, David Wingate]
affiliations: [Brigham Young University]
venue: "Political Analysis (2023), 31(3)"
year: 2022
---

# Out of One, Many: Using Language Models to Simulate Human Samples

LLM 社会模拟的**奠基论文之一**(BYU 团队,arXiv 2209.06899v1 2022-09;正式发表于 *Political Analysis* 2023)。核心论点:
[[gpt-3]] 的"算法偏见"并非铁板一块,而是**细粒度且与人口学相关**的——只要恰当 conditioning,模型就能准确**复刻各类人类子群体
的回答分布**。作者把这一性质命名为 **algorithmic fidelity(算法保真度)**。

## 问题
学界通常把 LLM 的 **algorithmic bias** 当作模型的一个**单一、宏观**缺陷去消除。作者提出相反视角:这种"偏见"其实是人类中
**观念 / 态度 / 语境之间多种关联模式**的复杂映射——"模型里不止一种偏见,而是许多种"。因此通过对模型条件化于带有目标身份与
人格画像的"虚拟个体",可以从一个庞大且常相互矛盾的回答集合中**精确选择**出对应子群体的回答。

## 方法
- **silicon samples / silicon sampling(硅样本)**:把真实大型调查中数千份**社会人口学背景故事 (backstory)** 注入 GPT-3 作为条件,
  生成与人类样本可比的合成回答;并讨论如何用它**校正偏斜的边缘分布**。
- 三项研究:**Study 1** 自由文本党派联想;**Study 2** 投票预测(基于 ANES 等美国选举调查数据);**Study 3** 封闭式问题与人类数据中的复杂相关结构。
- 全文附带成本分析(附录 E)。

## 结果
- **Study 1(自由文本党派联想,Pigeonholing Partisans)**:用 silicon sampling 生成词表,雇 **2,873** 名 Lucid 评审盲评 **7,675** 条文本。
  **类图灵测试**:评审把 **61.7%** 的真人文本判为"人写"、把 GPT-3 文本判为"人写"的比例为 **61.2%**(差异 p=0.44,**不可区分**)。
  内容特征也高度一致:提及人格特质的比例真人 72.3% vs GPT-3 66.5%,被判"极端"的 39.8% vs 41.0%。据词表猜党派:真人文本 60.1% 正确、
  GPT-3 文本 52.8% 正确(均显著高于 33% 随机)。
- **Study 2(投票预测,ANES 2012/2016/2020)**:GPT-3 硅样本与真实两党投票比高度吻合——Romney 2012:**0.391 vs 0.404**;
  Trump 2016:**0.432 vs 0.477**;Trump 2020:**0.472 vs 0.412**。存在轻微系统偏差;且 GPT-3 训练语料截至 2019,2020 数据构成**时间外**测试。
- **Study 3**:封闭式问题上 GPT-3 复现了人类数据中的复杂相关结构。
- 作者据此提出四条判据:Turing Test、Backward Continuity、Forward Compatibility、Pattern Correspondence,论证语言模型具足够
  **algorithmic fidelity** 时可作社会科学的**硅样本 / 合成受访者**;同时最早系统性警示其**代表性与偏见**风险。

## 在本 wiki 中的位置
是 [[generative-social-simulation]] 整条线的**理论源头之一**:早于 [[2023-generative-agents]] 的"行为模拟",本文聚焦"**态度 / 回答分布**
模拟",其 **algorithmic fidelity** 概念后被 [[2023-concordia-generative-agent-based-modeling]] 直接用作验证标尺,也是
[[2026-generative-social-simulation-validation]] 综述讨论"外部扎根"的关键参照。与 [[2025-socioverse-world-model-social-simulation]]
(千万真实用户人口学对齐)、[[2024-generative-agents-self-reports]](以真人自述接地的个体模拟)思路一脉相承。
连接 [[user-simulation]]、[[computational-social-science]]、[[gpt-3]]。
