---
type: source
subtype: paper
tags:
  - autonomous-driving
  - multi-modal-llm
  - llm-planning
  - closed-loop-control
  - alignment
  - embodied-reasoning
created: 2026-05-29
updated: 2026-05-29
arxiv: 2312.09245
raw: raw/10.1007_s44267-025-00095-w.pdf
authors:
  - Erfei Cui
  - Wenhai Wang
  - Zhiqi Li
  - Jiangwei Xie
  - Haoming Zou
  - Hanming Deng
  - Gen Luo
  - Lewei Lu
  - Xizhou Zhu
  - Jifeng Dai
year: 2025
---

# DriveMLM: aligning multi-modal large language models with behavioral planning states for autonomous driving

DriveMLM 把 multi-modal LLM(MLLM)对齐到自动驾驶系统「行为规划模块」的离散 decision state(决策状态),从而让 LLM 的语言输出可直接转成车辆控制信号,在 CARLA 模拟器上实现 closed-loop(闭环)驾驶,并可即插即用替换 Apollo/Autopilot 的决策模块。

> 发表于 *Visual Intelligence* (2025) 3:22,DOI 10.1007/s44267-025-00095-w(Open Access)。通讯作者 Jifeng Dai(Tsinghua University)。这是一篇 LLM-for-autonomous-driving 论文,与本 wiki 的 [[llm-agents]]、[[llm-planning]]、[[grounding]] 等条目高度相关。

## 问题

现有把 [[large-language-models]] 引入自动驾驶(AD)的工作,大多只生成「语言层面的决策」,却无法在真实模拟器中做 closed-loop 驾驶。根本困难在于:

1. LLM 输出是语言/概念性的,不能直接用于车辆控制(转向、油门、刹车);
2. 直接让 LLM 预测控制信号(如 DriveGPT4)又与实时闭环控制存在巨大 gap,且常受限于单目相机等单一模态;
3. 传统模块化 AD 系统(如 Apollo、Autoware)依赖手工规则的有限状态机(finite state machine),难以覆盖长尾 corner case,缺乏对真实世界的理解与复杂 [[reasoning]] 能力。

作者的核心洞察:传统模块化系统中,高层目标与底层动作之间由 behavioral planning module(行为规划模块)连接,其 decision state 可被下游 motion planning 轻易转成控制信号。于是把 LLM 对齐到这一层的决策状态,即可既保留 LLM 的世界知识/推理,又获得可执行的闭环控制。

## 方法

DriveMLM 框架包含三个关键设计:

- **行为planning states alignment(决策状态对齐)**:把驾驶决策拆为两类离散状态——速度决策 [KEEP, ACCELERATE, DECELERATE, STOP] 与路径决策 [FOLLOW, LEFT_CHANGE, RIGHT_CHANGE, LEFT_BORROW, RIGHT_BORROW];每个时刻输出一个速度+一个路径决策,送入 CARLA AutoPilot/Apollo 的 motion planning 模块转为控制。状态定义写入 system message,让 LLM 输出收敛到决策空间。这是一种把 LLM 与下游模块接口对齐的 [[grounding]] / [[alignment]] 做法。
- **MLLM planner**:由 multi-modal tokenizer + MLLM decoder 组成。
  - 时序多视角图像:经 [[clip]] 视觉 encoder(实现中用 EVA-CLIP 的 ViT-g/14)提特征,再用 temporal QFormer(每视角设 N_Q=32 query)+ 跨注意力融合历史帧;
  - LiDAR 点云:用 image-lidar CLIP 把随机初始化的 single-stride sparse transformer(SST,基于 ONCE 上微调的 GD-MAE)对齐到冻结的 ViT-L/14 图像特征空间(cosine similarity loss);
  - system message 与 user instruction 作为普通文本经 token embedding 接入;
  - MLLM decoder 基于 LLaMA-7B,以 cross-entropy / next-token prediction 训练,输出决策状态 token S 与文本 explanation E。
