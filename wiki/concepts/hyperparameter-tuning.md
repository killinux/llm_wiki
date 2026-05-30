---
type: concept
subtype: method
tags: [optimization, automl, training, recommender-system]
created: 2026-05-30
updated: 2026-05-30
sources: 6
---

# 超参数调优 (Hyperparameter Tuning)

超参数调优指搜索**不由训练直接学得的配置**(学习率、正则系数、网络结构、损失权重、RL 折扣因子等)以最大化验证集表现。
在深度推荐与 RL 中尤其关键:多目标损失权重、保守性系数、探索强度等都是敏感超参,且**搜索代价高**。

## 主流方法
- **网格 / 随机搜索**:简单但维度灾难;随机搜索在高维常优于网格。
- **贝叶斯优化**:用代理模型(高斯过程/TPE)主动选点,样本高效。
- **进化 / 群体训练 (PBT)**:边训练边演化超参。
- **梯度式 / 可微调参**:把部分超参变成可微目标联合优化。

## 在本 wiki 的体现
- 多目标推荐里"损失权重难调"正是 [[multi-objective-optimization]] 的痛点;[[2023-two-stage-constrained-actor-critic]] 把多约束的拉格朗日乘子
  统一取值以**回避**高维搜索。
- 自动调参工作:[[2025-hyperzero-auto-tuning]](自动超参生成)、[[2026-automatic-laplace-collapsed-sampling]] 等降低人工调参成本。
- offline RL 推荐的保守性系数 λ、熵惩罚权重(见 [[2023-dorl-matthew-effect-offline-rl-recommendation]])对结果影响显著,是典型敏感超参。

## 相关页
[[automl]]、[[multi-objective-optimization]]、[[reinforcement-learning-for-recommendation]]、[[2025-hyperzero-auto-tuning]]
