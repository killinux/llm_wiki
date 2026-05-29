---
type: concept
subtype: method
tags: [vision-language, multimodal, question-answering, perception]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Visual Question Answering

Visual Question Answering (VQA) 是一类多模态任务/方法:给定一张图像与一个自然语言问题,模型需要结合视觉感知与语言理解,生成对该问题的自然语言答案。

## 在本 wiki 中的出现

- [[2022-inner-monologue]]:在该工作中,VQA 模型被用作向 frozen LLM 注入视觉环境反馈的来源之一。机器人执行过程中,VQA 对场景图像进行提问与回答,把感知结果转写为自然语言,持续反馈给 LLM,从而支撑其形成"内心独白",实现闭环、可重规划的具身推理。

## 相关

- [[inner-monologue]]
- [[grounded-feedback]]
- [[multimodal]]
- [[embodied-reasoning]]
- [[frozen-llm]]
- [[scene-understanding]]
