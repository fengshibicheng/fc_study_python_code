# -*- coding: utf-8 -*-
"""
@Time ： 2026/5/10
@Auth ： fc
@File ： 4.1.if.py
@IDE ： PyCharm
"""
# -*- coding: utf-8 -*-

x = int(input('请输入一个整型数据'))

if x < 0:
    x = 0
    print("negative changed to zero")
elif x == 0:
    print('zero')
elif x == 1:
    print('single')
else:
    print('more')




