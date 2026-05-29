---
type: source
subtype: paper
tags: [llm, agents, reasoning, acting, prompting]
created: 2026-05-29
updated: 2026-05-29
arxiv: "2210.03629"
raw: raw/2210.03629.pdf
authors: [Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao]
affiliations: [Princeton University, Google Research (Brain team)]
venue: "ICLR 2023"
published: 2022-10-06
revised: 2023-03-10
---

# ReAct：在语言模型中协同推理与行动

一句话:提出 [[react]]——让 LLM **交替生成推理痕迹("思考")与任务相关的行动**,使二者协同:
推理帮助归纳/跟踪/更新行动计划并处理异常,行动则让模型与外部源(知识库、环境)交互以获取
更多信息。作者:[[shunyu-yao|Shunyu Yao]] 等(Princeton + Google)。

- **arXiv**:[2210.03629](https://arxiv.org/abs/2210.03629) · 2022-10-06 提交,2023-03-10 修订 · cs.CL / cs.AI / cs.LG
- **本地原文**:`raw/2210.03629.pdf`

## 问题
此前 LLM 的**推理**(如 [[chain-of-thought|思维链]])与**行动**(如行动计划生成)大多被当作两个
独立课题研究。纯推理(CoT)无法接触外部信息,容易出现**幻觉与错误传播**。

## 方法
ReAct 把"思考"和"行动"在单条轨迹里**交错**进行:思考用于归纳/跟踪/更新计划与异常处理,
行动用于调用外部接口(如 Wikipedia API、交互环境)获取观测。仅用 1–2 个上下文示例即可。

## 结果
- **问答 / 事实核查**——在 [[hotpotqa|HotpotQA]] 和 [[fever|Fever]] 上,通过与简单的 Wikipedia
  API 交互,**克服了 CoT 的幻觉与错误传播**,且轨迹更可解释、更可信。
- **交互式决策**——在 [[alfworld|ALFWorld]] 和 [[webshop|WebShop]] 上,绝对成功率分别比模仿学习/
  强化学习方法高 **+34%** 与 **+10%**(仅用 1–2 个示例提示)。

## 在本 wiki 中的位置
[[llm-agents|LLM 智能体]] 的奠基方法之一(行动 + 推理交替),针对 [[chain-of-thought|CoT]] 的
幻觉问题。后续被 [[language-agent-tree-search|LATS]] 推广为对一棵轨迹树做搜索;与
[[tree-of-thoughts|ToT]]、[[reflexion|Reflexion]] 同属该谱系,且 ReAct 与 ToT 均由
[[shunyu-yao|Shunyu Yao]] 主导。
