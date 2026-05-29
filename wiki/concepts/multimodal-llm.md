---
type: concept
subtype: method
tags: [multimodal, llm, vision-language, perception, llm-agent]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# 多模态大语言模型 (Multimodal LLM / MLLM)

多模态大语言模型 (Multimodal LLM, 常缩写为 MLLM) 是在 [[large-language-models]] 基础上接入视觉等非文本编码器(如 [[vit]]、[[clip]]),使模型能够同时理解文本与图像/视频/点云等多种模态,并以语言形式进行推理、决策与生成的一类模型。

## 概述

MLLM 通常由一个多模态 tokenizer(视觉编码器 + 对齐模块)与一个 LLM decoder 组成,把图像等模态特征对齐到语言 token 空间后再交由 LLM 统一处理。相比纯文本 LLM,它能够感知海报、商品图、场景图像、传感器数据等真实世界信息,因此被广泛用作具身决策、推荐用户模拟与可信 agent 社会等场景的核心控制器。在本 wiki 中,MLLM 既指 [[gpt-4o]]、[[gemini-2-5-flash]] 这类通用多模态基座模型,也指 DriveMLM 这类为特定任务训练的专用多模态架构。

## 在本 wiki 中的出现

- [[2024-lmagent-multimodal-agents-society]]:LMAgent 以多模态 LLM(gpt-4-1106-preview 与 gpt-4-vision-preview,即 [[gpt-4]])作为中央控制器,构建可模拟一万以上 agent 的电商 agent 社会;借助多模态感知整合商品图文与直播信息以更准确地模拟用户行为,并用 Memory Bank 缓存基本行为来减少约 40% 的多模态 LLM 调用、支撑万级规模仿真。
- [[2023-drivemlm-autonomous-driving]]:DriveMLM 用多模态 LLM(MLLM,decoder 基于 [[llama]],视觉用 ViT-g/14、LiDAR 用 SST)作为自动驾驶 planner,把 MLLM 的语言决策输出与模块化 AD 系统的行为规划状态对齐,从而在 CARLA 仿真器中实现闭环驾驶,代表 MLLM 在物理世界具身决策中的落地。
- [[2026-ab-agent-recsys-evaluation]]:A/B Agent 构建了一个多模态 LLM 用户智能体,在带海报的推荐沙盒 UI 中模拟用户的多模态感知、多页交互与疲劳退出,用以替代昂贵的在线 A/B testing 来评估推荐模型并进行数据增强。

## 相关

- [[large-language-models]]
- [[multimodal]]
- [[vit]]
- [[clip]]
- [[vqa]]
- [[gpt-4o]]
- [[gpt-4]]
- [[gemini-2-5-flash]]
- [[embodied-reasoning]]
- [[llm-agents|llm-agent]]
