---
type: concept
subtype: method
tags: [invariant-learning, causal-inference, debiasing, recommendation, confounding]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# 不变学习

不变学习(invariant learning)是一类旨在学习在不同环境/分布下保持稳定的因果关系或表征的方法,通过排除随分布变化而失效的虚假关联(spurious correlation),以提升模型在分布偏移与混杂干扰下的泛化与可识别性。

## 在本 wiki 中的出现

- [[2023-idcf-debiasing-recommendation]]:该工作面向推荐系统中的去混杂(debiasing)问题,提出 iDCF。其核心思路与不变学习的目标相呼应——在存在未观测混杂变量(unobserved confounders)时,设法识别出不受混杂干扰、稳定可靠的因果效应。iDCF 借助代理变量(用户特征)与近端因果推断(proximal causal inference),为推荐场景下的反事实反馈(counterfactual feedback)提供可识别性保证,并在 Coat、Yahoo!R3、KuaiRand 数据集上优于现有去混杂方法。

## 相关

- [[2023-idcf-debiasing-recommendation]]
- [[proximal-causal-inference]]
- [[counterfactual-inference]]
- [[unobserved-confounders]]
- [[debiasing-recommendation]]
- [[causal-inference]]
- [[distribution-shift]]
- [[spurious-correlation]]
