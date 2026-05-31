---
type: source
subtype: paper
tags: [agent, benchmark, tool-use, user-simulation, reliability, evaluation]
created: 2026-05-31
updated: 2026-05-31
arxiv: "2406.12045"
authors: [Shunyu Yao, Noah Shinn, Pedram Razavi, Karthik Narasimhan]
affiliations: [Princeton University, Sierra Technologies]
year: 2024
---

# τ-bench：工具-智能体-用户交互基准

一句话：τ-bench（tau-bench）评估语言智能体在**真实业务领域**中与模拟用户对话、调用领域专用 API 工具、遵守业务策略规范的综合交互能力，并提出 pass^k 指标衡量 [[llm-agents]] 的**可靠性**。

## 问题

现有 agent [[benchmark]] 多关注单次成功率，忽略了实际部署中最关键的**可靠性（reliability）**：一个 agent 在 k 次独立尝试中能否**每次都成功**？此外，大多数基准要么使用静态数据集缺乏动态交互，要么不涉及真实业务场景中的复杂约束——用户意图模糊、工具调用有严格的业务策略限制（如退货政策、折扣规则）、对话中用户可能改变需求或提出边界请求。

## 方法

τ-bench 构建了两个真实业务领域的评估场景：

- **零售（Retail）**：模拟在线零售客服，agent 需处理订单查询、退货、地址修改等任务，调用订单管理 API，遵守详细的退货/退款政策。
- **航空（Airline）**：模拟航空公司客服，涉及航班改签、行李政策查询、会员升级等，需遵守复杂的舱位和票价规则。

核心设计特点：
- **模拟用户（User Simulation）**：由 LLM 扮演用户，根据预设人设和需求进行多轮对话，使交互具有动态性和不可预测性。
- **领域专用工具 + 策略规范**：agent 可调用一组 API [[tool-use|工具]]（查订单、修改预订等），但必须遵守以自然语言描述的业务策略（policy guidelines）。
- **pass^k 指标**：对同一任务独立运行 k 次，计算全部 k 次都通过的比例。这比单次 pass rate 更严格地反映了 agent 在生产环境中的可靠性——用户不会容忍"有时对有时错"。

## 结果

- 即使是最强的 [[gpt-4o]]，在零售领域的单次成功率也**不到 50%**。
- 更关键的是，pass^8（连续 8 次全对）在零售域**低于 25%**，凸显了当前 LLM agent 的可靠性危机。
- 航空领域因策略更复杂，表现更差。
- 失败原因分析表明，**策略违反**（如错误授权退款）和**工具调用错误**（参数填写错误、遗漏必要确认步骤）是主要失败模式。
- 模型规模越大、推理能力越强，pass^k 衰减越慢，但即使顶级模型距离生产级可靠性仍有显著差距。

## 相关页

本文由 [[shunyu-yao|Shunyu Yao]]（[[react]]、[[tree-of-thoughts]] 作者）和 Noah Shinn（[[reflexion]] 作者）主导，延续了他们对 [[llm-agents]] 能力边界的系统性探索。τ-bench 的 pass^k 指标为 agent 评估引入了可靠性维度，与 [[agentbench]]（多环境单次评估）、[[swe-bench]]（代码修复）形成互补。[[user-simulation]] 方法论对构建更真实的 agent 评估至关重要。
