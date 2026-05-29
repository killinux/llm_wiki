---
type: source
subtype: paper
tags:
  - recommender-system
  - llm-agent
  - user-simulation
  - ab-testing
  - multimodal
created: 2026-05-29
updated: 2026-05-29
arxiv: "2601.04554"
raw: raw/2601.04554.pdf
authors:
  - Wenlin Zhang
  - Xiangyang Li
  - Qiyuan Ge
  - Kuicai Dong
  - Pengyue Jia
  - Xiaopeng Li
  - Zijian Zhang
  - Maolin Wang
  - Yichao Wang
  - Huifeng Guo
  - Ruiming Tang
  - Xiangyu Zhao
year: 2026
---

A/B Agent:一个多模态 LLM 用户智能体框架,在仿真沙盒中模拟用户的多模态感知、多页交互与决策,用以替代代价高昂的在线 A/B testing 来评估推荐模型。

## 问题

在工业推荐系统中,在线 [[ab-testing]] 是评估不同模型的关键手段,但存在三大痛点:资源消耗高、损害用户体验、评估延迟长(需收集足够数据才能得到统计显著性)。因此需要可靠的离线评估方法来仿真 A/B testing。

现有 [[user-simulation]] 方法难以复现真实用户行为,主要有两个 gap:
1. **仿真环境与真实平台 UI 之间的差距**:现有仿真环境(如 [[recsim]]、[[virtual-taobao]]、[[recagent]]、[[agent4rec]])只向用户呈现纯文本物品信息,忽略了真实用户在多粒度、多页 UI 上逐步感知与探索的过程,缺乏对丰富 [[multimodal]] 信息和多层界面的感知能力。
2. **多模态多层级信息下的用户行为轨迹建模**:真实用户跨界面与多模态内容交互、在感兴趣时探索、疲劳时退出,现有 agent 难以做到细粒度感知与拟人化探索。

## 方法

A/B Agent 框架由三部分组成(见 Figure 4):

**MM-ML-1M 数据集**:在 [[movielens-1m]] 基础上扩展,补充电影海报(image)、IMDB 评分、投票数、导演、演员、剧情简介等多模态/上下文元信息。统计:6,040 用户、3,952 部电影、交互稀疏度 4.19%。每部电影含 Title/Overview/Genres/Rating/Vote Count/Release Date/Directors/Actors(文本/数值)与 Poster(图像)。

**Recommendation Sandbox Environment**:模仿 Netflix/IMDB 的多模态交互式 UI,含 Home Page(海报、标题、评分、类型;可翻页/点击)与 Movie Detail Page(高清海报、剧情、元数据;可 watch/rate/back)。集成多种推荐算法(Popularity、[[factorization-machines|FM]]、[[deepfm|DeepFM]]、AFN 等),用 [[ctr|CTR]](点击率)、CVR(转化率,详情页查看比例)、Average Rating(AR)评估。

**A/B Agent 架构**,含四个模块:
- **Profile Module**:用户画像(性别、职业、年龄、地区)+ 由 LLM 根据交互历史 prompt 总结的 user preferences。
- **Memory Module**:整合文本与视觉检索的 [[agent-memory]]。长期记忆用 [[text-embedding-3-small|text-embedding-3-small]] 编码文本、用 [[clip|CLIP]] 编码海报视觉特征,跨 session 检索稳定偏好;短期记忆以结构化格式跟踪当前 session 内交互(界面类型、局部观察、1–5 兴趣估计、所采取动作)。
- **Action Module**:定义界面相关的动作(home page 上 click/next page/previous page;detail page 上 view/rate/back)。
- **Fatigue System**:每个 session 起始有初始疲劳值,每个动作消耗疲劳,降到 0 时主动退出。动作按真实频率分高/中/低频(浏览类高频、点击中频、观看评分低频)。疲劳成本由动作类型和当前兴趣水平决定,公式 F = C_a · (φ_max − (ι−ι_min)(φ_max−φ_min)/(ι_max−ι_min)),其中兴趣越高疲劳越低。

