---
type: source
subtype: paper
tags:
  - recommender-system
  - fairness
  - selection-bias
  - exposure-bias
  - bytedance-research
arxiv: 2406.05247
raw: raw/2406.05247.pdf
authors:
  - Yulong Dong
  - Kun Jin
  - Xinghai Hu
  - Yang Liu
year: 2024
created: 2026-05-29
updated: 2026-05-29
---

# Measuring Fairness in Large-Scale Recommendation Systems with Missing Labels

一句话:针对大规模 [[recommender-systems|recommender-system]] 中"缺失标签"导致公平性指标无法识别的问题,本文证明仅靠默认曝光日志无法准确估计 Ranking-based Equal Opportunity (REO),并提出用一小部分 random traffic(随机流量)来无偏估计公平性指标,给出估计误差的理论上界,同时首次公开来自 TikTok 的公平性研究数据集。

## 问题

现代大规模推荐系统面对海量 item,无法获得每个 user-item 对的真实偏好标签,只有曾被推荐过的 item 才有 ground truth,这就造成普遍的**缺失标签(missing labels)**问题。已有公平性研究大多假设 user-item 交互被完全观测,而缺失标签场景下的公平性测量被严重忽视。

本文聚焦 **Ranking-based Equal Opportunity (REO)** 这一以效用为基础、面向 creator/item 侧的群体公平性概念(Zhu et al. 2020),它是二分类 Equal Opportunity(Hardt et al. 2016)在排序/推荐场景的推广:要求在 user 对 item 有正偏好(Y=1)的条件下,推荐结果(R=1)的分布独立于敏感属性 S。群体 k 的 Ranking-based true positive rate (RTPR) 效用定义为 U_k := P(R=1 | Y=1, S=s_k);公平惩罚 ΔREO := std(U_1,...,U_K) / mean(U_1,...,U_K)。

核心障碍是**不可识别性(identifiability)**:全部 user-item 对可分为被推荐子集(R=1,可从用户互动反映 Y)与未被推荐子集(R=0,标签未知)。论文用 Example 3.1 的玩具数据(两个仅在 R=0 子集不同的数据集 A/B,在 R=1 子集完全一致)说明,A 的 ΔREO=0(完全公平)而 B 的 ΔREO=2/3(不公平),二者无法区分。因此(Theorem 3.3)在不探测未推荐子集的情况下 REO 指标一般**不可识别**。把缺失标签简单当作负样本、或只取有完整标签的子集,都会因为继承了数据中的 [[exposure-bias]] / [[selection-bias]] 而产生严重偏差。论文还论证:即使用模型预测用户偏好来绕过随机流量也不行——基于有偏数据估计的模型表现无法反映全体数据上的真实表现。

## 方法

- **Random traffic(随机流量)**:对每个进入的请求以激活概率 p_act > 0(伯努利分布,通常很小,如 p_act < 10⁻³)决定是否启用随机采样;一旦启用,就从整个候选池中**均匀随机**抽取 item 推荐给用户,从而探测未被推荐子集。default traffic(默认流量)则走正常推荐策略。随机流量最初用于检测 [[exposure-bias]](Chen et al. 2023),本文将其用作 REO 估计的关键探针,并指出这是克服反事实(counterfactual)不确定性的必要手段。
- **无偏估计器**:用 Bayesian 定理把群体效用分解为可由随机/默认流量测量的成分:
  U_k = P(Y=1, S=s_k | R=1) / P(Y=1, S=s_k) · P(R=1)。
  分别用随机流量 D_rand 估计 P̂_k、用默认流量 D_rec 估计 Q̂_k,再组装 Û_k := Q̂_k / P̂_k,进而得到 ΔÛ_k 与 ΔREO 的估计(公式 4)。由于相对效用与公平惩罚对效用函数的整体缩放不变,无法测量的 P(R=1) 标量被消掉。
- **理论保证(Theorem 3.4)**:当随机/默认流量规模 |D_rec|, |D_rand| = O(K²ε⁻²log(Kδ⁻¹)) 时,以至少 1−δ 概率,所有群体相对效用与 ΔREO 的估计误差一致地被 ε 上界控制。
- **A/B 测试与显著性检验**:把处理效应定义为 ΔREO^treatment − ΔREO^control;基于 REO 指标的统计分布与 delta method 给出置信区间(Algorithm 1)和快速显著性检验(Algorithm 2),相比文献中的 permutation test(DiCiccio et al. 2020)有显著的计算优势,便于大规模商用平台部署与公平性监控。

