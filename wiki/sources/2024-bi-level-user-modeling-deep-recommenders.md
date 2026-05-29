---
type: source
subtype: paper
tags: [recommender-system, ctr, user-modeling, deep-recommender-system, group-modeling, personalized-ranking]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2410.20730
raw: raw/2410.20730.pdf
authors: [Yejing Wang, Dong Xu, Xiangyu Zhao, Zhiren Mao, Peng Xiang, Ling Yan, Yao Hu, Zijian Zhang, Xuetao Wei, Qidong Liu]
year: 2024
---

# GPRec:面向深度推荐系统的双层(bi-level)用户建模

GPRec 提出一种即插即用的双层用户建模方法,同时在"群体(group)"与"个体(individual)"两个层面刻画用户:用可学习分类器把用户划入群体并配以双向(正/负)群体嵌入,再从 ID 类特征中提炼独立的个体偏好,在三个公开数据集上稳定提升各类深度推荐主干的 CTR 预测效果。

## 问题

深度推荐系统([[recommender-system]] / Deep Recommender Systems, DRS)通常对所有特征一视同仁,堆叠复杂结构来增强[[factorization-machines|特征交互]]的捕捉能力,却**未充分利用用户专属特征**进行 user modeling,从而错失关键用户模式。已有 user modeling 方法又往往只聚焦单一层面:

- **个体建模(individual modeling)**:为每个用户定制结构/参数(如 [[autoint|APG]]、PEPNet),能捕捉细粒度个人偏好,但忽视用户间联系,难以利用[[collaborative-filtering|协同]]知识。
- **群体建模(group modeling)**:先按用户特征把用户分到 G 个群体,再为各群体分配结构/参数(如 [[mmoe]]、[[ple]]、STAR、DGPM),更泛化但更粗粒度,且当群体模式与个人兴趣冲突时会误导推荐(例如偏好爵士乐的用户被归入宽泛的"音乐爱好者"群体)。

二者互补,但现有工作几乎不兼顾。论文要解决:如何在一个统一框架里**同时整合群体与个体模式**,且能灵活插入各种 DRS 主干。

## 方法

GPRec(**G**roup modeling + enhanced **P**ersonalization for **Rec**ommendation)是模块化、即插即用框架,在主干输出的基表示 r_b 之外,额外产出群体表示 r_G 与个体表示 r_P,再整合进预测模块,实现双层建模 F_{u,g(x_u)}(x)。

- **用户群体建模(可学习群体划分)**:不依赖 'Gender'/'Age' 等显式属性的刚性划分,而用一个可学习深度分类器 g 对用户嵌入 E_u 打分,得到 2×G 的分类分数 S(每个群体含"归入"与"排除"两类分数);再用 [[mixture-of-experts|Gumbel-Softmax]] 把平滑分数转成近似 0/1 的二值掩码 M,使群体划分更确定、避免正负群体模式混淆。用户可同时归属多个正群体。
- **双向群体嵌入(dual group embedding)**:为每个群体学习一对嵌入——正嵌入 p_i(代表组内用户偏好)与负嵌入 n_i(代表组外用户的相反倾向)。相比传统单嵌入只能表示 G 种模式,双向嵌入把表达空间扩展到 2^G。群体表示 r_G = M ⊙ E_G。配套两个辅助损失:用 r_G 预测物品偏好的监督损失 L_G,以及用反向掩码 (1−M) 构造对照表示 r_G^{Con} 的对比损失 L_G^{Con},以加深正负群体嵌入的区分度。
- **个体偏好学习(individual preference learning)**:把 'UserID' 等 ID 类(id-like)特征视为承载更深个人偏好的个人特征 E_p,经 MLP 得到个体表示 r_P。为避免 r_P 与 r_G 信息重叠(冗余),引入[[disentangled-representation-learning|正交损失]] L_O(r_G 与 r_P 的余弦相似度),解耦两层表示、凸显独特个人偏好。
- **三种与主干整合的策略**:Input 策略(把 r_b、r_G、r_P 直接拼入预测 MLP)、Dynamic Parameter 策略(由 r_G、r_P 动态生成预测层参数)、Ensemble 策略(对 r_b、r_G、r_P 各出一个预测再平均,思路类 [[deepfm]]、Wide&Deep)。总损失 L = L_major + λ1·L_G − λ2·L_G^{Con} + λ3·L_O,端到端训练。

