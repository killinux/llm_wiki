---
type: source
subtype: paper
tags:
  - llm-agent
  - role-playing-agent
  - game-npc
  - cross-platform
  - agent-memory
  - human-computer-interaction
created: 2026-05-29
updated: 2026-05-29
arxiv: "2504.13928"
raw: raw/2504.13928.pdf
authors:
  - Li Song
year: 2025
---

# LLM-Driven NPCs: Cross-Platform Dialogue System for Games and Social Platforms

一句话:本文提出并实现了一个原型系统,让由 [[large-language-models]] 驱动的游戏 NPC 能在游戏内(Unity)和社交平台(Discord)之间跨平台对话,并通过云数据库同步记忆,从而在两个平台间保持对话连贯与角色一致。

## 问题

传统游戏中的 NPC 通常受限于**静态对话树(static dialogue trees)和预设脚本**,缺乏灵活性,难以产生真实交互感。已有研究将 [[large-language-models]] 引入游戏 NPC 以生成更自然的对话,但这些 LLM 驱动的 NPC 几乎都**局限在游戏内环境**。然而现代玩家不再只在游戏客户端内与游戏互动,Discord 等社交平台已成为沟通与反馈的重要空间。作者认为:构建一个能在游戏与社交平台间一致互动的 NPC 系统,可显著增强玩家体验与连续感。

## 方法

系统是一个"虚拟陪伴(virtual companion)"游戏原型,核心是把单个 NPC 与一个 LLM 集成,并跨平台共享上下文:

- **游戏设计**:单个 NPC,带有简单的好感度(favorability,文中称 haogandu)机制——初始礼貌而疏远,随玩家在游戏内的交互增多而升温,语气变得更熟络;NPC 立绘与视觉反馈会体现其情绪与好感度状态。好感度**只在游戏内**变化,Discord 上交互不改变好感度,以此模拟"当面见"与"线上聊"的差别。
- **数据流(data flow)**:玩家在游戏内或 Discord 发送消息 → 通过 API 将交互写入云数据库(字段含 character、user ID、content、timestamp、favorability、platform)→ 系统取回最近的对话历史(限定为**最近六轮**)→ 构造新 prompt 送给 LLM → LLM 回复存回数据库并返回对应平台。
- **prompt 构成**:NPC 必须遵守的规则、基于当前好感度的回复语气、以及 NPC 的背景故事。LLM 会根据当前平台判断某个动作(如"拥抱"、"看外貌")是否合适并作出相应回应。
- **跨平台记忆同步**:借助云数据库统一存储对话,实现游戏与社交平台间的记忆一致([[agent-memory]])。

## 结果

这是一个原型(prototype)可行性研究,实验为定性的对话日志展示,未报告量化 benchmark 指标:

- **实现环境**:本地 Windows 机器;Discord bot 用 Python 实现,游戏端用 Unity 开发;所有对话生成使用 **[[deepseek-r1]]** 模型;对话记录通过 **LeanCloud** 云数据库存储与同步。
- **对话一致性测试(Dialogue Consistency Test)**:玩家在游戏内自我介绍("Song Li")后退出转到 Discord,NPC 仍记得玩家姓名并回指此前对话,显示**跨平台记忆保持成功**。
- **平台识别测试(Platform Recognition Test)**:玩家在 Discord 上请求查看 NPC 外貌(被设计为仅游戏内可用的动作),NPC 正确判断 Discord 不支持视觉交互并邀请玩家进入游戏;进入游戏后对话无缝衔接。
- **局限**:长期交互中 NPC 记忆会被稀释(例如约**二十轮(twenty rounds)**对话后可能遗忘玩家姓名),除非持续把全部历史送入 LLM,但这会显著增大输入 token;NPC 人格仅由静态 prompt 定义,缺乏动态发展;系统功能局限于对话与记忆同步,未深入游戏机制。作者建议未来引入向量数据库 / [[retrieval-augmented-generation]] 来支撑更持久的记忆。

## 在本 wiki 中的位置

本文属于 [[llm-agent]] 在游戏与社交场景的应用,具体是 [[role-playing-agent]] 与 [[generative-agents]] 思路在跨平台 NPC 上的工程化落地。其记忆稀释问题与缓解方向直接关联 [[agent-memory]]、[[llm-long-term-memory]] 与 [[retrieval-augmented-generation]];使用 [[deepseek-r1]] 作为对话生成模型。可与 [[generative-agents]]、[[siliconfriend]] 等"持久陪伴 / 类人记忆"工作对照阅读。
