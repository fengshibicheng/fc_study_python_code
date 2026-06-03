# 百钱买百鸡
'''
一共有100块钱，需要买100只鸡
公鸡 == 3 元 ==> 33只
母鸡 == 1元 ==> 100只
小鸡 == 0.5元 ==> 200只
问：100块钱买100只鸡，一共有多少种方案
'''
# 版本一
# num = 1
# for gj in range(34):
#     for mj in range(101):
#         for xj in range(201):
#             if gj + mj + xj == 100 and gj*3 + mj*1 + xj*0.5 == 100:
#                 print(f'公鸡买{gj}只，母鸡买{mj}只，小鸡买{xj}只，费用{gj*3 + mj*1 + xj*0.5}元')
#                 num +=1
# print(num)

# # 优化版本 二
# num = 1
# for gj in range(34):
#     for mj in range(101):
#         xj = 100 - gj - mj
#         if gj*3 + mj*1 + xj*0.5 == 100:
#             print(f'公鸡买{gj}只，母鸡买{mj}只，小鸡买{xj}只，费用{gj*3 + mj*1 + xj*0.5}元')
#             num +=1
# print(num)


# def fun(a, b=[]):
#     b.append(a)
#     return b
# print(fun(1))
# print(fun(2))
# print(fun(3, [4]))



def function(x, y = '+', *args):
    if y == '+':
        print('执行加法运算，' , args[1] + args[2])
    else:
        print('执行减法运算，', args[1] - args[2])

function(1, '+',11,12,12 )


