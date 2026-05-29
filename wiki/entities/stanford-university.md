---
type: entity
subtype: lab
tags: [university, research-lab, academia]
created: 2026-05-29
updated: 2026-05-29
sources: 6
---

# Stanford University

Stanford University 是位于美国加州的一所研究型大学,其研究人员在大语言模型推理等方向有相关工作。

## 在本 wiki 中的出现

- [[2022-star-self-taught-reasoner]]:作为提出 STaR(Self-Taught Reasoner)方法相关研究的所属机构。STaR 用少量 CoT 示例让模型自己生成推理过程,只保留答对的 rationale(并用 rationalization 从答错题反向补全)反复微调自身,从而 bootstrap 推理能力。
- [[2024-quiet-star]]:Quiet-STaR 让语言模型在每个 token 前生成隐式 rationale 来更好预测后续文本,以自监督方式从任意文本学会推理,zero-shot 提升 GSM8K(5.9%→10.9%)与 CommonsenseQA(36.3%→47.2%)。
- [[2024-generative-agents-self-reports]]:用基于真人深度访谈与问卷自述构建的 generative agents,可对单个个体在多种社会科学结果上做通用模拟,留出题目预测精度接近个体两周后的重测一致性。
- [[2025-sotopia-s4-social-simulation-system]]:面向非技术用户的快速、灵活、可扩展社会模拟系统,通过模拟引擎+RESTful API+Web UI,让研究者无需编程即可用自然语言设计、并行运行并自动评估多轮多方 LLM 社会交互。
- [[2025-multi-agent-llm-value-diversity]]:通过 Schwartz 价值观给 LLM 智能体注入价值多样性的多智能体社会模拟,发现价值多样性提升集体行为的价值稳定性、涌现与自发规则创造,但极端异质带来边际递减与不稳定。
- [[2026-entropy-guided-agentic-recommendation]]:提出 IDSS,用 Shannon 熵作为统一信号贯穿对话式推荐的偏好询问、排序与多样化呈现三阶段,在用户意图模糊时兼顾追问效率与残余不确定性驱动的多样化推荐。

## 相关

- [[chain-of-thought]]
- [[self-improvement]]
- [[rationalization]]
- [[fine-tuning]]
- [[generative-agents]]
- [[social-simulation]]
