---
type: concept
subtype: method
tags: [对话式推荐, conversational-recommendation, 推荐系统, 偏好询问, llm-agent, 用户模拟]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# 对话式推荐 (Conversational Recommendation / CRS)

对话式推荐(Conversational Recommendation System, CRS)是一种通过多轮自然语言交互逐步澄清用户偏好、并据此动态生成、排序与呈现推荐结果的推荐范式。

## 概述

与"基于历史行为一次性出列表"的传统 [[recommender-systems|recommender-system]] 不同,对话式推荐把推荐看作一个交互过程:系统主动追问澄清问题(preference elicitation),用户用自然语言给出反馈,系统据此更新对用户偏好的理解并多轮迭代。[[large-language-models|LLM]] 的兴起让 CRS 同时具备语言理解、解释与多轮交互能力,使其常被实现为以 LLM 为"大脑"、传统推荐模型/工具为"手脚"的 [[llm-agents|LLM agent]]。该范式的核心张力在于追问效率与偏好覆盖之间的权衡——既要问得少(避免 question fatigue),又要尽快收敛到准确且不过早坍缩的偏好估计;其评测因依赖多轮交互,普遍借助 [[user-simulation|用户模拟]] 与 LLM judge。

## 在本 wiki 中的出现

- [[2026-entropy-guided-agentic-recommendation]]:提出 IDSS,用 Shannon 熵作为统一信号贯穿对话式推荐的偏好询问、排序与多样化呈现三阶段;在候选集上选熵最大的属性维度发问,用残余不确定性驱动结果多样化,直面 CRS 的"过度追问 vs 过早收敛"两个失败模式。
- [[2025-llm-agents-for-recommender-systems-survey]]:把 LLM 推荐 agent 分为"面向推荐/面向交互/面向模拟"三范式,其中"面向交互"一类(AutoConcierge、RAH、MACRS、RecLLM 等)正是用对话与解释增强可解释性的对话式推荐,并用 Profile-Memory-Planning-Action 四模块统一刻画;评测上汇总了 ReDial、OpenDialKG 等会话推荐数据集与 Success Rate、Average Turn 等会话效率指标。
- [[2023-recommender-ai-agent-interec]]:提出 InteRecAgent,以 LLM 为大脑、传统推荐模型为工具,通过工具集(查询/召回/排序)、Candidate Bus 记忆与 plan-first execution 把 ID 类推荐模型改造为带自然语言交互界面的对话式推荐系统,并用 GPT-4 扮演的 user simulator 做多轮对话评测(Hit@k / Average Turns)。
- [[2026-convapparel-user-simulator-validation]]:面向服装购物 conversational recommender 构建人-AI 对话数据集 ConvApparel,并提出三支柱验证框架(统计对齐 / Human-Likeness Score / counterfactual validation),专门衡量基于 LLM 的对话式推荐用户模拟器的"realism gap"。
- [[2025-sim4ia-bench-user-simulation-benchmark]]:发布把真实搜索/会话日志与模拟下一步 query/话语关联起来的基准 Sim4IA-Bench,其 Task B(conversational session simulation)直接评估对话式检索/推荐场景下用户模拟的再现保真度。

## 相关

- [[recommender-systems]]
- [[interactive-recommendation]]
- [[preference-elicitation]]
- [[recommendation-diversity]]
- [[user-simulation]]
- [[llm-for-recommendation]]
- [[llm-agents]]
- [[maximal-marginal-relevance]]
- [[shannon-entropy]]
- [[recommendation-simulator]]
- [[interecagent]]
- [[recmind]]
- [[chat-rec]]
- [[recllama]]
- [[llm-redial]]
