---
type: concept
subtype: method
tags: [causal-inference, deconfounding, recommendation, latent-variable]
created: 2026-05-29
updated: 2026-05-29
sources: ["2022-deep-causal-reasoning-for-recommendations"]
---

# 替代混淆变量 (Substitute Confounders)

替代混淆变量是指当真实混淆变量(confounder)不可观测时,通过对多个观测到的“成因 (causes)”进行联合建模而构造出来的一个潜变量,用它来“替代”那些无法直接测量的混淆因素,从而在因果推断中近似实现去混淆(deconfounding)。

## 概述

在推荐等观测数据场景中,用户与物品之间往往存在大量无法直接测量的混淆因素(如用户的内在偏好、曝光机制等),这些因素同时影响了“用户对哪些物品产生交互(成因)”以及“最终评分/反馈(结果)”,从而引入 confounding bias。substitute confounders 的核心思想源自 multi-cause / deconfounder 框架:由于每个用户面对多个成因(multiple causes),可以拟合一个潜变量模型,使这些成因在给定潜变量后条件独立;该潜变量被证明可以充当未观测混淆变量的“替代品 (substitute)”。在估计因果效应时以该替代变量为条件进行调整,即可缓解偏差,而无需直接观测真实混淆变量。

## 在本 wiki 中的出现

- [[2022-deep-causal-reasoning-for-recommendations]]:该工作在推荐场景中构造 substitute confounders。它把用户对多个物品的交互视为 multiple causes,通过一个(变分)潜变量模型推断出替代混淆变量,并以其为条件来估计去偏后的用户偏好,从而在存在不可观测混淆因素时仍能得到更接近因果的推荐结果。

## 相关

- [[multi-cause-confounders]]:substitute confounders 的理论前提,即“多成因可共享一个潜在混淆变量”这一假设。
- [[deconfounding]]:利用 substitute confounders 进行调整正是去混淆的具体手段。
- [[confounding-bias]]:substitute confounders 旨在缓解的目标偏差。
- [[causal-inference]]:该方法所属的总体框架。
- [[variational-autoencoder]]:常用于推断 substitute confounders 这一潜变量的建模工具。
- [[deconf-mf]]、[[deep-deconf]]、[[vg-causal]]、[[ml-causal]]:本 wiki 中采用或评估该思想的相关模型/实体。
- [[yaochen-zhu]]:相关工作的作者实体。
