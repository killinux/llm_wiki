---
type: concept
subtype: method
tags: [causal-inference, identification, intervention, do-calculus, graphical-models]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# do-calculus

do-calculus 是 Judea Pearl 提出的一套公理化推断规则，用于在因果图（causal graph / DAG）上将含有干预算子 do(·) 的干预分布改写为仅由观测分布表示的表达式，从而判定因果效应是否可识别（identifiable）以及如何从观测数据估计。

## 在本 wiki 中的出现

- [[2023-causal-inference-for-recommendation]]：在这篇将因果推断引入推荐系统的系统综述中，do-calculus 属于其梳理的因果记号与识别工具的一部分。综述以 do(·) 算子刻画"对推荐/曝光进行干预"的语义，并借助 do-calculus 这类识别框架，把感兴趣的因果效应从观测到的（往往带有偏差的）交互数据中识别与估计出来，进而服务于该文关注的无偏性（debiasing）、uplift、公平性、鲁棒性与可解释性等实际问题。
- [[2024-deconfound-release-interval-bias]]：将 release interval 识别为短视频推荐中的 confounder，提出模型无关的因果框架 LDRI，通过 backdoor adjustment 阻断后门路径并按视频自身 recency sensitivity 个性化去偏。

## 相关

- [[causal-inference]]
- [[do-operator]]
- [[causal-graph]]
- [[backdoor-criterion]]
- [[frontdoor-criterion]]
- [[identifiability]]
- [[average-treatment-effect]]
- [[confounding]]
- [[uplift-modeling]]
- [[2023-causal-inference-for-recommendation]]
