---
type: entity
subtype: product
tags: [toxicity-detection, api, external-tool, content-moderation]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# PERSPECTIVE API

PERSPECTIVE API 是一个用于评估文本毒性(toxicity)等属性的在线服务,常被用作 LLM 工具增强与内容安全评测中的外部反馈来源。

## 在本 wiki 中的出现

- [[2023-critic]]:CRITIC 框架将 PERSPECTIVE API 作为可调用的外部工具之一(与搜索引擎、代码解释器等并列),用于毒性评估。在 [[realtoxicityprompts]] 上的毒性削减任务中,它返回细粒度的毒性分数作为外部反馈,让 LLM 据此自我验证并迭代修正输出(最多 n=4 轮),使毒性概率大幅下降;这印证了外部反馈对自我改进至关重要。

## 相关

- [[2023-critic]]
- [[realtoxicityprompts]]
- [[toxicity-detection]]
- [[external-tools]]
- [[self-correction]]
- [[content-moderation]]