## 结果

- **TikTok 公开数据集**:首次发布来自 TikTok 短视频推荐的公平性数据集,采集自日本地区 2024-04-18 至 2024-05-01 的推荐日志;TikTok 月活超 10 亿(1B+ MAU)。默认流量每日采样 150,000 行 user-item 对(共 14 天,150,000 × 14 = 2,100,000 行,7 列),random traffic 取七天日志的 300,000 行均匀随机样本;发布的字段含互动指标及一项由 creator 年龄派生的属性。
- **不可识别性的实证**:Example 3.1 中数据集 A 与 B 在被推荐子集完全相同,但真实 ΔREO 分别为 0 与 2/3,直观证明缺失标签下指标不可识别。
- **合成数据实验**:构造两群体、三组比例设置(如 p_1=0.01,p_2=0.05;p_1=0.001,p_2=0.005;p_1=0.0001,p_2=0.0005),默认流量相关比例设为 q_1=10×p_1、q_2=5×p_2(模拟推荐算法有效、q_k>p_k);对每个流量规模 n 独立重复采样与计算 50 次得到误差棒。结果显示 MSE(n) 随 n 呈 1/n 缩放(与大数定律方差缩放一致),说明估计器的偏差几乎消失;相关比例越小,估计问题越难、同样样本量下 MSE 越高,验证了理论。
- **TikTok 真实数据**:数据集含 7 个布尔字段,前六个(like_video / share / follow / finish / download / long_view)任一为正即记 Y(u,i)=1,第七个 young_adult(creator 年龄 18–24 岁)为敏感属性。以全量 150,000 行日数据的指标为基准 ΔREO,对子样本量 n 估计相对误差 |ΔREO(n)−ΔREO|/ΔREO,每个 n 重复 20 次:相对误差随 n 快速下降,方差对数回归斜率接近 −1(三天分别 −1.031 / −1.075 / −1.204),即方差 ∼1/n,与理论吻合。
- **公平性监控与显著性检验**:用 Algorithm 1 监控 young_adult 属性两周日度 ΔREO,除 4 月 25 日外均显著低于 11.1% 阈值(该阈值对应 80% rule,即 U_1=0.8·U_2 时 std/mean=1/9≈11.1%)。delta method 给出的置信区间与 standard bootstrap、BCa bootstrap(各 100 次重抽样)一致,但 delta method 是单遍计算、同时产出 CI,计算效率显著更优;bootstrap 估计的偏差低于 3% 且正负交替,无系统性偏差。
- **A/B 测试模拟(boosting 策略)**:模拟三种对 young_adult 的加权策略——"1.25x deboost" {0:1.25, 1:1}、"2x deboost" {0:2, 1:1}、"2x boost" {0:1, 1:2}(随机流量仍均匀采样不受影响),用 Algorithm 2 监控 difference-in-REO。结果:"1.25x deboost" 略微抑制原本占优的 young_adult 群体、降低公平惩罚;过激的 "2x deboost" 反而过度压制、使全局公平变差;"2x boost" 进一步放大优势、公平惩罚升高。

## 在本 wiki 中的位置

本文属于 [[recommender-systems|recommender-system]] 公平性 / 去偏方向,与 wiki 中关于 [[selection-bias]]、[[exposure-bias]]、[[debiasing]]、[[missing-at-random]] 的因果/统计去偏工作密切相关:它把"未被推荐即标签缺失"这一推荐场景特有的偏差,用随机流量(等价于一种 [[inverse-propensity-scoring]] 之外的均匀探测策略)加以校正,并强调 [[identifiability]] 在公平性测量中的核心地位。与 KuaiRand 等含随机曝光的推荐数据集(见 [[kuairand]]、[[kuairec]])类似,本文也通过引入随机流量来支持无偏评估,但首次将其用于 creator 侧群体公平性(REO)的估计与基准。来自 [[bytedance-research]] / TikTok。
