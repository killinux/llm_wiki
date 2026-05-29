---
type: entity
subtype: model
tags: [vae, causal-inference, identifiability, recommendation, debiasing]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# iVAE

iVAE(identifiable VAE)是一类引入辅助变量以获得潜变量可识别性保证的变分自编码器(VAE),用于在因果推断与表示学习中恢复真实的潜在因子。

## 在本 wiki 中的出现

- [[2023-idcf-debiasing-recommendation]]:该工作提出 iDCF,借助代理变量(用户特征)与近端因果推断,在存在未观测混杂变量(unobserved confounders)时为推荐反事实反馈提供可识别性保证;iVAE 作为其中实现可识别潜变量推断的建模思路/组件,与近端因果推断框架结合,使方法在 Coat、Yahoo!R3、KuaiRand 等数据集上优于现有去混杂方法。

## 相关

- [[vae]]
- [[identifiability]]
- [[proximal-causal-inference]]
- [[unobserved-confounders]]
- [[idcf]]
- [[debiasing-recommendation]]
