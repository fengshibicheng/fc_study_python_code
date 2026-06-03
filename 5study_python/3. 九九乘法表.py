
# 正向输出乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(f'{i}×{j}={i*j}', end=' ')
#     print()

# while 循环实现九九乘法表
# i = 1
# while i <= 9:
#     for j in range(1, i+1):
#         print(f'{i}×{j}={i*j}', end=' ')
#     print()
#     i +=1

# # 反向输出乘法表
# i = 9
# while i >= 1:
#     for j in range(1, i+1):
#         print(f'{i}×{j}={i * j}', end=' ')
#     print()
#     i -=1

for i in range(9, 0, -1):
    for j in range(1, i):
        print(f'{i}×{j}={i*j}', end=' ')
    print()