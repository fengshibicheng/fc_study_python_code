
# 斐波那契数列
# 递归 1 1 2 3 5 8 13 21 34....
# def feibo(n):
#     if n == 1 or n ==2:
#         return 1
#     else:
#         return  feibo(n-1) + feibo(n-2)
#
# print(feibo(6))

# # 递归实现街城管
# def jiecheng(n):
#     for i in range(n):
#         for j in range(1, i+1):
#             print(f'{i} × {j} = {i*j}', end='  ')
#         print()
#
# jiecheng(9)


# 比如输入7 输出应为 =  1 * 2 * 3 * 4 * 5 * 6 * 7
def diguijc(n):
    if n == 1:
        return 1
    else:
        return diguijc(n-1) * n

res = diguijc(5)
print(res)