---
type: topic
tags: [recommender-system, causal-inference, debiasing, doubly-robust, deconfounder, counterfactual]
created: 2026-05-30
updated: 2026-05-30
sources: 18
---

# 推荐系统去偏与因果推断 (Debiasing & Causal Inference in Recommendation)

> 一句话:推荐日志是**观察性而非实验性**数据,充满偏差(曝光/选择/流行度/位置/从众)。直接拟合相关性会学到虚假关联
> ("贵的商品更易得负反馈""啤酒推尿布"),损害公平、鲁棒与用户满意度。去偏的目标是把"曝光=treatment、反馈=potential outcome"
> 当**因果问题**来估计**反事实**:若把未曝光 item 推给用户会得到什么反馈。

概念枢纽见 [[causal-inference]]、[[deconfounder]];综述见 [[2023-causal-inference-for-recommendation]]、[[2024-causal-discovery-recommender-systems]]。
本线在"评估可靠性"上与 [[rl-for-recommendation]]、[[generative-social-simulation]] 共享同一条**验证**张力。

---

## 一、两个因果框架与偏差谱
- **潜在结果 (Rubin / Neyman)** 与 **结构因果模型 (Pearl SCM)**:推荐去偏多用前者(treatment=曝光,outcome=反馈)。
- **偏差类型**:[[selection-bias|选择偏差]]、曝光偏差、流行度偏差(放大马太效应)、位置偏差、从众 (conformity) 偏差。根因是
  **隐藏混杂 (hidden confounder)** 同时影响曝光与反馈(如社会经济地位)。

## 二、三大方法族

### 1) 倾向加权 (IPS)
用逆倾向分数 (Inverse Propensity Scoring) 对样本重加权以还原无偏期望;简单但**方差高**、对倾向估计敏感。是 [[offline-evaluation|离线评估]] 的基础。

### 2) Doubly Robust (DR) 家族
结合**倾向**与**插补 (imputation)** 两个估计器,只要其一准确即无偏——但插补模型在小样本上训练、外推到全体易失准:
- [[2023-conservative-doubly-robust]](CDR)指出 **"毒性插补 (poisonous imputation)"**:不准的插补反而**增大**偏差/方差,实测毒性比例普遍 **>35%**(DR-JL 在 Coat 上达 45.9%);
  用 **MC-Dropout** 估计插补的均值/方差来**审查过滤**不可靠插补。

### 3) Deconfounder(替代/潜在混杂)家族 —— 一条清晰演化线
不依赖工具变量,直接**推断未观测混杂的替代变量**再校正:
| 工作 | 关键推进 |
|---|---|
| [[deconf-mf]] | 浅层 Poisson MF 推断 substitute confounder(建模力弱,退化为 single-cause) |
| [[2022-deep-causal-reasoning-for-recommendations]](Deep-Deconf) | 用 **VAE** 把推荐建模为 multi-cause multi-outcome,捕捉非线性 co-exposure |
| [[2023-idcf-debiasing-recommendation]](iDCF) | 引入**代理变量 + 近端因果推断**给出**可识别性**保证(破解 Deconfounder 的 non-identification:如 p(rᵃ) 落在 [0.33,0.78] 区间矛盾) |
| [[2025-causality-constraint-debiasing-recommender]](LCDR)/ [[2024-mitigating-dual-latent-confounding-biases]](IViDR) | 用 **identifiable VAE (iVAE)** 在**低质量/有噪代理**下仍恢复混杂,处理双重潜在混杂 |

另见 [[deep-deconf]]、[[2025-policy-guided-causal-state-representation]]、反事实数据增强 [[2025-caserec-counterfactual-augmentation-system-exposure]]。

## 三、短视频时长去偏(垂直战场)
观看时长 (watch time) 是短视频主目标,但严重受**视频长度偏置**等干扰:
- [[2023-video-length-debiasing-microvideo-rec]]、[[2023-d2co-watch-time-debias]]、[[2024-counterfactual-watch-time]]、
  [[2024-conditional-quantile-estimation-watch-time]]、[[2025-relative-advantage-debiasing-watch-time]]、[[2024-deconfound-release-interval-bias]]。
  与生成式时长建模 [[2024-generative-regression-watch-time-prediction]] 互补。

## 四、核心争议:去偏的"评估"本身可能不可靠
与本 wiki 反复出现的验证主题同构:
- [[2025-debias-can-be-unreliable]] 证明:用 **randomly-exposed 数据集**(代理全曝光)按传统方式算 Recall **并不可靠**——
  只有在大 K 时才与全曝光 Recall 强相关,而实际关心的小 K(如 K=50)处相关性很弱,可能导致对既往去偏方法效果的**错误结论**;提出 **URE** 做无偏 Recall 估计。
- 全曝光数据稀缺(公开仅 [[kuairec|KuaiRec]]),使去偏方法的"真值"评估长期困难。

## 五、开放问题
- **可识别性 vs 假设强度**:Deconfounder 无需 IV 但有 non-identification;加代理变量/iVAE 缓解,但代理质量难保证。
- **评估金标准缺失**:全曝光数据稀缺 + 离线指标不可靠([[2025-debias-can-be-unreliable]]、[[2025-sampling-strategies-offline-recommender-evaluation]])。
- **与 RL / 长期价值结合**:去偏的反事实估计如何嵌入 [[reinforcement-learning-for-recommendation]] 的信用分配([[uplift-modeling]] 是接口)。
- **LLM 时代**:用 LLM 做因果发现/反事实生成是否可靠。

## 相关概念页
[[causal-inference]]、[[deconfounder]]、[[doubly-robust]]、[[inverse-propensity-scoring]]、[[counterfactual-reasoning]]、
[[selection-bias]]、[[uplift-modeling]]、[[implicit-feedback]]、[[offline-evaluation]]、[[recommendation-fairness]]
