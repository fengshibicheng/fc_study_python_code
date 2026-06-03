# -*- coding: utf-8 -*-
"""
@Time ： 2026/5/21
@Auth ： 冯成
@File ： s3.py
@IDE ： PyCharm
"""
import torch
import torch.nn as nn
import torch.optim as optim

# 1、定义一个简单的网络模型
class SimpleNN(nn.Module):

     def __init__(self):
         super(SimpleNN, self).__init__()
         self.fc1 = nn.Linear(2, 3)
         self.fc2 = nn.Linear(3, 1)
         self.act = nn.Sigmoid()

     def forward(self, x):
         x = self.fc1(x)
         x = self.act(self.fc2(x)) + x

         return x

# 2、初始化网络模型
model = SimpleNN()

# 3、初始化损失函数以及优化器
criter = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# 4、定义假设的数据集
X = torch.randn(10, 2)
Y = torch.randn(10, 1)

# 5、模型训练
for epoch in range(100):
    # 清理梯度缓存
    optimizer.zero_grad()
    # 前向传播
    target = model(X)
    # 计算损失值
    los_mse = criter(target, Y)
    # 反向传播
    los_mse.backward()
    # 更新梯度信息
    optimizer.step()

    # 打印训练信息
    if (epoch+1) % 10 == 0:
        # print(f'当前epoch为：{epoch+1}/100, 损失值为：{los_mse.item():.4f}')
        print(f'当前epoch为：{epoch+1}/100, 损失值为：{los_mse}')


model.eval()
with torch.no_grad():
    tag = model(X)
    los = nn.MSELoss(tag, Y)
    print(f'测试loss:{los.item():.4f}')