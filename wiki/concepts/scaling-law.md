---
type: concept
subtype: method
tags: [scaling-law, recommendation, generative-recommendation, hstu]
created: 2026-05-29
updated: 2026-05-29
sources: 7
---

# Scaling Law

Scaling Law(扩展定律)描述模型性能随模型规模、数据量与计算量的增长而可预测地提升的经验规律。

## 在本 wiki 中的出现

- [[2024-large-recommendation-models-scaling]]:华为诺亚与 USTC 的工作,系统评估 large recommendation models 的 scaling law,以生成式推荐模型 HSTU 为代表,在多 backbone、复杂用户行为与 ranking 任务上验证可扩展性及其来源组件。
- [[2025-multi-agent-llm-value-diversity]]:通过 Schwartz 价值观给 LLM 智能体注入价值多样性的多智能体社会模拟,发现价值多样性提升集体行为的价值稳定性、涌现与自发规则创造,但极端异质带来边际递减与不稳定。
- [[2026-smes-scalable-multi-task-expert-sparsity]]:SMES 是 Kuaishou 提出的可扩展稀疏 MoE 多任务推荐框架,用 progressive expert routing 与 multi-task load-balancing 解决多任务稀疏路由的 exploded activation 与 load skew,使参数 scaling 在工业延迟约束下带来稳定收益。
- [[2026-fuxi-linear]]:线性复杂度的时间感知序列推荐模型,解耦时间与语义信号、用可学习核近似相对位置编码,在数千 token 长序列上提升推荐质量并实现最高 21× 推理加速。
- [[2026-policysim-proactive-policy-optimization]]:PolicySim 是一个基于 LLM 智能体的社会模拟沙盒,用 SFT+DPO 训练用户智能体、用带消息传递的 contextual bandit 自适应优化推荐与曝光控制等平台干预策略,实现部署前的主动评估与优化。
- [[2026-tencent-advertising-algorithm-challenge-2025]]:腾讯广告算法大赛 2025 发布两个真实工业广告日志构建的大规模全模态生成式推荐数据集(TencentGR-1M/10M)、基线模型与含转化加权的评测协议。
- [[2026-nestpipe-nested-pipelining]]:NestPipe 通过两层嵌套流水线(inter-batch 的 Dual-Buffer Pipelining 与 intra-batch 的 Frozen-Window Pipelining)在保持同步训练语义下隐藏大规模推荐 embedding 训练的 lookup 与 All2All 通信瓶颈,在 1,536 worker 上实现 3.06× 加速、94.07% 扩展效率。

## 相关

- [[generative-recommendation]]
- [[hstu]]
- [[recommendation-model]]
