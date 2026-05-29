---
type: source
subtype: paper
tags: [generative-infinite-game, character-life-simulation, llm-game-engine, regional-ip-adapter, text-to-image, llm-distillation, multi-agent-collaboration, user-simulation]
title: "UNBOUNDED: A Generative Infinite Game of Character Life Simulation"
title_zh: "UNBOUNDED:一个角色生活模拟的生成式无限游戏"
arxiv: "2410.18975"
created: 2026-05-29
updated: 2026-05-29
raw: raw/2410.18975.pdf
authors: [Jialu Li, Yuanzhen Li, Neal Wadhwa, Yael Pritch, David E. Jacobs, Michael Rubinstein, Mohit Bansal, Nataniel Ruiz]
year: 2024
---

# UNBOUNDED: A Generative Infinite Game of Character Life Simulation

UNBOUNDED 提出"生成式无限游戏(generative infinite game)"这一概念,并实现了一个角色生活模拟游戏:全部游戏机制、叙事、角色与环境图像均由 [[large-language-models]] 与 text-to-image 模型实时生成,而非由硬编码逻辑或图形系统控制。

## 问题

传统电子游戏受限于编程语言与计算机图形学,本质上是"有限游戏(finite game)"——规则、边界、胜负条件都需预先定义,只能给出有限且预设的动作与路径集合。作者借用 James P. Carse 在《Finite and Infinite Games》(1986)中"有限游戏 vs 无限游戏(以延续游戏本身为目的、无固定边界、规则可演化)"的区分,提出要构建首个完全封装在生成模型中的交互式"无限游戏"。

要实现这一目标面临两类核心挑战:

- 视觉侧:需要将用户自定义角色一致地放入多个不同环境中并跟随文本指令,同时保持(1)环境一致性、(2)角色一致性、(3)文本对齐。直接用 [[clip]] 风格的 IP-Adapter 同时编码环境与角色会相互干扰,且要满足交互速度(约 1 秒刷新)。
- 语言侧:需要一个能维持游戏机制(饥饿/能量/趣味/卫生等状态)、生成连贯叙事与角色响应、并实时跟随用户自然语言指令的"游戏引擎"。虽然 [[gpt-4]]、GPT-4o 等超大模型经提示后可胜任,但延迟过高(一次响应约 5 秒),无法支撑实时交互。

## 方法

UNBOUNDED 在视觉与语言两个领域分别提出技术创新。

视觉侧——带 Block Drop 的 regional IP-Adapter(基于 [[regional-ip-adapter]]):
- 用 latent consistency model([[lcm-lora]] / [[latent-consistency-model]],SDXL 基座)实现仅 2 步扩散的实时 T2I 生成。
- 用 [[dreambooth]] LoRA(秩 16)对自定义角色做个性化,引入特殊标记 "sks",并将角色 LoRA 与 LCM-LoRA 做算术合并以兼顾速度与角色保真。
- 提出 regional IP-Adapter,实现对"环境"与"角色"的双重条件注入(dual-conditioning)。在每个 cross-attention 层,计算角色文本嵌入 K_c 与文本 cross-attention 输出隐状态之间的注意力图 A_c,按 top r%(设为 60%)阈值动态生成 mask M_c,据此把环境 IP-Adapter 输出 O_e 与角色 IP-Adapter 输出 O_c 分区注入:O = O_t + α_e M_c·O_e + α_c (1−M_c)·O_c,从而避免环境条件干扰角色外观、反之亦然。
- Block Drop:观察到 down sample 块更多捕捉空间布局、up sample 块更多捕捉风格,故在 down 块丢弃 regional IP-Adapter,仅在 mid 与 up 块使用,改善角色与环境的分离。

语言侧——LLM 游戏引擎 + 小模型蒸馏:
- 多 LLM 协作的角色生活模拟([[llm-multi-agent]]):一个 world simulation model 负责搭建环境、生成叙事/图像描述、追踪角色状态;一个 user model([[user-simulation]])模拟玩家三类交互——延续当前动作、探索新环境、开放式交互。
- 自动数据采集:用大模型生成"主题—角色"对,用 ROUGE-L 相似度 < 0.7 过滤以保证多样性,得到 5,000 个独特 topic-character 对;再让两个 LLM 多轮交互(每会话 5 轮),得到 5,000 条 user-simulator 交互样本(数据由 GPT-4 系列自动生成,无需人工标注)。
- 蒸馏([[knowledge-distillation]] 思路):用这 5,000 条合成样本对 [[gemma-2b]] 做监督微调(屏蔽 user 输入上的 loss,训练 6,500 步,batch 8,跨 4 块 A100,学习率 1e-4),使其作为实时游戏引擎,性能接近 GPT-4o。

## 结果

图像生成(评测集:5,000 条 character-environment-prompt 三元组,5 个角色 / 100 个环境 / 1,000 条 prompt,由 GPT-4o 构造;指标含 CLIP-I、DINO、DreamSim 的环境/角色版本及 [[clip]]-T 语义对齐,并用 Grounding-DINO 检测角色是否出现):

- Table 1 中 UNBOUNDED 在环境一致性与角色一致性上均优于 IP-Adapter、IP-Adapter-Instruct 与 StoryDiffusion,同时语义对齐相当。本方法 CLIP-I^E=0.563、DINO^E=0.322、DreamSim^E=0.675;CLIP-I^C=0.676、DINO^C=0.470、DreamSim^C=0.488;CLIP-T=0.242。
- 相对 StoryDiffusion:角色一致性 CLIP-I^C 提升 0.047、DreamSim^C 提升 0.057;环境一致性 CLIP-I^E 提升 0.035、DINO^E 提升 0.065、DreamSim^E 提升 0.058。
- Table 2 消融显示 Block Drop 与 regional IP-Adapter 同时使用时一致性最佳(scale=1.0 时第 3 行同时开启两者达到上述最优数值)。

语言生成:在 100 条 user-simulator 交互样本(每条 5 轮)上,用 GPT-4 作为 judge([[llm-as-judge]]),从总体分、角色状态更新准确性、环境相关性、故事连贯性、用户指令跟随五个维度(0–10)比较。蒸馏后的 Gemma-2B 表现与 GPT-4o 相当,同时支持实时交互。

系统层面:相对朴素实现取得 5–10 倍加速,每个新场景延迟约 1 秒,实现"无限"开放式交互。

## 在本 wiki 中的位置

本文把 [[llm-agent]] / [[llm-multi-agent]] 的世界模拟思路(world model + user model 协作)与 text-to-image 个性化生成结合,落到"生成式游戏引擎"这一新应用。它与 [[generative-agents]] 类社会/角色模拟相邻,但强调实时图像生成与游戏机制;在视觉侧延续 [[dreambooth]]、[[lora]]、[[regional-ip-adapter]]、[[clip]] 等个性化与一致性技术;在语言侧体现了用大模型合成数据蒸馏到小模型([[gemma-2b]])以换取交互速度的范式,与 [[user-simulation]]、[[llm-as-judge]] 等评估方法相关。出自 [[google]] 与 University of North Carolina at Chapel Hill。