- **Efficient data engine(数据引擎)**:在 CARLA 采集 280 小时、50k 条路线(8 张地图、30 个场景),用手工规则自动标注决策状态,explanation 先按场景生成再由人工精修、并用 [[gpt-3-5]] 扩充多样性,大幅降低标注成本。

实现细节:AdamW(β1=0.9, β2=0.95),cosine 学习率衰减,lr=5×10⁻⁵,2 个 epoch,batch size 256,图像分辨率 448×448;另以 InternVL 系列(Mini-InternVL、InternVL2.5)作为替换 backbone 验证模型无关性。

## 结果

闭环(CARLA Town05 Long,指标 DS/RC/IS/MPI):

- DriveMLM 取得 **DS 76.1、RC 98.1、IS 0.78、MPI 0.96**,DS 上大幅领先所有方法;相比规则式 Apollo(DS 71.4),提升约 **4.7 个点**(摘要称在 Town05 Long 上比 Apollo/Autopilot 决策模块替换分别提升 3.2、4.7 点),MPI 也为全场最高(0.96 vs Apollo 0.76),表示更少人工接管。
- 对比 data-driven 方法:Roach DS 43.6、Interfuser 68.3、ThinkTwice 70.9、MILE 61.1。

开环驾驶知识(CARLA Town05,Table 3):

- Ours-InternVL2.5 取得 **Acc 77.35%、BLEU-4 48.35、METEOR 58.30**,Ours-LLaMA 取得 Acc 75.23%、CIDEr 124.91,均显著优于 LLaVA-1.5(22.92%)、InternVL 2.0(34.26%)、LMDrive(42.93%)、OmniDrive(50.65%)、OpenEMMA(46.21%)等基线。

nuScenes 开环规划(L2 / collision / intersection):

- Ours-nuscenes 取得 L2 平均 0.33 m、collision 0.32%、intersection 1.56%,与 SOTA(UniAD、OmniDrive 等)相当或更优。

消融:

- sensor modality 上,multi-view(MV)图像比单视角带来约 **18.19% 的 accuracy 提升**;temporal QFormer 比直接拼接时序 token 再提升约 7.4%;LiDAR 点云对性能影响很小(疑因 SST 与 MLLM decoder 表征 gap)。
- backbone 替换(LLaMA→InternVL 系列)性能稳定,验证设计的 model-agnostic 特性。

此外,DriveMLM 能依自然语言指令改变决策偏好(如让行救护车而变道、或被指示闯红灯),展示出 instruction-following 与决策泛化能力;论文也分析了无信号灯路口等高动态场景的失败案例与实时推理速度(用 LMDeploy/vLLM 加速)。

## 在本 wiki 中的位置

本文是「把 LLM 作为规划器嵌入具身/真实控制系统」的代表作,与本 wiki 多条主线相连:

- **LLM 规划与具身**:把 [[large-language-models]] 用作 AD 的 behavioral planner,属于 [[llm-planning]] 与 [[embodied-reasoning]] 在自动驾驶垂直域的落地,可与 [[saycan]]、[[inner-monologue]]、[[voyager]] 等具身/规划 agent 对照。
- **对齐到可执行接口**:通过把语言输出对齐到离散 decision state 实现 [[grounding]] / [[alignment]],呼应本 wiki 中 LLM 输出落地为可执行动作的设计模式。
- **多模态 + CLIP 表征**:使用 [[clip]](EVA-CLIP/ViT)做视觉与 LiDAR 的跨模态对齐,体现 [[foundation-models]] 向下游控制任务迁移。
- **LLM 辅助数据标注**:用 [[gpt-3-5]] 扩充 explanation 多样性,是 LLM 用于数据引擎/合成标注的实例。

可作为「LLM agent 进入真实闭环控制」与「多模态 grounding」交叉处的参考条目。
