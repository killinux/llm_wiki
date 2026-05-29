---
type: source
subtype: paper
tags: [llm, multimodal, autonomous-driving, motion-planning, closed-loop-control, llm-agent, embodied-reasoning]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2312.09245
raw: raw/2312.09245.pdf
authors: [Erfei Cui, Wenhai Wang, Zhiqi Li, Jiangwei Xie, Haoming Zou, Hanming Deng, Gen Luo, Lewei Lu, Xizhou Zhu, Jifeng Dai]
year: 2023
---

DriveMLM 是一个基于 LLM 的自动驾驶框架,通过将多模态 LLM(MLLM)的语言决策输出与模块化 AD 系统的行为规划状态(behavioral planning states)对齐,从而在 CARLA 仿真器中实现闭环(closed-loop)自动驾驶。

## 问题

[[large-language-models]] 拥有世界知识、逻辑推理与类人认知能力,被视为自动驾驶(AD)中潜在的 planner。但已有把 LLM 接入 AD 的工作大多只生成语言/概念层面的决策,无法直接转化为车辆控制信号,因而难以在真实环境或写实仿真器中做**闭环驾驶**。传统模块化 AD 系统(如 Apollo、Autopilot)用行为规划模块连接高层策略目标与底层操作动作,其决策状态可被后续运动规划与控制模块转成控制信号。因此本文的核心问题是:如何让 LLM 的语言决策与行为规划模块的决策状态对齐,设计一个可在写实仿真器上跑闭环的 LLM 驱动 AD 系统。

## 方法

DriveMLM 框架包含三个关键设计:

- **行为规划状态对齐(Behavioral Planning States Alignment)**:把 LLM 的语言决策输出与 CARLA Apollo 系统行为规划模块的决策阶段对齐。决策分为两类:速度决策状态 [KEEP, ACCELERATE, DECELERATE, STOP] 与路径决策状态 [FOLLOW, LEFT_CHANGE, RIGHT_CHANGE, LEFT_BORROW, RIGHT_BORROW]。这样 LLM 输出可即插即用(plug-and-play)转成控制信号。

- **MLLM Planner**:由多模态 tokenizer 与 MLLM decoder 组成。tokenizer 处理三类输入:(1) 时序多视角图像,用 CLIP/[[vit]] 视觉编码器 + Temporal QFormer 处理;(2) LiDAR 点云,用 single-stride sparse transformer (SST) 编码,并通过 image-lidar CLIP 模型把点云特征对齐到图像特征空间;(3) 系统消息 M 与用户指令 U,用 LLM 的 token embedding 层编码。decoder 基于 [[llama]](LLaMA-7B,husky 模型)生成决策状态 S 与对应的自然语言解释 E。属于 [[tool-use]] 之外的 embodied 决策范式,可看作面向驾驶的 [[llm-agent]]。

- **高效数据引擎(Efficient Data Engine)**:在 CARLA 采集 280 小时驾驶数据(50k 路线,30 个驾驶场景,8 张地图),由专家司机/agent 驾驶并记录;速度与路径决策由手工规则从轨迹自动标注,解释标注由规则生成后经人工与 [[gpt-3-5]] 精炼,以低成本生成决策状态 + 解释数据。

整个 MLLM 用 cross-entropy loss 做 next-token prediction 训练,视觉编码器用 ViT-g/14(EVA-CLIP),LiDAR 用 GD-MAE(在 ONCE 上微调),图像分辨率 448×448,训练 2 epoch、batch size 256。

## 结果

- **闭环驾驶(CARLA Town05 Long)**:DriveMLM 取得 **Driving Score (DS) 76.1**、Route Completion (RC) 98.1、Infraction Score (IS) 0.78、**Miles Per Intervention (MPI) 0.96**,DS 与 MPI 均为对比方法中最高。相比规则法 Apollo(DS 71.4),DS 高 4.7 点;相比 ThinkTwice(DS 70.9)、Interfuser(DS 68.3)、Roach(DS 43.6)等数据驱动法均大幅领先。摘要中指出替换 Autopilot 与 Apollo 决策模块后分别带来 3.2 / 4.7 点的 DS 提升。
- **开环评测(CARLA Town05)**:决策准确率 **75.23%**,远超 LLaVA-1.5(22.92%)、InstructBLIP(17.92%)与 Apollo(18.53%);路径/速度各类决策 F1 全面领先(如 path-change 0.52、path-borrow 0.89、speed-keep 0.91);解释质量 BLEU-4 40.46、CIDEr 124.91、METEOR 56.54,均显著优于基线。
- **消融**:多视角图像(MV)带来 +18.19% 准确率提升;Temporal QFormer (TQ) 比直接拼接时序 token 提升 7.4% 且计算量更小;点云(PC)对性能提升有限(疑因 sparse pyramid transformer 与 MLLM decoder 表征差异大)。
- **真实场景泛化**:在 nuScenes 验证集标注 6019 帧做 zero-shot 评测,决策准确率 0.395,显示一定泛化能力。
- 还测试了 lmdeploy / vLLM 下的推理速度(s/token),发现轻量模型(如 mini-InternVL-2b)有实现实时决策的潜力。

## 在本 wiki 中的位置

DriveMLM 是把 [[large-language-models]] 与多模态感知应用到 **自动驾驶闭环控制** 的代表性工作,可视为面向具身/驾驶场景的 [[llm-agent]]。它把 LLM 决策与传统行为规划状态对齐,连接了语言推理与车辆控制,与本 wiki 中 [[embodied-reasoning]]、[[grounding]]、[[saycan]] 等"语言模型驱动具身/物理动作"的条目同属一脉;作者来自 [[tsinghua-university]] 与 Shanghai AI Lab,模型构建在 [[llama]] 与 [[vit]] 之上,可作为理解 MLLM 在物理世界决策落地的入口。
