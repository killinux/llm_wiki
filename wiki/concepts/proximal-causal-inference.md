---
type: concept
subtype: method
tags: [causal-inference, proxy-variables, confounding, identification, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# 近端因果推断

近端因果推断(proximal causal inference)是一类在存在未观测混杂变量(unobserved confounder)的情况下,借助与混杂相关的代理变量(proxy / proxy variables)来恢复因果效应可识别性(identifiability)的因果推断方法。

## 在本 wiki 中的出现

- [[2023-idcf-debiasing-recommendation]]:该工作提出 iDCF,将近端因果推断引入推荐系统的去混杂(debiasing)问题。它把用户特征作为代理变量,在存在未观测混杂变量时,为推荐场景下的反事实反馈(counterfactual feedback)提供可识别性保证;实验表明该方法在 Coat、Yahoo!R3、KuaiRand 数据集上优于现有去混杂方法。
- [[2024-mitigating-dual-latent-confounding-biases]]:IViDR 联合工具变量(IV)与 identifiable VAE,同时缓解推荐系统中 item-feedback 与 exposure-feedback 两类潜在混淆偏差。

## 相关

- [[proxy-variables]]
- [[unobserved-confounding]]
- [[causal-inference]]
- [[debiasing-recommendation]]
- [[counterfactual-feedback]]
- [[identifiability]]
