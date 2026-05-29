---
type: entity
subtype: model
tags: [recommendation, debiasing, causal-inference, proximal-causal-inference, confounding]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# iDCF

iDCF(identifiable Deconfounder)是一种用于推荐系统去混杂的方法,在存在未观测混杂变量时,借助代理变量与近端因果推断为反事实反馈提供可识别性保证。

## 在本 wiki 中的出现

- 在 [[2023-idcf-debiasing-recommendation]] 中作为核心方法被提出:利用代理变量(用户特征)与近端因果推断(proximal causal inference),在存在未观测混杂变量(unobserved confounders)的情形下,为推荐中的反事实反馈(counterfactual feedback)提供可识别性(identifiability)保证;实验在 Coat、Yahoo!R3、KuaiRand 数据集上优于现有去混杂方法。

## 相关

- [[proximal-causal-inference]]
- [[unobserved-confounders]]
- [[counterfactual-feedback]]
- [[debiasing-recommendation]]
- [[coat-dataset]]
- [[yahoo-r3-dataset]]
- [[kuairand-dataset]]
