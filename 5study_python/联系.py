import torch
import torch.nn.functional as F

input = torch.tensor([[1, 2, 3, 4, 5],
                      [6, 7, 8, 9, 0],
                      [1, 1, 1, 2, 2],
                      [2, 3, 4, 5, 6],
                      [3, 5, 6, 7, 8]])

kernel = torch.tensor([[1, 1, 1],
                        [2, 2, 2],
                        [3, 4, 5]])

input = torch.reshape(input, (1, 1, 5, 5))
kernel = torch.reshape(kernel, (1, 1, 3, 3))

output = F.conv2d(input, kernel, stride=1)

print(output)
