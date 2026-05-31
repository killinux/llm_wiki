---
type: source
subtype: paper
tags: [agent, benchmark, code-generation, software-engineering, evaluation, github]
created: 2026-05-31
updated: 2026-05-31
arxiv: "2310.06770"
venue: "ICLR 2024 Oral"
year: 2023
---

# SWE-bench：语言模型能解决真实 GitHub Issue 吗？

一句话：SWE-bench 是一个从真实 GitHub 仓库的 Issue-PR 对中构建的 [[benchmark]]，要求模型在给定代码库和 issue 描述的条件下**自动生成修复补丁**，是 [[llm-agents]] 在软件工程领域的标杆评测（ICLR 2024 Oral）。

## 问题

此前的 [[code-generation]] 基准（如 [[humaneval]]、MBPP）只评估模型生成**独立函数**的能力，与真实软件开发严重脱节：真实 bug 修复/功能实现需要理解整个代码库的上下文（数千至数万个文件）、定位问题所在位置、理解项目规范和测试框架，最后生成一个跨文件的 diff 补丁。缺乏一个贴近真实软件工程流程的评测基准。

## 方法

SWE-bench 的构建流程：

- **数据来源**：从 12 个流行的 Python 开源仓库（包括 Django、Flask、scikit-learn、sympy、matplotlib、requests、pytest、astropy 等）中收集经过人工审核并合入的 Issue-PR 对。
- **任务规模**：共 **2,294 个问题实例**，每个实例包含：(1) issue 描述（自然语言 bug 报告或 feature request）、(2) 对应版本的完整代码库快照、(3) 参考补丁（gold patch）、(4) 用于验证的测试用例。
- **评估方式**：模型输出一个 git diff 格式的补丁，系统自动 apply 补丁后运行测试套件，**通过全部相关测试即为成功**。这种端到端评估不依赖中间步骤的人工判断。
- **SWE-bench Verified**：后续推出的人工验证子集，包含 **500 个实例**，经人类专家确认 issue 描述清晰、测试充分、参考补丁正确，旨在消除原始数据集中因 issue 描述模糊或测试不充分导致的噪声。

## 结果

- 论文发表时的最佳模型 [[claude-2]]（使用 BM25 检索 + 直接生成补丁）仅解决了 **1.96%** 的问题（45/2,294），凸显任务难度。
- 即使在提供了 oracle 级的文件定位（告知模型需要修改哪些文件）的简化设置下，最佳表现也仅约 **4.8%**。
- 主要失败原因：
  - **定位困难**：在庞大代码库中找到需要修改的正确位置是核心瓶颈。
  - **上下文窗口限制**：完整代码库远超当时模型的上下文长度，检索质量直接决定上限。
  - **跨文件依赖**：许多修复涉及多个文件的协调修改，模型难以生成一致的跨文件补丁。
- 后续进展（论文发表后）：随着 [[llm-agents]] 框架（如 SWE-Agent、Devin 等）的引入，在 SWE-bench Verified 上的成功率已大幅提升至 30-50%+，表明 agent 化架构（搜索-定位-编辑-测试循环）是解决此类任务的关键。

## 相关页

SWE-bench 是 [[llm-agents]] 在 [[code-generation|软件工程]] 领域的核心 [[benchmark]]，与 [[humaneval]]（函数级生成）形成难度阶梯。它催生了一系列 agent 系统（SWE-Agent、[[devin]] 等），推动了 [[llm-agents]] 从简单工具调用向复杂软件工程工作流的演进。与 [[agentbench]]（综合 agent 评估）、[[osworld]]（真实 OS 环境）共同定义了 agent 能力的多个维度。
