---
type: source
subtype: paper
tags:
  - llm-agent
  - agent-memory
  - llm-long-term-memory
  - tool-use
  - long-context
  - retrieval-augmented-generation
created: 2026-05-29
updated: 2026-05-29
arxiv: "2310.08560"
raw: raw/2310.08560.pdf
authors:
  - Charles Packer
  - Sarah Wooders
  - Kevin Lin
  - Vivian Fang
  - Shishir G. Patil
  - Ion Stoica
  - Joseph E. Gonzalez
year: 2023
---

# MemGPT: Towards LLMs as Operating Systems

MemGPT 借鉴传统操作系统的分层内存与虚拟内存分页思想,用函数调用让 LLM 自主管理"上下文窗口内/外"的多级存储,从而在固定上下文模型上制造出"无限上下文"的假象。

## 问题

[[large-language-models]] 受限于固定长度的上下文窗口,在长对话、长文档分析等任务上能力严重受限。直接扩展 transformer 上下文长度会因 self-attention 带来二次方的计算与内存开销;即使训练出长上下文模型,近期研究也表明 LLM 难以有效利用增加的上下文(中间位置的信息容易被忽略,即 lost-in-the-middle),且收益递减。因此需要一种无需无限扩展上下文、就能支持长上下文的替代技术。

## 方法

作者提出 **virtual context management(虚拟上下文管理)**,类比操作系统在物理内存与磁盘之间的分页机制,设计了 MemGPT(MemoryGPT)——一个"LLM OS"。核心组件:

- **Main context(主上下文 / prompt tokens)**:类比 OS 的主存/RAM,即模型实际可见的固定上下文窗口。分为三段:**system instructions**(只读,描述内存层级与函数用法)、**working context**(可读写、存储用户关键事实与 persona)、**FIFO queue**(滚动消息历史,队首为被驱逐消息的递归摘要)。
- **External context(外部上下文)**:类比磁盘存储,包括 **archival storage**(任意长度文本的读写数据库)与 **recall storage**(消息数据库),数据必须经函数调用显式移入主上下文才能被推理使用。
- **Queue manager**:管理 FIFO queue 与 recall storage,负责上下文溢出控制——当 prompt tokens 达到"warning token count"(如上下文窗口的 70%)时,向 LLM 注入 memory pressure 警告;达到"flush token count"(100%)时,刷新队列、生成新的递归摘要并释放空间。
- **Function executor**:把 LLM 的输出当作 [[tool-use]] 函数调用解析执行,实现主上下文与外部上下文之间的数据搬移。内存的编辑与检索完全 **self-directed**(自主)。

MemGPT 依赖 LLM 的 function calling 能力(类似 [[toolformer]]),并支持 **function chaining**:输出中带 `request_heartbeat=true` 时立即触发后续推理,把多次函数调用串联起来,实现多步检索(multi-hop retrieval)。检索结果分页返回以避免溢出上下文。**Events**(用户消息、系统消息、定时事件等)触发 LLM 推理,使 agent 可在无用户输入时"主动"运行。

## 结果

实验在两个长上下文领域评估,基线为不带 MemGPT 的 GPT-3.5 Turbo、[[gpt-4]] 与 GPT-4 Turbo(GPT-4 Turbo 指 `gpt-4-1106-preview`,128k 上下文)。

**对话 agent(基于 Multi-Session Chat 数据集)**:

- Deep Memory Retrieval(DMR,一致性):MemGPT 显著超过固定上下文基线。Accuracy 从 GPT-4 的 32.1% 提升到 +MemGPT 的 92.5%;GPT-4 Turbo 从 35.3% 提升到 **93.4%**(ROUGE-L 0.827)。GPT-3.5 Turbo 从 38.7% 提升到 66.9%。
- Conversation opener(参与度):MemGPT 生成的开场白可媲美甚至超过人工撰写。GPT-4+MemGPT 在 SIM-1/SIM-3 上达 0.868/0.843(均超过人类 0.800),GPT-3.5 在 SIM-H 上达 0.817(人类为 1.000)。

**文档分析**:

- Multi-document QA(NaturalQuestions-Open):固定上下文基线的准确率被检索器表现"封顶",随检索文档数 K 增加而下降(因截断/压缩);MemGPT 可对 archival storage 反复分页查询,准确率不随检索文档数增加而退化。GPT-4 与 GPT-4 Turbo 配 MemGPT 结果相当;GPT-3.5 因函数调用能力弱表现明显较差。
- Nested KV retrieval(多跳检索,140 对 UUID ≈ 8k tokens,嵌套层级 0–4):GPT-3.5 在 1 层嵌套即降到 0% 准确率,GPT-4 / GPT-4 Turbo 在 3 层降到 0%;而 **MemGPT(GPT-4)在所有嵌套层级保持不受影响**,通过对主上下文中 KV 对的重复函数查询完成多跳查找。

作者公开了代码、增强版 MSC 数据集、nested KV 数据集,以及 2000 万篇 Wikipedia 文章的 embeddings。

## 在本 wiki 中的位置

本文是 [[llm-agents|llm-agent]] 长期记忆([[llm-long-term-memory]]、[[agent-memory]])方向的代表性工作,把操作系统的分层内存抽象引入 LLM,与基于检索的 [[retrieval-augmented-generation]] 思路互补:不同于一次性把检索结果塞进上下文,MemGPT 让 agent 通过 [[tool-use]] 函数调用 **自主** 决定读写哪一层存储,并以 function chaining 实现多步检索。

它与 [[generative-agents]]([[joon-sung-park]] 等的 memory stream / 反思机制,见 [[memory-stream]])、[[memorybank]]、[[reflexion]]([[shunyu-yao]])、[[voyager]] 等记忆/自我改进型 agent 工作可对照阅读;在"LLM 作为可调用工具的规划器"层面与 [[toolformer]]、[[react]] 相关。其针对的固定上下文窗口与 lost-in-the-middle 问题,也连接到长上下文模型与 [[test-time-compute]] 的讨论。作者来自 UC Berkeley([[ion-stoica]]、Joseph E. Gonzalez 等),后续演化为 Letta/MemGPT 开源框架。
