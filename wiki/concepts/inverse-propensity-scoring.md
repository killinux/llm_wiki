---
type: concept
subtype: method
tags: [causal-inference, debiasing, recommendation, propensity, estimation]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# Inverse Propensity Scoring

Inverse Propensity Scoring(IPS,逆倾向性加权)是一种因果推断中的去偏估计方法,通过对每个观测样本按其被观测(被处理/被曝光)的倾向性(propensity)的倒数进行加权,从而校正非随机的数据采集机制,得到对目标量的无偏估计。

## 在本 wiki 中的出现

- [[2023-causal-inference-for-recommendation]]:作为综述梳理的核心估计方法之一出现。该文系统介绍了将因果推断引入推荐系统的因果记号、假设、效应与估计方法,IPS 在其中是处理选择偏差(selection bias)、实现无偏性(unbiasedness)的代表性技术,并与可解释性、公平性、鲁棒性、uplift 等实际问题相关联。
- [[2023-idcf-debiasing-recommendation]]:作为去偏的对照与方法背景出现。该文提出 iDCF,借助代理变量(用户特征)与近端因果推断(proximal causal inference),在存在未观测混杂变量(unobserved confounders)时为推荐反事实反馈提供可识别性保证;IPS 类方法属于其所改进/比较的去混杂思路范畴,iDCF 在 Coat / Yahoo!R3 / KuaiRand 上优于现有去混杂方法。
- [[2023-video-length-debiasing-microvideo-rec]]:VLDRec 通过 play-progress 去偏标注、视频长度条件采样与多任务学习缓解微视频推荐中长视频被偏好的 video-length bias,以 NFM 为基座在 View_Time@120 上较最佳基线提升 1.81%(Kuaishou)与 11.32%(WeChat)。
- [[2024-fairness-recommendation-missing-labels]]:证明大规模推荐系统在缺失标签下 REO 公平性指标不可识别,提出用小比例 random traffic 无偏估计公平性指标并给出误差上界,首次公开 TikTok 公平性数据集。
- [[2024-roler-reward-shaping-offline-rl-recsys]]:ROLeR 用非参数(kNN/聚类)reward shaping 与解耦的不确定性惩罚修正 model-based offline RL 推荐中 world model 的 reward 估计误差,在 KuaiRand/KuaiRec/Coat/Yahoo 四个 benchmark 上达到 SOTA。

## 相关

- [[causal-inference]]
- [[debiasing]]
- [[deconfounding]]
- [[confounding-bias]]
- [[off-policy-evaluation]]
- [[exposure-bias]]
- [[propensity-score]]
- [[counterfactual-learning]]
- [[recommender-systems]]
