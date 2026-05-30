---
type: concept
subtype: method
tags: [recommender-system, implicit-feedback, debiasing, ranking]
created: 2026-05-30
updated: 2026-05-30
sources: 8
---

# 隐式反馈 (Implicit Feedback)

隐式反馈指从用户**行为**(点击、浏览、停留时长、购买、完播)中**间接**推断偏好的信号,区别于评分/点赞这类**显式反馈**。
它在真实系统中海量易得,是工业推荐的主要训练信号,但带来一系列**偏差**与**缺失语义**问题。

## 核心挑战
- **只有正例、缺负例**:未点击 ≠ 不喜欢(可能没曝光)。需负采样或把未观测当弱负例。
- **Missing-Not-At-Random (MNAR) / 曝光偏差**:用户只能对**被推荐**的内容反馈,数据非随机缺失——是去偏推荐的根因,
  催生因果/IPS 类方法([[2023-idcf-debiasing-recommendation]]、[[2024-counterfactual-watch-time]]、doubly robust 家族)。
- **信号歧义**:点击≠满意、长时长可能因诱导;短视频里时长还受**视频长度偏置**干扰([[2023-video-length-debiasing-microvideo-rec]]、[[2023-d2co-watch-time-debias]])。
- **位置/流行度偏置**:高位 / 热门更易被点。

## 经典建模
- **成对排序**:[[bpr|BPR]](Bayesian Personalized Ranking)用"正例 > 未观测"的成对偏好优化。
- **加权矩阵分解**:对未观测项赋低置信度权重(WMF/ALS)。
- **多行为 / 多目标**:把点击、时长、转化等多种隐式信号联合建模([[esmm]]、[[multi-objective-optimization]])。

## 相关页
[[recommender-systems]]、[[bpr]]、[[causal-inference]]、[[2023-d2co-watch-time-debias]]、[[user-retention]]、[[ranking]]
