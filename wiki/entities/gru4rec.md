---
type: entity
subtype: model
tags: [recommendation, sequential-recommendation, rnn, gru]
created: 2026-05-29
updated: 2026-05-29
sources: 7
---

# GRU4Rec

GRU4Rec 是一种基于门控循环单元(GRU)的会话/序列推荐模型,通过 RNN 对用户的行为序列建模来预测下一个交互物品,是序列推荐领域的经典基线之一。

## 在本 wiki 中的出现
- [[2024-tim4rec-time-aware-mamba]]:TiM4Rec 用 Time-aware Structured Masked Matrix 把时间感知增强首次引入 SSD/Mamba2 架构,在线性复杂度下弥补 SSD 在低维序列推荐场景相对 SSM 的性能退化。
- [[ssm]]
- [[tim4rec]]

- [[2024-recmamba-lifelong-sequential-recommendation]]:提出 RecMamba,用带选择机制的状态空间模型 Mamba 替换 Transformer 层来建模长度 >=2k 的终身用户行为序列,在 KuaiRand 与 LFM-1b 上达到与 SASRec 相当的推荐效果,同时训练时长降低约 73%、推理时间约 61%、显存约 80%,并在 5k 长度下避免 SASRec 的 OOM。GRU4Rec 作为序列推荐的经典 RNN 基线在该工作所属领域被对照参考。
- [[2024-agentic-feedback-loop-recommendation]]:提出 AFL,让 recommendation agent 与 user agent 通过基于 memory 的多轮文本反馈回路相互协作,同时提升推荐(平均 +11.52%)与用户模拟(平均 +21.12%),且不放大流行度/位置偏差。
- [[2025-t2diff-two-tower-diffusion-matching]]:T2Diff 在双塔召回的用户塔内用扩散模型重建用户"下一个正向意图"并以 mixed-attention 实现交叉交互,在保持低延迟的同时打破双塔的 Late Interaction 瓶颈,离线/在线均显著超越 SOTA。
- [[2025-autocdsr-self-attention]]:AutoCDSR 把跨域序列推荐建模为偏好感知的 Pareto 最优多目标问题,通过动态最小化 cross-domain attention scores,仅优化 transformer 内在 self-attention 即可自动迁移有益跨域知识并抑制 negative transfer。
- [[2025-pub-personality-user-behaviour-simulator]]:PUB 是一个基于 LLM 的用户行为模拟器,把 Big Five 人格特质嵌入用户建模,从行为日志推断人格并生成高保真合成交互,用于推荐系统的离线评估。
- [[2025-grasp-world-knowledge-sequential-recommendation]]:GRASP 用"生成增强检索 + Sigmoid 整体注意力增强"把 LLM 世界知识作为辅助输入(而非监督信号)注入序列推荐,抵抗 LLM 幻觉噪声,在 Beauty/Fashion/Industry-100K 上叠加多种 backbone 均达 SOTA,并通过线上 A/B 验证 GMV +1.71%。
- [[2025-fuxi-gamma-efficient-sequential-recommendation]]:decoder-only 生成式序列推荐框架,用受 Ebbinghaus 遗忘曲线启发的指数幂时间编码器与对角稀疏位置剪枝,在 SOTA 推荐质量下把训练加速最多 4.74×、推理 6.18×。

## 相关

- [[sasrec]]
- [[recmamba]]
- [[sequential-recommendation]]
- [[mamba]]
- [[session-based-recommendation]]
- [[two-tower|two-tower-model]]
- [[cross-domain-sequential-recommendation]]
- [[user-behaviour-simulation]]
- [[grasp]]
- [[fuxi-gamma]]
