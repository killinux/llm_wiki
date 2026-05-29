---
type: entity
subtype: model
tags: [model, gemini, google, llm, agent]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Gemini 2.5 Flash

Gemini 2.5 Flash 是 Google 推出的 Gemini 2.5 系列中的轻量、低延迟模型,常作为大规模多 agent 实验中的参与模型。

## 在本 wiki 中的出现

- [[2025-agentsnet-multi-agent-reasoning]]:AGENTSNET 是一个可任意扩展的多 agent LLM 基准,借鉴分布式计算的五个经典问题(coloring、vertex cover、matching、leader election、consensus)来衡量 agent 网络在给定通信拓扑下的自组织、去中心化通信与协作推理能力,实验最多探测 100 个 agent。
- [[2026-ab-agent-recsys-evaluation]]:A/B Agent——一个多模态 LLM 用户智能体,在带海报的推荐沙盒 UI 中模拟用户多模态感知、多页交互与疲劳退出,用以替代昂贵的在线 A/B testing 评估推荐模型并做数据增强。
- [[2026-convapparel-user-simulator-validation]]:Google 提出 ConvApparel(4,146 段人-AI 服装购物对话、双 agent good/bad 协议、逐轮第一人称标注)及 PLSA+HLS+counterfactual validation 三支柱框架,系统量化 LLM user simulator 的 realism gap,发现所有 simulator 平均 HLS 仅 0.004,但 ICL/SFT 在反事实泛化上优于纯 prompting。

## 相关

- [[gemini-2-5-pro]]
- [[2025-agentsnet-multi-agent-reasoning]]
- [[google]]
- [[llm-user-simulator]]
- [[multimodal-llm]]
- [[ab-testing]]
