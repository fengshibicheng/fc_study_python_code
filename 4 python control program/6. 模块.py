# # -*- coding: utf-8 -*-
# """
# @Time ： 2026/5/10
# @Auth ： fc
# @File ： 6. 模块.py
# @IDE ： PyCharm
# """
# # -*- coding: utf-8 -*-
#
# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()
#
# def fib2(n):
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)
#         a, b = b, a+b
#     return result
#
# year = 2026
# word = '1246'
# print(f'今年是{year}年，单词是{word}')
#
# with open('11.txt', encoding='utf-8') as f:
#     read_data = f.read()

# class B(Exception):
#     pass
#
# class C(B):
#     pass
#
# class D(C):
#     pass
#
# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print('D')
#     except C:
#         print('C')
#     except B:
#         print('B')

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)