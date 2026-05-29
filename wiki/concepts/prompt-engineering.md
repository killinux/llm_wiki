---
type: concept
subtype: method
tags: [prompting, reasoning, in-context-learning, llm]
created: 2026-05-29
updated: 2026-05-29
sources: 8
---

# Prompt Engineering

Prompt Engineering 指通过精心设计输入提示(prompt)的内容与结构,在不更新模型参数的前提下引导大语言模型(LLM)产生更准确、更可控的输出的一类方法。

## 在本 wiki 中的出现

- [[2022-chain-of-thought]]:该论文提出 chain-of-thought prompting,是一种代表性的 prompt engineering 技术——在 few-shot 示例中显式加入中间推理步骤,从而显著提升大模型的多步推理能力;这一增益随模型规模而涌现(PaLM 540B 在 GSM8K 上达到 57%)。
- [[2023-plan-and-solve-prompting]]:该论文提出零样本 Plan-and-Solve(PS / PS+)提示,属于 prompt engineering 中的零样本提示设计——让 LLM 先制定计划再分步执行子任务,从而显著改进 Zero-shot-CoT 的多步推理表现。
- [[2025-llm-multi-agent-swarm-intelligence]]:把 agent-based modeling 中 agent 的硬编码程序替换为 GPT-4o 驱动的 prompt,在蚁群觅食与鸟群 flocking 两个经典 swarm intelligence 场景中复现并诱导涌现集体行为。
- [[2023-chain-of-verification]]:Chain-of-Verification (CoVe) 让 LLM 先生成草稿,再独立回答自我规划的验证问题来核查事实,显著降低幻觉。
- [[2024-lusifer-llm-user-simulation]]:提出 Lusifer:基于 LLM 的用户模拟环境,在每次交互后增量更新可解释的用户画像,为 RL-based 推荐系统生成动态真实的用户反馈,并在 cold-start 场景超越传统协同过滤基线。
- [[2025-self-surrogate-light-feature-selection]]:提出 SELF,用多个 LLM 的世界知识对特征做语义排序、再以轻量 bridge network 融合任务信号,缓解深度推荐系统特征选择对 surrogate model 的依赖。
- [[2024-prompt-tuning-item-cold-start]]:PROMO 用高价值正反馈(pinnacle feedback)替代内容描述作 prompt,并为每个 item 构造个性化 prompt network,同时缓解 item cold-start 推荐的数据成本与热门偏置,已在快手十亿用户级平台部署。
- [[2026-policysim-proactive-policy-optimization]]:PolicySim 是一个基于 LLM 智能体的社会模拟沙盒,用 SFT+DPO 训练用户智能体、用带消息传递的 contextual bandit 自适应优化推荐与曝光控制等平台干预策略,实现部署前的主动评估与优化。

## 相关

- [[chain-of-thought]]
- [[zero-shot-cot]]
- [[plan-and-solve]]
- [[in-context-learning]]
- [[few-shot-prompting]]
- [[reasoning]]
- [[large-language-models|large-language-model]]
