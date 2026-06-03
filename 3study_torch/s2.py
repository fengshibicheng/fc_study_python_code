import torch

# # 创建一个 2*3 的全 0 张量
# a = torch.zeros(2, 3)
# print(a)
#
# # 创建一个 2* 3 的全 1 张量
# b = torch.ones(2, 3)
# print(b)
#
# # 创建一个 2*3 的随机张量
# c = torch.randn(2, 3)
# print(c)
#
# # 从numpy 数组中创建张量
# import numpy as np
# numpy_array = np.array([[1, 2], [3, 4]])
# torch_array = torch.from_numpy(numpy_array)
# print(torch_array)
#
# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# # 在指定设备上创建张量
# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# d = torch.tensor([[1, 2], [3, 4]], device=device)
# e = torch.randn(2, 2, device=device)
#
# # 逐个元素相加
# print(d + e)
# # 逐个元素相乘
# print(d * e)
#
# # 张量的转置
# g = torch.randn(3, 2)
# print(g.t())
# # 返回张量的形状
# # print(g.shape()) # 返回形状
#
# # if torch.cuda.is_available():
# #     tensor_gpu = tensor_from_numpy.to('cuda')
#
# # 创建一个需要梯度的张量
# tensor_require_grad = torch.tensor([1.0], requires_grad=True)
#
# # 进行一些操作
# tensor_result_grad = tensor_require_grad * 2
#
# # 计算梯度
# tensor_result_grad.backward()
# print(tensor_result_grad) # 输出梯度
#
# # 创建一个需要计算梯度的张量
# x = torch.randn(2, 2, requires_grad=True)
# print('x', x)
#
# # 执行某些操作
# y = x + 2
# print('y', y)
# z = x * y * 3
# print('z', z)
# out = z.mean()
#
# print(out)
#
# # 反向传播，计算梯度
# out.backward()
#
# # 查看 x 的梯度
# print(x.grad)
#
# # 停止梯度计算
#
# # 使用 torch.no_grad() 禁用梯度计算
# with torch.no_grad():
#     y = x * 2


# 创建一个简单的神经网络

import torch.nn as nn
import torch.optim as optim

# 定义一个简单的全连接神经网络
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(2, 2)
        self.fc2 = nn.Linear(2, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# 创建模型实例
model = SimpleNN()

print(model)

class SimpleNN1(nn.Module):
    def __init__(self):
        super(SimpleNN1, self).__init__()
        self.fc1 = nn.Linear(6, 6)
        self.act = nn.Sigmoid()
        self.fc2 = nn.Conv2d(3, 1, 1)

    def forward(self, x):
        x = self.act(self.fc1(x))
        x = x + self.fc2(x)

        return x
model1 = SimpleNN1()
# print("model1的形状是：", model1)

# 随机输入
x = torch.randn(1, 2)
y = torch.rand(6, 6)

# 前向传播
output = model(x)

# output1 = model1(y)
print("output在model的结果是：", output)

# 定义损失函数
criterion = nn.MSELoss()

# 假设目标值是 1
target = torch.randn(1,1)

# 计算损失函数
loss = criterion(output, target)
print(loss)

# 定义优化器（使用Adam优化器）
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 训练步骤
optimizer.zero_grad() #清空梯度
loss.backward() # 反向传播
optimizer.step() # 更新参数