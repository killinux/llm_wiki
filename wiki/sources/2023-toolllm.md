---
type: source
subtype: paper
tags: [tool-use, llm-agents, fine-tuning, benchmark, api, dataset]
created: 2026-05-31
updated: 2026-05-31
arxiv: 2307.16789
year: 2023
---

ToolLLM 是一个让大型语言模型掌握 16,000+ 真实 API 调用能力的框架,包含数据构建（ToolBench）、模型训练（ToolLLaMA）和评估协议（ToolEval）三大组件。

## 问题

开源 LLM 在 [[tool-use]] 方面远落后于 [[gpt-4]] 等闭源模型。主要瓶颈在于：(1) 缺乏大规模、高质量的工具使用训练数据；(2) 现有工具使用研究局限于少量手工定义的简单 API,无法覆盖真实世界 API 的多样性与复杂性；(3) 缺少系统性的工具使用评估协议。

## 方法

- **ToolBench 数据集**：从 RapidAPI Hub 收集 **16,464 个 RESTful API**,跨越 **49 个类别**。利用 ChatGPT 自动生成多步 API 调用链的指令-解答对,覆盖单工具单 API、单工具多 API、多工具多 API 三种复杂度级别。
- **DFSDT（Depth-First Search-based Decision Tree）**：提出基于深度优先搜索的决策树策略,取代线性的 [[chain-of-thought]] 推理。模型在每一步可以回退并探索替代路径,显著提升多步工具调用的成功率。
- **ToolLLaMA**：在 ToolBench 数据上对 [[llama-2]] 进行 [[fine-tuning]],使其获得通用 API 调用能力。
- **ToolEval 评估协议**：提出两个自动指标——**通过率（pass rate）**衡量任务是否完成,**胜率（win rate）**通过 ChatGPT 评判比较不同方案的质量。

## 结果

- ToolLLaMA 在 ToolEval 上的表现与 ChatGPT 相当,在部分场景中甚至可比肩 GPT-4。
- DFSDT 策略相较于 ReAct 式线性推理,通过率显著提升,尤其在需要多步复杂 API 编排的任务上。
- ToolLLaMA 展现出对未见过 API 的泛化能力,在 out-of-distribution 的 API 类别上仍能有效调用。
- ToolEval 的自动评估与人类判断的一致性较高,为 [[tool-use]] 研究提供了可扩展的评估方案。

## 相关页

本文是 [[tool-use]] 方向的里程碑工作,构建了迄今规模最大的 API 调用 [[benchmark]]（[[toolbench]]）。与 [[metatool]]（测试何时使用工具）和 [[toolemu]]（工具安全性）互补。训练范式基于 [[fine-tuning]] + [[llama-2]],评估思路可与 [[agentbench]] 对照。属于 [[llm-agents]] 工具增强路线的核心文献。