backbone LLM 使用 [[gpt-4o]]、[[gpt-4o-mini]]、[[gemini-2-5-flash]]。

## 结果

在 MovieLens 与 Amazon Fashion 两域评估,交互按时间 7:2:1 划分,真实反馈用 Recall@20 / NDCG@20 度量仿真保真度。

**模型评估(Table 2)**:在三种 backbone 下,A/B Agent 给出的模型排序与离线评估一致——Pop 优于 Random,FM 优于二者,DeepFM 与 AFN 表现最佳。例如 ML 域 GPT-4o 下 DeepFM 取得最佳 CTR 0.4453、CVR 0.3458、AR 4.75;真实世界 DeepFM Recall 0.0429、AFN NDCG 0.1238。三种 backbone 给出一致排序,显示对 LLM 选择不敏感(backbone robustness),且在 CTR/CVR/AR 三指标上排序一致。跨域(Amazon Fashion)仿真结果仍与真实趋势一致。

**数据规模影响(Table 3)**:DeepFM 在 50%/75%/100% 训练数据下,CTR、CVR、AR 随数据增加单调提升(如 GPT-4o-mini 下 CTR 从 0.2205→0.2745→0.2891),与真实评估一致。

**特征重要性(Table 4)**:消融 User ID Only / Movie ID Only / All 三变体,减少特征导致全指标下降;Movie ID Only 在 CTR/CVR 上优于 User ID Only,显示物品侧特征更有信息量;A/B Agent 能检测细粒度差异。

**用户口味对齐(Figure 5)**:用 1:9 / 1:4 / 1:1 正负比推荐列表测试,正样本越多 CTR/CVR/AR 越高,显示与真实偏好强对齐。

**活跃特质对齐(Figure 6)**:为 agent 分配 low/medium/high 三种活跃特质,点击分布均近高斯,均值点击数从 3.2(low)→4.0(medium)→5.8(high),验证疲劳系统对用户参与度的调节有效。

**数据增强(Table 5)**:采集 2,518 次首页点击与 1,884 次详情页观看记录(约 4K,远小于原 700K 训练集),并入原数据训练 8 个 CTR 模型(NFM、xDeepFM、Wide&Deep、DCN、DeepFM、AFN、AutoInt、PNN)。带视觉的仿真数据使 AUC 普遍提升超过 0.002(CTR 预测中 0.001 即视为显著改进),如 view data 上 NFM/xDeepFM/DeepFM 分别提升 0.0037/0.0039/0.0022。

**视觉模态消融(Table 5)**:去掉海报后仿真数据增益明显变小(DeepFM 带视觉点击数据从 0.7520→0.7541,无视觉仅 0.7501),证明视觉模态对产生真实用户行为关键。

**Case Study(Table 6)**:展示 click(喜欢海报与类型)、next page(讨厌剧情类型)、watch & rate 5.0(匹配过往高评分)、exit(影片偏老且疲劳高)四类决策,验证 agent 对偏好、拒绝信号与疲劳退出的细致模拟。

**与现有 simulator 对比(Table 7)**:A/B Agent 是唯一采用 Sandbox UI 且支持多模态的用户 simulator,评估覆盖 Offline + Case Study。

局限:框架在封闭环境内运行,未纳入社交媒体/同伴影响等外部因素;LLM 的 [[hallucination]] 与重复行为可能影响仿真可靠性。

## 在本 wiki 中的位置

本文属于 [[llm-agents|llm-agent]] 用于 [[recommender-systems|recommender-system]] 评估的 [[user-simulation]] 方向,与 [[agent4rec]]、[[recagent]]、[[recsim]]、[[virtual-taobao]] 同源,但首创在带海报的 multimodal Sandbox UI 中模拟多页感知与疲劳驱动的退出行为。它把 [[clip]] 视觉编码与 [[agent-memory]] 结合,服务于替代在线 [[ab-testing]] 的离线推荐模型评估与数据增强。作者主要来自 [[city-university-of-hong-kong]] 与 [[huawei-noahs-ark-lab]],与 [[deepfm]]、[[factorization-machines]] 等 CTR 模型工作一脉相承。
