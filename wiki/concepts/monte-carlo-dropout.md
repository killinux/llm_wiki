---
type: concept
subtype: method
tags: [uncertainty-estimation, dropout, bayesian-approximation, regularization]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Monte Carlo Dropout

Monte Carlo Dropout 是一种在推理阶段仍保持 dropout 开启、并对同一输入进行多次随机前向传播,以采样得到预测分布的方法,从而把标准神经网络近似为 Bayesian 推断,用来估计预测的均值与不确定性(方差)。

## 在本 wiki 中的出现

- [[2023-conservative-doubly-robust]]:该论文提出 CDR(Conservative Doubly Robust)方法,用于 Doubly Robust 推荐去偏。其核心思想是审查插补值(imputed values)的均值与方差,以识别并过滤会引入偏差的"毒性插补"(poisonous imputation)。这种基于均值与方差对插补值进行多次采样、评估其可靠性的思路,与 Monte Carlo Dropout 通过多次随机前向传播获得预测分布、从均值与方差中刻画不确定性的机制高度一致——均通过采样统计量来识别不可靠的估计,从而降低偏差与方差并提升性能。

## 相关

- [[dropout]]:Monte Carlo Dropout 在推理阶段复用训练时的 dropout 机制,是其直接基础。
- [[uncertainty-estimation]]:Monte Carlo Dropout 是估计模型预测不确定性的常用手段之一。
- [[bayesian-neural-network]]:Monte Carlo Dropout 可被视为对 Bayesian 神经网络后验的一种近似推断。
- [[doubly-robust]]:在 [[2023-conservative-doubly-robust]] 中,对插补值均值/方差的审查与 Monte Carlo Dropout 的采样统计思路相呼应。
