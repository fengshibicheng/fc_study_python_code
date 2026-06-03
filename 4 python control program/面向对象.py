# -*- coding: utf-8 -*-
"""
@Time ： 2026/5/13
@Auth ： 冯成
@File ： 面向对象.py
@IDE ： PyCharm
"""
# -*- coding: utf-8 -*-
class FCmodel():
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school

    def hs(self):
        print(f"大家好，我是{self.name}，今年{self.age}岁了，我的来自的学校是{self.school}")

fcmodel = FCmodel("冯某", 20, "某某大学")
fcmodel.hs()

print("hello world!")