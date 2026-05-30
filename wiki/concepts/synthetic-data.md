---
type: concept
subtype: method
tags: [synthetic-data, data-generation, llm, distillation, simulation]
created: 2026-05-30
updated: 2026-05-30
sources: 9
---

# 合成数据 (Synthetic Data)

合成数据指由模型/仿真**生成**而非真实采集的训练或评测数据。LLM 时代它成为缓解数据稀缺、隐私与标注成本的关键手段:
用强模型生成指令、推理轨迹、对话、用户行为等,再回灌训练或评测。

## 主要用途
- **指令 / 对齐数据**:自举指令([[2023-star-self-taught-reasoner|STaR]] 拒绝采样推理轨迹、self-instruct 风格)、批评/偏好数据([[2023-shepherd-critic-for-lm-generation]])。
- **角色 / persona**:[[2025-opencharacter-role-playing-synthetic-personas]]、[[persona-driven-data-synthesis]] 合成多样人格数据。
- **用户 / 社会行为模拟**:用 LLM agent 生成合成用户日志与社会数据,是 [[generative-social-simulation]] 的一大应用([[2023-concordia-generative-agent-based-modeling]] 的合成用户研究、[[2024-lusifer-llm-user-simulation]]);
  "硅样本"奠基见 [[2023-out-of-one-many-llm-simulate-human-samples]]。
- **冷启动 / 数据增强**:推荐中造反事实样本([[2025-caserec-counterfactual-augmentation-system-exposure]])。

## 风险与争议
- **保真度 / 偏差**:合成数据可能复制并放大模型偏见,或与真实分布失配——需外部校准(呼应 [[generative-social-simulation]] 的"验证"争议)。
- **模型崩溃 (model collapse)**:用自身输出反复训练会退化,需混入真实数据。
- **数据泄漏 / 评测污染**:合成评测可能与训练分布重叠([[2025-emergent-llm-behaviors-data-leakage]])。

## 相关页
[[knowledge-distillation]]、[[generative-social-simulation]]、[[user-simulation]]、[[star-self-taught-reasoner]]、[[persona-driven-data-synthesis]]
