# -*- coding: utf-8 -*-
"""
@Time ： 2026/6/2
@Auth ： 冯成
@File ： 11扩展python或运算法的重写.py
@IDE ： PyCharm
"""

# 或运算符 |
class Test(object):
    def __init__(self, name):
        self.name = name

    def __or__(self, other):
        return Mysequence(self, other)

    def __str__(self):
        return self.name


class Mysequence(object):
    def __init__(self, *args):
        self.sequence = []
        for arg in args:
            self.sequence.append(arg)

    def __or__(self, other):
        self.sequence.append(other)
        return self

    def run(self):
        for i in self.sequence:
            print(i)


if __name__ == '__main__':
    a = Test('a')
    b = Test('b')
    c = Test('c')
    d = a | b | c
    d.run()
    print(type(d))

