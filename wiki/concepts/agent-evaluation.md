---
type: concept
subtype: method
tags: [llm-agents, evaluation, benchmark, llm-as-judge, multi-agent]
created: 2026-05-30
updated: 2026-05-30
sources: 10
---

# 智能体评测 (Agent Evaluation)

智能体评测研究如何衡量 [[llm-agents|LLM 智能体]]在交互式、多步、有状态环境中的能力——区别于静态 NLP 基准的单轮问答,
agent 评测要考察**长程任务完成、工具使用、规划、协作/对抗、社会智能**等,且常面临可复现性与评判可靠性难题。

## 评测维度与基准
- **任务完成 / 工具**:[[agentbench]](多环境)、[[webshop]]、[[webarena]]、[[mind2web]] 等考察 web/具身/工具任务。
- **社会智能 / 多智能体**:[[2023-sotopia-social-intelligence-evaluation]](7 维交互式社交)、[[2025-multiagentbench]]、[[2025-agentsnet-multi-agent-reasoning]]。
- **记忆**:[[locomo]]、[[longmemeval]]、[[2026-evaluating-memory-structure-llm-agents]](StructMemEval,测"组织知识"而非事实回忆)。
- **推荐 agent / 用户模拟**:[[2025-sim4ia-bench-user-simulation-benchmark]]、[[2026-ab-agent-recsys-evaluation]]。
- **综述**:[[2025-llm-agent-evaluation-survey]]。

## 共性难题
- **评判可靠性**:[[llm-as-judge]] 普及但有自我偏好/循环性问题(见 [[generative-social-simulation]] 的验证争议)。
- **过程 vs 结果**:只看最终成功率会漏掉过程错误;[[2025-can-llm-agents-simulate-human-behavior]] 主张**过程级**对齐评测。
- **基准是否测到点子上**:简单基线常超过复杂架构([[2026-evaluating-memory-structure-llm-agents]] 揭示记忆基准的此问题),提示需设计"真正需要目标能力才能解"的任务。
- **静态 ≠ 交互**:[[2023-sotopia-social-intelligence-evaluation]] 发现静态基准强 ≠ 交互场景强。

## 相关页
[[llm-agents]]、[[benchmark]]、[[llm-as-judge]]、[[agentbench]]、[[2025-llm-agent-evaluation-survey]]