## 结果

- **数据集**:ML1M([[movielens-1m]])、TenRec([[tencent]] 浏览器数据)、[[kuairand]](取 pure 版,30 个用户特征),均按 8/1/1 划分,任务为 [[ctr]] 预测,指标 AUC(越高越好)与 LogLoss(越低越好),取 5 个随机种子均值,best 方法用单侧 t-test(p<0.05)做显著性检验。
- **RQ1/RQ2 对比基线(Table II)**:GPRec 可与 MLP、[[deepfm]]、DCN、GDCN、FinalMLP、DESTINE 等特征交互主干结合。以 GDCN 为主干时,GPRec(GDCN) 在三数据集上 AUC 全面领先所有基线:ML1M 0.8161、TenRec 0.9180、KuaiRand 0.7573,均为标星显著提升;LogLoss 同样最优(如 ML1M 0.5167、TenRec 0.3231)。与 user modeling 类方法([[mmoe]]、[[ple]]、STAR、APG、PEPNet)相比,GPRec(MLP) 在 ML1M(AUC 0.8141)等也取得最优/具竞争力结果。值得注意,需预定义划分准则的 MMoE/PLE/STAR 在缺 'Gender' 的 KuaiRand 上反而掉点,凸显可学习群体划分的优势。
- **RQ3 兼容性 + 消融(Table III & Fig.2)**:'Base' 为裸主干,GPRec 在 DCN/GDCN/DESTINE/FinalMLP 上一致超过裸主干与最相近基线 DGPM(DGPM 无法接入 FinalMLP)。五个变体消融显示:去掉双向群体嵌入(GPRec-1)、去掉个体表示 r_P(GPRec-2,LogLoss 明显变差)、分别去掉 L_G / L_G^{Con} / L_O(GPRec-3/4/5)都会降性能,证明各组件均有贡献。
- **RQ4 超参(Fig.3,ML1M+MLP)**:群体数 G 与温度 τ 单调改变测试,最优配置 G=60、τ=0.5;G 过大会导致群体嵌入欠训练,τ 过小/过大都会损害正负群体对比学习;所有设置下 GPRec 的 AUC 均超过裸 MLP 基线(0.8081),体现稳定性。
- **RQ5 可视化(Fig.4)**:GPRec 学到的群体嵌入余弦相似度热图中,正负嵌入对相似度很低(如 p_2 与 n_2 仅 0.03),而 DGPM 平均相似度高达 0.9,验证 GPRec 学到了对照、多样的群体模式。

## 在本 wiki 中的位置

- 属于 [[recommender-system]] / [[ctr]] 预测中的 **user modeling** 方向,核心是把"群体"与"个体"两层显式建模并解耦,与单层方法形成对比:个体侧对照 [[autoint|APG]]/PEPNet 的逐用户参数化,群体侧对照 [[mmoe]]、[[ple]] 等多任务/多场景框架及 DGPM 的动态群体参数建模。
- 作为即插即用框架,可叠加在 [[deepfm]]、DCN/GDCN、FinalMLP、DESTINE 等[[factorization-machines|特征交互]]主干之上,与本 wiki 的[[recommender-systems]]条目互为补充。
- 方法上用 [[mixture-of-experts|Gumbel-Softmax]] 做硬性群体划分、用对比损失增强嵌入区分度、用[[disentangled-representation-learning|正交损失]]解耦表示,与表示学习/解耦表示相关条目相通。
- 由小红书(Xiaohongshu)等工业界与 City University of Hong Kong 等高校合作产出,面向真实工业推荐场景,代码已开源。
