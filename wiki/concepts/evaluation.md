---
type: concept
subtype: method
tags: [evaluation, metrics, analysis]
created: 2026-05-29
updated: 2026-05-29
sources: 8
---

# Evaluation

评估(Evaluation)指通过指标、实验或分析手段,系统性地衡量模型、方法或系统的性能、行为与局限,从而验证假设并指导改进。

## 在本 wiki 中的出现

- [[2024-feature-level-bias-ctr]]:采用自上而下的分析式评估方法,揭示 CTR 模型的 feature-level bias 主要源自线性部分,并据此评估"移除/重建线性权重"这一极简非侵入式去偏策略的有效性。
- [[2025-debias-can-be-unreliable]]:揭示用随机曝光数据集传统评估去偏推荐不可靠,提出 URE 方案无偏估计全曝光数据上的 Recall@K。
- [[2024-scenario-wise-rec]]:首个面向多场景推荐(MSR)的开源 benchmark,整合 6 个公开数据集、12 个基线模型与统一的数据处理/训练/评测流水线,并在工业广告数据集上验证。
- [[2025-emergent-llm-behaviors-data-leakage]]:批判性短文:LLM 多智能体模拟中"自发涌现的社会约定"在观测上等价于 data leakage——模型只是复述预训练中已知的协调博弈知识,而非真正自组织。
- [[2025-pub-personality-user-behaviour-simulator]]:PUB 是一个基于 LLM 的用户行为模拟器,把 Big Five 人格特质嵌入用户建模,从行为日志推断人格并生成高保真合成交互,用于推荐系统的离线评估。
- [[2025-llm-agent-evaluation-survey]]:SAP Labs 的 LLM agent 评测综述,提出"评测目标 × 评测过程"二维分类法,并强调企业落地中的可靠性、合规与 RBAC 等挑战。
- [[2026-convapparel-user-simulator-validation]]:Google 提出 ConvApparel(4,146 段人-AI 服装购物对话、双 agent good/bad 协议、逐轮第一人称标注)及 PLSA+HLS+counterfactual validation 三支柱框架,系统量化 LLM user simulator 的 realism gap,发现所有 simulator 平均 HLS 仅 0.004,但 ICL/SFT 在反事实泛化上优于纯 prompting。
- [[2026-memory-for-autonomous-llm-agents]]:一篇 LLM agent 记忆综述,把 agent memory 形式化为 POMDP 内的写入-管理-读取循环,提出三维分类法、五类机制、四层评测栈与工程实践,覆盖 2022 至 2026 年初。

## 相关

- [[bias]]
- [[debiasing]]
- [[ctr-prediction]]
