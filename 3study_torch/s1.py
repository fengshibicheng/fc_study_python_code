# -*- coding: utf-8 -*-
"""
@Time ： 2026/5/14
@Auth ： fc
@File ： s1.py
@IDE ： PyCharm
"""
import torch

# 设置数据类型和设备
dtype = torch.float      # 张量数据类型为浮点型
# device = torch.device('cpu')     # 本次计算在CPU上进行
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')     # 自适应选择平台进行计算

# 创建并打印两个随机张量 a 和 b
a = torch.randn(2, 3, dtype = dtype, device = device)   # 创建一个 2*3 的随机张量
b = torch.randn(2, 3, dtype = dtype, device = device)   # 创建一个 2*3 的随机张量

print("张量 a：", a)
print("张量 b：", b)

# 两个张量逐元素相乘
print("两个张量逐个元素相乘 a * b：", a * b)

# 张量中元素求和
print("张量a元素求和：", a.sum())

# 输出张量 a 中第 2 行第 3 列的元素（注意索引从 0 开始）
print("张量 a 中第 2 行第 3 列的元素为：", a[1, 2])

# 输出张量 b 中最大的元素
print("张量 b 中最大的元素：", b.max())

