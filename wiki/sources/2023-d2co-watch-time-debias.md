---
type: source
subtype: paper
tags:
  - recommendation
  - video-recommendation
  - watch-time
  - duration-bias
  - debiasing
  - causal-inference
created: 2026-05-29
updated: 2026-05-29
arxiv: "2308.08120"
raw: raw/2308.08120.pdf
authors:
  - Haiyuan Zhao
  - Lei Zhang
  - Jun Xu
  - Guohao Cai
  - Zhenhua Dong
  - Ji-Rong Wen
year: 2023
---

提出 D²Co(Debiased and Denoised watch time Correction),从统一因果视角同时矫正视频推荐中观看时长的"时长偏差(duration bias)"与"噪声观看(noisy watching)",从被偏置和噪声污染的 watch time 中还原用户真实兴趣。

## 问题

在视频推荐中,watch time(观看时长)常被当作用户兴趣的标签,但它并非只由兴趣决定,还受两类非兴趣因素影响:

- 时长偏差(duration bias):用户倾向于在时长更长的视频上花更多时间,无论是否真正感兴趣;因此直接用 watch time 会让模型偏向推荐长视频。
- 噪声观看(noisy watching):用户需要时间(如 10s)去判断是否喜欢新推荐的视频,因而会在并不感兴趣的视频上停留一段时间。

作者在 [[kuairand]] 数据集上做先导实验(图 2)验证两者均真实存在。已有方法(如 Play Complete Rate / [[wtg]] / [[d2q]])大多只处理时长偏差、忽略噪声观看,且依赖关于用户兴趣分布的强假设(如各时长组兴趣分布一致),现实中往往不成立。

## 方法

将 watch time 视为三者的混合:用户真实兴趣水平、时长偏置观看时长 $w_d^+$、噪声观看时长 $w_d^-$。基于因果图(X 特征、D 时长、R 兴趣、W 观看时长)推导得到统一公式 $w = p_x^r w_d^+ + (1-p_x^r) w_d^-$,并给出 watch time 误差上界可分解为时长偏差误差 + 噪声观看误差(定理 1)。

D²Co 分两步:

- 估计偏置项与噪声项:在每个时长档(duration level)上,把 watch time 分布建模为两个隐高斯分布的混合,用 duration-wise 高斯混合模型(GMM, 2 个分量)估计 $w_d^+$、$w_d^-$;再用双向的频率加权移动平均(frequency-weighted moving average,窗口 $T$)对相邻时长的估计序列做平滑。
- 从 watch time 分离用户兴趣:用敏感度可控的矫正函数(sensitivity-controlled correction,式 12,含控制项 $\alpha$)而非普通仿射矫正来还原兴趣,得到 D²Co(S);可证明其对 $w_d^+$、$w_d^-$ 估计误差的敏感度低于普通仿射版 D²Co(A)(定理 3、命题 1)。

得到的兴趣作为监督信号训练推荐模型,不依赖用户兴趣分布的关键假设。整体流程见算法 1。

## 结果

在两个公开视频推荐数据集 [[kuairand]](KuaiRand-pure,26,988 用户 / 6,598 视频 / 1,266,560 交互,时长 [5,240]s)和 WeChat([[wechat-channels-dataset]],20,000 用户 / 96,418 视频 / 7,310,108 交互,时长 [5,60]s)上实验,采用 GAUC 与 nDCG@{1,3,5},backbone 为 [[fm]]、[[deepfm]]、[[autoint]]。

- 总体性能(表 2):D²Co(S) 在两数据集、所有 backbone 上均取得最优。以 AutoInt 为例,KuaiRand 上 GAUC 0.658、nDCG@1 0.453、nDCG@3 0.499、nDCG@5 0.532;WeChat 上 GAUC 0.556、nDCG@1 0.581、nDCG@3 0.586、nDCG@5 0.593,均显著优于次优方法($p<0.05$ 单尾 t 检验)。
- 用 debiased 标签(PCR/D2Q/WTG)训练普遍优于直接用 Watch Time;D²Co(A) 与 D²Co(S) 因额外考虑噪声观看进一步领先;敏感度矫正使 D²Co(S) 优于 D²Co(A)。
- 偏差 vs 噪声主导(图 5):KuaiRand 误差主要由时长偏差主导(噪声误差接近 0);WeChat 中噪声观看是主要问题。分时长档实验(表 3)显示 D²Co 在各档位相对提升显著,如 KuaiRand 长时长档 (94,240] 上 D²Co(S) nDCG@1 相对 Watch Time 提升 +92.9%,WeChat 短时长档 (0,16] 上 +108.9%。
- 在线 A/B(华为视频浏览器,数千万 DAU,表 4):D²Co(S) 相对生产基线 7 天平均提升 Impression +5.41%、VV +8.35%、MWT +1.31%、PCR +4.81%、CTR +2.92%。

代码开源:https://github.com/hyz20/D2Co.git

## 在本 wiki 中的位置

本文属于推荐系统中的 [[debiasing]] 与 [[causal-inference]] 方向,聚焦短视频场景下 watch time 作为兴趣标签的可靠性问题。它与同样关注短视频 watch time / 用户留存的工作([[kuairand]] 数据集、用户留存优化等)以及推荐去偏方法相邻,可作为"如何从有偏有噪的隐式反馈中还原真实用户兴趣"专题的核心节点。
