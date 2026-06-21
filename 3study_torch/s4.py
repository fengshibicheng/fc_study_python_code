# -*- coding: utf-8 -*-
"""
@Time ： 2026/5/21
@Auth ： fc
@File ： s4.py
@IDE ： PyCharm
"""
import torch
from torch.utils.data import Dataset
from torch.utils.data import DataLoader

# 自定义数据集类
class MyDataset(Dataset):

    def __init__(self, X_data, Y_data):
        """
        初始化数据集，X_data和Y_data是两个列表或者数组
        :param X_data: 输入数据
        :param Y_data: 对应的标签数据
        """
        self.x_data = X_data
        self.y_data = Y_data

    def __len__(self):

        return len(self.x_data)

    def __getitem__(self, idx):
        """返回指定索引的数据集"""
        x = torch.tensor(self.x_data[idx], dtype=torch.float32)
        y = torch.tensor(self.y_data[idx], dtype=torch.float32)

        return x, y

X_data = [[1, 2], [3, 4], [5, 6], [7, 8]]
Y_data = [1, 0, 1, 0]

# # 创建数据集实例
# dataset = MyDataset(X_data, Y_data)
#
# # 创建Dataloader 实例，batchsize设置每次加载的样本数量
# dataloader = DataLoader(dataset, batch_size=2, shuffle=True)
#
# for epoch in range(1):
#     for idx, (inputs, labels) in enumerate(dataloader):
#         print(f'Batch: {idx+1}')
#         print(f'Inputs: {inputs}')
#         print(f'Labels: {labels}')

# 创建数据集实例
dataset = MyDataset(X_data, Y_data)

# 创建Dataloader实例， batchsize设置每次加载的样本数量
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

for epoch in range(1):
    for indx, (inputs, labels) in enumerate(dataloader):
        print()

import torchvision.transforms as transforms
from PIL import Image

# 定义数据预处理的流水线
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  #标准化
])

# 加载图像
image = Image.open('image.jpg')

# 应用预处理
image_tensor = transform(image)
print(image_tensor.shape) # 输出张量的形状