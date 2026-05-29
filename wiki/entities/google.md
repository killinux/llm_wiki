---
type: entity
subtype: lab
tags: [google, ai-lab, gemma, generative-ai]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Google

Google 是一家科技公司及人工智能研究机构,旗下进行大语言模型、生成式 AI 与多模态系统的研究与开发。

## 在本 wiki 中的出现

- [[2024-unbounded-generative-infinite-game]]:提出"生成式无限游戏"概念并实现一个角色生活模拟系统,游戏机制、叙事与角色/环境图像全部由 LLM 与 text-to-image 模型实时生成;核心创新是带 Block Drop 的 regional IP-Adapter(保证角色与环境一致性),以及将多 LLM 协作能力蒸馏进 Gemma-2B 的实时游戏引擎。
- [[2026-convapparel-user-simulator-validation]]:Google 提出 ConvApparel(4,146 段人-AI 服装购物对话、双 agent good/bad 协议、逐轮第一人称标注)及 PLSA+HLS+counterfactual validation 三支柱框架,系统量化 LLM user simulator 的 realism gap,发现所有 simulator 平均 HLS 仅 0.004,但 ICL/SFT 在反事实泛化上优于纯 prompting。
- [[2026-automatic-laplace-collapsed-sampling]]:ALCS 用自动微分把高维隐变量在每次 likelihood 评估时坍缩为 MAP+Laplace 标量贡献,使 nested sampling 只在低维超参数空间运行,把 Bayesian evidence 计算扩展到 d_z~25,600。

## 相关

- [[gemma]]
- [[ip-adapter]]
- [[text-to-image]]
- [[generative-infinite-game]]
- [[user-simulator]]
- [[nested-sampling]]
- [[bayesian-inference]]
