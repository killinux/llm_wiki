---
type: source
subtype: paper
tags: [agent, benchmark, multimodal, gui, computer-use, evaluation]
created: 2026-05-31
updated: 2026-05-31
arxiv: "2404.07972"
venue: "NeurIPS 2024"
year: 2024
---

# OSWorld：真实计算机环境中的多模态智能体基准

一句话：OSWorld 是首个在**真实操作系统环境**（Ubuntu/Windows/macOS）中评估多模态 [[llm-agents]] 执行开放式计算机任务能力的可扩展 [[benchmark]]。

## 问题

此前的智能体评估要么基于简化的模拟环境（如 [[alfworld]]、[[webshop]]），要么局限于单一应用（如 [[webarena]] 仅限网页浏览），无法反映真实桌面计算中的复杂性：用户在日常工作中需跨越多个应用程序（浏览器、文件管理器、终端、办公软件等）完成任务，需要 GUI 视觉理解、鼠标/键盘操作、文件系统交互等综合能力。缺乏一个在真实 OS 上运行、支持多应用工作流的统一评估平台。

## 方法

OSWorld 提供了一个基于虚拟机的可扩展评估框架：

- **真实 OS 环境**：任务在完整的 Ubuntu 和 Windows 操作系统上执行，包含真实桌面应用（LibreOffice、GIMP、VLC、VS Code、Thunderbird、Chrome 等）。
- **369 个多样化任务**：涵盖桌面应用操作、文件管理、网页浏览、以及需要**跨多个应用协作**的复合工作流（如从邮件下载附件→用表格软件处理→上传到网页）。
- **可执行评估**：每个任务都有程序化的验证脚本，自动检查最终状态（而非中间步骤），确保评估可重复且不依赖人工判断。
- 智能体通过**截图观察**（accessibility tree 也可用）感知环境，通过 pyautogui 等方式执行鼠标点击、键盘输入等操作。

## 结果

- **人类基准**：72.36% 成功率（人类评估者完成同一任务集）。
- **最佳模型**：基于 [[gpt-4v]] 的智能体仅达 **12.24%** 成功率，与人类差距悬殊（60+ 百分点）。
- **关键瓶颈分析**：
  - **GUI grounding**：模型难以准确定位屏幕元素（按钮、菜单项、文本框），尤其在复杂布局中。
  - **操作知识（Operational Knowledge）**：模型缺乏对特定应用操作流程的了解（如 GIMP 的图层操作、LibreOffice 的宏设置）。
  - **长程规划**：跨应用任务需要较长的动作序列，模型在多步规划中频繁出错或陷入死循环。
- 使用 accessibility tree 作为辅助输入可部分缓解 GUI grounding 问题，但整体成功率提升有限。

## 相关页

本文是 [[llm-agents]] 在**真实计算机环境**中评估的里程碑，将 agent 评估从受限环境（[[webarena]]、[[agentbench]]）推进到完整 OS 级别。与 [[benchmark]] 谱系中的 [[webarena]]（纯网页）、[[agentbench]]（多环境但非真实 OS）形成互补。GUI grounding 挑战与 [[multimodal-llm]] 的视觉理解能力直接相关。
