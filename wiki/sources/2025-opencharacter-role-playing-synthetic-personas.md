---
type: source
subtype: paper
tags: [role-playing, character-generalization, data-synthesis, synthetic-personas, instruction-tuning, sft, llama-3]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2501.15427
raw: raw/2501.15427.pdf
authors: [Xiaoyang Wang, Hongming Zhang, Tao Ge, Wenhao Yu, Dian Yu, Dong Yu]
year: 2025
---

# OpenCharacter: Training Customizable Role-Playing LLMs with Large-Scale Synthetic Personas

用大规模合成 persona 造数据,对 [[llama-3]] 8B 做 [[supervised-fine-tuning]]([[fine-tuning]]),让 LLM 获得「角色泛化」(character generalization)能力,即可即时扮演训练时未见过的任意用户自定义角色,效果可与 [[gpt-4o-mini]]/GPT-4o 相当。

## 问题

可定制角色扮演(customizable role-playing),也称**角色泛化(character generalization)**,要求 [[large-language-models]] 能扮演训练阶段未出现的、由用户自定义的任意角色(out-of-domain role-playing),适用于在线客服、内容创作、游戏 NPC 对话等场景。现有 role-playing dialogue agent 研究多依赖人工标注或众包数据,难以覆盖来自众多不同角色的对比性数据分布;Character.ai、Doubao 等商业产品和 CharacterGLM 等研究虽实现了自定义角色对话,但缺少公开的语料与具备此能力的指令跟随模型。本文要解决的就是如何低成本地为 LLM 注入 out-of-domain 的角色泛化能力。

## 方法

核心思路:角色泛化可通过在「足够多样、profile 丰富、对话高质量」的角色对齐 [[instruction-tuning]] 数据上做 SFT 来获得。整体框架(数据合成)分三步:

1. **角色 profile 合成(Character Profile Synthesis)**:以 Persona Hub 公开的 200,000 条合成 persona(每条为一句话的职业/兴趣短描述)为输入,prompt LLM 扩写出包含 name、age、gender、race、birth place、appearance、general experience、personality 的细粒度合成角色 profile。相比从 Wikipedia 等知识库抽取真实人物,合成角色不受现存人物数量上限约束,也避免「名人偏置」。
2. **两种角色对齐回复合成策略**:
   - **OpenCharacter-R(Response Rewriting)**:保留 LIMA、Alpaca 等公开指令语料的指令 x,只把原回复 y 改写为符合角色 C 风格/背景的 y_C,以多轮 JSON 格式输出。优点是保留原回复的知识细节。
   - **OpenCharacter-G(Response Generation)**:直接根据角色 profile 为指令 x 生成新回复 y_C(turn-by-turn)。Persona Hub 另释出 50,000 条无回复的复杂合成指令(称 PH-Instruct),只能用 G 策略;对 LIMA/Alpaca 则两种策略都试。
3. **SFT**:训练目标为 θ_g = argmax Σ log P(y_i | x_i, C_i; θ)。每条对话随机从 M=20,000 个合成角色池中抽 n=3 个角色合成回复,混合后用于微调。backbone 用 LLaMA-3-8B-Base 或 LLaMA-3-8B-Instruct,通过 Megatron-LM(tensor parallel=8)训练,system prompt 内嵌 persona 与 character profile,只对 response token 计 loss,Adam(β=0.9,0.95),学习率从 1e-5 线性衰减到 1e-6。

数据合成的 prompting model 同时尝试 GPT-4o(gpt-4o-2024-05-13)与 LLaMA-3-70B-Instruct。

## 结果

合成与发布数据:约 20k 合成角色 profile、306k 角色扮演指令-回复对(指令来自 LIMA 1,074 + Alpaca 51,010 + PH-Instruct 50,000,共 102,084 条,n=3)。

评测基准为 [[benchmark]] **PersonaGym**(200 personas、10k 问题)及作者裁剪出的 **PersonaGym-Light**(200 personas、1k 问题,每 metric 只留首题以省成本)。五项指标均为 1-5 分:expected action (EA)、toxicity control (TC)、linguistic habits (LH)、persona consistency (PC)、action justification (AJ),取平均为 PScore(完整版)/PScore-L(轻量版)。统一用 GPT-4o(gpt-4o-2024-08-06)作 evaluator(因 LLaMA-3-70B 的 8k 上下文不够)。

- **PersonaGym-Light(表 3)**:OpenCharacter(基于 LLaMA-3-8B-Instruct)PScore-L = 4.66,超过 gpt-3.5-turbo-1106(4.31)、gpt-4o-2024-05-13(4.60)、gpt-4o-mini(4.58)、gpt-4o-2024-08-06(4.60),略高于同尺寸的 LLaMA-3 8B Instruct(4.62),低于 LLaMA-3 70B Instruct(4.72)。
- **PersonaGym 完整版(表 5)**:基于 LLaMA-3-8B-Instruct 的 OpenCharacter PScore = 4.52,超过 gpt-4o-2024-05-13(4.48)与 gpt-4o-mini(4.51),仅略低于 gpt-4o-2024-08-06(4.53);基于 LLaMA-3-8B-Base 的 Ablation-5/OpenCharacter(4.48/4.46)也超过 LLaMA-3 8B Instruct(4.45)。LLaMA-3 70B Instruct 仍最高(4.58)。
- **消融结论**:(1)以 LLaMA-3-8B-Instruct 为 backbone 始终优于 8B-Base;(2)出乎意料地,OpenCharacter-G 在所有对比中显著优于 OpenCharacter-R——作者解释 LIMA/Alpaca 原回复质量偏低,改写反而劣化;但 R 策略对需严格遵守原知识的虚拟世界/游戏场景仍有价值(避免 [[hallucination]]);(3)用 LLaMA-3-70B-Instruct 做 prompting model 在 4 组对比中有 3 组优于 GPT-4o;(4)LIMA+Alpaca 指令略优于 PH-Instruct,后者更复杂,需更强 backbone 才能学好。

## 在本 wiki 中的位置

本文属于 LLM 角色扮演 / persona agent 与「合成数据驱动的后训练」交叉方向。它把 [[self-instruct]] 一脉的数据合成思想(persona-driven synthesis,源自 Persona Hub)用于 role-playing,通过 [[instruction-tuning]] 在 [[llama-3]] 上实现以小博大(8B 比肩 GPT-4o)的角色泛化。可与角色扮演/社会模拟类工作([[role-playing-agent]]、[[generative-agents]]、[[sotopia]])、persona/角色一致性评测,以及合成数据/[[fine-tuning]] 方法相互参照。作者来自 [[tencent-ai-lab]](Tencent AI Lab Seattle),数据与角色已公开发布。
