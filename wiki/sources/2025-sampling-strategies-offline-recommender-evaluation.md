---
type: source
subtype: paper
tags:
  - recommender-system
  - evaluation
  - offline-evaluation
  - sampling
  - exposure-bias
  - selection-bias
created: 2026-05-29
updated: 2026-05-29
arxiv: 2508.05398
raw: raw/2508.05398.pdf
authors:
  - Bruno L. Pereira
  - Alan Said
  - Rodrygo L. T. Santos
year: 2025
---

# On the Reliability of Sampling Strategies in Offline Recommender Evaluation

通过一个全观测数据集 + 受控模拟曝光偏差,系统评估离线推荐评估中负样本采样策略在分辨力(resolution)、保真度(fidelity)、鲁棒性(robustness)、预测力(predictive power)四个维度上的可靠性。

## 问题

离线评估在推荐系统基准测试中占据核心地位(因为线上 A/B 测试昂贵且有风险),但它易受两类偏差影响:

- **曝光偏差(exposure bias)/ logging bias**:用户只能与被展示的 item 交互,日志数据极度稀疏且 missing-not-at-random (MNAR),偏向于复现历史曝光模式的模型。这是 [[selection-bias]] / [[exposure-bias]] 在推荐场景的体现,常用 [[inverse-propensity-scoring]] 等手段缓解。
- **采样偏差(sampling bias)**:计算 top-k 指标时,因 item 库过大,通常对每个正样本只采样一小撮负样本(uniform、按 popularity、按 positivity,或 WTD/Skew 等加权策略)。这会显著改变评估结论。

以往工作大多在**固定的 logged 数据**上评估采样策略,并把 logged 数据本身当作 ground truth,从而忽略了:采样结论在不同曝光偏差强度下是否稳定?采样评估在多大程度上反映**真实用户偏好**?本文针对这一空白。

## 方法

提出一个概念框架,将离线评估拆为三个顺序阶段:用户偏好 → item 曝光 → 评估采样。定义三个核心矩阵:

- **Ground-Truth Preferences (G)**:全观测的用户-item 偏好矩阵,作为可测量的真值。
- **Logged Interactions (L)**:对 G 施加曝光策略后得到的部分观测矩阵。
- **Sampled Interactions ($G_S$ / $L_S$)**:对 G 或 L 施加采样策略后得到的评估集;$L_S$ 是主要研究对象。

**数据集**:使用 [[kuairec]](KuaiRec),目前唯一公开的带完整曝光日志的数据集。测试集近 100% 稠密(density 99.6%),可构造全观测二值相关性矩阵 G。统计:训练集 7,176 用户 / 10,728 item;测试集 1,411 用户 / 3,327 item。隐式反馈定义为视频累计观看时长超过其时长(following Gao et al.)。

**Logger 模拟**(3 种曝光策略 × 8 个稀疏度 0%/10%/30%/50%/70%/85%/90%/95%):
- Uniform(无偏基线)、Popularity-biased(按全局热度)、Positivity-biased(按正反馈数)。

**采样策略**(9 种):Full(全量,无采样)、Exposed(全部曝光负样本)、Random@e、Random@n、Popularity@n、Positivity@n、WTD@n、WTDH@n、Skew@n;参数化采样器在 n ∈ {1,2,5,10,20,50,100,200,500,1000} 上取值。共 63 个采样器 × 24 个 logger 配置 = 1,512 个评估场景。

**推荐模型(7 个)**:ALS、[[bpr]](BPR)、[[lightfm]](LightFM)、SAR-Cosine、SAR-Jaccard、Popularity、Random;超参用 Hyperopt 随机搜索 + [[ray]](Ray Tune)调优,128 次迭代 5 折交叉验证。实验基于 Microsoft Recommenders 框架。

**四个评估问题与指标**:
- **Q1 Resolution**:采样器能否区分模型?用 **tie rate**(在 nDCG@100 上得分相同的模型对比例)衡量。
- **Q2 Fidelity**:$L_S$ 排名与 L 全量评估的一致性,用 **Kendall's τ**。
- **Q3 Robustness**:对 L($L_S$)与对 G($G_S$)用同一采样器,比较排名 τ,衡量对曝光偏差的稳定性。
- **Q4 Predictive Power**:$L_S$(偏差+采样)排名与真值 G 排名的 τ,衡量恢复真实偏好的能力。

主指标用 nDCG@100;置信区间用 1,000 次 bootstrap 重采样。

## 结果

- **Q1 分辨力**:tie rate 在 nDCG 极高或极低时偏高;稀疏度起关键作用,90%/95% 高稀疏下 tie rate 仍显著偏高。Skew、Popularity、Positivity 等加权采样器即使在高稀疏 + 偏差曝光下也持续给出更低 tie rate(更强分辨力)。Full 在多数设置下区分力最好。小到中等样本量 n 即可给出稳健结果。
- **Q2 保真度**:Kendall's τ 随 n 上升;WTD、WTDH、Random 在中等稀疏(10%–50%、n≥200)即接近最大保真度。Skew 在高稀疏下退化较快(尤其 positivity-biased logger)。即便在 0% 稀疏(L=G)下,采样本身也会扭曲排名——保真度不仅取决于样本量,还取决于采样哪些 item。
- **Q3 鲁棒性**:0% 稀疏下 $L_S$ 与 $G_S$ 比较退化为同一总体的内部一致性(各采样器近似平线 τ≈1)。WTD、WTDH 在有 MAR 数据、低稀疏、Uniform logger 下能很好抵御曝光偏差;Popularity、Positivity 增益有限。Random@e 持续优于 Exposed(Exposed 受 logger 偏差影响大)。
- **Q4 预测力**:τ 随 n 上升但严重依赖采样器与 logger。Skew、WTD、WTDH 即使中等采样也能强对齐 G,在 10%–50% 稀疏区间常 τ>0.7(n≥200)。Random 表现可与加权方法相当,是简单通用的选择。Popularity、Random@e 在稀疏/偏差下较弱。

**总结论**:没有单一采样器在所有维度上最优,存在权衡——高分辨力方法可能在偏差下失效,鲁棒方法可能丢失细粒度差异;更大样本未必更好,关键在 item 选择是否有偏/有信息。Bias-aware 策略(WTD、WTDH、Skew)持续优于朴素基线;Exposed 是意外强劲的竞争者(在现实约束下)。

## 在本 wiki 中的位置

本文属于[[recommender-systems|recommender-system]]离线[[evaluation]]方法学研究,聚焦负样本[[sampling]]策略的可靠性。它与[[exposure-bias]]、[[selection-bias]]、[[popularity-bias]]、[[debiasing]]等偏差主题相关,缓解手段上呼应[[inverse-propensity-scoring]]、[[doubly-robust]]等思路。评估指标层面使用 [[ndcg]]、Kendall's τ、[[recall]]、precision 与 tie rate。与 [[krichene-rendle]] 关于采样指标不可靠的经典论点一脉相承(本文将其扩展到偏差曝光维度)。数据集上依赖 [[kuairec]]/[[kuairand]] 这类带曝光日志的稠密测试集;评测的推荐模型涵盖 [[bpr]]、[[lightfm]]、[[matrix-factorization]] 等。与本 wiki 中 LLM-for-recommendation、[[recommendation-simulator]] 等条目共同构成推荐系统评估生态的一部分。
