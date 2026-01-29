# GPA Calculator

版本：1.0
作者：Rafe Mei
许可协议：MIT

---
## 1. 项目简介

这是一个易于扩展的简易 GPA 计算器，可以通过原始的百分制成绩来使用多种主流算法得到均分以及 GPA。适用于本科阶段成绩整理、留学 GPA 换算预估与不同算法对比。

---

## 2. 功能特性

- 支持多种 GPA 计算模型（PKU / WES / Linear 等）
- 支持按学期或总体计算 GPA
- 通过 CSV 文件导入原始百分制成绩数据
- 便于新增 GPA 映射模型与统计方式

---

## 3. 环境依赖

- Python: 3.13.6 (tested)

---

## 4. 使用教程与计算模型

您可以打开 instructions 文件夹以查看软件的完整使用教程与 GPA 计算模型及其原理。

默认支持的计算标准：

1. 均分
	- Weighted Average
	- Arithmetic Mean
2. GPA（4分制）
	- PKU Model
	- WES Model (Non-official, Approximation)
	- Standard 4.0 Model
3. GPA（5分制）
	- Standard Linear Model
	- Step Mapping Model
