---
type: concept
subtype: method
tags: [evaluation, interaction, agents, social-intelligence]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Interactive Evaluation

交互式评测(Interactive Evaluation)指通过让模型在动态环境或多轮交互场景中行动,根据其交互过程与结果来评估模型能力的评测方法,区别于基于静态数据集的单轮打分。

## 在本 wiki 中的出现

- [[2023-sotopia-social-intelligence-evaluation]]:SOTOPIA 提出一个开放式社交互动模拟环境与多维评测框架 SOTOPIA-EVAL,交互式地评估 LLM 智能体在目标导向社交场景中的社会智能,发现 GPT-4 在最难子集上的目标完成率显著低于人类。
- [[2024-generative-agents-self-reports]]:用基于真人深度访谈与问卷自述构建的 generative agents,可对单个个体在多种社会科学结果上做通用模拟,留出题目预测精度接近个体两周后的重测一致性。
- [[2026-convapparel-user-simulator-validation]]:Google 提出 ConvApparel(4,146 段人-AI 服装购物对话、双 agent good/bad 协议、逐轮第一人称标注)及 PLSA+HLS+counterfactual validation 三支柱框架,系统量化 LLM user simulator 的 realism gap,发现所有 simulator 平均 HLS 仅 0.004,但 ICL/SFT 在反事实泛化上优于纯 prompting。

## 相关

- [[social-intelligence]]
- [[llm-agents]]
- [[evaluation-framework]]
- [[goal-oriented-dialogue]]
- [[user-simulator]]
- [[counterfactual-validation]]
